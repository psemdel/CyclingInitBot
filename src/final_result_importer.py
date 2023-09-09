#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:19:04 2023

@author: maxime
"""

from .base import CyclingInitBot
from .classification_importer import ClassificationImporter
from .startlist_importer import StartlistImporter
from .team_importer import TeamImporter

class FinalResultImporter(CyclingInitBot):
    def __init__(self, 
                 id_race: str,
                 maxkk: int,
                 fc:int,
                 chrono: bool,
                 man_or_woman: str, 
                 single_race:bool,
                 year:int=None,
                 force_nation_team: bool=False,
                 add_unknown_rider:bool=False,
                 **kwargs):
        '''
        For single day race or ending, import all results and the startlist in one step        
        
        Parameters
        ----------
        id_race : str
            Wikidata id of the race
        maxkk : int
            Maximum rank to be imported to wikidata
        fc : int
            Id in firstcycling   
        chrono : bool
            Is there an ITT during the whole race
        man_or_woman : str
            age category and gender of the races to be created
        single_race : bool, optional
            Is it a single stage race
        year : int, optional
        force_nation_team : bool
            Is there only national team?    
        add_unknown_rider : bool
            Add missing riders or stop the process if one is missing
        '''
        super().__init__(**kwargs)
        for k in ["maxkk","id_race", "fc", "year","chrono","man_or_woman","force_nation_team","add_unknown_rider"]:
            setattr(self,k,locals()[k])
            
        self.stage_or_general=9 #only all acceptable
        if single_race:
            self.prologue_or_final=2
        else:
            self.prologue_or_final=1
        
    def main(self):
        print("starting result import")
        f=ClassificationImporter(
            self.stage_or_general,
            self.id_race,
            self.maxkk, 
            test=False,
            startliston=True,
            fc=self.fc, 
            stage_num=-1, #only for stage, put -1 otherwise for the main race
            year=self.year)
        f.run_all()
        
        print("starting startlist import")
        f=StartlistImporter(
            self.prologue_or_final,
            self.id_race, 
            self.chrono,
            self.man_or_woman, 
            force_nation_team=self.force_nation_team,
            test=False,
            fc=self.fc,
            add_unknown_rider=self.add_unknown_rider)
        f.main()
        
        print("starting team import")
        f=TeamImporter(
            self.id_race, 
            test=False,
            fc=self.fc)
        f.main()
    