#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:35:53 2019

@author: maxime
"""
from .cycling_init_bot_low import get_label
import csv
from .bot_log import Log

def f(pywikibot,site,repo,time):
    
    def sub_findwinner(item_this_year,id_race,champ_table, result_dic, road_or_clm,ll):
          date_found=False
          invalid_precision=False
          there_is_a_winner=False
          warning_written=False
          offset=0
          champ_table[ll][result_dic[road_or_clm + ' champ']]=id_race
          
          if (u'P585' in item_this_year.claims):
             list_of_race_date=item_this_year.claims.get(u'P585')
             race_date=list_of_race_date[0].getTarget()
             if race_date.day==1 and race_date.month==1:
                 invalid_precision=True
             else:
                 date_found=True
          
          if (u'P1346' in item_this_year.claims): #winner
             winners=item_this_year.claims.get(u'P1346')
             for winner in winners:
                 id_this_qual=winner.qualifiers['P642'][0].getTarget().getID()
                 if id_this_qual=='Q20882667': #check qualifier
                     id_temp_winner=winner.getTarget().getID()
                     there_is_a_winner=True   
                 if date_found and there_is_a_winner:
                     champ_table[ll][result_dic[road_or_clm + ' day']]=race_date.day
                     champ_table[ll][result_dic[road_or_clm + ' month']]=race_date.month
                     champ_table[ll][result_dic[road_or_clm + ' year']]=race_date.year  
                     champ_table[ll][result_dic[road_or_clm + ' winner']]=id_temp_winner
                     offset=1
                 elif invalid_precision and there_is_a_winner:
                     if warning_written==False:
                         print(get_label('fr',item_this_year))
                         print('unsufficient precision')
                         warning_written=True
          return champ_table, offset   
    
    def sub_champlist(champ_table, result_dic,dic_road_race, road_or_clm,ll):
        for id_race in dic_road_race:
            item_race =pywikibot.ItemPage(repo, id_race)
            item_race.get()            
            if(u'P527' in item_race.claims):
                 list_of_comprend=item_race.claims.get(u'P527')
                 for in_comprend in list_of_comprend:  
                     item_this_year =in_comprend.getTarget()
                     item_this_year.get()
                     champ_table, offset=sub_findwinner(item_this_year,id_race,champ_table, result_dic, road_or_clm,ll)
                     ll=ll+offset
                     
        return champ_table, ll         
    
    def sub_courseenligne(in_comprend,champ_table, result_dic,course_en_ligne_or_clm, road_or_clm,ll):
        item_this_race =in_comprend.getTarget()
        item_this_race.get()
        this_label=get_label('fr', item_this_race)
        offset=0
                        
        if this_label.find(course_en_ligne_or_clm)==0:
            if (u'P31' in item_this_race.claims):
                list_of_nature=item_this_race.claims.get(u'P31')
                id_master=list_of_nature[0].getTarget().getID()
            else:
                id_master=u'Q1'
            champ_table, offset=sub_findwinner(item_this_race,id_master,champ_table, result_dic, road_or_clm,ll)
        return champ_table, offset
    
    ##Begin main function ##
    #Championnats nationaux de cyclisme sur route 
    dic ={2020 : 'Q70655305',
        2019 : 'Q60015262', 2018 : 'Q43920899', 2017 : 'Q28005879', 2016 : 'Q22021840',
		2015 : 'Q19296998', 2014 : 'Q15621925', 2013: 'Q3339162',
		2012 : 'Q1333003', 2011 : 'Q1143844', 2010 : 'Q1568490',
		2009 : 'Q263224', 2008 : 'Q826505', 2007 : 'Q43286248',
		2006 : 'Q43286261', 2005 : 'Q1335357', 2004 : 'Q43286272',
		2003 : 'Q43286289', 2002 : 'Q43286297', 2001 : 'Q43286309'
	}
    
    #World champ, continental champs
    dic_road_race =['Q934877','Q30894544','Q25400085','Q54315111','Q50061750','Q31271454']
    dic_clm=['Q2630733','Q30894543','Q25400088','Q50062728','Q54314912','Q31271381']
    
    result_dic={
    'Road champ':0,
    'Road day':1,
    'Road month':2,
    'Road year':3,
    'Road winner':4,
    'Clm champ':5,
    'Clm day':6,
    'Clm month':7,
    'Clm year':8,
    'Clm winner':9,
    }
    
    verbose=False
    log=Log()
       
    startYear=2017
    EndYear=2021
    champ_table = [[0 for x in range(10)] for y in range(1000)] 
    
    #header
    for dic_content in result_dic:
        champ_table[0][result_dic[dic_content]]=dic_content

    #fill world champs...
    champ_table, ll_road=sub_champlist(champ_table, result_dic,dic_road_race, 'Road',1)
    log.concat("Road world and continental championships completed")
    champ_table, ll_clm=sub_champlist(champ_table, result_dic,dic_clm, 'Clm',1)
    log.concat("Clm world and continental championships completed")
    
    if verbose:     
        log.concat(champ_table)  

    #Look in the national championships
    for ii in range( startYear,EndYear):
        log.concat("start year " + str(ii))
        id_all_national=dic[ii]
        item_all_national =pywikibot.ItemPage(repo, id_all_national)
        item_all_national.get()
        
        if(u'P527' in item_all_national.claims):
             list_of_comprend=item_all_national.claims.get(u'P527')
             for in_comprend in list_of_comprend:  
                  item_this_national =in_comprend.getTarget()
                  item_this_national.get()
                  list_of_comprend2=item_this_national.claims.get(u'P527')
                  
                  for in_comprend2 in list_of_comprend2:                      
                      champ_table, offset=sub_courseenligne(in_comprend2,champ_table, result_dic,"Course en ligne féminine aux", "Road",ll_road)
                      ll_road=ll_road+offset
                      champ_table, offset=sub_courseenligne(in_comprend2,champ_table, result_dic,"Contre-la-montre féminin aux", "Clm",ll_clm)
                      ll_clm=ll_clm+offset
                      
    ll_max=max(ll_road,ll_clm)
    final_table = [[0 for x in range(10)] for y in range(ll_max)]
    final_table=champ_table[:ll_max]

    if verbose:     
        log.concat(champ_table)  
    with open('input/champ2.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        writer.writerows(final_table)