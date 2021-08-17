#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:31 2020

@author: maxime
"""

import pywikibot
import unittest
import os
import csv
from src.cycling_init_bot_low import (search_race, is_it_a_cyclist, search_item,
search_rider, define_article, get_class, get_present_team, CIOtoIDsearch,
get_class_WWT, get_country, table_reader, compare_dates, get_year, checkid,
checkprop, get_single_or_stage,excel_to_csv,bot_or_site, date_finder, search_team_by_code,
float_to_int, IDtoCIOsearch, get_nationality, get_race_begin, get_end_date,
search_team_by_code_man, is_it_a_teamseason, get_race_name, teamCIOsearch)
from src import race_list
from src import nation_team_table

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestSearch(unittest.TestCase):  
    def test_get_nationality(self):
        this_date1=pywikibot.WbTime(site=site,year=2009, month=12, day=31, precision='day')    
        
        res=get_nationality(pywikibot, repo, site, "Q13893333", this_date1)
        self.assertEqual(res,"Q142")
        res=get_nationality(pywikibot, repo, site, "Q16215626", this_date1)
        self.assertEqual(res,"Q212")       
        res=get_nationality(pywikibot, repo, site, "Q270555", this_date1)
        self.assertEqual(res,"Q35")   
        
        this_date2=pywikibot.WbTime(site=site,year=2019, month=12, day=31, precision='day')    
        res=get_nationality(pywikibot, repo, site, "Q270555", this_date2)
        self.assertEqual(res,"Q664")  
        
    def test_IDtoCIOsearch(self):
        nation_table= nation_team_table.load()
        
        self.assertEqual(IDtoCIOsearch(nation_table,456789),"no code")
        self.assertEqual(IDtoCIOsearch(nation_table,889),"AFG")
        self.assertEqual(IDtoCIOsearch(nation_table,804),"PAN")
    
    def test_search_race(self):
        race_table, race_dic = race_list.load()
        result1, result2 = search_race('Tour Santos Women', race_table,race_dic)
        self.assertEqual(result1, "Q22661614")
        self.assertEqual(result2 , "du ")
        result1, result2 = search_race('Santos Women Tour', race_table,race_dic)
        self.assertEqual(result1, "Q22661614")
        self.assertEqual(result2 , "du ")    
        result1, result2 = search_race('Sintos Women Tour', race_table,race_dic)
        self.assertEqual(result1, "Q0" )
        self.assertEqual(result2 , "")   
        result1, result2 = search_race("Grand Prix International d'Isbergues", race_table,race_dic)
        self.assertEqual(result1, "Q56703296")
        self.assertEqual(result2 , "du ")
        result1, result2 = search_race("GP de Plouay - Lorient- Agglomération Trophée CERATIZIT", race_table,race_dic)
        self.assertEqual(result1, "Q1110856")
        self.assertEqual(result2 , "du ")
        
    def test_search_team_by_code(self):
        self.assertEqual(search_team_by_code(pywikibot, site, repo, "MTS 2020"),'Q74725715')
        self.assertEqual(search_team_by_code(pywikibot, site, repo, "ASA 2020"),'Q74725122')
        self.assertEqual(search_team_by_code(pywikibot, site, repo, "TFS 2020"),'Q82315001')
        self.assertEqual(search_team_by_code(pywikibot, site, repo, "LSL 2020"),'Q74725666')
        
    def test_search_team_by_code_man(self):
        self.assertEqual(search_team_by_code_man(pywikibot, site, repo, "TFS 2020"),'Q78075353')
        self.assertEqual(search_team_by_code_man(pywikibot, site, repo, "DQT 2020"),'Q78075314')

    def test_is_it_a_cyclist(self):
        self.assertFalse(is_it_a_cyclist(pywikibot, repo, 'Q38222'))
        self.assertTrue(is_it_a_cyclist(pywikibot, repo, 'Q563737'))
        self.assertTrue(is_it_a_cyclist(pywikibot, repo, 'Q47295776'))
        self.assertFalse(is_it_a_cyclist(pywikibot, repo, 'Q75271148'))

    def test_is_it_a_teamseason(self):
        self.assertTrue(is_it_a_teamseason(pywikibot, repo, 'Q78075314'))
        self.assertTrue(is_it_a_teamseason(pywikibot, repo, 'Q82315001'))
        self.assertFalse(is_it_a_teamseason(pywikibot, repo, 'Q563737'))

    def test_other(self):
        self.assertEqual(search_item(pywikibot, site, 'Anna van der Breggen'),'Q563737')
        self.assertEqual(search_item(pywikibot, site, 'Anna'),'Q1')
        self.assertEqual(search_item(pywikibot, site, 'zz14563465465wuichWRUPIUDGCOIUWR'),'Q0')
        self.assertEqual(search_item(pywikibot, site, 'Elizabeth Banks'),'Q1')
        
        self.assertEqual(search_rider(pywikibot, site, repo,'Anna van der Breggen','',''),'Q563737')
        self.assertEqual(search_rider(pywikibot, site, repo,'Elizabeth Banks','',''),'Q47295776')
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'Elizabeth', 'Banks'),'Q47295776')
        #exception
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'Felix', 'GROß'),'Q39885866')
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'felix', 'groß'),'Q39885866')
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'Felix', 'Groß'),'Q39885866')
        
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'Felix', 'GROß'),'Q39885866')
        #Character
        self.assertEqual(search_rider(pywikibot, site, repo,'W. Mathias Sorgho','',''),'Q27644062')
        #exception
        self.assertEqual(search_rider(pywikibot, site, repo,0, '1501996785028', 'ERIC'),'Q19661759')
        self.assertEqual(search_rider(pywikibot, site, repo,'GARCIA CAÑELLAS Margarita Victo', 0, 0),'Q23907253')
        
    def test_define_article(self):
        self.assertEqual(define_article("La Classique des Alpes"),("de la ", "Classique des Alpes"))
        self.assertEqual(define_article("Women's Tour"),("du ", "Women's Tour"))
        self.assertEqual(define_article("Tour of the Gila"),("du ", "Tour of the Gila"))
        self.assertEqual(define_article("Le Samyn des Dames"),("du ", "Samyn des Dames"))
        self.assertEqual(define_article("Chrono des nations"),("du ", "Chrono des nations"))
        self.assertEqual(define_article("Flèche wallonne"),("de la ", "Flèche wallonne"))
        self.assertEqual(define_article("Amstel Gold Race"),("de l'", "Amstel Gold Race"))
 
    def test_get_class(self):
        self.assertEqual(get_class(pywikibot, repo, "Q57163391"), "Q22231106")
        self.assertEqual(get_class(pywikibot, repo, "Q57277539"), "Q23005601")
           
    def compare_dates(self):
        this_date1=pywikibot.WbTime(site=site,year=2008, month=1, day=1, precision='day')    
        this_date2=pywikibot.WbTime(site=site,year=2008, month=1, day=2, precision='day')    
        this_date3=pywikibot.WbTime(site=site,year=2008, month=2, day=1, precision='day')    
        this_date4=pywikibot.WbTime(site=site,year=2008, month=12, day=31, precision='day') 
        this_date5=pywikibot.WbTime(site=site,year=2009, month=1, day=1, precision='day')    
        self.assertEqual(compare_dates(this_date1,this_date1),0)
        self.assertEqual(compare_dates(this_date4,this_date4),0)
        self.assertEqual(compare_dates(this_date2,this_date1),1)
        self.assertEqual(compare_dates(this_date1,this_date2),2)
        self.assertEqual(compare_dates(this_date3,this_date1),1)
        self.assertEqual(compare_dates(this_date1,this_date3),2)
        self.assertEqual(compare_dates(this_date4,this_date1),1)
        self.assertEqual(compare_dates(this_date1,this_date4),2)
        self.assertEqual(compare_dates(this_date5,this_date4),1)
        self.assertEqual(compare_dates(this_date4,this_date5),2)
    
    def test_get_present_team(self):
        this_date1=pywikibot.WbTime(site=site,year=2009, month=12, day=31, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q604919")
        this_date1=pywikibot.WbTime(site=site,year=2009, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q604919")
        this_date1=pywikibot.WbTime(site=site,year=2010, month=12, day=31, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q1")
        this_date1=pywikibot.WbTime(site=site,year=2012, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q17011604")
        this_date1=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q1886678")
        this_date1=pywikibot.WbTime(site=site,year=2017, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q2651858")
        this_date1=pywikibot.WbTime(site=site,year=2018, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q2651858")
        this_date1=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')    
        self.assertEqual(get_present_team(pywikibot, site, repo, "Q563737", this_date1), "Q2651858")
        
    def test_CIOtoIDsearch(self):
        team_table=nation_team_table.load()
        self.assertEqual(CIOtoIDsearch(team_table, "FRA") , 142)
        self.assertEqual(CIOtoIDsearch(team_table, "GBR") , 145)
        self.assertEqual(CIOtoIDsearch(team_table, "ZZZ") , 0)
        
    def test_get_class_WWT(self): 
        self.assertEqual(get_class_WWT("blabla"), (True, 0, 0))
        self.assertEqual(get_class_WWT("1.1"), (True, False, False))
        self.assertEqual(get_class_WWT("1.WWT"), (True, True, False))
        self.assertEqual(get_class_WWT("1.UWT"), (True, False, True))
        
    def test_get_country(self):
        self.assertEqual(get_country(pywikibot, repo, "Q57277539"), "Q31")
        self.assertEqual(get_country(pywikibot, repo, "Q75"), "Q0")
        self.assertEqual(get_country(pywikibot, repo, "Q104640102"), "Q774")
     
    def test_get_year(self):
        self.assertEqual(get_year(pywikibot, repo, "Q57277539"),2019)
        self.assertEqual(get_year(pywikibot, repo, "Q19361204"),2015)

    def test_table_reader(self):
        result_dic={
            'road champ':[-1, 0,''],
            'road day':[-1, 1,''],
            'road month':[-1, 2,''],
            'road year':[-1, 3,''],
            'road winner':[-1, 4,''],
            'clm champ':[-1, 5,''],
            'clm day':[-1, 6,''],
            'clm month':[-1, 7,''],
            'clm year':[-1, 8,''],
            'clm winner':[-1, 9,''],
            }
   
        result_table, row_count, ecart= table_reader('champ',result_dic, 0, False)
        self.assertTrue(row_count>0)

    def test_checkprop(self):
        self.assertEqual(checkprop("P5"),"P5")
        self.assertEqual(checkprop("5"),"P5")
        self.assertEqual(checkprop(5),"P5")

    def test_checkid(self):
        self.assertEqual(checkid("Q5"),"Q5")
        self.assertEqual(checkid("5"),"Q5")
        self.assertEqual(checkid(5),"Q5")

    def test_get_single_or_stage(self):
        self.assertEqual(get_single_or_stage("1.1"),True)
        self.assertEqual(get_single_or_stage("2.1"),False)
        self.assertEqual(get_single_or_stage(21),True) 
        self.assertEqual(get_single_or_stage("abc"),True)
 
    def test_excel_to_csv(self):
        filepath="tests/Conversion_test.xlsx"
        destination="tests/Conversion_test.csv"
        res=excel_to_csv(filepath, destination)
        self.assertEqual(res,destination)
        
        filepath=res
        default_separator=";"
        kk=1
        
        with open(filepath, newline='') as csvfile:
            file_object = csv.reader(csvfile, delimiter=default_separator, quotechar='|')
            for row in file_object: 
                if kk==1:
                    self.assertEqual(row[0],'Rank')
                    self.assertEqual(row[1],'BIB')
                    self.assertEqual(row[2],'Last Name')
                elif kk==2:
                    self.assertEqual(row[0],'1')
                    self.assertEqual(row[1],'21')
                    self.assertEqual(row[2],'GUNNEWIJK')
                kk=kk+1

    def test_bot_or_site(self):
        self.assertEqual(bot_or_site(),True)  
        
    def test_teamCIOsearch(self):
        nation_table= nation_team_table.load()
        
        self.assertEqual(teamCIOsearch(nation_table,"AAA"),0)    
        self.assertEqual(teamCIOsearch(nation_table,"AFG"),0)
        self.assertEqual(teamCIOsearch(nation_table,"ALB"),1)
        self.assertTrue(teamCIOsearch(nation_table,"MGL")!=0)
       
    def test_float_to_int(self):
        self.assertEqual( float_to_int('1149.67'),1149)  
        self.assertEqual( float_to_int("1149.67"),1149)  
        self.assertEqual( float_to_int("1149.07"),1149)  
        self.assertEqual( float_to_int(1149.67),1149)  
        self.assertEqual( float_to_int(1149),1149)  
        self.assertEqual( float_to_int(''),0)  #exception management
        self.assertEqual( float_to_int(""),0)
 
    def test_get_race_name(self):
        res=get_race_name(pywikibot, repo, "Q104640102")   
        self.assertEqual(res,"Tour féminin du Guatemala")
 
    def test_get_race_begin(self):
        race_begin=pywikibot.WbTime(site=site,year=2020, month=10, day=14, precision='day')    
        res=get_race_begin(pywikibot, repo, "Q79137942")
        self.assertEqual( res,race_begin)  

    def test_get_end_date(self):
        race_end=pywikibot.WbTime(site=site,year=2020, month=10, day=16, precision='day')    
        res=get_end_date(pywikibot, repo, "Q79137942")
        self.assertEqual( res,race_end) 
         
    def test_time_converter(self):
        res=time_converter("03:38'05''")
        self.assertEqual(res,(13085,False))
        res=time_converter("03:38:05")
        self.assertEqual(res,(13085,False))   
    def test_date_finder(self):
        #easy case
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=4, precision='day')    
       
        number=1
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(pywikibot,2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=3, precision='day')    
        self.assertEqual(res,exp)
        #check that the function does not change the value of race_begin
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        res=date_finder(pywikibot,1,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,exp)
        
        res=date_finder(pywikibot,4,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=4, precision='day')    
        self.assertEqual(res,exp)  
        self.assertEqual(res,race_end)  
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=6, precision='day') 
        res=date_finder(pywikibot,4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  

        #not possible
        number=0
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        
        #prologue
        first_stage=0
        number=0
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        number=1
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        self.assertEqual(res,exp)
        
        #month limit, january
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=1, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=2, day=2, precision='day')    
        number=1
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(pywikibot,2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=31, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=2, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  
        
        #month limit, april
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=4, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=5, day=3, precision='day')    
        number=1
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(pywikibot,2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=5, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=5, day=2, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)       
        
        #year limit
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2014, month=12, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        number=1
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(pywikibot,2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2014, month=12, day=31, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(pywikibot,4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  

        #case thailand
        first_stage=1
        last_stage=3
        number=1
        race_begin=pywikibot.WbTime(site=site,year=2020, month=10, day=14, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2020, month=10, day=16, precision='day')  
        res=date_finder(pywikibot,number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
              
if __name__ == '__main__':
    unittest.main()
