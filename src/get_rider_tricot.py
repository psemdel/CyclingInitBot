#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:38:20 2019

@author: maxime
"""

import pywikibot
from .base import CyclingInitBot, Cyclist, Race
from .func import table_reader,cyclists_table_reader

class GetRiderTricot(CyclingInitBot):
    def __init__(self, id_rider,time_of_race,claim,chrono, man_or_woman,**kwargs):
        super().__init__(**kwargs)
        self.rider=Cyclist(id=id_rider)
        self.time_of_race=time_of_race
        self.claim=claim
        self.chrono=chrono
        self.man_or_woman=man_or_woman
 
    def insert_quali(self,quali):
        if quali is not None:  
           target_qualifier = pywikibot.ItemPage(self.repo, quali)
           qualifier_tricot=pywikibot.page.Claim(self.site, 'P2912', is_qualifier=True)
           qualifier_tricot.setTarget(target_qualifier)
           self.claim.addQualifier(qualifier_tricot) 
          
    def sub_function(self):
        #candidate
        quali=None
        dic={}
        list_=["World","CC","National"]

        if self.road_or_clm=='Road':
            dic["World"]='Q934877'
            dic["CC"]='Q30894543'
        else:
            dic["World"]='Q2630733'
            dic["CC"]='Q30894543'

        if self.road_or_clm=="Clm":
            sub_df1=self.df[self.df["Clm"]==True]
        else:
            sub_df1=self.df[self.df["Clm"]==False]

        sub_df=sub_df1[sub_df1["Winner"]==self.rider.id]
        sub_df=sub_df[sub_df["Year"]>=self.time_of_race.year-1] #champ not too much in the past

        dates_ok=[]
        
        for ii in range(len(sub_df)):
            this_date=pywikibot.WbTime(site=self.site,
                                       year=sub_df["Year"].values[ii], 
                                       month=sub_df["Month"].values[ii], 
                                       day=sub_df["Day"].values[ii], 
                                       precision='day')  
            if this_date.toTimestamp()<self.time_of_race.toTimestamp():
                dates_ok.append(True)
            else:
                dates_ok.append(False)
        sub_df=sub_df[dates_ok]
      
        if len(sub_df)>0:
            for k in list_:
                if k in ["World","CC"]:
                    sub_df2=sub_df[sub_df["Champ"]==dic[k]]
              #      print("worldCC")
              #      print(sub_df2)
                else:
                    sub_df2=sub_df[(sub_df["Champ"]!=dic["World"])&(sub_df["Champ"]!=dic["CC"])]
                    
                if len(sub_df2)>1:
                    sub_df2=sub_df2[sub_df2["Year"]==self.time_of_race.year]

                if len(sub_df2)>0:
                    if int(sub_df2['Year'])==self.time_of_race.year: #then it is clear
                        quali=sub_df["Champ"].values[0]
                    else: #not clear, look for a championship this year
                        sub_df3=sub_df1[sub_df1["Champ"]==sub_df["Champ"].values[0]]
                        sub_df3=sub_df3[sub_df3["Year"]==self.time_of_race.year]
                        if len(sub_df3)>0:
                            this_date=pywikibot.WbTime(site=self.site,
                                                       year=int(sub_df3["Year"]), 
                                                       month=int(sub_df3["Month"]), 
                                                       day=int(sub_df3["Day"]), 
                                                       precision='day')    
                            
                            if this_date.toTimestamp()>=self.time_of_race.toTimestamp(): #otherwise it is another champ
                                quali=sub_df["Champ"].values[0]
    
                        else:
                            quali=sub_df["Champ"].values[0]
                     
                if quali is not None:    
                    rider_label=self.rider.get_label('fr')
                    print(rider_label+' is the ' + k + " " + self.road_or_clm + ' champ')
                    if not self.test:
                        self.insert_quali(quali)
                    else:
                        return quali
                    break
        return None
            
    def main(self):
        #road champ
        self.road_or_clm='Road'
        result=None
        
        if self.man_or_woman==u'woman':
            self.df,_,_,_=table_reader('champ')
        else:
            self.df,_,_,_=table_reader('champ_man')
     
        result=self.sub_function()
        if self.test and result is not None:
            return result
   
        #clm
        result=None
        if self.chrono: 
            self.road_or_clm='Clm'
            result=self.sub_function()
            if self.test and result is not None:
                return result

        if self.test:
            return 0

class Scan(CyclingInitBot):
    def __init__(self, id_race, chrono, man_or_woman):
        super().__init__()   
        self.race=Race(id=id_race)
        self.time_of_race=self.race.get_date()
        self.chrono=chrono
        self.man_or_woman=man_or_woman
        
    def main(self):
        df,_,_,_=table_reader('Results')
        #Sort by dossard
        if "BIB" in df.columns:
            df=df.sort_values(["BIB"])
        else:
            raise ValueError("BIB not present in import file")
        self.log.concat('table read and sorted')
        list_of_cyclists, _,= cyclists_table_reader(df)
        
        if not self.test:
            for cyclist in list_of_cyclists:
                if cyclist.id not in ['Q0','Q1']:
                    grt=GetRiderTricot(cyclist.id,
                                   self.time_of_race,
                                   pywikibot.Claim(self.repo, u'P710'),
                                   self.chrono,
                                   self.man_or_woman
                                   )
                    grt.main()
                    

class ScanExisting(CyclingInitBot):
    def __init__(self, id_race, chrono, man_or_woman):
        super().__init__()   
        self.race=Race(id=id_race)
        self.time_of_race=self.race.get_date()
        self.chrono=chrono
        self.man_or_woman=man_or_woman
        
    def main(self):
        if(u'P710' in self.race.item.claims): 
            startlist=self.race.claims.get(u'P710')
            
            for c in startlist:
                cyclist=Cyclist(id=c.getTarget().getID())
                claim=pywikibot.Claim(self.repo, u'P710')
                claim.setTarget(cyclist.item)
                grt=GetRiderTricot(cyclist.id,
                               self.time_of_race,
                               claim,
                               self.chrono,
                               self.man_or_woman
                               )
                grt.main()

