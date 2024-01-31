#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:34:29 2019

@author: maxime
"""
import pywikibot
import sys
import traceback
import pandas as pd
from .base import CyclingInitBot, Race, Search
from .get_rider_tricot import GetRiderTricot
from .func import cyclists_table_reader, table_reader    
  
class StartlistImporter(CyclingInitBot):
    def __init__(
            self,
            prologue_or_final: int, 
            id_race: str, 
            chrono: bool,
            man_or_woman: str, 
            force_nation_team: bool=False,
            file:str="Results",
            fc:int=None,
            verbose:bool=False,
            add_unknown_rider:bool=False,
            **kwargs
            ):
        '''
        Import a startlist for a race

        Parameters
        ----------
        prologue_or_final : int
            Is the start list imported from the result of the first stage/prologue, or from the final results?
            Code is prologue=0, final=1, single day race=2
        id_race : str
            wikidata id of the race,
        chrono : bool
            Is there an ITT during the whole race
        man_or_woman : str
            age category and gender of the races to be created
        force_nation_team : bool
            Is there only national team?
        file : str, optional
            name of the file to be read
        fc : int, optional
            Id in firstcycling    
        add_unknown_rider : bool
            Add missing riders or stop the process if one is missing
        '''
        super().__init__(**kwargs)
        for k in ["prologue_or_final","man_or_woman","force_nation_team","file", "chrono","fc",
                  "verbose","add_unknown_rider"]:
            setattr(self,k,locals()[k])

        self.race=Race(id=id_race)
        self.time_of_race=self.race.get_date()
        self.year=self.time_of_race.year

        if self.fc==0:
            self.fc=None

    def IDtoCIOsearch(self,country_id:str):
        '''
        Return the CIO code of a country, for instance "FRA", from the country id in wikidata

        Parameters
        ----------
        country_id : str
            country id in wikidata
        '''
        if country_id=="Q55":
            return 'NED'
        
        for keys in self.nation_table:
            if self.nation_table[keys]["country"]==country_id:
                return keys
        print("country ID not found: " + str(country_id))  
        return ""

    def get_national_team_id(self, country_id: str):
        '''
        Search for the national team of a country for a certain year

        Parameters
        ----------
        country_id : str
            country id in wikidata
        '''        
        if self.man_or_woman==u'woman':
            positive_list=['féminine de cyclisme']
            negative_list=[]
        elif self.man_or_woman=='manU':
            positive_list=['espoirs de cyclisme'] 
            negative_list=[]
        elif self.man_or_woman=='man':
            positive_list=['de cyclisme']
            negative_list=['féminine de cyclisme','espoirs de cyclisme']
        else:
            return 'Q0'
        
        s=Search(self.IDtoCIOsearch(country_id) + " " + str(self.year))
        return s.national_team(positive_list=positive_list,negative_list=negative_list)

    def find_national_team(self, df: pd.core.frame.DataFrame):
        '''
        Try to detect national team in the start list by checking the nationality of successive riders in it
        
        Parameters
        ----------
        df: pd.core.frame.DataFrame
            dataframe containing the imported file
        '''          
        try:
            national_team_detected=False #otherwise insert nothing during first loop
            all_same_team=1
            national_team_nation=u'reset'
            national_team_begin=0
            
            for ii, cyclist in enumerate(self.list_of_cyclists):
                #check national team
                if not self.force_nation_team:
                    if df["BIB"].values[ii]%10==1:
                                #insert last team
                        if self.verbose:
                            print("all_same_team" + str(all_same_team))
                            
                        if (national_team_detected and all_same_team<0):
                            print(u'national team detected '+ self.IDtoCIOsearch(national_team_nation))
                            #insert the team
                            for jj in range(national_team_begin,ii):
                                id_national_team=self.get_national_team_id(national_team_nation)
                                if id_national_team!='Q0':
                                    self.list_of_cyclists[jj].team=id_national_team
                                    self.list_of_cyclists[jj].national_team=True #for testing
                        #re-init the variable
                        national_team_detected=True
                        national_team_begin=ii
                        national_team_nation=u'reset'
                        proteam=u'reset'
                        all_same_team=1 #if all_same_team is 1 then it is probably not a national team
                       
                    if national_team_detected: 
                        if self.verbose:
                            print(cyclist.dossard)
                        #get nationality
                        nationality=cyclist.get_nationality(self.time_of_race)    
                        if nationality !="Q0":
                            if self.verbose:
                                print("nationality: "+ nationality)
                            cyclist.nationality=nationality   
                            if national_team_nation==u'reset':
                                national_team_nation=nationality   
                            else:
                                if national_team_nation!=nationality: 
                                    #not the same nation --> not a national team
                                    if self.verbose:
                                        print("different nation")
                                    national_team_detected=False 
                        team=cyclist.get_present_team(self.time_of_race) 
                        if self.verbose:
                            print("team: "+ team)
                        if proteam==u'reset':
                            if team!="Q1":
                                proteam=team
                            else:
                                all_same_team-=1
                        else:
                            if team!='Q1' and proteam!=team: 
                                all_same_team-=1
                            elif team=='Q1':
                                all_same_team-=1
                    #last team
                else: #force_nation_team, then only look at nation value
                    #item_rider=list_of_cyclists[ii].item
                    nationality=cyclist.get_nationality(self.time_of_race)    
                    id_national_team=self.get_national_team_id(nationality)
    
                    if id_national_team not in ['Q0','Q1']:
                        cyclist.team=id_national_team
                        cyclist.national_team=True #for testing
    
            if not self.force_nation_team and national_team_detected and all_same_team<0:
                 print("last team")
                 print(u'national team detected '+self.IDtoCIOsearch(national_team_nation))
                        #insert the team
                 for jj in range(national_team_begin,len(self.list_of_cyclists)):
                     id_national_team=self.get_national_team_id(national_team_nation)
                     if id_national_team!='Q0':
                         self.list_of_cyclists[jj].team=id_national_team
                         self.list_of_cyclists[jj].national_team=True #for testing
    
            if self.test:
                return self.list_of_cyclists
        except Exception as msg:
             _, _, exc_tb = sys.exc_info()
             print("line " + str(exc_tb.tb_lineno))
             print(msg)
 
    def add_rank(self, claim, cyclist):
        target_DNFqual = pywikibot.ItemPage(self.repo, u'Q1210380')
        target_DNSqual = pywikibot.ItemPage(self.repo, u'Q1210382')
        target_DSQqual = pywikibot.ItemPage(self.repo, u'Q1229261')
        target_OOTqual = pywikibot.ItemPage(self.repo, u'Q7113430')
        
        if cyclist.rank==0 or cyclist.rank=="DNF": #no ranking
            self.race.add_qualifier(claim,'P1534',target_DNFqual)
        elif cyclist.rank=="DNS":
            self.race.add_qualifier(claim,'P1534',target_DNSqual)
        elif cyclist.rank=="DSQ": 
            self.race.add_qualifier(claim,'P1534',target_DSQqual)
        elif cyclist.rank=="OOT": 
            self.race.add_qualifier(claim,'P1534',target_OOTqual)    
        else:
            target_q =  pywikibot.WbQuantity(amount=cyclist.rank, site=self.site)
            self.race.add_qualifier(claim,'P1352',target_q)
            
    def main(self):
        '''
        Main function of this script
        '''
        try:
            df, all_riders_found, _, log=table_reader(
                self.file,
                self.fc,
                verbose=self.verbose,
                need_complete=not self.add_unknown_rider,
                rider=True,
                year=self.year)
            self.log.concat(log)
            #Sort by dossard
            if df is None:
                raise ValueError("table reader failed")
                
            if not all_riders_found and not self.add_unknown_rider:
                self.log.concat(u'Not all riders found, request stopped')
                return 1, self.log
                
            if "BIB" in df.columns:
                df=df.sort_values(["BIB"])
            else:
                raise ValueError("BIB not present in import file")

            self.log.concat('table read and sorted')
            self.list_of_cyclists, _= cyclists_table_reader(df)
            list_of_lost=[]
            
            if not self.test:
                already_list=False
                if 'P710' in self.race.item.claims:
                    already_list=True
                    list_of_comprend=self.race.item.claims.get(u'P710')
                    list_of_lost=list_of_comprend.copy()
                    if self.prologue_or_final in [0,2]:  #already there do nothing
                        self.log.concat("warning ")
                        self.log.concat(u'List of starters already there')

                if self.prologue_or_final!=1: #for prologue_or_final==1 no detection
                    self.log.concat(u'looking for national team')
                    self.find_national_team(df)
                    
                target_DNFqual = pywikibot.ItemPage(self.repo, u'Q1210380')
                
                #add starting/finishing number of participants
                if self.prologue_or_final in [0,2]:
                    nb_starter=0
                    for ii, cyclist in enumerate(self.list_of_cyclists):
                        if cyclist.id not in ['Q0','Q1']:
                            if cyclist.rank!="DNS":
                                nb_starter+=1
                    target=pywikibot.WbQuantity(amount=nb_starter, site=self.site)
                    _, claim=self.race.add_values('P1132', target, 'number of participants', False,noId=True)
                    target_q = pywikibot.ItemPage(self.repo, 'Q529711')
                    self.race.add_qualifier(claim,'P276',target_q)
                if self.prologue_or_final in [1,2]:  
                    if "Rank" in df.columns:
                        l=[e for e in df["Rank"] if not isinstance(e,str)]
                        target=pywikibot.WbQuantity(amount=int(max(l)), site=self.site)
                        _, claim=self.race.add_values('P1132', target, 'number of participants', False,noId=True)
                        target_q = pywikibot.ItemPage(self.repo, 'Q12769393')
                        self.race.add_qualifier(claim,'P276',target_q)
                
                self.log.concat(u'inserting start list')
                for ii, cyclist in enumerate(self.list_of_cyclists):
                    if cyclist.id not in ['Q0','Q1']:
                        #look for it
                        claim=None
                        if already_list:
                            for jj, e in enumerate(list_of_comprend):
                                if e.getTarget() is not None and e.getTarget().getID()==cyclist.id: #Already there
                                    claim=e
                                    if self.prologue_or_final==1 and e in list_of_lost:
                                        list_of_lost.remove(e)
                                        
                        if claim is None:  ##add the rider to the property
                            if self.prologue_or_final==1:
                                self.log.concat('\n rider not found in present startlist, id: '+str(cyclist.id))
                            _, claim=self.race.add_values('P710', cyclist.id, 'starterlist', False)
                            self.race.add_qualifier(claim,'P1618',str(cyclist.dossard))
                            
                            if cyclist.team: #national team
                                target_q = pywikibot.ItemPage(self.repo, cyclist.team)
                                self.race.add_qualifier(claim,'P54',target_q)
                                
                        if self.prologue_or_final in [1,2]:
                            self.add_rank(claim,cyclist)
                        if not self.force_nation_team and self.prologue_or_final!=1: #when only national team, no national tricot
                            #to avoid being called every time, should be centralized
                            grt=GetRiderTricot(cyclist.id, self.time_of_race, claim, self.chrono, self.man_or_woman)
                            grt.main()
                    elif self.add_unknown_rider and self.prologue_or_final in [0,2]: #otherwise it will add the same riders several time
                        _, claim=self.race.add_values('P710', "Q120122853", 'starterlist', False)
                        self.race.add_qualifier(claim,'P1618',str(cyclist.dossard))
                        self.add_rank(claim,cyclist)
                        
                #all riders are classified, assumption the other are DNF
                if self.prologue_or_final==1:
                    for claim in list_of_lost:
                        self.race.add_qualifier(claim,'P1534',target_DNFqual)
            print("start list insertion finished")
            return 0, self.log                          
        except:
            self.log.concat("General Error in startlist_importer")
            self.log.concat(traceback.format_exc())
            return 10, self.log     
