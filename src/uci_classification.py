#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
import pywikibot
import sys
from .base import CyclingInitBot, Team
from .func import table_reader, cyclists_table_reader

class UCITeamClassification(CyclingInitBot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.man_or_woman=kwargs.get("man_or_woman",None)
        self.filename=kwargs.get("filename",None)
        self.id_master_UCI=kwargs.get("id_master_UCI",None)
        self.bypass=kwargs.get("bypass",False)
        self.cleaner=kwargs.get("cleaner",False)
        self.year=kwargs.get("year",None)
        
    def main(self):
        try:
            #Check the non optional arguments, done like that otherwise it is difficult to find which position arg is what
            if self.man_or_woman is None or self.filename is None or\
               self.id_master_UCI is None or self.year is None:
                   raise ValueError("Missing mandatory input by UCI classification")
                   self.log.concat("Missing mandatory input by UCI classification")
                   return 10, self.log
               
            df, _, all_teams_found,log=table_reader(self.filename,
                            verbose=False,                                 
                            team=True,
                            year=self.year,
                            convert_team_code=True,
                            need_complete=not self.bypass,
                            result_points=True)   
            self.log.concat(log)
                
            if not all_teams_found and self.bypass==False:
                self.log.concat(u'Not all teams found, request stopped')
                return 1, self.log 
            
            print("starting introduction")
            if not self.test:
                for ii in range(len(df)):
                    row=df.iloc[ii]
                    if row["ID Team"] not in ['Q0','Q1']:
                        this_team=Team(id=row["ID Team"])
                        
                        if row['Rank']:
                            _, claim=this_team.add_values('P1344',self.id_master_UCI,'classification',False)
                            target_q = pywikibot.WbQuantity(amount=row['Rank'], site=self.site)
                            this_team.add_qualifier(claim,'P1352',target_q)
                   
            return 0, self.log
        except Exception as msg:
            print(msg)
            self.log.concat("General Error in UCI team ranking")
            return 10, self.log        
        except:
            self.log.concat("General Error in UCI team ranking")
            return 10, self.log    
                
class UCIClassification(CyclingInitBot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.UCIranking=kwargs.get("UCIranking",False)
        self.man_or_woman=kwargs.get("man_or_woman",None)
        self.filename=kwargs.get("filename",None)
        self.id_master_UCI=kwargs.get("id_master_UCI",None)
        self.bypass=kwargs.get("bypass",False)
        self.cleaner=kwargs.get("cleaner",False)
        self.year=kwargs.get("year",None)

    def main(self):
        try:
            #Check the non optional arguments, done like that otherwise it is difficult to find which position arg is what
            if self.man_or_woman is None or self.filename is None or\
               self.id_master_UCI is None or self.year is None:
                   raise ValueError("Missing mandatory input by UCI classification")
                   self.log.concat("Missing mandatory input by UCI classification")
                   return 10, self.log

            
            df, all_riders_found, all_teams_found,log=table_reader(self.filename,
                            verbose=False,                                 
                            rider=True, 
                            team=True,
                            year=self.year,
                            convert_team_code=True,
                            need_complete=not self.bypass,
                            result_points=True)
            self.log.concat(log)
    
            #post-processing
            points_bool=False #note: Team Code is there, otherwise uci_classification sends an error
            if "Points" in df.columns:
                points_bool=True
    
            self.log.concat('result_table created')
           
            if not all_riders_found and self.bypass==False:
                self.log.concat(u'Not all riders found, request stopped')
                return 1, self.log
            
            if not all_teams_found and self.bypass==False:
                self.log.concat(u'Not all teams found, request stopped')
                return 1, self.log     
           
            list_of_cyclists, list_of_teams=cyclists_table_reader(df)
            self.log.concat('cyclists_table_reader finished')
            
            team_done=[]
        
            #fill the rider
            if not self.test:
                for ii, this_rider in enumerate(list_of_cyclists):
                    row=df.iloc[ii]
                    
                    if this_rider.id not in ['Q0','Q1']:
                        if not self.cleaner:
                            Addc, claim=this_rider.add_values('P1344',self.id_master_UCI,'classification',False)
                            if Addc:
                               target_q = pywikibot.WbQuantity(amount=this_rider.rank, site=self.site) #repo
                               this_rider.add_qualifier(claim,'P1352',target_q)
                               
                               if points_bool:
                                    target_q = pywikibot.WbQuantity(amount=row["Points"], site=self.site) #row["Points"] is normally already int
                                    this_rider.add_qualifier(claim,'P1358',target_q)
                                       
                            #First in the teamm
                            this_team=list_of_teams[ii]
                            if this_team.id not in ['Q0','Q1'] and this_team.id not in team_done:
                                #we assume that listofcyclist in sorted normally from 1st to last and that an additional sorting is not required
                                #add the ranking
                                _, claim=this_team.add_values('P1344',self.id_master_UCI,'classification',False)
                                this_team.add_qualifier(claim,'P710',this_rider.item)
                                this_team.add_qualifier(claim,'P1545',str(this_rider.rank))
                                
                                team_done.append(this_team.id)
                                
                            if this_team.id not in ['Q0','Q1']:
                            #Whole ranking in the team, only for UCI ranking up to now
                                if self.UCIranking:
                                    Addc, claim=this_team.add_values('P3494',this_rider.item,'classification',False)
                                    if Addc:
                                        target_q = pywikibot.WbQuantity(amount=this_rider.rank, site=self.site)
                                        this_team.add_qualifier(claim,'P1352',target_q)
                                       
                                        if points_bool:
                                           target_q =pywikibot.WbQuantity(amount=row["Points"],site=self.site)
                                           this_team.add_qualifier(claim,'P1358',target_q)
                        else: #cleaner
                            this_rider.delete_value(u'P1344', self.id_master_UCI, 'cleaning')
            
            return 0, self.log
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            self.log.concat("line " + str(exc_tb.tb_lineno))
            self.log.concat(msg)
            self.log.concat("General Error in UCI ranking")
            return 10, self.log        
        except:
            _, _, exc_tb = sys.exc_info()
            self.log.concat("line " + str(exc_tb.tb_lineno))
            self.log.concat("General Error in UCI ranking")
            return 10, self.log    