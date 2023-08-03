#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:31 2020

@author: maxime
"""

import pywikibot
import unittest

from src.startlist_importer import StartlistImporter
from src.func import cyclists_table_reader, table_reader
from src.base import PyItem

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestStartList(unittest.TestCase):  
    def test_find_national_team1(self):
        man_or_woman=u'woman'
          
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team=False,test=True)
        
        df,_,_,log=table_reader('National_team_tests',None,need_complete=True,rider=True)
        df=df.sort_values(["BIB"])
        sl.list_of_cyclists,_ = cyclists_table_reader(df)
        res_list_of_cyclists=sl.find_national_team(df)
        
        #NED makes problem
        self.assertEqual(res_list_of_cyclists[9].national_team,True) #Fra then ITA
        self.assertEqual(res_list_of_cyclists[10].national_team,True)
        self.assertEqual(res_list_of_cyclists[11].national_team,True)
        self.assertEqual(res_list_of_cyclists[12].national_team,True)
        self.assertEqual(res_list_of_cyclists[13].national_team,True)
        self.assertEqual(res_list_of_cyclists[14].national_team,True)
        self.assertEqual(res_list_of_cyclists[15].national_team,True)
        self.assertEqual(res_list_of_cyclists[16].national_team,True)
        self.assertEqual(res_list_of_cyclists[17].national_team,True)
        self.assertEqual(res_list_of_cyclists[18].national_team,True)
        self.assertEqual(res_list_of_cyclists[19].national_team,True)
        self.assertEqual(res_list_of_cyclists[20].national_team,True)

    def test_find_national_team3(self):    
        man_or_woman=u'woman'
        
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team=False,test=True)
        sl.time_of_race=pywikibot.WbTime(site=site,year=2020, month=8, day=27, precision='day')    
        sl.year=sl.time_of_race.year
        
        df,_,_,log=table_reader('National_team_tests_neg',None,need_complete=True,rider=True)
        df=df.sort_values(["BIB"])
        sl.list_of_cyclists,_ = cyclists_table_reader(df)
        res_list_of_cyclists=sl.find_national_team(df)   
        
        self.assertEqual(res_list_of_cyclists[0].national_team,False)
        self.assertEqual(res_list_of_cyclists[1].national_team,False)
        self.assertEqual(res_list_of_cyclists[2].national_team,False)
        self.assertEqual(res_list_of_cyclists[3].national_team,False)
        self.assertEqual(res_list_of_cyclists[4].national_team,False)
        self.assertEqual(res_list_of_cyclists[5].national_team,False)
        self.assertEqual(res_list_of_cyclists[6].national_team,False)
        self.assertEqual(res_list_of_cyclists[7].national_team,False)
        self.assertEqual(res_list_of_cyclists[8].national_team,False)
        self.assertEqual(res_list_of_cyclists[9].national_team,False)
        self.assertEqual(res_list_of_cyclists[10].national_team,False)
        self.assertEqual(res_list_of_cyclists[11].national_team,False)
 
    def test_find_national_team4(self):
        man_or_woman=u'woman'
        
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team=False,test=True)
        sl.time_of_race=pywikibot.WbTime(site=site,year=2015, month=8, day=27, precision='day')   
        sl.year=sl.time_of_race.year
        
        df, _, _, _=table_reader('National_team_tests2',None,need_complete=True,rider=True)
        df=df.sort_values(["BIB"])
        sl.list_of_cyclists, _ = cyclists_table_reader(df)
        res_list_of_cyclists=sl.find_national_team(df)
    
        #FRA and BEL
        self.assertEqual(res_list_of_cyclists[93].national_team,True)
        self.assertEqual(res_list_of_cyclists[94].national_team,True)
        self.assertEqual(res_list_of_cyclists[95].national_team,True)
        self.assertEqual(res_list_of_cyclists[96].national_team,True)
        self.assertEqual(res_list_of_cyclists[97].national_team,True)
        self.assertEqual(res_list_of_cyclists[98].national_team,True)
        self.assertEqual(res_list_of_cyclists[99].national_team,True)
        self.assertEqual(res_list_of_cyclists[100].national_team,True)
        self.assertEqual(res_list_of_cyclists[101].national_team,True)
        self.assertEqual(res_list_of_cyclists[102].national_team,True)
        self.assertEqual(res_list_of_cyclists[103].national_team,True)
       # self.assertEqual(res_list_of_cyclists[104].national_team,True)
 
    def test_main(self):
        id_race='Q4115189' #sandbox
        prologue_or_final=0 #0=prologue, 1=final, 2=one day race
        chrono=True
        man_or_woman=u'woman'
        
        pyItem=PyItem(id=id_race)
        pyItem.add_value("P2094","Q1451845","add women cycling")
        
        d=pywikibot.WbTime(site=site, year=2023, month=7, day=8, precision='day')  
        pyItem.add_value("P585",d,"add date",date=True)

        f=StartlistImporter(
            prologue_or_final,
            id_race, 
            chrono,
            man_or_woman, 
            force_nation_team=False,
            test=False,
            fc=9064,
            add_unknown_rider=False)
        f.main()
        
        

        
if __name__ == '__main__':
    unittest.main()
