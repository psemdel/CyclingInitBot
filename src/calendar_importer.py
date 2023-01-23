#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:54:17 2019

@author: maxime
"""
import pywikibot
from .func import table_reader, get_single_or_stage    
from .base import CyclingInitBot, PyItem, Search 
from .race_creator import RaceCreator

class CalendarImporter(CyclingInitBot):
    def __init__(self, filename, man_or_woman, year,**kwargs):
        super().__init__(**kwargs)
        self.filename=filename
        self.man_or_woman=man_or_woman
        self.verbose=False
        
    def main(self):
        #delete the first line of file
        df, _,_,log=table_reader(self.filename,verbose=self.verbose)
        self.log.concat(log)
        if self.verbose:
            self.log.concat(df)
            
        for ii in range(len(df)):  
            row=df.iloc[ii]
            if 'Name' in row:
                s=Search(row['Name'])
                id_master, master_genre=s.race()

                if id_master != "Q0" and 'Class' in row:
                    pyItem_master=PyItem(id=id_master)
                    id_country=pyItem_master.get_country() 
                    master_name =pyItem_master.get_label('fr')
                    
                    if 'Date From' in row:
                        if "." in row['Date From']:
                            table_date = row['Date From'].split(".")
                        elif "/" in row['Date From']:
                            table_date = row['Date From'].split("/")
                        else:
                            print("date separator not recognized, please check")
                            return 10, self.log
                        
                        year = int(table_date[2])
                        
                        race_begin = pywikibot.WbTime(
                            site=self.site,
                            year=int(table_date[2]),
                            month=int(table_date[1]),
                            day=int(table_date[0]),
                            precision='day')
                        
                        single_race=get_single_or_stage(row['Class']) 
                        
                        s2=Search( master_name + " " +str(year-1))
                        id_previous =s2.simple()
                        edition_nr=None

                        if id_previous not in ['Q0','Q1']:
                            pyItem_previous=PyItem(id=id_previous)

                            if(u'P393' in pyItem_previous.item.claims): #edition
                                edition_list = pyItem_previous.item.claims.get(u'P393')
                                edition_nr=int(edition_list[0].getTarget())+1
                        #note: country is a name which is not correct, make inherit the country
                        #note 2: get edition from last year
                        if single_race:
                            if not self.test:
                                 raceCreator=RaceCreator(
                                     race_name= master_name,
                                     single_race=single_race,
                                     man_or_woman=self.man_or_woman,
                                     start_date=race_begin,
                                     edition_nr=edition_nr,
                                     id_race_master=id_master,
                                     country=id_country,
                                     classe=row['Class'],
                                     year=year
                                     )                               
                        else: #stage race
                            if 'Date To' in row:
                                if "." in row['Date To']:
                                    table_date = row['Date To'].split(".")
                                elif "/" in row['Date To']:
                                    table_date = row['Date To'].split("/")
                                else:
                                    print("date separator not recognized, please check")
                                    return 10, self.log
                                
                                stage_race_end = pywikibot.WbTime(
                                    site=self.site,
                                    year=int(table_date[2]),
                                    month=int(table_date[1]),
                                    day=int(table_date[0]),
                                    precision='day')
    
                                if not self.test:
                                    raceCreator=RaceCreator(
                                          race_name= master_name,
                                          single_race=single_race,
                                          man_or_woman=self.man_or_woman,
                                          start_date=race_begin,
                                          edition_nr=edition_nr,
                                          id_race_master=id_master,
                                          country=id_country,
                                          classe=row['Class'],
                                          end_date=stage_race_end,
                                          only_stages=False,
                                          create_stages=False,
                                          year=year
                                          )
                        if not self.test:
                            status, log, res_id=raceCreator.main()
                elif row['Class'] != "CN" and row['Class'] != "CC" and row['Class'] !="CRT":
                    self.log.concat(row['Name'])
                    self.log.concat("race not found")
        return 0, self.log   
