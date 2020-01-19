#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:38:20 2019

@author: maxime
"""
from cycling_init_bot_low import * 

def get_rider_tricot(pywikibot,site,repo,id_rider,time_of_race,claim,chrono):
    #look for the tricot of rider
    def disambiguation(this_champ, ischamp, result_table,result_dic, row_count, road_or_clm, time_of_race):
        if this_champ!=0 and ischamp==0:
            for ii in range(1,row_count):
                if result_table[ii][result_dic[road_or_clm +' champ'][1]]==this_champ:
                    this_day=int(result_table[ii][result_dic[road_or_clm +' day'][1]])
                    this_month=int(result_table[ii][result_dic[road_or_clm +' month'][1]])
                    this_year=int(result_table[ii][result_dic[road_or_clm +' year'][1]])
                    this_date=pywikibot.WbTime(site=site,year=this_year, month=this_month, day=this_day, precision='day')    
                    if this_date.year==time_of_race.year:
                        if compare_dates(time_of_race,this_date)==1:   
                            return -1
            #no other championship found, and he is champion of one year
            return 1
        elif ischamp==1:
            return 1
        elif this_champ==0:
            return -1
        return 0 #nothing           
    
    def insert_quali(site,repo,quali,claim):
        if quali!=0:  
           target_qualifier = pywikibot.ItemPage(repo, quali)
           qualifier_tricot=pywikibot.page.Claim(site, 'P2912', is_qualifier=True)
           qualifier_tricot.setTarget(target_qualifier)
           claim.addQualifier(qualifier_tricot)  
  
    def sub_function(result_table,result_dic,road_or_clm,id_worldchamp,id_eurchamp, time_of_race,repo,claim):
            worldchamp=0 #0 is we don't know, 1 is yes, -1 is no
            eurchamp=0
            champ=0
            isworldchamp=0
            iseurchamp=0
            ischamp=0
            quali=0
            this_day=int(result_table[ii][result_dic[road_or_clm +' day'][1]])
            this_month=int(result_table[ii][result_dic[road_or_clm +' month'][1]])
            this_year=int(result_table[ii][result_dic[road_or_clm +' year'][1]])
            this_date=pywikibot.WbTime(site=site,year=this_year, month=this_month, day=this_day, precision='day')    
            this_champ=result_table[ii][result_dic[road_or_clm +' champ'][1]]

            if compare_dates(time_of_race,this_date)==1 and time_of_race.year<=(this_date.year+1):
                    #time_of_race>timeofroad and time_of_race<=timeofroad+1 year
                    #if race after championship
                        if id_worldchamp==this_champ:
                            worldchamp=this_champ
                        elif id_eurchamp==this_champ:
                            eurchamp=this_champ
                        else:
                            champ=this_champ
                        if this_date.year==time_of_race.year:  #then it is clear
                            if worldchamp!=0:
                                isworldchamp=1
                            elif eurchamp!=0:
                                iseurchamp=1
                            else:
                                ischamp=1

            ischamp=disambiguation(champ, ischamp, result_table, row_count, road_or_clm, time_of_race)
            isworldchamp=disambiguation(worldchamp, isworldchamp, result_table, row_count, road_or_clm, time_of_race)
            iseurchamp=disambiguation(eurchamp, iseurchamp, result_table, row_count, road_or_clm, time_of_race)

            if isworldchamp==1:
                print('this is the world ' + road_or_clm + ' champ')
                quali=worldchamp
            elif iseurchamp==1:
               print('this is the european ' + road_or_clm + ' champ')  
               quali=eurchamp
            elif ischamp==1:
               print('this is the ' + road_or_clm + ' champ')
               quali=champ
            insert_quali(site,repo,quali,claim)
         
    result_dic={
    'Road champ':[-1, 0,''],
    'Road day':[-1, 1,''],
    'Road month':[-1, 2,''],
    'Road year':[-1, 3,''],
    'Road winner':[-1, 4,''],
    'Clm champ':[-1, 5,''],
    'Clm day':[-1, 6,''],
    'Clm month':[-1, 7,''],
    'Clm year':[-1, 8,''],
    'Clm winner':[-1, 9,''],
    }

    id_worldroadchamp=u'Q2630733'
    id_eurroadchamp=u'Q30894544'
    id_worldclmchamp=u'Q2630733'
    id_eurclmchamp= u'Q30894543'
    
    result_table, row_count, ecart=table_reader('input/Champ.csv',result_dic,0,False)
    
    for ii in range(row_count):
        if id_rider==result_table[ii][result_dic['Road winner'][1]]:
            sub_function(result_table,result_dic,'Road',id_worldroadchamp,id_eurroadchamp, time_of_race,repo,claim)
       
        if chrono:   
            if id_rider==result_table[ii][result_dic['Clm winner'][1]]:
                sub_function(result_table,result_dic,'Clm',id_worldclmchamp,id_eurclmchamp, time_of_race,repo,claim)
 