# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdel
"""

import pywikibot

site = pywikibot.Site("wikidata", "wikidata")

def cycling_init_bot():
    selector=9
    #0-4: init the year
    #5-6: sorter
    #7-8: create races
    #9-10: complete the ranking and start list
    #11-21: others
    
    if selector==0:
        from src.national_team_creator import NationalTeamCreator
        
        man_or_woman=u'man'
        start_year=2023
        end_year=2023
        
        f=NationalTeamCreator(
            man_or_woman,
            start_year,
            end_year,
            country=None #u'FRA'  #None is not
            )
        f.main()    
                               
    elif selector==1:
        from src.national_championship_creator import NationalChampionshipCreator

        man_or_woman=u'both' #both
        start_year=2023
        end_year=2023
        
        f=NationalChampionshipCreator(
            man_or_woman,
            start_year,
            end_year,
            CC=True, 
            clm=True, 
            road=False)
        f.main()    

    elif selector==2:#
        from src.national_championship_creator import NationalChampionshipCreator
        
        man_or_woman=u'man'
        start_year=1989
        end_year=2010

        f=NationalChampionshipCreator(
            man_or_woman,
            start_year,
            end_year,
            CC=False,
            country="DEN",  #optional/False u'ESA'
            clm=True, 
            road=True)
        f.main()    
        
    elif selector==3: 
        from src.calendar_importer import CalendarImporter
       
        man_or_woman=u'woman'
        filename='Calendar2023'
        year=2023
        
        f=CalendarImporter(
            filename, 
            man_or_woman, 
            year,
            test=False)
        f.main() 

    elif selector==4: 
        #more details in the table with activate and group
        from src.team_creator import TeamCreator

        name="Juvederm Specialized"
        id_master="Q114006589"
        country="CAN"
        UCIcode="JSD"
        year=2011
        """
        UCI WorldTeam (Q6154783)
        UCI ProTeam (Q78464255)
        UCI Continental Team (Q1756006)
        UCI Women’s WorldTeam (Q80425135)
        WOmen conti Q2466826
        Female amateur cycling team (Q26849121)
        Amateur cycling team (Q20652655)
        """
        f=TeamCreator(
            name,
            id_master,
            country,
            UCIcode,
            year,
            category_id="Q2466826")
        f.main()    
        
    elif selector==5:   
        from src.sorter import NameSorter

        id_team=u'Q110773806'
        prop="P1923" # 'has part (P527)', 'participating team (P1923)'
        
        f= NameSorter(
            id_team, 
            prop,
            test=False)
        f.main()    

    elif selector==6:
        from src.sorter import DateSorter
        id_team=u'Q115517229'
        # if victory:   property_number = 2522  # victoire
        # else:  #      property_number = 527  # comprend
        prop="P527"
        
        f= DateSorter(
            id_team, 
            prop,
            test=False)
        f.main()   

    elif selector==7:
        from src.race_creator import RaceCreator

        start_date=pywikibot.WbTime(site=site,year=year, month=10, day=21, precision='day')
        end_date=pywikibot.WbTime(site=site,year=year, month=10, day=23, precision='day')

        f=RaceCreator(
            race_name="Vuelta a Formosa",
            single_race=False,
            man_or_woman='woman',
            id_race_master="Q114912404",
            country='ARG',
            classe='2.2',
            start_date=start_date,
            edition_nr='1',
            end_date=end_date,
            only_stages=False,
            create_stages=True, 
            first_stage=1,
            last_stage=4,
            year=2022
            )
        f.main()
         
    elif selector==8:
         from src.race_creator import RaceCreator

         start_date=pywikibot.WbTime(site=site,year=year, month=10, day=5, precision='day')

         f=RaceCreator(
                race_name="Binche-Chimay-Binche féminin",
                single_race=True,
                man_or_woman='woman',
                start_date=start_date,
                edition_nr='1',
                id_race_master="Q108914692",
                country='BEL',
                classe='1.2',
                year=2021)
         f.main()
         
    elif selector==9:
        from src.classification_importer import ClassificationImporter
        
        id_race='Q120116745'
        stage_or_general=9# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, 
        #5 team, #6 team points, #7 youth points, #8 == sprints, #9 == all
        maxkk=10
        
        f=ClassificationImporter(
            stage_or_general,
            id_race,
            maxkk, 
            test=False,
            startliston=True,
            fc=9064, 
            stage_num=7, #only for stage, put -1 otherwise for the main race
            year=2023)
        
        if stage_or_general==9:
            f.run_all()
        else:
            f.main()

    elif selector==10:
        from src.startlist_importer import StartlistImporter
        
        id_race='Q116304222'
        prologue_or_final=1 #0=prologue, 1=final, 2=one day race
        chrono=False
        man_or_woman=u'woman'
        
        f=StartlistImporter(
            prologue_or_final,
            id_race, 
            chrono,
            man_or_woman, 
            force_nation_team=False,
            test=False,
            fc=9054,
            add_unknown_rider=False)
        f.main()

    elif selector==12:
        from src.rider_fast_init import RiderFastInit 
        name=u"Courtney Sherwell"
        country=u'AUS'
        man_or_woman=u'woman'
        
        f=RiderFastInit(
            name, 
            country, 
            man_or_woman)
        f.main()

    elif selector==13:
        from src.champ_list_creator import ChampListCreator
        
        man_or_woman=u'woman'
        actualize=True
        start_year=2023
        
        f=ChampListCreator(
            man_or_woman,
            start_year,
            actualize)
        f.main()

    elif selector==14:   
        from src.uci_classification import UCIClassification
       
        f=UCIClassification(
            UCIranking=False,
            id_master_UCI='Q109000605',
            file='AsiaRanking2022man', #'UCIranking'  CIranking2020man
            cleaner=False, #delete the UC I ranking
            man_or_woman='man',
            bypass=True,  #don't interru pt if not all riders found
            year=2022,
            test=False)
        f.main()

    elif selector==15:  
        from src.uci_classification import UCITeamClassification
        
        f=UCITeamClassification(
            id_master_UCI='Q109000605'  ,
            filename='AsiaRanking2022teamman' ,
            cleaner=False,
            man_or_woman='man',
            bypass=True,
            year=2022,
            test=False)
        f.main()

    elif selector==16: 
        #only stage
        from src.race_creator import RaceCreator
        
        f= RaceCreator(
            stage_race_id="Q110774135",#only for onlystages
            first_stage=1,
            last_stage=6,
            man_or_woman='woman',
            only_stages=True
            )
        f.main()
        
    elif selector==17:
        from src.get_rider_tricot import Scan
        
        id_race='Q65956705'
        chrono=False
        man_or_woman=u'woman'
        #read the result table
        f=Scan( 
            id_race, 
            chrono, 
            man_or_woman,
            test=False)
        f.main()
    
    elif selector==18:
        from src.get_rider_tricot import ScanExisting
        
        id_race='Q116303680'
        chrono=False
        man_or_woman=u'woman'
        #had already the results
        
        f=ScanExisting(
            id_race, 
            chrono, 
            man_or_woman,
            test=False)
        f.main()
    elif selector==19:
        from src.sparql import SparQL
        
        f=SparQL()
        f.list_elements()
    
    elif selector==20:
        from src.team_importer import TeamImporter
        
        id_race='Q116304222'
        
        f=TeamImporter(
            id_race, 
            test=False,
            fc=9054)
        f.main()
        
    elif selector==21:
        from src.nat import NationalCreator2
        
        f=NationalCreator2()
        f.main()
    elif selector==22:
        from src.palmares_importer import PalmaresImporter
        
        f=PalmaresImporter(base_str="Contre-la-montre masculin aux championnats du Danemark de cyclisme sur route")
        f.main()
        
    else: 
        print('do nothing')
   
if __name__ == '__main__':
    cycling_init_bot()
