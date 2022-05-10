#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:34:29 2019

@author: maxime
"""
import pywikibot
import sys
from .base import CyclingInitBot, Race, Search
from .get_rider_tricot import GetRiderTricot
from .func import cyclists_table_reader, table_reader    
  
class StartlistImporter(CyclingInitBot):
    def __init__(self,prologue_or_final, id_race, 
          chrono,man_or_woman, force_nation_team,**kwargs):
        super().__init__(**kwargs)
        self.prologue_or_final=prologue_or_final
        self.race=Race(id=id_race)
        self.time_of_race=self.race.get_date()
        self.year=self.time_of_race.year
        self.chrono=chrono
        self.man_or_woman=man_or_woman
        self.force_nation_team=force_nation_team
        self.file=kwargs.get('file','Results')
        self.verbose=kwargs.get('verbose')

    def IDtoCIOsearch(self,this_id):
        if this_id=="Q55":
            return 'NED'
        
        for keys in self.nation_table:
            if self.nation_table[keys]["country"]==this_id:
                return keys
        print("country ID not found: " + str(this_id))  
        return ""

    def get_national_team_id(self, country_id):
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

    def find_national_team(self, df):
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
                            all_same_team=all_same_team-1
                    else:
                        if team!='Q1' and proteam!=team: 
                            all_same_team=all_same_team-1
                        elif team=='Q1':
                            all_same_team=all_same_team-1
                #last team
            else: #force_nation_team, then only look at nation value
                #item_rider=list_of_cyclists[ii].item
                nationality=cyclist.get_nationality(self.time_of_race)    
                id_national_team=self.get_national_team_id(nationality)

                if id_national_team!=u'Q0':
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

    def main(self):
        try:
            df, all_riders_found, _, log=table_reader(self.file,verbose=self.verbose,need_complete=True,rider=True)
            self.log.concat(log)
            #Sort by dossard
            if df is None:
                raise ValueError("table reader failed")
                
            if not all_riders_found:
                log.concat(u'Not all riders found, request stopped')
                return 1, self.log
                
            if "BIB" in df.columns:
                df=df.sort_values(["BIB"])
            else:
                raise ValueError("BIB not present in import file")

            self.log.concat('table read and sorted')
            self.list_of_cyclists, _= cyclists_table_reader(df)

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

                self.log.concat(u'inserting start list')
                for ii, cyclist in enumerate(self.list_of_cyclists):
                    if cyclist.id not in ['Q0','Q1']:
                        #look for it
                        claim=None
                        if already_list:
                            for jj, e in enumerate(list_of_comprend):
                                if e.getTarget().getID()==cyclist.id: #Already there
                                    claim=e
                                    if self.prologue_or_final==1:
                                        list_of_lost.remove(e)
                                        
                        if claim is None:  ##create the rider
                            if self.prologue_or_final==1:
                                self.log.concat('\n rider not found, id: '+str(cyclist.id))
                            claim=pywikibot.Claim(self.repo, u'P710')  #reinit everytime
                            claim.setTarget(cyclist.item)
                            self.race.item.addClaim(claim, summary=u'Adding starterlist')
                            qualifier_dossard=pywikibot.page.Claim(self.site, 'P1618', is_qualifier=True)
                            qualifier_dossard.setTarget(str(cyclist.dossard))
                            claim.addQualifier(qualifier_dossard)
                            
                            if cyclist.team: #national team
                                target_qualifier = pywikibot.ItemPage(self.repo, cyclist.team)
                                qualifier_team=pywikibot.page.Claim(self.site, 'P54', is_qualifier=True)
                                qualifier_team.setTarget(target_qualifier)
                                claim.addQualifier(qualifier_team)
                                
                        if self.prologue_or_final in [1,2]:
                           if cyclist.rank==0: #no ranking
                               qualifier_DNF=pywikibot.page.Claim(self.site, 'P1534', is_qualifier=True)
                               qualifier_DNF.setTarget(target_DNFqual)
                               claim.addQualifier(qualifier_DNF)
                           else:
                               target_qualifier =  pywikibot.WbQuantity(amount=cyclist.rank, site=self.site)
                               qualifier_rank=pywikibot.page.Claim(self.site, 'P1352', is_qualifier=True)
                               qualifier_rank.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_rank)
                        if not self.force_nation_team and self.prologue_or_final!=1: #when only national team, no national tricot
                            #to avoid being called every time, should be centralized
                            grt=GetRiderTricot(cyclist.id, self.time_of_race, claim, self.chrono, self.man_or_woman)
                            grt.main()
                #all riders are classified, assumption the other are DNF
                if self.prologue_or_final==1:
                    for e in list_of_lost:
                        qualifier_DNF=pywikibot.page.Claim(self.site, 'P1534', is_qualifier=True)
                        qualnotfound=True
                        for qual in e.qualifiers.get('P1534', []):
                            qualnotfound=False
                        if qualnotfound:
                            qualifier_DNF.setTarget(target_DNFqual)
                            e.addQualifier(qualifier_DNF)
            return 0, self.log                          
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            self.log.concat("General Error in startlist_importer")
            return 10, self.log     
