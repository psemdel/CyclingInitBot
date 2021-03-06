# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdel
"""

import time
import pywikibot
from src import nation_team_table

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

def cycling_init_bot():
    nation_table= nation_team_table.load()
    
    selector=5
    #0-4: init the year
    #5-6: sorter
    #7-8: create races
    #9-10: complete the ranking and start list
    #11-15: others
    
    if selector==0:
        from src import national_team_creator
        
        man_or_woman=u'man'
        start_year=2021
        end_year=2021
        #optional
        country=False #false is not
        
        national_team_creator.f(pywikibot,site,repo,time,nation_table,
                                man_or_woman,start_year,end_year,country=country)
    elif selector==1:
        from src import national_championship_creator
        from src import cc_table
        #cc
        cc_table=cc_table.load()
        man_or_woman=u'both' #both
        option=u'clmon' #'clmoff'
        start_year=2021
        end_year=2021
        CC=True
        national_championship_creator.f(pywikibot,site,repo,time,cc_table,
                                    man_or_woman,option,start_year,end_year,CC)      
        
    elif selector==2:#
        #not cc
        from src import national_championship_creator
        
        man_or_woman=u'woman'
        option=u'clmon' #'clmoff'
        start_year=2021
        end_year=2021
        country=False  #optional/False u'ESA'
        CC=False
        national_championship_creator.f(pywikibot,site,repo,time,nation_table,
                                    man_or_woman,option, start_year,end_year,CC,country=country)    
    elif selector==3: 
        from src import calendar_importer
        from src import race_list
        race_table, race_dic = race_list.load()
        test=False
        man_or_woman=u'woman'
        filename='Calendar'
        year=2021
        
        calendar_importer.f(pywikibot, site, repo,time, nation_table, test, race_table, race_dic, man_or_woman, filename, year)
    elif selector==4: 
        #more details in the table with activate and group
        from src import team_creator
        from src import pro_team_table
        from src import amateur_team_table
        pro_or_amateur=1 #1 is pro
        year=2010
        prov=True
        
        if prov:
            team_table = [[0 for x in range(7)] for y in range(2)]
            team_table[1][1] = u"Tibco-To the Top"
            team_table[1][2] = 537946 #optional, then put 0
            team_table[1][3] = u'USA' #country
            team_table[1][4] = u''
            team_table[1][5] = 2 #don't modify
            team_table[1][6] = 1 #don't modify
            [_, team_dic]=pro_team_table.load()
        else:
            if pro_or_amateur==1:
                [team_table, team_dic]=pro_team_table.load()
            else:
                [team_table, team_dic]=amateur_team_table.load()
        team_creator.f(pywikibot,site,repo,time,team_table,nation_table, team_dic,year)
    elif selector==5:   
        from src import sorter
        id_team=u'Q21856732'
        # 'has part (P527)', 'participating team (P1923)'
        prop="P1923"
        test=True
        
        sorter.name_sorter( pywikibot,site,repo,time,id_team, prop , test)
    elif selector==6:
        from src import sorter
        id_team=u'Q70443700'
        # if victory:   property_number = 2522  # victoire
        # else:  #      property_number = 527  # comprend
        prop="P2522"
        test=True
        
        sorter.date_sorter(pywikibot,site,repo,time,id_team,prop,test )
    elif selector==7:
        from src import race_creator
        race_name=u"Semaine cycliste valencienne"
        id_race_master=28752781
        create_stages=True
        year=2010
        race_begin=pywikibot.WbTime(site=site,year=year, month=2, day=20, precision='day')
        end_date=pywikibot.WbTime(site=site,year=year, month=2, day=23, precision='day')
        first_stage=1
        last_stage=4
        countryCIO=u'ESP'
        classe='2.2'
        edition_nr=''
        single_race=False
        man_or_woman=u'woman'
        
        
        race_creator.f(pywikibot,site,repo,time,
                      nation_table,
                      race_name,
                      single_race,
                      man_or_woman,
                      id_race_master=id_race_master,
                      countryCIO=countryCIO,
                      classe=classe,
                      race_begin=race_begin,
                      edition_nr=edition_nr,
                      end_date=end_date,
                      only_stages=False,
                      create_stages=create_stages, 
                      first_stage=first_stage,
                      last_stage=last_stage,
                      year=year)
         
    elif selector==8:
         from src import race_creator
         race_name=u"Tour du Nanxijiang "
         id_race_master=71731311 
         year=2010
         race_date=pywikibot.WbTime(site=site,year=year, month=10, day=17, precision='day')
         countryCIO=u'CHN'
         classe='1.2'
         edition_nr=''
         single_race=True
         man_or_woman=u'woman'
         
         race_creator.f(pywikibot,site,repo,time,
                nation_table,
                race_name,
                single_race,
                man_or_woman,
                race_begin=race_date,
                edition_nr=edition_nr,
                id_race_master=id_race_master,
                countryCIO=countryCIO,
                classe=classe,
                year=year)
         
    elif selector==9:
        from src import classification_importer
        id_race='Q74127378'
        stage_or_general=0# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team, #6 team ponts, #7 youth points
        #8 == sprints
        final=False
        maxkk=10
        year=2020 #for team
        startliston=True
        test=False
        man_or_woman=u'woman'
        classification_importer.f(pywikibot,site,repo,stage_or_general,id_race,final,
                               maxkk,test,year=year,startliston=startliston,
                               man_or_woman=man_or_woman)
    elif selector==10:
        from src import startlist_importer
        id_race='Q74127378'
        prologue_or_final=2 #0=prologue, 1=final, 2=one day race
        chrono=False
        test=False
        man_or_woman=u'woman'
        force_nation_team=False
        time_of_race=pywikibot.WbTime(site=site,year=2020, month=10, day=11, precision='day')    
        startlist_importer.f(pywikibot,site,repo, prologue_or_final, id_race, 
                                   time_of_race,chrono,test,nation_table,man_or_woman,
                                   force_nation_team)  
    elif selector==12:
        from src import rider_fast_init
        name=u"Iara Gillespie"
        countryCIO=u'IRL'
        man_or_woman=u'woman'
        rider_fast_init.f(pywikibot,site,repo,time,nation_table, name,countryCIO,man_or_woman)
    elif selector==13:
        from src import champ_list_creator
        man_or_woman=u'man'
        actualize=False
        start_year=2005
        champ_list_creator.f(pywikibot,site,repo,time,man_or_woman,start_year,actualize)
    elif selector==14:  
        from src import uci_classification
        man_or_woman=u'man'
        id_master_UCI=u'Q97367360'  #Q97367360
        year=u'2020'
        filename=u'UCIranking2020man' #'UCIranking'  CIranking2020man
        test=False
        cleaner=False #delete the UCI ranking
        UCIranking=True
        bypass=True #don't interrupt if not all riders found
        uci_classification.f(pywikibot,site,repo,year,id_master_UCI, filename,cleaner,test,man_or_woman,UCIranking,bypass)
    elif selector==15:
        from src import cycling_init_bot_low as low
        id_item=u'Q57267790'
        property_nummer="P3496"
        low.delete_property(pywikibot,repo,id_item,property_nummer)
    elif selector==16: 
        #only stage
        from src import race_creator
        race_name=u"Tour de Thaïlande féminin"
        id_race_master=1
        year=2020
        stage_race_id="Q79137942" #only for onlystages
        first_stage=1
        last_stage=3
        single_race=False
        man_or_woman=u'woman'
        
        race_creator.f(pywikibot,site,repo,time,
                      nation_table,
                      race_name,
                      single_race,
                      man_or_woman,
                      stage_race_id=stage_race_id,
                      only_stages=True,
                      first_stage=first_stage,
                      last_stage=last_stage,
                      year=year)
        
    elif selector==17:
        from src import get_rider_tricot
        id_race='Q78661713'
        chrono=False
        test=False
        man_or_woman=u'woman'
        time_of_race=pywikibot.WbTime(site=site,year=2020, month=10, day=18, precision='day')    
        get_rider_tricot.scan(pywikibot,site,repo, id_race, time_of_race,chrono, test,man_or_woman)
    
    elif selector==18:
        from src import get_rider_tricot
        id_race='Q21856739'
        chrono=False
        test=False
        man_or_woman=u'woman'
     
        get_rider_tricot.scan_existing(pywikibot,site,repo, id_race, chrono, test,man_or_woman)

    else: 
        print('do nothing')
        
if __name__ == '__main__':
    cycling_init_bot()
