# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdely
"""

##Main function of the bot
def cycling_init_bot():
    [pywikibot,site,repo,time]=wikiinit()
    [nation_table, endkk]= nation_tab()
    [tempcc_table, ccendkk]=cc_table()
    
    selector=4
    
    if selector==0:
        man_or_woman=u'man'
        national_team_creator(pywikibot,site,repo,time,nation_table,endkk,man_or_woman)
    elif selector==1:
        man_or_woman=u'man'
        option=u'clmon' #'clmoff'
        start_year=2020
        end_year=2021
        country=u'ESA'  
        national_championship_creator(pywikibot,site,repo,time,nation_table,endkk,
                                    man_or_woman,option, start_year,end_year,country,False)    
    elif selector==2:
        StageRaceName=u"Tour de Colombie féminin"
        StageRaceGenre=u"du "  
        StageRaceid_master=27684043
        StageRaceMaster=57277615 #only for onlystages
        Year=2019
        UCI=u"yes"
        Onlystages=False
        Createstage=True
        StageRaceBegin=pywikibot.WbTime(site=site,year=Year, month=12, day=3, precision='day')
        StageRaceEnd=pywikibot.WbTime(site=site,year=Year, month=12, day=7, precision='day')
        FirstStage=1
        LastStage=5
        CountryCIO=u'COL'
        Class='2.2'
        StageRaceCreator(pywikibot,site,repo,time,teamTable,StageRaceName,StageRaceGenre,StageRaceid_master,Year,UCI,StageRaceBegin,
                         StageRaceEnd,FirstStage,LastStage,CountryCIO,Createstage,Class,Onlystages,StageRaceMaster)
    elif selector==3:        
        id_team=u'Q21856738'
        team=False
        champ=False #else competition
        test=False
        name_sorter(pywikibot,site,repo,time, id_team, team, champ, test)
    elif selector==4:
        id_team=u'Q70443700'
        victory=False #else competition
        test=False
        date_sorter(pywikibot,site,repo,time,id_team,victory,test )
    elif selector==5:
        id_calendar=u"Q57267790"
        calendarSymmetrizer(pywikibot,site,repo,time, id_calendar)
    elif selector==6:
        id_master=u"Q27684043"
        addUCIcalendar(pywikibot,site,repo,time, id_master)
    elif selector==7:
        calendarSymmetrizerMass(pywikibot,site,repo,time)
    elif selector==8: 
       [pro_team_table, proendkk]=pro_team_tab()
       [amateur_team_table, amateurendkk]=amateur_team_tab()
       proamateur=1 #1 is pro
       group=1 #group to create
       countrytocreate=u'SUI'
       if proamateur==1:
           proteamcreator(pywikibot,site,repo,time,proteamTable,teamTable,proendkk,proamateur, countrytocreate)
       else:
           proteamcreator(pywikibot,site,repo,time,amateurteamTable,teamTable,amateurendkk,proamateur, countrytocreate)
    elif selector==9:
       man_or_woman=u'woman'
       option=u'clmon' #'clmoff'
       #ccChampionshipCreator(pywikibot,site,repo,time,tempccTable,ccendkk,man_or_woman, option)
       national_championship_creator(pywikibot,site,repo,time,nation_table,endkk,
                                    man_or_woman,option, start_year,end_year,country,True) 
    elif selector==10:
         race_name=u"Tour du Nanxijiang "
         race_genre=u"du "
         id_master=71731311 
         year=2019
         UCI=True
         WWT=False
         race_date=pywikibot.WbTime(site=site,year=Year, month=10, day=17, precision='day')
         countryCIO=u'CHN'
         classe=12
         race_creator(pywikibot,site,repo,time,nation_table,race_name,race_genre,
                 id_master,year,UCI,WWT,race_date,countryCIO,classe,True)
    elif selector==11:
        id_race='Q24299309'
        stage_or_general=0# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team, #6 team ponts, #7 youth points
        #8 == sprints
        final=False
        separator=";"
        maxkk=10
        year=2019
        startliston=True
        test=True
        classification_importer(pywikibot,site,repo,stage_or_general,id_race,final,
                                separator,maxkk,year,startliston,test)
    elif selector==12: 
        year=u'2019'
        separator=";"
        test=False
        UCI_classification_importer(pywikibot,site,repo,year,separator,test)
    elif selector==13:
        id_race='Q13548460'
        prologueorfinal=1 #0=prologue, 1=final, 2=one day race
        separator=";"
        chrono=True
        test=False
        time_of_race=pywikibot.WbTime(site=site,year=2013, month=6, day=30, precision='day')    
        list_of_starters_importer (pywikibot,site,repo, prologueorfinal, id_race, separator,
                                   time_of_race,chrono,test,team_table)    
    elif selector==14:
        name=u"Vanessa Serrano"
        description='coureuse cycliste du Salvador' #française
        countryCIO=u'ESA'
        rider_fast_init(pywikibot,site,repo,time,nation_table, name,description,countryCIO)
    elif selector==15:
        id_champion='Q43744788'
        test=False
        palmares_importer(pywikibot,site,repo,id_champion,test)
    elif selector==16:
        champ_list_creator(pywikibot,site,repo,time)
    elif selector==17:  
        year=u'2019'
        separator=";"
        test=False
        UCIclassificationCleaner(pywikibot,site,repo,year,separator,test)
    elif selector==18:
        id_item=u'Q57267790'
        property_nummer=3496
        deleteProperty(pywikibot,repo,id_item,property_nummer)
    elif selector==19:
        id_master_UCI=u'Q57267790'
        year=u'2019'
        separator=";"
        test=False
        filename=u'UCIranking' #'UCIranking'
        UCI_classification_importer_rider(pywikibot,site,repo,year, separator,test,id_master_UCI, filename)
    elif selector==20: 
        race_table = race_list()
        test=False
        UCI_calendar_importer(pywikibot, site, repo,time, nation_table, ";", test, race_table)
    else: 
        print('do nothing')
        
if __name__ == '__main__':
    cycling_init_bot()
