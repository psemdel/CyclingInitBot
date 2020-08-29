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
from src.startlist_importer import (find_sortkey, search_item_national_team,
                                    find_national_team)

from src.cycling_init_bot_low import (table_reader, cyclists_table_reader)
from src.bot_log import Log
from src import race_list
from src import nation_team_table

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class NationalTeam(unittest.TestCase):  
    def test_find_sortkey(self):
        dic=['féminine de cyclisme']
        
        self.assertEqual(
            find_sortkey('équipe de France féminine de cyclisme sur route 2019',dic),
            True)
        self.assertEqual(
            find_sortkey('équipe de France de cyclisme sur route 2019',dic),
            False)   
        self.assertEqual(
            find_sortkey('équipe de France espoirs de cyclisme sur route 2018',dic),
            False)   
    
        dic=['espoirs de cyclisme']
    
        self.assertEqual(
            find_sortkey('équipe de France féminine de cyclisme sur route 2019',dic),
            False)
        self.assertEqual(
            find_sortkey('équipe de France de cyclisme sur route 2019',dic),
            False)   
        self.assertEqual(
            find_sortkey('équipe de France espoirs de cyclisme sur route 2018',dic),
            True)   
    
        dic=['de cyclisme']
    
        self.assertEqual(
            find_sortkey('équipe de France féminine de cyclisme sur route 2019',dic),
            True)
        self.assertEqual(
            find_sortkey('équipe de France de cyclisme sur route 2019',dic),
            True)   
        self.assertEqual(
            find_sortkey('équipe de France espoirs de cyclisme sur route 2018',dic),
            True)   
        

    def test_search_item_national_team(self):
         search_string="FRA 2019"
         dic=['féminine de cyclisme']
         dic_neg=[]
         
         res=search_item_national_team(pywikibot, site,repo, search_string, dic,dic_neg)
         self.assertEqual(res,'Q56887783')
         
         dic=['de cyclisme']
         dic_neg=['féminine de cyclisme','espoirs de cyclisme']
         res=search_item_national_team(pywikibot, site, repo,search_string, dic,dic_neg)
         self.assertEqual(res,'Q60418112')
         
         dic=['espoirs de cyclisme']
         dic_neg=[]
         res=search_item_national_team(pywikibot, site,repo, search_string, dic,dic_neg)
         self.assertEqual(res,'Q0')      
     
         search_string="équipe de France féminine de cyclisme sur route 2019"
         dic=['féminine de cyclisme']
         dic_neg=[]
         res=search_item_national_team(pywikibot, site,repo, search_string, dic,dic_neg)
         self.assertEqual(res,'Q56887783')
       
    def test_find_national_team(self):
        man_or_woman=u'woman'
        force_nation_team=False
        time_of_race=pywikibot.WbTime(site=site,year=2020, month=8, day=27, precision='day')    
        year=time_of_race.year
        log=Log()
        nation_table= nation_team_table.load()
        result_dic={
        'rank':[-1, 0, ''],
        'last name':[-1, 1,''],
        'first name':[-1, 2,''],
        'name':[-1, 3,''],
        'result':[-1, 4,'time'],  #startlist only with time
        'points':[-1, 5, 'points'],
        'team code':[-1, 7, ''],
        'ecart':[1,6,'time'],  #always created
        'bib':[-1,8,''] #dossard
        }
    
        result_table, row_count, ecart=table_reader('National_team_tests', result_dic,0,False)
        result_table=sorted(result_table, key=lambda tup: int(tup[8]))
        list_of_cyclists, all_riders_found=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, nosortkey=True)

        res_list_of_cyclists, log=find_national_team(pywikibot,site,repo,list_of_cyclists, 
                       result_table, result_dic, row_count, nation_table, 
                      force_nation_team, year, log, man_or_woman,
                       time_of_race)
    
        
        self.assertEqual(res_list_of_cyclists[0].national_team,True)
        self.assertEqual(res_list_of_cyclists[1].national_team,True)
        self.assertEqual(res_list_of_cyclists[2].national_team,True)
        self.assertEqual(res_list_of_cyclists[3].national_team,True)
        self.assertEqual(res_list_of_cyclists[4].national_team,True)
        self.assertEqual(res_list_of_cyclists[5].national_team,True)
        self.assertEqual(res_list_of_cyclists[6].national_team,True)
        self.assertEqual(res_list_of_cyclists[7].national_team,True)
        self.assertEqual(res_list_of_cyclists[8].national_team,True)
        self.assertEqual(res_list_of_cyclists[9].national_team,True)
        self.assertEqual(res_list_of_cyclists[10].national_team,True)
        self.assertEqual(res_list_of_cyclists[11].national_team,True)
        
        force_nation_team=True
        res_list_of_cyclists, log=find_national_team(pywikibot,site,repo,list_of_cyclists, 
                 result_table, result_dic, row_count, nation_table, 
                 force_nation_team, year, log, man_or_woman,
                 time_of_race)
       
        self.assertEqual(res_list_of_cyclists[0].national_team,True)
        self.assertEqual(res_list_of_cyclists[1].national_team,True)
        self.assertEqual(res_list_of_cyclists[2].national_team,True)
        self.assertEqual(res_list_of_cyclists[3].national_team,True)
        self.assertEqual(res_list_of_cyclists[4].national_team,True)
        self.assertEqual(res_list_of_cyclists[5].national_team,True)
        self.assertEqual(res_list_of_cyclists[6].national_team,True)
        self.assertEqual(res_list_of_cyclists[7].national_team,True)
        self.assertEqual(res_list_of_cyclists[8].national_team,True)
        self.assertEqual(res_list_of_cyclists[9].national_team,True)
        self.assertEqual(res_list_of_cyclists[10].national_team,True)
        self.assertEqual(res_list_of_cyclists[11].national_team,True)
         
        force_nation_team=False
        result_table, row_count, ecart=table_reader('National_team_tests_neg', result_dic,0,False)
        result_table=sorted(result_table, key=lambda tup: int(tup[8]))
        list_of_cyclists, all_riders_found=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, nosortkey=True)

        res_list_of_cyclists, log=find_national_team(pywikibot,site,repo,list_of_cyclists, 
                       result_table, result_dic, row_count, nation_table, 
                      force_nation_team, year, log, man_or_woman,
                       time_of_race)
        
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
        
if __name__ == '__main__':
    unittest.main()