# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

import pywikibot
from .base import CyclingInitBot, Race
from .func import table_reader
import math
import sys

class ClassificationImporter(CyclingInitBot):
    def __init__(self, general_or_stage, id_race,
                       final, maxkk,**kwargs):
        super().__init__(**kwargs)
        self.general_or_stage=general_or_stage
        self.race=Race(id=id_race)
        self.final=final
        self.maxkk=maxkk

        self.verbose=False
        
        self.there_is_a_startlist=False
        self.in_parent=False
        self.startlist=None
        
        self.year=kwargs.get('year',None)
        self.man_or_woman=kwargs.get('man_or_woman',u'woman')
        self.startliston=kwargs.get('startliston',True)
        self.file=kwargs.get('file','Results')
        #code
        self.general_or_stage_addwinner=[0, 2, 3,4]
        
        general_or_stage_prop={
               0:'P2321', #general
               1:'P2417',#stage
               2:'P3494',#points
               3:'P4320',#mountains
               4:'P4323',#youth 
               5:'P3497',#teamtime
               6:'P3496',#team points   
               7:'P4323',#youth points
               8:'P4322'#sprint 
               }
        
        if general_or_stage in general_or_stage_prop:
            self.prop=general_or_stage_prop[general_or_stage]  
            
        if self.general_or_stage in [2,3,6,7,8]:
            self.result_points=True
        else:
            self.result_points=False
            
        if self.general_or_stage in [5,6]:
            self.team_bool=True
        else:
            self.team_bool=False
            
    def is_there_a_startlist(self):
        item_with_startlist=None
        
        if (not self.team_bool) and self.startliston:
            if(u'P710' in self.race.item.claims): 
                item_with_startlist=self.race.item
            elif (u'P361' in self.race.item.claims):
                list_of_comprend=self.race.item.claims.get(u'P361')
                parent=list_of_comprend[0].getTarget()
                parent.get()
                if(u'P710' in parent.claims): 
                    item_with_startlist=parent
                    self.in_parent=True
           
            if item_with_startlist is not None:
                self.startlist=item_with_startlist.claims.get(u'P710')
        
        if self.test:
            return self.startlist, self.in_parent
                
    def copy_team(self, claim, target):
         this_starter=None
         this_starter_id=None
         team=None
         
         if self.startlist is not None:
             for starter in self.startlist:
                 if starter.getTarget()==target: #Already there
                     this_starter=starter
                     break
         if this_starter is not None:
             for qual in this_starter.qualifiers.get('P54', []):
                 team=qual.getTarget().getID()
                 qualifier_team=pywikibot.page.Claim(self.site, 'P54', is_qualifier=True)
                 qualifier_team.setTarget(qual.getTarget())
                 if not self.test:
                     claim.addQualifier(qualifier_team)
         if self.test:
             if this_starter is not None:
                 this_starter_id=this_starter.getTarget().getID()
             return this_starter_id, team
         
    def put_dnf_in_startlist(self,df):
        stage_nummer=-1
        if(u'P1545' in self.race.item.claims):  
            list_of_order=self.race.item.claims.get(u'P1545')
            stage_nummer=str(list_of_order[0].getTarget())
        
        sub_df=df[df['Rank'].apply(lambda x: math.isnan(x))]

        for ii in range(len(sub_df)):
            this_id=sub_df["ID Rider"].values[ii]

            if this_id not in ['Q1','Q0']:
                target = pywikibot.ItemPage(self.repo, this_id)
                this_starter=None
                for starter in self.startlist:
                   if starter.getTarget()==target: #Already there
                        this_starter=starter
                        break
                    
                if this_starter!=None:
                     qualnotfound=True
                     for qual in this_starter.qualifiers.get('P1534', []):
                         qualnotfound=False
                     if qualnotfound:
                         target_qualifier = pywikibot.ItemPage(self.repo, u'Q1210380')
                         qualifier_DNF=pywikibot.page.Claim(self.site, 'P1534', is_qualifier=True)
                         qualifier_DNF.setTarget(target_qualifier)
                         if not self.test:
                             this_starter.addQualifier(qualifier_DNF)
                     #add the stage_number of the DNF       
                     qualnotfound=True
                     for qual in this_starter.qualifiers.get('P1545', []):
                         qualnotfound=False 
                     if qualnotfound and stage_nummer!=-1:   
                         qualifier_stage_number=pywikibot.page.Claim(self.site, 'P1545', is_qualifier=True)
                         qualifier_stage_number.setTarget(stage_nummer)
                         if not self.test:
                             this_starter.addQualifier(qualifier_stage_number)
                     if self.test and stage_nummer!=-1: 
                         return this_starter, stage_nummer #return first dnf rider
        if self.test:
            return None, -1                       

    def main(self):
        try:
            if self.year is None:
                self.year=self.race.get_year()
            if self.year is None:
                raise ValueError('no year found')
            
            if self.team_bool: #team
                df, _, _, log=table_reader(self.file,result_points=self.result_points, team=True, 
                                           year=self.year,convert_team_code=True) 
            else: #rider
                df, _, _, log=table_reader(self.file,result_points=self.result_points, rider=True,
                                           year=self.year) 
            self.log.concat(log)
            
            df2=df.iloc[:self.maxkk]
            self.log.concat('result_table created')
            if self.verbose:
                print(df2)
                
            self.is_there_a_startlist()
            if self.startlist is not None:
                self.log.concat('startlist found')
            
            if not self.test:
                if(self.prop in self.race.item.claims):  #already there do nothing
                    self.log.concat(u'Classification already there')
                else: 
                    claim=pywikibot.Claim(self.repo, self.prop)  
                    for ii in range(len(df2)):
                        row=df2.iloc[ii]
                        if self.team_bool:
                            this_id=row["ID Team"]
                        else:
                            this_id=row["ID Rider"]

                        if this_id not in ['Q0','Q1']:
                           claim=pywikibot.Claim(self.repo, self.prop)  
                           target = pywikibot.ItemPage(self.repo, this_id)
                           claim.setTarget(target)
                           self.race.item.addClaim(claim, summary=u'Adding classification')
                           qualifier_rank=pywikibot.page.Claim(self.site, 'P1352', is_qualifier=True)
                           target_qualifier =  pywikibot.WbQuantity(amount=row['Rank'], site=self.site)
                           qualifier_rank.setTarget(target_qualifier)
                           claim.addQualifier(qualifier_rank)
                           itemSeconds=pywikibot.ItemPage(self.repo, "Q11574")
                           if self.result_points:
                               qualifier_points=pywikibot.page.Claim(self.site, 'P1358', is_qualifier=True)
                               target_qualifier = pywikibot.WbQuantity(amount=row['Points'], site=self.site)
                               qualifier_points.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_points)
                           elif row['Rank']==1:
                               qualifier_time=pywikibot.page.Claim(self.site, 'P2781', is_qualifier=True)
                               target_qualifier = pywikibot.WbQuantity(amount=row['Time'], site=self.site, unit=itemSeconds)
                               qualifier_time.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_time)
                           else:
                               if row['Ecart']!=-1:
                                   qualifier_ecart=pywikibot.page.Claim(self.site, 'P2911', is_qualifier=True)
                                   target_qualifier = pywikibot.WbQuantity(amount=row['Ecart'], site=self.site, unit=itemSeconds)
                                   qualifier_ecart.setTarget(target_qualifier)
                                   claim.addQualifier(qualifier_ecart)
                           #look for team in startlist
                           if self.startlist is not None:
                               self.copy_team(claim, target)
        
                           if (self.general_or_stage in self.general_or_stage_addwinner) and self.final:
                               self.race.add_winner(this_id,row['Rank'],self.general_or_stage) 
                               
                        else:
                           if 'Name' in row:
                               self.log.concat(row['Name'])
                           elif 'First Name' in row:
                               self.log.concat(row['First Name'] + " " + row['Last Name'])
                           self.log.concat(u'item not found, interrupted')
                           return 0, self.log
                self.log.concat('result inserted')
                #fill startlist with DNF, HD and so on
                if self.startlist is not None and not self.team_bool and self.general_or_stage==1:
                    self.log.concat('completion of startlist with DNF')
                    self.put_dnf_in_startlist(df)
                    self.log.concat('completion of startlist with DNF finished')
                return 0, self.log                          
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            self.log.concat("General Error in classification_importer")
            return 10, self.log  
