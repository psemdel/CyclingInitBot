# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdel
"""

import pywikibot

site = pywikibot.Site("wikidata", "wikidata")

def cycling_init_bot():
    selector=19
    #0-4: init the year
    #5-6: sorter
    #7-8: create races
    #9-10: complete the ranking and start list
    #11-15: others
    
    if selector==0:
        from src.national_team_creator import NationalTeamCreator
        
        man_or_woman=u'man'
        start_year=2022
        end_year=2022
        #optional
        country=False #u'FRA'  #None is not
        
        f=NationalTeamCreator( man_or_woman,start_year,end_year,country=country)
        f.main()    
                               
    elif selector==1:
        from src.national_championship_creator import NationalChampionshipCreator

        man_or_woman=u'both' #both
        option=u'clmon' #'clmoff'
        start_year=2022
        end_year=2022
        CC=True
        
        f=NationalChampionshipCreator(man_or_woman,option, start_year,end_year,CC)
        f.main()    

    elif selector==2:#
        from src.national_championship_creator import NationalChampionshipCreator
        
        man_or_woman=u'both'
        option=u'clmon' #'clmoff'
        start_year=2022
        end_year=2022
        country=False  #optional/False u'ESA'
        CC=False

        f=NationalChampionshipCreator(man_or_woman,option, start_year,end_year,CC,country=country)
        f.main()    
        
    elif selector==3: 
        from src.calendar_importer import CalendarImporter
       
        test=False
        man_or_woman=u'woman'
        filename='calendrier2022'
        year=2022
        
        f=CalendarImporter(filename, man_or_woman, year,test=test)
        f.main() 

    elif selector==4: 
        #more details in the table with activate and group
        from src.team_creator import TeamCreator

        name="Macadam’s Cowboys & Girls"
        id_master="Q105702884"
        countryCIO="FRA"
        UCIcode=None
        year=2022
        """
        UCI WorldTeam (Q6154783)
        UCI ProTeam (Q78464255)
        UCI Continental Team (Q1756006)
        UCI Women’s WorldTeam (Q80425135)
        WOmen conti Q2466826
        Female amateur cycling team (Q26849121)
        Amateur cycling team (Q20652655)
        """
        category_id="Q26849121"

        f=TeamCreator(name,id_master,countryCIO,UCIcode,year,category_id=category_id)
        f.main()    
        
    elif selector==5:   
        from src.sorter import NameSorter

        id_team=u'Q110773806'
        prop="P1923" # 'has part (P527)', 'participating team (P1923)'
        test=False
        
        f= NameSorter(id_team, prop,test=test)
        f.main()    

    elif selector==6:
        from src.sorter import DateSorter
        id_team=u'Q107093611'
        # if victory:   property_number = 2522  # victoire
        # else:  #      property_number = 527  # comprend
        prop="P527"
        test=False
        
        f= DateSorter(id_team, prop,test=test)
        f.main()   

    elif selector==7:
        from src.race_creator import RaceCreator
        
        race_name=u"Watersley Womens Challenge"
        id_race_master="Q79032687"
        create_stages=True
        year=2021
        start_date=pywikibot.WbTime(site=site,year=year, month=9, day=3, precision='day')
        end_date=pywikibot.WbTime(site=site,year=year, month=9, day=5, precision='day')
        first_stage=1
        last_stage=3
        countryCIO=u'NED'
        classe='2.2'
        edition_nr='1'
        single_race=False
        man_or_woman=u'woman'
        
        f=RaceCreator(
            race_name=race_name,
            single_race=single_race,
            man_or_woman=man_or_woman,
            id_race_master=id_race_master,
            countryCIO=countryCIO,
            classe=classe,
            start_date=start_date,
            edition_nr=edition_nr,
            end_date=end_date,
            only_stages=False,
            create_stages=create_stages, 
            first_stage=first_stage,
            last_stage=last_stage,
            year=year
            )
        f.main()
         
    elif selector==8:
         from src.race_creator import RaceCreator
         
         race_name=u"Binche-Chimay-Binche féminin"
         id_race_master=108914692
         year=2021
         start_date=pywikibot.WbTime(site=site,year=year, month=10, day=5, precision='day')
         countryCIO=u'BEL'
         classe='1.2'
         edition_nr='1'
         single_race=True
         man_or_woman=u'woman'
         
         f=RaceCreator(
                race_name=race_name,
                single_race=single_race,
                man_or_woman=man_or_woman,
                start_date=start_date,
                edition_nr=edition_nr,
                id_race_master=id_race_master,
                countryCIO=countryCIO,
                classe=classe,
                year=year)
         f.main()
         
    elif selector==9:
        from src.classification_importer import ClassificationImporter
        
        id_race='Q111732415'
        stage_or_general=0# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, 
        #5 team, #6 team points, #7 youth points, #8 == sprints
        final=False
        maxkk=10
        year=2022 #for team
        startliston=True
        test=False
        man_or_woman=u'woman'
        
        f=ClassificationImporter(stage_or_general,id_race,final,
                                 maxkk, test=test ,year=year,startliston=startliston,
                                 man_or_woman=man_or_woman)
        f.main()

    elif selector==10:
        from src.startlist_importer import StartlistImporter
        
        id_race='Q110773757'
        prologue_or_final=1 #0=prologue, 1=final, 2=one day race
        chrono=False
        test=False
        man_or_woman=u'woman'
        force_nation_team=False
        
        f=StartlistImporter(prologue_or_final, id_race, chrono,
                            man_or_woman, force_nation_team,test=test)
        f.main()

    elif selector==12:
        from src.rider_fast_init import RiderFastInit 
        name=u"Courtney Sherwell"
        countryCIO=u'AUS'
        man_or_woman=u'woman'
        
        f=RiderFastInit(name, countryCIO, man_or_woman)
        f.main()

    elif selector==13:
        from src.champ_list_creator import ChampListCreator
        
        man_or_woman=u'woman'
        actualize=True
        start_year=2022
        
        f=ChampListCreator(man_or_woman,start_year,actualize)
        f.main()

    elif selector==14:  
        from src.uci_classification import UCIClassification
        
        man_or_woman=u'man'
        id_master_UCI=u'Q104218422'  #Q97367360
        year=u'2021'
        filename=u'OceaniaRanking2021man' #'UCIranking'  CIranking2020man
        test=False
        cleaner=False #delete the UCI ranking
        UCIranking=False #for team team
        bypass=True #don't interrupt if not all riders found
        
        f=UCIClassification(
            UCIranking=UCIranking,
            id_master_UCI=id_master_UCI,
            filename=filename,
            cleaner=cleaner,
            man_or_woman=man_or_woman,
            bypass=bypass,
            year=year,
            test=test)
        f.main()

    elif selector==16: 
        #only stage
        from src.race_creator import RaceCreator
        #race_name=u"Grand Prix Mediterrennean"
       # id_race_master='104640104'
        #year=2021
        stage_race_id="Q110774135" #only for onlystages
        first_stage=1
        last_stage=6
        #single_race=True
        man_or_woman=u'woman'
        
        f= RaceCreator(
            stage_race_id=stage_race_id,
            first_stage=first_stage,
            last_stage=last_stage,
            man_or_woman=man_or_woman,
            only_stages=True
            )
        f.main()
        
    elif selector==17:
        from src.get_rider_tricot import Scan
        
        id_race='Q65956705'
        chrono=False
        test=False
        man_or_woman=u'woman'
        #read the result table
        f=Scan( id_race, chrono, man_or_woman,test=False)
        f.main()
    
    elif selector==18:
        from src.get_rider_tricot import ScanExisting
        
        id_race='Q110774449'
        chrono=True
        test=False
        man_or_woman=u'woman'
        #had already the results
        
        f=ScanExisting( id_race, chrono, man_or_woman,test=False)
        f.main()
    elif selector==19:
        from src.sparql import SparQL
        
        f=SparQL()
        f.list_elements()
    
    else: 
        print('do nothing')
   
if __name__ == '__main__':
    cycling_init_bot()
