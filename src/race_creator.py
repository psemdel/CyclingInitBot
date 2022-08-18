# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
                                  
from .data.calendar_list import calendaruciID, calendarWWTID, calendarUWTID
from .func import get_class_id, define_article, date_finder, man_or_women_to_is_women

from .base import CyclingInitBot, Race, create_present, PyItem
import copy

def get_class_WWT(classe):    
    UCI=True
    
    dic_WWT={
      "1.1":False,
      "2.1":False,
      "1.2":False,
      "2.2":False,
      "1.5":False,
      "1.WWT":True,
      "2.WWT":True,
      "1.Pro":False,
      "2.Pro":False,
      "1.UWT":False,
      "2.UWT":False,
         } 
    
    dic_UWT={
      "1.1":False,
      "2.1":False,
      "1.2":False,
      "2.2":False,
      "1.5":False,
      "1.WWT":False,
      "2.WWT":False,
      "1.Pro":False,
      "2.Pro":False,
      "1.UWT":True,
      "2.UWT":True,
         }  
    
    if classe in dic_WWT:
        return UCI, dic_WWT[classe], dic_UWT[classe]
    else:
        return UCI, False, False    

class RaceCreator(CyclingInitBot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.verbose=False
        self.class_id=None
        
        self.race_begin=kwargs.get('race_begin')
        self.end_date=kwargs.get('end_date')
        self.classe=kwargs.get('classe') #text 1.2 not id
        self.countryCIO=kwargs.get('countryCIO')
        self.id_race_master=kwargs.get('id_race_master')
        self.edition_nr=kwargs.get('edition_nr')
        self.year=kwargs.get('year')
        self.UWT=kwargs.get('UWT')
        self.WWT=kwargs.get('WWT')
        self.UCI=kwargs.get('UCI')
        self.race_name=kwargs.get('race_name')
        self.man_or_woman=kwargs.get('man_or_woman')
        
        self.is_women=None
        if self.man_or_woman is not None:
            self.is_women=man_or_women_to_is_women(self.man_or_woman)
        
        self.single_race=kwargs.get('single_race',False)
        
        if self.single_race:
            self.only_stages=False
            self.create_stages=False
            self.end_date=None
            self.create_main=True
            
            if self.countryCIO is not None:
                self.country=self.nation_table[self.countryCIO]["country"]
            
        else:
            self.only_stages=kwargs.get('only_stages',False)
            self.create_main_bool= not self.only_stages
            self.end_date=kwargs.get('end_date')
            
            if self.only_stages:
                self.create_stages_bool=True
                
                present_id=kwargs.get('stage_race_id')
                if present_id is None:
                    raise ValueError("create stage require stage_race_id")
                    self.log.concat("create stage require stage_race_id")

                self.first_stage=kwargs.get('first_stage')
                if self.first_stage is None:
                    raise ValueError("create stage require first_stage")
                    self.log.concat("create stage require first_stage")
                
                self.last_stage=kwargs.get('last_stage')
                if self.last_stage is None:
                    raise ValueError("create stage require last_stage")
                    self.log.concat("create stage require last_stage")
                   
                #present_id is know we have a lot of info
                self.race=Race(id=present_id)
                
                if self.race_begin is None:
                    self.race_begin=self.race.get_begin_date()
                if self.end_date is None:
                    self.end_date=self.race.get_end_date()
                if self.classe is None:
                    self.class_id=self.race.get_class()
                if self.year is None:
                    self.year=self.race.get_year()
                if self.race_name is None:
                    self.race_name=self.race.get_race_name()
                if self.countryCIO is None:
                    self.country=self.race.get_country()
                if self.is_women is None:
                    self.is_women=self.get_is_women()
                    
            else:
                self.create_stages_bool=kwargs.get('create_stages')

        if self.year is None and self.race_begin is not None: 
            self.year=self.race_begin.year

        self.class_id=get_class_id(self.classe) #self.classe None is handled inside
        self.genre, self.race_name=define_article(self.race_name)
            
    def main(self):
        try: 
            if self.country is None:
                raise ValueError("country not found")
                self.log.concat("country not found")
                return 10, self.log, "Q1"
            
            if self.year is None:
                raise ValueError("year of the race not found")
                self.log.concat("year of the race not found")
                return 10, self.log, "Q1"
            
            if self.race_name is None:
                raise ValueError("race name not defined")
                self.log.concat("race name not defined")
                return 10, self.log, "Q1"

            if self.create_main_bool:
                self.create_main()
            if self.create_stages_bool:
                self.create_stages()

            return 0, self.log, self.race.id     
        except Exception as msg:
            print(msg)
            return 10, self.log, "Q1"      
        except:
            self.log.concat("General Error in race creator")
            return 10, self.log, "Q1"   
    
    def UCI_to_calendar_id(self):
        calendar_id=None
        if self.WWT:
             calendar_id=calendarWWTID(str(self.year))
        elif self.UWT:
             calendar_id=calendarUWTID(str(self.year))
        elif self.UCI and self.man_or_woman==u"woman":  
             calendar_id=calendaruciID(str(self.year))
             
        return calendar_id   

    def stage_label(self,number):
        if number==0:
            label_part1_fr = u"Prologue"
        elif number==1:
            label_part1_fr = u"1re étape"
        else:
            label_part1_fr = str(number)+u"e étape"
    
        return {'fr': label_part1_fr+" " + self.genre + self.race_name + 
                " "+ str(self.year)}

    def create_stages(self):
        self.log.concat("stage creation")
        pyItem_stage_previous=None
        
        for number in range(self.first_stage,self.last_stage+1):
            stage_label_present=self.stage_label(number)
            pyItem_stage=create_present(stage_label_present)
            self.log.concat("id stage present "+pyItem_stage.id)
            
            if pyItem_stage.id!='Q1':
                if pyItem_stage.get_description('fr')=='':
                    mydescription={'fr':u'étape'+" " + self.genre + 
                                   self.race_name + " "+ str(self.year)}
                    pyItem_stage.item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
                
                if number==0:
                    pyItem_stage.add_value("P31","Q485321",u'Nature')  #prologue
                else:
                    pyItem_stage.add_value("P31","Q18131152",u'Nature')  #étape
                
                pyItem_stage.add_value("P361",self.race.id,u'part of')
                pyItem_stage.add_value("P641","Q3609",u'cyclisme sur route')
                pyItem_stage.add_value("P17",self.country,u'country')
                pyItem_stage.add_value("P1545",str(number),u'order',noId=True)

                stage_date=date_finder(number,self.first_stage,self.last_stage, 
                                       self.race_begin,self.end_date)
                
                pyItem_stage.add_value("P585",stage_date,u'date',date=True)

                if self.is_women:
                    pyItem_stage.add_value('P2094',"Q1451845","women cycling")

                #Link to the master for this year, so item
                self.race.add_values("P527",pyItem_stage.id,u'link stage '+str(number),False) 
                #Link to previous
                
                if number>self.first_stage:
                    pyItem_stage.add_value("P155",pyItem_stage_previous.id,u'link previous') 
                    pyItem_stage_previous.add_value("P156",pyItem_stage.id,u'link next')
                pyItem_stage_previous=copy.copy(pyItem_stage)
        
    def create_main(self):
        UCI, WWT, UWT=get_class_WWT(self.classe) #not required for stages, where classe is not defined
        
        mylabel={'fr': self.race_name + " " + str(self.year)}
        self.race=create_present(mylabel)
        
        if self.race.id!=u'Q1':
            if self.race.get_description('fr')=='':
                mydescription={'fr':u'édition ' + str(self.year) +" "+ self.genre + self.race_name}
                self.race.item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')

                self.race.add_value("P31",self.id_race_master,u'Nature')
                self.race.add_value("P641","Q3609",u'cyclisme sur route')
                self.race.add_value("P17",self.country,u'country')
            
                if self.single_race:
                    self.race.add_value("P585", self.start_date, u' date',date=True)
                else:
                    self.race.add_value("P580",self.start_date,u'starting date', date=True)
                    if self.end_date:
                        self.race.add_value("P582",self.end_date,u'ending date',date=True)
            
                if self.edition_nr is not None:
                     self.race.add_value("P393",str(self.edition_nr),u'edition nr',noId=True)

                calendar_id=self.UCI_to_calendar_id()
                if calendar_id is not None:
                    self.race.add_value("P361",calendar_id,u'part of')
                    pyItem_cal=PyItem(id=calendar_id)
                    pyItem_cal.add_values("P527",self.race.id,u'in',False)

                if self.class_id:
                    self.race.add_values("P279", self.class_id,u'Class',0)   
                    
                if self.is_women:
                    self.race.add_value('P2094',"Q1451845","women cycling")
                
                self.race.link_year(self.year,id_master=self.id_race_master)  
                pyItem_master=PyItem(id=self.id_race_master)
                pyItem_master.add_value("P527",self.race.id,u'adding a year')

    
    
      
