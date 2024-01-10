#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
import pywikibot
from .base import CyclingInitBot, Team
from .func import table_reader, cyclists_table_reader
import traceback

class UCIClassification(CyclingInitBot):
    def __init__(self,
                 UCIranking:bool=False,
                 man_or_woman:str=None,
                 file:str=None,
                 fc:int=None,
                 id_master_UCI:str=None,
                 bypass:bool=False,
                 cleaner:bool=False,
                 year:int=None,
                 pcs_link: str=None,
                 fc_rank: int=None,
                 page: int=None,
                 date_rank: str=None,
                 **kwargs):
        '''
        Insert the yearly UCI ranking into the team items

        Parameters
        ----------
        UCIranking : str, optional
            Is it the UCI ranking that will be inserted --> then fill also the team  
        man_or_woman : str, optional
            age category and gender of the races to be created
        file : str, optional
            name of the file to be read
        fc : int, optional
            Id in firstcycling
        id_master_UCI : str, optional
            id in wikidata of the UCI calendar to fill
        bypass : bool, optional
            To bypass the completeness check
        cleaner : bool, optional
            to remove the last insertion of this function
        year : int, optional
        pcs_link: str
            Link to Procyclingstats to be parsed
        fc_rank : int, optional
            Number of the ranking  
        page: int, optional
            To get next page of the ranking
        date_rank: str, optional
            String for the date of the ranking
        '''
        super().__init__(**kwargs)
        
        for k in ["UCIranking","man_or_woman","file","fc","id_master_UCI",
                  "bypass","cleaner","year","pcs_link","fc_rank",
                 "date_rank","page" ]:
            setattr(self,k,locals()[k])
            
    def main(self):
        #Check the non optional arguments, done like that otherwise it is difficult to find which position arg is what
        if self.man_or_woman is None or (self.file is None and self.pcs_link is None and (self.fc_rank is None or self.date_rank is None)) or\
           self.id_master_UCI is None or self.year is None:
               raise ValueError("Missing mandatory input by UCI classification")
               self.log.concat("Missing mandatory input by UCI classification")
               return 10, self.log

class UCITeamClassification(UCIClassification):
    def main(self):
        '''
        Main function of this script
        '''
        try:
            super().main()
            df, _, all_teams_found,log=table_reader(
                            self.file,
                            self.fc,
                            verbose=False,                                 
                            team=True,
                            year=self.year,
                            convert_team_code=True,
                            need_complete=not self.bypass,
                            result_points=True,
                            man_or_woman=self.man_or_woman,
                            pcs_link=self.pcs_link,
                            fc_rank=self.fc_rank,
                            page=self.page,
                            date_rank=self.date_rank)  
            
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
        except:
            self.log.concat("General Error in UCI team ranking")
            self.log.concat(traceback.format_exc())
            return 10, self.log        
                
class UCIRiderClassification(UCIClassification):
    def main(self):
        '''
        Main function of this script
        '''
        try:
            #Check the non optional arguments, done like that otherwise it is difficult to find which position arg is what
            super().main()
            df, all_riders_found, all_teams_found,log=table_reader(
                            self.file,
                            self.fc,
                            verbose=False,                                 
                            rider=True, 
                            team=True,
                            year=self.year,
                            convert_team_code=True,
                            need_complete=not self.bypass,
                            result_points=True,
                            man_or_woman=self.man_or_woman,
                            pcs_link=self.pcs_link,
                            fc_rank=self.fc_rank,
                            page=self.page,
                            date_rank=self.date_rank)
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
                    
                    if this_rider.id in ['Q0','Q1']:
                        this_team=list_of_teams[ii]
                        if this_team.id not in ['Q0','Q1'] and this_team.id not in team_done:
                            team_done.append(this_team.id) #avoid to put the wrong first rider                        
                    else:
                        if not self.cleaner:
                            Addc, claim=this_rider.add_values('P1344',self.id_master_UCI,'classification',False)
                            if Addc:
                               target_q = pywikibot.WbQuantity(amount=this_rider.rank, site=self.site) #repo
                               this_rider.add_qualifier(claim,'P1352',target_q)
                               
                               if points_bool:
                                    points=row["Points"] #float
                                    if points==int(points):
                                        points=int(points)
                                    target_q = pywikibot.WbQuantity(amount=points, site=self.site) #row["Points"] is normally already int
                                    this_rider.add_qualifier(claim,'P1358',target_q)
                                       
                            #First in the teamm
                            this_team=list_of_teams[ii]
                            if this_team.id not in ['Q0','Q1'] and this_team.id not in team_done:
                                #we assume that listofcyclist in sorted normally from 1st to last and that an additional sorting is not required
                                #add the ranking
                                _, claim=this_team.add_values('P1344',self.id_master_UCI,'classification',False)
                                if len(claim.qualifiers.get('P710', []))==0:
                                    this_team.add_qualifier(claim,'P710',this_rider.item)
                                    this_team.add_qualifier(claim,'P1545',str(this_rider.rank))
                                
                                team_done.append(this_team.id)
                                
                            if this_team.id not in ['Q0','Q1']:
                            #Whole ranking in the team, only for UCI ranking up to now
                                if self.UCIranking:
                                    Addc, claim=this_team.add_values('P3494',this_rider.id,'classification',False)
                                    if Addc:
                                        target_q = pywikibot.WbQuantity(amount=this_rider.rank, site=self.site)
                                        this_team.add_qualifier(claim,'P1352',target_q)
                                       
                                        if points_bool:
                                           target_q =pywikibot.WbQuantity(amount=row["Points"],site=self.site)
                                           this_team.add_qualifier(claim,'P1358',target_q)
                        else: #cleaner
                            this_rider.delete_value(u'P1344', self.id_master_UCI, 'cleaning')
            
            return 0, self.log
        except:
            self.log.concat("General Error in UCI ranking")
            self.log.concat(traceback.format_exc())
            return 10, self.log        
