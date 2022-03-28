#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:35:53 2019

@author: maxime
"""
from datetime import date
import pandas as pd
 
from .base import CyclingInitBot, PyItem, Race
from .data import calendar_list

class ChampListCreator(CyclingInitBot):
    def __init__(self,man_or_woman,start_year, actualize):
        super().__init__()
        self.man_or_woman=man_or_woman
        self.start_year=start_year
        self.end_year=date.today().year+1
        self.actualize=actualize

        self.dic =calendar_list.nationChampionshipMaster()
        self.dic_road_race_women, self.dic_clm_women,\
        self.dic_road_race_men, self.dic_clm_men=calendar_list.worldCCchampionships()
        
        self.champ_table=[] 
       
        self.verbose=False
    
    def main(self):
        #Road
        if self.man_or_woman=="woman":
            self.filename='src/input/champ2.csv'
            self.old_filename='src/input/champ.csv'
            self.dic_worldconti=self.dic_road_race_women
            self.pattern="Course en ligne féminine aux"
        else:
            self.filename='src/input/champ_man2.csv'
            self.old_filename='src/input/champ_man.csv'
            self.dic_worldconti=self.dic_road_race_men
            self.pattern="Course en ligne masculine aux"
            
        self.road_or_clm='Road'
        self.sub_create_champ()

        print("road scan finished")
        #Clm
        if self.man_or_woman=="woman":
            self.dic_worldconti=self.dic_clm_women
            self.pattern="Contre-la-montre féminin aux"
        else:
            self.dic_worldconti=self.dic_clm_men
            self.pattern="Contre-la-montre masculin aux"
        self.road_or_clm='Clm'
        self.sub_create_champ()
        print("itt scan finished")
        
        final_df=pd.DataFrame(self.champ_table)
        if self.actualize:
            old_df = pd.read_csv(self.old_filename)
            old_df=old_df[old_df["WorldCC"]==False] #remove the world
            old_df=old_df[old_df["Year"]<self.start_year]
            final_df=pd.concat([old_df, final_df])
    
        final_df.to_csv(self.filename)
        print("csv file " + self.filename + " written")
        
    def sub_findwinner(self,pyItem,id_race,**kwargs):
          date_found=False
          invalid_precision=False
          there_is_a_winner=False
          warning_written=False
          row={}
          row['Champ']=id_race
          
          if (u'P585' in pyItem.item.claims):
             list_of_race_date=pyItem.item.claims.get(u'P585')
             race_date=list_of_race_date[0].getTarget()
             if race_date is None:
                 invalid_precision=True
             elif ((race_date.day==1 and race_date.month==1) or
                 race_date.day==0 or
                 race_date.month==0):
                 invalid_precision=True
             else:
                 date_found=True
          
          if (u'P1346' in pyItem.item.claims): #winner
             winners=pyItem.item.claims.get(u'P1346')
             for winner in winners:
                 there_is_qual=False
                 id_this_qual=None
                 
                 for qual in winner.qualifiers.get('P642', []):
                     there_is_qual=True
                 if there_is_qual:
                     id_this_qual=winner.qualifiers['P642'][0].getTarget().getID()
                 else:
                     print(pyItem.get_label('fr'))
                     print("no qualifier")
                    
                 if id_this_qual is not None and id_this_qual=='Q20882667': #winner general classification 
                     #check qualifier
                     if winner.getTarget() is not None:
                         id_temp_winner=winner.getTarget().getID()
                         there_is_a_winner=True   
                     if date_found and there_is_a_winner:
                         row['Day']=race_date.day
                         row['Month']=race_date.month
                         row['Year']=race_date.year  
                         row['Winner']=id_temp_winner
                         if kwargs.get("WorldCC",False):
                             row['WorldCC']=True
                         else:
                             row['WorldCC']=False
                         if self.road_or_clm=="Clm":
                             row['Clm']=True
                         else:
                             row['Clm']=False
                         self.champ_table.append(row)
                     elif invalid_precision and there_is_a_winner:
                         if warning_written==False:
                             print(pyItem.get_label('fr'))
                             print('unsufficient precision')
                             warning_written=True
    
    def sub_champlist(self):
        for id_race in self.dic_worldconti:
            race=Race(id=id_race)
            if(u'P527' in race.item.claims):
                 for e in race.item.claims.get(u'P527'):  
                     pyItem_this_year=PyItem(id=e.getTarget().getID())
                     self.sub_findwinner(pyItem_this_year, id_race,WorldCC=True) 
    
    def sub_course(self,race):
        this_label=race.get_label('fr')
        if this_label.find(self.pattern)==0: #filter with fr label
            if (u'P31' in race.item.claims):
                list_of_nature=race.item.claims.get(u'P31')
                id_master=list_of_nature[0].getTarget().getID()
            else:
                id_master=u'Q1'
            self.sub_findwinner(race, id_master)
    
    def sub_create_champ(self):
        #world and continental championships are recreated all the time
        self.sub_champlist()
        self.log.concat(self.road_or_clm +" world and continental championships "+ \
                        self.man_or_woman + " completed")

        if self.verbose:     
            self.log.concat(self.WorldCC_champ_table)  
        
        #Look in the national championships
        for year in range(self.start_year,self.end_year):
            year=str(year)
            self.log.concat(self.road_or_clm + " start year " + year)
            
            pyItem_all_national=PyItem(id=self.dic[year])
            
            if(u'P527' in pyItem_all_national.item.claims):
                 for e in pyItem_all_national.item.claims.get(u'P527'): 
                     race_this_national=Race(id=e.getTarget().getID())

                     if(u'P527' in race_this_national.item.claims):
                         for e2 in race_this_national.item.claims.get(u'P527'):
                             race_this_year=Race(id=e2.getTarget().getID())
                             self.sub_course(race_this_year)
                     else:
                         print(race_this_national.get_label('fr') + " has no P527")
        





