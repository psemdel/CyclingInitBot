# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdely
"""

import time
import pywikibot
import nation_team_table

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

def cycling_init_bot():
    nation_table= nation_team_table.load()

    selector=12
    #0-4: init the year
    #5-6: sorter
    #7-8: create races
    #9-10: complete the ranking and start list
    #11-15: others
    
    if selector==0:
        import national_team_creator
        
        man_or_woman=u'man'
        national_team_creator.f(pywikibot,site,repo,time,nation_table,man_or_woman)
    elif selector==1:
        import national_championship_creator
        import cc_table
        #cc
        cc_table=cc_table.load()
        man_or_woman=u'woman'
        option=u'clmon' #'clmoff'
        start_year=2020
        end_year=2021
        national_championship_creator.f(pywikibot,site,repo,time,nation_table,
                                    man_or_woman,option,start_year,end_year,True)      
        
    elif selector==2:#
        #not cc
        import national_championship_creator
        
        man_or_woman=u'man'
        option=u'clmon' #'clmoff'
        start_year=2020
        end_year=2021
        country=u'ESA'  #optional 
        national_championship_creator.f(pywikibot,site,repo,time,nation_table,
                                    man_or_woman,option, start_year,end_year,False,country=country)    
    elif selector==3: 
        import calendar_importer
        import race_list
        race_table, race_dic = race_list.load()
        test=False
        calendar_importer.f(pywikibot, site, repo,time, nation_table, ";", test, race_table, race_dic)
    elif selector==4: 
        #more details in the table with activate and group
        import pro_team_creator
        pro_or_amateur=1 #1 is pro
        year=2020
        prov=False
        
        if prov:
            team_table = [[0 for x in range(7)] for y in range(2)]
            team_table[1][1] = u"Stepfwd it Suzuki"
            team_table[1][2] = 59195419 #optional, then put 0
            team_table[1][3] = u'AUS' #country
            team_table[1][4] = u''
            team_table[1][5] = 2 #don't modify
            team_table[1][6] = 1 #don't modify
            [_, team_dic]=pro_team_tab()
        else:
            if pro_or_amateur==1:
                [team_table, team_dic]=pro_team_tab.load()
            else:
                [team_table, team_dic]=amateur_team_tab.load()
        pro_team_creator.f(pywikibot,site,repo,time,team_table,nation_table,pro_or_amateur, team_dic,year)
    elif selector==5:   
        import sorter
        id_team=u'Q48994098'
        team=False
        champ=False #else competition
        test=False
        sorter.name_sorter( pywikibot,site,repo,time,id_team, team, champ, test)
    elif selector==6:
        import sorter
        id_team=u'Q70443700'
        victory=False #else competition
        test=False
        sorter.date_sorter(pywikibot,site,repo,time,id_team,victory,test )
    elif selector==7:
        import race_creator
        race_name=u"Semaine cycliste valencienne"
        race_genre=u"de la "  
        id_race_master=28752781
        stage_race_id=78658035 #only for onlystages
        year=2020
        UCI=True
        WWT=False
        only_stages=True
        create_stages=True
        race_begin=pywikibot.WbTime(site=site,year=year, month=2, day=20, precision='day')
        end_date=pywikibot.WbTime(site=site,year=year, month=2, day=23, precision='day')
        first_stage=1
        last_stage=4
        countryCIO=u'ESP'
        classe='2.2'
        edition_nr=''
        
        race_creator.f(pywikibot,site,repo,time,nation_table,race_name,race_genre,
                      id_race_master,year,UCI,WWT,race_begin,countryCIO,classe,False,edition_nr,
                      stage_race_id=stage_race_id, end_date=end_date,
                      only_stages=only_stages,create_stages=create_stages, first_stage=first_stage,
                      last_stage=last_stage)
    elif selector==8:
         import race_creator
         race_name=u"Tour du Nanxijiang "
         race_genre=u"du "
         id_master=71731311 
         year=2019
         UCI=True
         WWT=False
         race_date=pywikibot.WbTime(site=site,year=year, month=10, day=17, precision='day')
         countryCIO=u'CHN'
         classe=12
         edition_nr=''
         race_creator.f(pywikibot,site,repo,time,nation_table,race_name,race_genre,
                 id_master,year,UCI,WWT,race_date,countryCIO,classe,True,edition_nr)
    elif selector==9:
        import classification_importer
        id_race='Q17010500'
        stage_or_general=0# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team, #6 team ponts, #7 youth points
        #8 == sprints
        final=False
        maxkk=10
        year=2013 #for team
        startliston=False
        test=False
        classification_importer.f(pywikibot,site,repo,stage_or_general,id_race,final,
                               maxkk,year,startliston,test)
    elif selector==10:
        import startlist_importer
        id_race='Q48994098'
        prologue_or_final=2 #0=prologue, 1=final, 2=one day race
        chrono=False
        test=False
        time_of_race=pywikibot.WbTime(site=site,year=2012, month=2, day=20, precision='day')    
        startlist_importer.f(pywikibot,site,repo, prologue_or_final, id_race, 
                                   time_of_race,chrono,test,nation_table)  
    elif selector==12:
        import rider_fast_init
        name=u"Victoria Kondel"
        countryCIO=u'RUS'
        rider_fast_init.f(pywikibot,site,repo,time,nation_table, name,countryCIO)
    elif selector==13:
        import champ_list_creator
        champ_list_creator.f(pywikibot,site,repo,time)
    elif selector==14:  
        import uci_classification
        id_master_UCI=u'Q57267790'
        year=u'2019'
        filename=u'UCIranking' #'UCIranking'
        test=False
        cleaner=False #delete the UCI ranking
        uci_classification.f(pywikibot,site,repo,year,id_master_UCI, filename,cleaner,test)
    elif selector==15:
        from cycling_init_bot_low import delete_property
        id_item=u'Q57267790'
        property_nummer=3496
        delete_property(pywikibot,repo,id_item,property_nummer)
    else: 
        print('do nothing')
        
if __name__ == '__main__':
    cycling_init_bot()
