# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

import pywikibot
from .base import CyclingInitBot, Race, Team, PyItem
from .func import table_reader, get_fc_dic
import math
import sys

class ClassificationImporter(CyclingInitBot):
    def __init__(self, general_or_stage, id_race,
                       maxkk,**kwargs):
        super().__init__(**kwargs)
        self.race=Race(id=id_race)
        self.maxkk=maxkk

        self.verbose=False
        
        self.there_is_a_startlist=False
        self.in_parent=False
        self.startlist=None
        
        self.year=kwargs.get('year',None)
        if self.year is None:
            self.year=self.race.get_year()

        self.is_women=self.race.get_is_women()
        self.startliston=kwargs.get('startliston',True)
        self.file=kwargs.get('file','Results')
        fc=kwargs.get("fc",None)
        if fc==0:
            fc=None
        self.fc=fc
        self.stage_num=kwargs.get("stage_num")

        self.general_or_stage_init(general_or_stage)
            
        #WWT functionality
        self.WWT=False
        if (u'P279' in self.race.item.claims):
            P279=self.race.item.claims.get(u'P279')
            for p279 in P279:
                if p279.getTarget().getID() in ["Q23005601","Q23005603"]: #WWT
                    self.WWT=True
                    
    def general_or_stage_init(self,general_or_stage):
        #code
        self.general_or_stage=general_or_stage
        self.general_or_stage_addwinner=[0, 2, 3,4,8]
        
        general_or_stage_prop={
               0:'P2321', #general
               1:'P2417',#stage
               2:'P3494',#points
               3:'P4320',#mountains
               4:'P4323',#youth 
               5:'P3497',#teamtime
               6:'P3496',#team points   
               7:'P4323',#youth points
               8:'P4322',#sprint 
               9:'P2321', #all
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
        
        sub_df=df[df['Rank'].apply(lambda x: (type(x)==str or math.isnan(x)))]

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
                     pyItem=PyItem(id=this_id) #does not really matter, we need a pyItem to call the method
                    
                     target_q = pywikibot.ItemPage(self.repo, u'Q1210380')
                     if not self.test:
                         pyItem.add_qualifier(this_starter,'P1534',target_q)

                     if stage_nummer!=-1: 
                         if not self.test:   
                             pyItem.add_qualifier(this_starter,'P1545',str(stage_nummer))
                         else:
                             return this_starter, stage_nummer #return first dnf rider
        if self.test:
            return None, -1  

    def run_all(self):
        general_or_stages=get_fc_dic(self.fc, year=self.year, stage_num=self.stage_num)

        for general_or_stage in general_or_stages:
            if len(general_or_stages)==1 and self.stage_num==None:
                general_or_stage=0 #for single day race
            
            self.general_or_stage_init(general_or_stage)
            print("run all, starting code: "+ str(self.general_or_stage))
            try:
                code, self.log=self.main()      
            except:
                print("routine :"+str(self.general_or_stage)+ " crashed, performing further other rankings")
                pass 
            
        return code, self.log

    def main(self):
        try:
            if self.year is None:
                self.year=self.race.get_year()
            if self.year is None:
                raise ValueError('no year found')
                
            if self.WWT and self.general_or_stage==0 and not self.race.get_is_stage():
                maxkk=None #we need full ranking here
            else:
                maxkk=self.maxkk
                
            if self.team_bool: #team
                df, _, _, log=table_reader(self.file,self.fc,result_points=self.result_points, team=True, 
                                           year=self.year,convert_team_code=True, is_women=self.is_women,
                                           stage_num=self.stage_num, general_or_stage=self.general_or_stage,
                                           maxkk=maxkk) 
            else: #if self.WWT: #rider, but team needed
                df, _, _, log=table_reader(self.file,self.fc,result_points=self.result_points, rider=True,team=True,
                                           year=self.year, is_women=self.is_women,
                                           stage_num=self.stage_num, general_or_stage=self.general_or_stage,
                                           maxkk=maxkk)   
            #else: #rider
#                df, _, _, log=table_reader(self.file,result_points=self.result_points, rider=True,
                    #                       year=self.year) 
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
                    #claim=pywikibot.Claim(self.repo, self.prop)  
                    for ii in range(len(df2)):
                        row=df2.iloc[ii]
                        if self.team_bool:
                            this_id=row["ID Team"]
                        else:
                            this_id=row["ID Rider"]

                        if this_id not in ['Q0','Q1']:
                           _, claim=self.race.add_values(self.prop, this_id, 'classification', False) 
                           target_q =  pywikibot.WbQuantity(amount=int(row['Rank']), site=self.site)
                           self.race.add_qualifier(claim,'P1352',target_q)
                           target = pywikibot.ItemPage(self.repo, this_id)

                           itemSeconds=pywikibot.ItemPage(self.repo, "Q11574")
                           if self.result_points:
                               target_q = pywikibot.WbQuantity(amount=row['Points'], site=self.site)
                               self.race.add_qualifier(claim,'P1358',target_q)
                           elif row['Rank']==1:
                               target_q = pywikibot.WbQuantity(amount=row['Time'], site=self.site, unit=itemSeconds)   
                               self.race.add_qualifier(claim,'P2781',target_q)
                           else:
                               if row['Ecart']!=-1:
                                   target_q = pywikibot.WbQuantity(amount=row['Ecart'], site=self.site, unit=itemSeconds)
                                   self.race.add_qualifier(claim,'P2911',target_q)
                           #look for team in startlist
                           if self.startlist is not None:
                               self.copy_team(claim, target)
        
                           if (self.general_or_stage in self.general_or_stage_addwinner) and not self.race.get_is_stage():
                              self.race.add_winner(this_id,int(row['Rank']),self.general_or_stage)
                           elif self.race.get_is_stage():
                               if self.general_or_stage==1:
                                   self.race.add_winner(this_id,int(row['Rank']),100) #stage winner
                               elif self.general_or_stage==0:
                                   self.race.add_winner(this_id,int(row['Rank']),101) #stage leader                             
                        else:
                           if 'Name' in row:
                               self.log.concat(row['Name'])
                           elif 'First Name' in row:
                               self.log.concat(row['First Name'] + " " + row['Last Name'])
                           self.log.concat(u'item not found, interrupted')
                           return 0, self.log
                  
                #add victory automatically to the team
                if (self.general_or_stage==0 and not self.race.get_is_stage()) or\
                   (self.general_or_stage==1 and self.race.get_is_stage()):
                    row=df[df['Rank'].astype('str')=='1.0'] 
                    if len(row)==0:
                        row=df[df['Rank'].astype('str')=='1'] 
                    
                    if "ID Team" in row and len(row["ID Team"].values)>0 and row["ID Team"].values[0] not in ['Q0','Q1']:
                        this_team=Team(id=row["ID Team"].values[0])
                        _, claim=this_team.add_values('P2522',self.race.id,'victory',False)
                        
                if self.WWT and self.general_or_stage==0 and not self.race.get_is_stage(): #add ranking in the team then, no contradiction with Classification already there
                    team_done=[]
                    for ii in range(len(df)): #no maxkk
                        row=df.iloc[ii]
                        if self.team_bool:
                            this_id=row["ID Team"]
                        else:
                            this_id=row["ID Rider"]
                        
                        if row["ID Team"] and row["ID Team"] not in ['Q0','Q1'] and \
                            row["ID Team"] not in team_done:
                            this_team=Team(id=row["ID Team"])
                            
                            _, claim=this_team.add_values('P1344',self.race.id,'classification',False)
                            this_team.add_qualifier(claim,'P710',pywikibot.ItemPage(self.repo, this_id))
                            try: #"DNF" will give an error
                                target_q =pywikibot.WbQuantity(amount=int(row['Rank']), site=self.site)
                                this_team.add_qualifier(claim,'P1352',target_q)
                            except:
                                pass
                            team_done.append(this_team.id)
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
