#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:26:55 2024

@author: maxime
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:19:04 2023

@author: maxime
"""

from .base import CyclingInitBot, Log, Race, PyItem
from .classification_importer import ClassificationImporter
from .startlist_importer import StartlistImporter
from .team_importer import TeamImporter
from .FirstCyclingAPI.first_cycling_api.combi import combi_results_startlist
import re 

class UpdateResult(CyclingInitBot):
    def __init__(self, 
                 id_race: str,
                 maxkk: int,
                 fc:int,
                 force_nation_team: bool=False,
                 add_unknown_rider:bool=False,
                 **kwargs):
        '''
        Update results in a clever way 
        Check if team have been imported
        Check if startlist have been imported
        Update stage results
        Update main race results
        
        Parameters
        ----------
        id_race : str
            Wikidata id of the race
        maxkk : int
            Maximum rank to be imported to wikidata
        fc : int
            Id in firstcycling   
        force_nation_team : bool
            Is there only national team?    
        add_unknown_rider : bool
            Add missing riders or stop the process if one is missing
        '''
        super().__init__(**kwargs)
        for k in ["maxkk","id_race", "fc","force_nation_team","add_unknown_rider"]:
            setattr(self,k,locals()[k])
            
        self.race=Race(id=id_race)    
        self.man_or_woman=self.race.get_man_or_woman()
        self.single_race=self.race.single_race()
        self.stage_or_general=9 #only all acceptable
        self.year=self.race.get_year()
        
    def main(self):
        log_total=Log()
        try:
            '''
            First look for what is filled in fc and in wikidata
            '''
            self.startlist=False
            if 'P710' in self.race.item.claims:   
                self.startlist=True
            
            if not self.single_race:
                first_stage=None
                last_stage=None
                last_stage_in_fc=None
                res1=0
                res2=0
                res3=0
                
                filled={-1:{"id":self.id_race}}
                #search for stage
                if u'P527' in self.race.item.claims:
                    for p527 in self.race.item.claims.get(u'P527'):
                        pyItem_v=PyItem(item=p527.getTarget(),id=p527.getTarget().getID())
                        
                        if u'P1545' in pyItem_v.item.claims:
                            raw_order=pyItem_v.item.claims.get(u'P1545')[0].getTarget()
                            try:
                                order=int(raw_order)
                            except: #Half-stage
                                main_order=int(re.search(r'\d+', raw_order).group())
                                if 'a' in raw_order:
                                    order=main_order+0.1
                                elif 'b' in raw_order:
                                    order=main_order+0.2
                                elif 'c' in raw_order:
                                    order=main_order+0.3
                                else:
                                    if main_order+0.4 in filled:
                                        log_total.concat("too many half-stage, check the code")
                                        return 10, log_total
                                    else:
                                        order=main_order+0.4
                                
                            if first_stage is None or order<first_stage:
                                first_stage=order
                            if last_stage is None or order>last_stage:
                                last_stage=order
                          
                            filled[order]={}    
                            filled[order]["id"]=pyItem_v.id
                            filled[order]["wd"]=False
                            if (u'P2417' in pyItem_v.item.claims) and (u'P2321' in pyItem_v.item.claims): #general ranking or stage ranking
                                filled[order]["wd"]=True
                
                #for the main race
                if 'P2321' in self.race.item.claims:    
                    filled[-1]["wd"]=True
                else:
                    filled[-1]["wd"]=False

                continue_search=True
                for ii in filled:
                    if continue_search:
                        tt=ii
                        if ii==-1:
                            tt=None

                        t=combi_results_startlist(self.fc,self.year, classification_num=1, stage_num=tt)
                    # note: does not really need to work with old race format in fc, as we want to update races that happen now
                    if "results_table" in t.__dir__():
                        filled[ii]["fc"]=True
                        if ii!=-1:
                            last_stage_in_fc=ii
                    else:
                        if ii!=-1:
                            continue_search=False
                        filled[ii]["fc"]=False
                    
                if last_stage_in_fc==last_stage:
                    self.prologue_or_final=1 #race completed
                else:
                    self.prologue_or_final=0
            else:
                self.prologue_or_final=2

            print(filled)
                
            if not self.startlist or self.prologue_or_final==1:
                print("starting startlist import")
                f=StartlistImporter(
                    self.prologue_or_final,
                    self.id_race, 
                    force_nation_team=self.force_nation_team,
                    test=False,
                    fc=self.fc,
                    add_unknown_rider=self.add_unknown_rider)
                res2, log2= f.main()
                log_total.concat(log2.txt)

            if res2==0: # if the startlist import crashed, the results will be halfway filled, let's avoid that
                for ii in filled:
                   if filled[ii]["fc"] and not filled[ii]["wd"]:
                       print("starting result import, stage: "+str(ii))
                       f=ClassificationImporter(
                           9,
                           filled[ii]["id"],
                           self.maxkk, 
                           test=False,
                           startliston=True,
                           fc=self.fc, 
                           stage_num=ii, #only for stage, put -1 otherwise for the main race
                           year=self.year)
                       res1, log1= f.run_all()
                       log_total.concat(log1.txt)
                    
            if not ("P1923" in self.race.item.claims):  #already there do nothing
                print("starting team import")   
                f=TeamImporter(
                    self.id_race, 
                    test=False,
                    fc=self.fc)
                res3, log3= f.main()
                log_total.concat(log3.txt)
            
            return max(res1,res2,res3), log_total
        except Exception as msg:
            import traceback
            print(msg)
            print(traceback.format_exc())
            
            return 10, log_total
    