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

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestStartList(unittest.TestCase):  
    def test_find_national_team1(self):
        man_or_woman=u'woman'
        force_nation_team=False
          
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team,test=True)
        
        df,_,_,log=table_reader('National_team_tests',need_complete=True,rider=True)
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
        force_nation_team=False
        
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team,test=True)
        sl.time_of_race=pywikibot.WbTime(site=site,year=2020, month=8, day=27, precision='day')    
        sl.year=sl.time_of_race.year
        
        df,_,_,log=table_reader('National_team_tests_neg',need_complete=True,rider=True)
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
        force_nation_team=False
        
        sl=StartlistImporter(0, "Q20681024", False, man_or_woman,force_nation_team,test=True)
        sl.time_of_race=pywikibot.WbTime(site=site,year=2015, month=8, day=27, precision='day')   
        sl.year=sl.time_of_race.year
        
        df, _, _, _=table_reader('National_team_tests2',need_complete=True,rider=True)
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
 
        
if __name__ == '__main__':
    unittest.main()
