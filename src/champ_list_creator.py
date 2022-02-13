#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:35:53 2019

@author: maxime
"""
from .cycling_init_bot_low import get_label
import csv
from .bot_log import Log
from datetime import date
 
def f(pywikibot,site,repo,man_or_woman,start_year, actualize):

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
             if race_date is None:
                 invalid_precision=True
             elif ((race_date.day==1 and race_date.month==1) or
                 race_date.day==0 or
                 race_date.month==0):
                 invalid_precision=True
             else:
                 date_found=True
          
          if (u'P1346' in item_this_year.claims): #winner
             winners=item_this_year.claims.get(u'P1346')
             for winner in winners:
                 there_is_qual=False
                 id_this_qual=None
                 
                 for qual in winner.qualifiers.get('P642', []):
                     there_is_qual=True
                 if there_is_qual:
                     id_this_qual=winner.qualifiers['P642'][0].getTarget().getID()
                 else:
                     print(get_label('fr',item_this_year))
                     print("no qualifier")
                    
                 if id_this_qual is not None and id_this_qual=='Q20882667': #check qualifier
                     if winner.getTarget() is not None:
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
    
    def sub_champlist(champ_table, result_dic,dic_road_race, road_or_clm,ll, actualize, start_year):
        for id_race in dic_road_race:
            item_race =pywikibot.ItemPage(repo, id_race)
            item_race.get()            
            if(u'P527' in item_race.claims):
                 list_of_comprend=item_race.claims.get(u'P527')
                 for in_comprend in list_of_comprend:  
                     item_this_year =in_comprend.getTarget()
                     item_this_year.get()
                     
                     if (u'P585' in item_this_year.claims):
                         list_of_race_date=item_this_year.claims.get(u'P585')
                         race_year=list_of_race_date[0].getTarget().year
                         
                         if (actualize and race_year>=start_year) or (actualize==False):
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
    
    def sub_create_champ(result_dic,dic, dic_worldconti, road_or_clm,verbose,
                         start_year,EndYear,filename,old_filename,actualize,
                         pattern):
        
        champ_table = [[0 for x in range(10)] for y in range(2000)] 
        
        #header
        for dic_content in result_dic:
            champ_table[0][result_dic[dic_content]]=dic_content
        
        #if not actualize:
        if True:
            champ_table, ll=sub_champlist(champ_table, result_dic,dic_worldconti, road_or_clm,1, actualize, start_year)
            log.concat(road_or_clm +" world and continental championships "+ man_or_woman + " completed")
        #else:
        #    ll=1
        
        
        if verbose:     
            log.concat(champ_table)  
            
        #Look in the national championships
        for ii in range( start_year,EndYear):
            log.concat(road_or_clm + " start year " + str(ii))
            id_all_national=dic[ii]
            item_all_national =pywikibot.ItemPage(repo, id_all_national)
            item_all_national.get()
            
            if(u'P527' in item_all_national.claims):
                 list_of_comprend=item_all_national.claims.get(u'P527')
                 for in_comprend in list_of_comprend:  
                      item_this_national =in_comprend.getTarget()
                      item_this_national.get()
                      list_of_comprend2=item_this_national.claims.get(u'P527')
                      
                      if list_of_comprend2 is None:
                          print(get_label('fr',item_this_national) + " has no P527")
                      else:
                          for in_comprend2 in list_of_comprend2:  
                              champ_table, offset=sub_courseenligne(in_comprend2,
                                                                    champ_table, result_dic,pattern, road_or_clm,ll)
                              ll=ll+offset
        #write file
        final_table=champ_table[:ll]
        default_separator=';'
        
        if actualize:
            kk=0
            old_table = [[0 for x in range(10)] for y in range(2000)]
            
            #test separator
            with open(old_filename, newline='') as csvfile:
                file_object = csv.reader(csvfile, delimiter=default_separator, quotechar='|')
            
                for row in file_object: 
                    if len(row)==1:  #wrong separator, try coma
                        separator=','
                    else:
                        separator=default_separator
                    break #always break
            if verbose: 
                print(u'separator :' + separator)
            
            with open(old_filename, newline='') as csvfile:
                file_object = csv.reader(csvfile, delimiter= separator, quotechar='|')
                for row in file_object: 
                    if kk==0: #first line
                        old_table[kk]=row
                        kk=kk+1
                    else:
                        is_empty=True
                        for ii in range(len(row)):
                            if row[ii]!='' and row[ii]!=0 and row[ii]!='0':
                                is_empty=False
                        if is_empty:
                            break
                        else:
                            #new results are actualized
                            if int(row[result_dic[road_or_clm + ' year']]) < start_year or kk<100: #save the World Champ and so on.
                                old_table[kk]=row
                                kk=kk+1
        
            kk =kk-1  
            #concat
            #total_table = [[0 for x in range(10)] for y in range(kk+ll+1)]
            total_table=old_table
            total_table[kk+1:kk+ll]=final_table[1:] #no first line
            #write
        else:
            total_table = [[0 for x in range(10)] for y in range(ll+1)]
            total_table=final_table

        #write results
        with open(filename, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=';')
            writer.writerows(total_table) 
        print("csv file " + filename + " written")
    ##Begin main function ##
    #Championnats nationaux de cyclisme sur route 
    dic ={
        2021 : 'Q104303043',  2020 : 'Q70655305', 2019 : 'Q60015262',   
        2018 : 'Q43920899',   2017 : 'Q28005879', 2016 : 'Q22021840',
		2015 : 'Q19296998',   2014 : 'Q15621925', 2013: 'Q3339162',
		2012 : 'Q1333003',    2011 : 'Q1143844',  2010 : 'Q1568490',
		2009 : 'Q263224',     2008 : 'Q826505',   2007 : 'Q640286',
		2006 : 'Q492135',     2005 : 'Q1335357',  2004 : 'Q43286272',
		2003 : 'Q43286289',   2002 : 'Q43286297', 2001 : 'Q43286309'
	}
    
    #World champ, continental champs
    dic_road_race_women =['Q934877','Q30894544','Q25400085','Q54315111','Q50061750','Q31271454']
    dic_clm_women=['Q2630733','Q30894543','Q25400088','Q50062728','Q54314912','Q31271381']
    dic_road_race_men =['Q13603535','Q30894537','Q23069702','Q23889479','Q22980916','Q85519571']
    dic_clm_men=['Q2557477','Q30894535','Q23069708','Q22980937','Q23889469','Q85519577']
    
    result_dic={
    'Road champ':0,
    'Road day':1,
    'Road month':2,
    'Road year':3,
    'Road winner':4,
    'Clm champ':0,
    'Clm day':1,
    'Clm month':2,
    'Clm year':3,
    'Clm winner':4,
    }
    
    verbose=False
    log=Log()
       
    EndYear=date.today().year+1

    #Road
    if man_or_woman=="woman":
        filename='input/champ2.csv'
        old_filename='input/champ.csv'
        dic_worldconti=dic_road_race_women
        pattern="Course en ligne féminine aux"
    else:
        filename='input/champ_man2.csv'
        old_filename='input/champ_man.csv'
        dic_worldconti=dic_road_race_men
        pattern="Course en ligne masculine aux"
        
    sub_create_champ(result_dic,dic,dic_worldconti, 'Road',verbose,
                         start_year,EndYear,filename,old_filename,actualize,
                         pattern)

    print("road scan finished")
    #Clm
    if man_or_woman=="woman":
        filename='input/champ_clm2.csv'
        old_filename='input/champ_clm.csv'
        dic_worldconti=dic_clm_women
        pattern="Contre-la-montre féminin aux"
    else:
        filename='input/champ_man_clm2.csv'
        old_filename='input/champ_man_clm.csv'
        dic_worldconti=dic_clm_men
        pattern="Contre-la-montre masculin aux"
        
    sub_create_champ(result_dic,dic,dic_worldconti, 'Clm',verbose,
                         start_year,EndYear,filename,old_filename,actualize,
                         pattern)

    print("itt scan finished")


