#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
import pywikibot
from .base import CyclingInitBot
from .func import table_reader, cyclists_table_reader

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
                            team=self.UCIranking,
                            year=self.year,
                            convert_team_code=True,
                            result_points=True)
            self.log.concat(log)
    
            #post-processing
            points_bool=False #note: Team Code is there, otherwise uci_classification sends an error
            if "Points" in df.columns:
                points_bool=True
    
    
            self.log.concat('result_table created')
           
            list_of_cyclists, list_of_teams=cyclists_table_reader(df)

            if not all_riders_found and self.bypass==False:
                self.log.concat(u'Not all riders found, request stopped')
                return 1, self.log
            
            if (not all_teams_found and self.UCIranking) and self.bypass==False:
                self.log.concat(u'Not all teams found, request stopped')
                return 1, self.log           
        
            #fill the rider
            if not self.test:
                for this_rider, ii in enumerate(list_of_cyclists):
                    row=df.iloc[ii]
                    
                    if this_rider.id not in ['Q0','Q1']:
                        if not self.cleaner:
                            #action in the rider 
                            Addc=True
                            if(u'P1344' in this_rider.item.claims):
                                 for e in this_rider.item.claims.get(u'P1344'):
                                    if e.getTarget().getID() == self.id_master_UCI:  # Already there
                                        Addc = False
                                        self.log.concat('Item already in the Master list')
                            #no property or not there
                            if Addc:
                               #add the calendar to P1344
                               claim = pywikibot.Claim(self.repo, u'P1344')
                               item_to_add = pywikibot.ItemPage(self.repo, self.id_master_UCI)
                               claim.setTarget(item_to_add)
                               this_rider.item.addClaim(claim, summary=u'Adding classification')
                               
                               qualifier_rank = pywikibot.page.Claim(self.site, 'P1352', is_qualifier=True)
                               target_qualifier = pywikibot.WbQuantity(amount=this_rider.rank, site=self.site) #repo
                               qualifier_rank.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_rank)
                               
                               if points_bool:
                                   qualifier_points = pywikibot.page.Claim(self.site, 'P1358', is_qualifier=True)
                                   target_qualifier = pywikibot.WbQuantity(amount=row["Points"], site=self.site)
                                   qualifier_points.setTarget(target_qualifier)
                                   claim.addQualifier(qualifier_points)
            
                            #action in the team, only for UCI ranking up to now
                            if self.UCIranking:
                                this_team=list_of_teams[ii]
                                if this_team.id not in ['Q0','Q1']:
                                    Addc=True
                                    if(u'P3494' in this_team.item.claims):
                                        for e in this_team.item.claims.get(u'P3494'):
                                            if e.getTarget().getID() == this_rider.id:  # Already there
                                                Addc = False
                                                self.log.concat('Item already in the Master list')
                                    #no property or not there
                                    if Addc:
                                       claim = pywikibot.Claim(self.repo, u'P3494')
                                       claim.setTarget(this_rider.item)
                                       this_team.item.addClaim(claim, summary=u'Adding classification')
                                       
                                       qualifier_rank = pywikibot.page.Claim(
                                               self.site, 'P1352', is_qualifier=True)
                                       target_qualifier = pywikibot.WbQuantity(
                                               amount=this_rider.rank, site=self.site)
                                       qualifier_rank.setTarget(target_qualifier)
                                       claim.addQualifier(qualifier_rank)
                                       
                                       if points_bool:
                                           qualifier_points = pywikibot.page.Claim(
                                                   self.site, 'P1358', is_qualifier=True)
                                           target_qualifier = pywikibot.WbQuantity(amount=row["Points"],
                                                                                   site=self.site)
                                           qualifier_points.setTarget(target_qualifier)
                                           claim.addQualifier(qualifier_points)
                        else: #cleaner
                            this_rider.delete_value(u'P1344', self.id_master_UCI, 'cleaning')
            
            return 0, self.log
        except Exception as msg:
            print(msg)
            self.log.concat("General Error in UCI ranking")
            return 10, self.log        
        except:
            self.log.concat("General Error in UCI ranking")
            return 10, self.log    