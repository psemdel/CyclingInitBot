# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
                                  
from .data.calendar_list import calendaruciID, calendarWWTID, calendarUWTID
from .func import get_class_id, define_article, date_finder, man_or_women_to_is_women

from .base import CyclingInitBot, Race, create_item, PyItem, Search
import copy
import pywikibot
import traceback

def get_class_WWT(classe: str):    
    '''
    Return the appartenance to UCI calendar, WWT and UWT

    Parameters
    ----------
    classe : str
        class name of the race
    '''
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
    def __init__(
            self,
            start_date: pywikibot.WbTime=None,
            end_date:pywikibot.WbTime=None,
            classe:str=None,
            country: str=None,
            country_id: str=None,
            id_race_master: str=None,
            edition_nr=None,
            year=None,
            UWT:bool=False,
            WWT:bool=False,
            UCI:bool=False,
            race_name: str=None,
            man_or_woman:str=None,
            single_race: bool=False,
            only_stages:bool=False,
            create_stages:bool=True,
            stage_race_id:str=None,
            first_stage:int=None,
            last_stage:int=None,
            **kwargs):
        '''
        Create an edition race with or without its stages

        Parameters
        ----------
        start_date : pywikibot.WbTime, optional
            First day of the race
        end_date : pywikibot.WbTime, optional
            Last day of the race
        classe : str, optional
            class name of the race
        country : str, optional
            UCI code of a country, if false then all countries will be created
        country_id : str, optional
            wikidata id of the country
        id_race_master : str, optional
            id of the race, without year
        edition_nr, optional
            number of the edition for the current year
        year : TYPE, optional
        UWT : bool, optional
            Is the race part of the world tour?
        WWT : bool, optional
            Is the race part of the women world tour?
        UCI : bool, optional
            Is the race part of the UCI calendar?
        race_name : str, optional
            race name for the current year
        man_or_woman : str, optional
            age category and gender of the races to be created
        single_race : bool, optional
            Is it a single stage race
        only_stages: bool, optional
            To create only the stage of a race without the race itself
        create_stages: bool, optional
            Should the stages be created
        stage_race_id : str, optional
            wikidata id of the race, when wanting to create only it stage
        first_stage : int, optional
            Number of first stage, 0 is for prolog
        last_stage : int, optional
            Number of the last stage            
        '''
        super().__init__(**kwargs)
                
        for k in ["start_date", "end_date","classe","country", "country_id","id_race_master","edition_nr",
                  "year","UWT","WWT","UCI","race_name","man_or_woman","single_race","only_stages",
                  "create_stages","stage_race_id","first_stage","last_stage"]:
            setattr(self,k,locals()[k])
        
        self.verbose=False
        self.class_id=None
        
        self.is_women=None
        if self.man_or_woman is not None:
            self.is_women=man_or_women_to_is_women(self.man_or_woman)
        
        if self.country is not None and self.country_id is None:
            self.country_id=self.nation_table[self.country]["country"]
            
        if self.single_race:
            self.create_stages=False
            self.create_main=True
        else:
            self.create_main= not self.only_stages

            if self.only_stages:
                self.create_stages=True
                
                if self.stage_race_id is None:
                    raise ValueError("create only stages require stage_race_id")
                    self.log.concat("create only stages require stage_race_id")
                #stage_race_id is known we have a lot of info
                self.race=Race(id=stage_race_id)
                
                if self.start_date is None:
                    self.start_date=self.race.get_begin_date()
                if self.end_date is None:
                    self.end_date=self.race.get_end_date()
                if self.classe is None:
                    self.class_id=self.race.get_class()
                if self.year is None:
                    self.year=self.race.get_year()
                if self.race_name is None:
                    self.race_name=self.race.get_race_name()
                if self.country_id is None:
                    self.country_id=self.race.get_country()
                if self.is_women is None:
                    self.is_women=self.race.get_is_women()

            if self.create_stages:        
                for k in ["first_stage","last_stage"]:
                    if getattr(self,k) is None:
                        raise ValueError("create stage require "+k)
                        self.log.concat("create stage require "+k)

        if self.year is None and self.start_date is not None: 
            self.year=self.start_date.year

        self.class_id=get_class_id(self.classe) #self.classe None is handled inside
        self.genre, self.race_name=define_article(self.race_name)
            
    def main(self):
        '''
        Main function of this script
        '''
        try: 
            for k in ["country_id","year","race_name","start_date"]:
                if getattr(self,k) is None:
                    raise ValueError(k+"  not found")
                    self.log.concat(k +" not found")
                    return 10, self.log, "Q1"

            if self.create_main:
                self.create_main_f()
            if self.create_stages:
                self.create_stages_f()

            return 0, self.log, self.race.id     
        except Exception as msg:
            print(msg)
            return 10, self.log, "Q1"      
        except:
            print(traceback.format_exc())
            self.log.concat("General Error in race creator")
            self.log.concat(traceback.format_exc())
            return 10, self.log, "Q1"   
    
    def UCI_to_calendar_id(self):
        '''
        Search the corresponding calendar to add, depending on if the race is UWT, WWT or not
        '''
        calendar_id=None
        if self.WWT:
             calendar_id=calendarWWTID(str(self.year))
        elif self.UWT:
             calendar_id=calendarUWTID(str(self.year))
        elif self.UCI and self.man_or_woman==u"woman":  
             calendar_id=calendaruciID(str(self.year))
        return calendar_id   

    def stage_label(self,number:int):
        '''
        Create the label of the stage
        '''
        if number==0:
            label_part1_fr = u"Prologue"
        elif number==1:
            label_part1_fr = u"1re étape"
        else:
            label_part1_fr = str(number)+u"e étape"
    
        return {'fr': label_part1_fr+" " + self.genre + self.race_name + 
                " "+ str(self.year)}

    def create_stages_f(self):
        '''
        Function that creates the stages
        '''
        self.log.concat("stage creation")
        pyItem_stage_previous=None
        
        for number in range(self.first_stage,self.last_stage+1):
            stage_label_present=self.stage_label(number)
            pyItem_stage=create_item(stage_label_present)
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
                pyItem_stage.add_value("P17",self.country_id,u'country')
                pyItem_stage.add_value("P1545",str(number),u'order',noId=True)

                stage_date=date_finder(number,self.first_stage,self.last_stage, 
                                       self.start_date,self.end_date)
                
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
                
    def check_year_already_present(
            self,
            year:int,
            id_master:str=None,
            ):
        '''
        Check if the race edition is already present, even if under another title
        ----------
        year : int
        id_master : str, optional
            id of the race parent
        '''
        item_master = pywikibot.ItemPage(self.repo, id_master)
        item_master.get()
        
        #look for next and previous
        if (u'P527' in item_master.claims):
            for claim in item_master.claims.get(u'P527'):
                v=claim.getTarget().getID()
                pyItem_v=PyItem(item=claim.getTarget(),id=v)
                
                for _, label in pyItem_v.item.labels.items():
                    if str(year) in label:
                        return True
        return False        
    def create_main_f(self):
        '''
        Function that create the edition of a race
        '''
        self.UCI, self.WWT, self.UWT=get_class_WWT(self.classe) #not required for stages, where classe is not defined
        
        if not self.check_year_already_present(self.year, self.id_race_master):
            mylabel={'fr': self.race_name + " " + str(self.year)}
            self.race=create_item(mylabel)
            
            if self.race.id!=u'Q1':
                if self.race.get_description('fr')=='':
                    mydescription={'fr':u'édition ' + str(self.year) +" "+ self.genre + self.race_name}
                    self.race.item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
    
                self.race.add_value("P31",self.id_race_master,u'Nature')
                self.race.add_value("P641","Q3609",u'cyclisme sur route')
                self.race.add_value("P17",self.country_id,u'country')
            
                if self.single_race:
                    self.race.add_value("P585", self.start_date, u' date',date=True)
                else:
                    self.race.add_value("P580",self.start_date,u'starting date', date=True)
                    if self.end_date:
                        self.race.add_value("P582",self.end_date,u'ending date',date=True)
            
                #get edition from last year
                if self.edition_nr is None:
                    s2=Search( self.race_name + " " +str(self.year-1))
                    id_previous =s2.simple()
    
                    if id_previous not in ['Q0','Q1']:
                        pyItem_previous=PyItem(id=id_previous)
    
                        if(u'P393' in pyItem_previous.item.claims): #edition
                            edition_list = pyItem_previous.item.claims.get(u'P393')
                            self.edition_nr=int(edition_list[0].getTarget())+1
                    
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
                pyItem_master.add_values("P527",self.race.id,u'adding a year',False)

    
      
