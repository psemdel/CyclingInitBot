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

import pywikibot
from .base import CyclingInitBot, Race, Team, PyItem
from .func import table_reader
import math
import sys
import pandas as pd

class TeamImporter(CyclingInitBot):
    def __init__(self, id_race,**kwargs):
        super().__init__(**kwargs)
        self.race=Race(id=id_race)
        self.verbose=True
        
        self.year=kwargs.get('year',None)
        if self.year is None:
            self.year=self.race.get_year()
        
        self.is_women=self.race.get_is_women()
        self.file=kwargs.get('file','Results')
        fc=kwargs.get("fc",None)
        if fc==0:
            fc=None
        self.fc=fc
        self.prop="P1923"

    def main(self):
        try:
            if self.year is None:
                self.year=self.race.get_year()
            if self.year is None:
                raise ValueError('no year found')
                
            df, _, _, log=table_reader(self.file,self.fc, team=True, 
                                       year=self.year,convert_team_code=True, is_women=self.is_women) 
            self.log.concat(log)
            df2=pd.unique(df["ID Team"])
            self.log.concat('result_table created')
            if self.verbose:
                print(df2)
 
            if not self.test:
                if(self.prop in self.race.item.claims):  #already there do nothing
                    self.log.concat(u'Classification already there')
                else: 
                    #claim=pywikibot.Claim(self.repo, self.prop)  
                    for ii in range(len(df2)):
                        self.race.add_values(self.prop, df2.values[ii], 'participating team', False) 
                     
                self.log.concat('teams inserted')
                return 0, self.log   
                       
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            self.log.concat("General Error in team_importer")
            return 10, self.log  
