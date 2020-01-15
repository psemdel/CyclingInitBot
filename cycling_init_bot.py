# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdely
"""

##Main function of the bot
def cycling_init_bot():
    [pywikibot,site,repo,time]=wiki_init()
    [nation_table, endkk]= nation_tab()
    [tempcc_table, ccendkk]=cc_table()
    
    selector=4
    #0-4: init the year
    #5-6: sorter
    #7-8: create races
    #9-10: complete the ranking and start list
    #11-15: others
    
    if selector==0:
        man_or_woman=u'man'
        national_team_creator(pywikibot,site,repo,time,nation_table,endkk,man_or_woman)
    elif selector==1:
        #cc
        man_or_woman=u'woman'
        option=u'clmon' #'clmoff'
        national_championship_creator(pywikibot,site,repo,time,nation_table,endkk,
                                    man_or_woman,option, start_year,end_year,country,True)      
        
    elif selector==2:#
        #not cc
        man_or_woman=u'man'
        option=u'clmon' #'clmoff'
        start_year=2020
        end_year=2021
        country=u'ESA'  
        national_championship_creator(pywikibot,site,repo,time,nation_table,endkk,
                                    man_or_woman,option, start_year,end_year,country,False)    
    elif selector==3: 
        race_table, race_dic = race_list()
        test=False
        calendar_importer(pywikibot, site, repo,time, nation_table, ";", test, race_table, race_dic)
    elif selector==4: 
        #more details in the table with activate and group
        pro_or_amateur=0 #1 is pro
        if pro_or_amateur==1:
            [team_table, endkk, team_dic]=pro_team_tab()
            pro_team_creator(pywikibot,site,repo,time,team_table,nation_table,endkk,pro_or_amateur, team_dic)
        else:
            [team_table, endkk, team_dic]=amateur_team_tab()
            pro_team_creator(pywikibot,site,repo,time,team_table,nation_table,endkk,pro_or_amateur, team_dic)
    elif selector==5:        
        id_team=u'Q16274704'
        team=False
        champ=False #else competition
        test=False
        name_sorter(pywikibot,site,repo,time, id_team, team, champ, test)
    elif selector==6:
        id_team=u'Q70443700'
        victory=False #else competition
        test=False
        date_sorter(pywikibot,site,repo,time,id_team,victory,test )
    elif selector==7:
        race_name=u"Santos Women's Tour"
        race_genre=u"du "  
        id_race_master=22661614
        stage_race_id=78486081 #only for onlystages
        year=2020
        UCI=True
        WWT=False
        only_stages=True
        create_stages=True
        race_begin=pywikibot.WbTime(site=site,year=year, month=1, day=16, precision='day')
        end_date=pywikibot.WbTime(site=site,year=year, month=1, day=19, precision='day')
        first_stage=1
        last_stage=4
        countryCIO=u'AUS'
        classe='2.Pro'
        edition_nr=''
        
        race_creator(pywikibot,site,repo,time,nation_table,race_name,race_genre,
                      id_race_master,year,UCI,WWT,race_begin,countryCIO,classe,False,edition_nr,
                      stage_race_id=stage_race_id, end_date=end_date,
                      only_stages=only_stages,create_stages=create_stages, first_stage=first_stage,
                      last_stage=last_stage)
    elif selector==8:
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
         race_creator(pywikibot,site,repo,time,nation_table,race_name,race_genre,
                 id_master,year,UCI,WWT,race_date,countryCIO,classe,True,edition_nr)
    elif selector==9:
        id_race='Q16154118'
        stage_or_general=0# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team, #6 team ponts, #7 youth points
        #8 == sprints
        final=False
        maxkk=10
        year=2009
        startliston=False
        test=False
        classification_importer(pywikibot,site,repo,stage_or_general,id_race,final,
                               maxkk,year,startliston,test)
    elif selector==10:
        id_race='Q16274704'
        prologue_or_final=2 #0=prologue, 1=final, 2=one day race
        chrono=False
        test=True
        time_of_race=pywikibot.WbTime(site=site,year=2013, month=3, day=31, precision='day')    
        startlist_importer(pywikibot,site,repo, prologue_or_final, id_race, 
                                   time_of_race,chrono,test,nation_table)  
    elif selector==11: 
        year=u'2019'
        test=False
        UCI_classification_importer(pywikibot,site,repo,year,test)
    elif selector==12:
        name=u"Vanessa Serrano"
        description='coureuse cycliste du Salvador' #française
        countryCIO=u'ESA'
        rider_fast_init(pywikibot,site,repo,time,nation_table, name,description,countryCIO)
    elif selector==13:
        champ_list_creator(pywikibot,site,repo,time)
    elif selector==14:  
        id_master_UCI=u'Q57267790'
        year=u'2019'
        filename=u'UCIranking' #'UCIranking'
        test=False
        cleaner=False #delete the UCI ranking
        UCI_classification_importer(pywikibot,site,repo,year,id_master_UCI, filename,cleaner,test)
    elif selector==15:
        id_item=u'Q57267790'
        property_nummer=3496
        deleteProperty(pywikibot,repo,id_item,property_nummer)
    else: 
        print('do nothing')
        
if __name__ == '__main__':
    cycling_init_bot()
