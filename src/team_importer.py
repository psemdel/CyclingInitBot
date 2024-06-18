#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:22:08 2023

@author: maxime
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

from .base import CyclingInitBot, Race, Team
from .func import table_reader
import sys
import traceback
import pandas as pd

class TeamImporter(CyclingInitBot):
    def __init__(
            self, 
            id_race:str,
            year:int=None,
            file:str='Results',
            fc:int=None,
            **kwargs):
        '''
        Import the list of teams in a race        

        Parameters
        ----------
        id_race : str
            id in wikidata of the race where the team must be imported
        year : int, optional
        file : str, optional
            name of the file to be read
        fc : int, optional
            Id in firstcycling

        '''
        super().__init__(**kwargs)
        
        for k in ["id_race","year","file","fc"]:
            setattr(self,k,locals()[k])
        self.race=Race(id=id_race)
        self.verbose=False

        if self.year is None:
            self.year=self.race.get_year()
        
        self.is_women=self.race.get_is_women()

        if self.fc==0:
            self.fc=None
        self.prop="P1923"

    def main(self):
        '''
        Main function of this script
        '''
        try:
            if self.year is None:
                raise ValueError('no year found')
                
            df, _, all_teams_found, log=table_reader(
                self.file,
                self.fc, 
                team=True, 
                year=self.year,
                convert_team_code=True, 
                is_women=self.is_women,
                need_complete=True
                ) 
            self.log.concat(log)
            df2=pd.unique(df["ID Team"])
            self.log.concat('result_table created')
            if self.verbose:
                print(df2)
            
            if not all_teams_found:
                self.log.concat('not all teams found, request interrupted')
                return 11, self.log
            else:
                #sorting
                dic={}
                for e in df2:
                    o=Team(id=e)
                    dic[o.sortkey]=o
                sorted_team =  sorted(dic.items(), key=lambda tup: tup[0])   
                self.log.concat("sorted teams:"+ str([s[0] for s in sorted_team]))
                
                if not self.test:
                    if(self.prop in self.race.item.claims):  #already there do nothing
                        self.log.concat(u'Classification already there')
                    else: 
                        for v in sorted_team:
                            self.race.add_values(self.prop, v[1].id, 'participating team', False) 
                         
                    self.log.concat('teams inserted')
                    return 0, self.log   
                       
        except:
            self.log.concat("General Error in team_importer")
            self.log.concat(traceback.format_exc())
            return 10, self.log  
