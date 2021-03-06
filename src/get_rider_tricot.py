#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:38:20 2019

@author: maxime
"""
from .cycling_init_bot_low import (compare_dates, table_reader, cyclists_table_reader,
                                   get_label, get_date)
from .bot_log import Log
                                   
def f(pywikibot,site,repo,id_rider,time_of_race,claim,chrono, man_or_woman, **kwargs):
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
  
    def sub_function(result_table,result_dic,road_or_clm,id_worldchamp,id_eurchamp,
                     time_of_race,repo,claim,test,id_rider):
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

            ischamp=disambiguation(champ, ischamp, result_table, result_dic, row_count, road_or_clm, time_of_race)
            isworldchamp=disambiguation(worldchamp, isworldchamp, result_table, result_dic, row_count, road_or_clm, time_of_race)
            iseurchamp=disambiguation(eurchamp, iseurchamp, result_table, result_dic, row_count, road_or_clm, time_of_race)

            if isworldchamp==1 or iseurchamp==1 or ischamp==1:
                item_rider =pywikibot.ItemPage(repo, id_rider)
                item_rider.get() 
                rider_label=get_label('fr', item_rider)
            if isworldchamp==1:
                print(rider_label+' is the world ' + road_or_clm + ' champ')
                quali=worldchamp
            elif iseurchamp==1:
               print(rider_label+' is the european ' + road_or_clm + ' champ')  
               quali=eurchamp
            elif ischamp==1:
               print(rider_label+' is the ' + road_or_clm + ' champ')
               quali=champ
            else:
                return 0
            if not test:
                insert_quali(site,repo,quali,claim)
            return quali
            
    result_dic={
    'road champ':[-1, 0,''],
    'road day':[-1, 1,''],
    'road month':[-1, 2,''],
    'road year':[-1, 3,''],
    'road winner':[-1, 4,''],
    'clm champ':[-1, 0,''],
    'clm day':[-1, 1,''],
    'clm month':[-1, 2,''],
    'clm year':[-1, 3,''],
    'clm winner':[-1, 4,''],
    }

    id_worldroadchamp=u'Q934877'
    id_eurroadchamp=u'Q30894544'
    id_worldclmchamp=u'Q2630733'
    id_eurclmchamp= u'Q30894543'
    
    test=kwargs.get('test',False)
    #road champ
    if man_or_woman==u'woman':
        result_table, row_count, ecart=table_reader('champ',result_dic,0,False)
    else:
        result_table, row_count, ecart=table_reader('champ_man',result_dic,0,False)
     
    for ii in range(row_count):
        if id_rider==result_table[ii][result_dic['road winner'][1]]: #potential candidate
            result=sub_function(result_table,result_dic,'road',id_worldroadchamp,id_eurroadchamp, 
                                time_of_race,repo,claim,test,id_rider)
            if test and result!=0:
                return result
   
    #clm
    if chrono:   
        if man_or_woman==u'woman':
            result_table, row_count, ecart=table_reader('champ_clm',result_dic,0,False)
        else:
            result_table, row_count, ecart=table_reader('champ_man_clm',result_dic,0,False)

        for ii in range(row_count):
            if id_rider==result_table[ii][result_dic['clm winner'][1]]:
                result=sub_function(result_table,result_dic,'clm',id_worldclmchamp,id_eurclmchamp,
                                    time_of_race,repo,claim,test,id_rider)
                if test and result!=0:
                    return result
    if test:
        return 0

def scan(pywikibot,site,repo,id_race, time_of_race,chrono, test,man_or_woman):
    
    result_dic={
    'rank':[-1, 0, ''],
    'last name':[-1, 1,''],
    'first name':[-1, 2,''],
    'name':[-1, 3,''],
    'result':[-1, 4,'time'],  #startlist only with time
    'points':[-1, 5, 'points'],
    'team code':[-1, 7, ''],
    'ecart':[1,6,'time'],  #always created
    'bib':[-1,8,''] #dossard
    }
    
    log=Log()
    result_table, row_count, ecart=table_reader('Results', result_dic,0,True)
    #Sort by dossard
    result_table=sorted(result_table, key=lambda tup: int(tup[8]))
    log.concat('table read and sorted')
    list_of_cyclists, all_riders_found, cycling_log, list_of_teams, all_teams_found=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, nosortkey=True)
    if not test:
         item =pywikibot.ItemPage(repo, id_race)
         item.get() 

         for ii in range(row_count):
            if list_of_cyclists[ii].id_item!='Q0' and list_of_cyclists[ii].id_item!='Q1':
                this_rider=list_of_cyclists[ii]
                claim=pywikibot.Claim(repo, u'P710')  #reinit everytime
                f(pywikibot,site,repo,this_rider.id_item,time_of_race,claim,chrono,man_or_woman)
             
def scan_existing(pywikibot,site,repo,id_race, chrono, test,man_or_woman):

    item =pywikibot.ItemPage(repo, id_race)
    item.get()     
    time_of_race=get_date(pywikibot, repo, id_race)
    
    if(u'P710' in item.claims): 
        startlist=item.claims.get(u'P710')
        
        for ii in range(len(startlist)):
            claim=pywikibot.Claim(repo, u'P710')
            rider_id=startlist[ii].getTarget().getID()
            item_rider=pywikibot.ItemPage(repo, rider_id)
            item_rider.get()
            claim.setTarget(item_rider)
            f(pywikibot,site,repo,rider_id,time_of_race,claim,chrono,man_or_woman)
