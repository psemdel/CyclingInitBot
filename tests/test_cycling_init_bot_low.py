#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:31 2020

@author: maxime
"""
import time
import sys, os

import unittest
from Bot.race_list import *
import pywikibot
from Bot.cycling_init_bot_low import *


site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestSearch(unittest.TestCase):  
    def test_search_race(self):
        race_table, race_dic = race_list.load()
        result1, result2 = low.search_race('Tour Santos Women', race_table,race_dic)
        self.assertEqual(result1, 22661614)
        self.assertEqual(result2 , "du ")
        result1, result2 = low.search_race('Santos Women Tour', race_table,race_dic)
        self.assertEqual(result1, 22661614)
        self.assertEqual(result2 , "du ")    
        result1, result2 = low.search_race('Sintos Women Tour', race_table,race_dic)
        self.assertEqual(result1, 0 )
        self.assertEqual(result2 , 0)     
        
    def test_other(self):
        self.assertFalse(low.is_it_a_cyclist(pywikibot, repo, 'Q38222'))
        self.assertTrue(low.is_it_a_cyclist(pywikibot, repo, 'Q563737'))
        
        self.assertEqual(low.search_item(pywikibot, site, 'Anna van der Breggen'),'Q563737')
        self.assertEqual(low.search_item(pywikibot, site, 'Anna'),'Q1')
        self.assertEqual(low.search_item(pywikibot, site, 'zz14563465465wuichWRUPIUDGCOIUWR'),'Q0')
        self.assertEqual(low.search_item(pywikibot, site, 'Elizabeth Banks'),'Q1')
        
        self.assertEqual(low.search_rider(pywikibot, site, repo,'Anna van der Breggen','',''),'Q563737')
        self.assertEqual(low.search_rider(pywikibot, site, repo,'Elizabeth Banks','',''),'Q47295776')
        self.assertEqual(low.search_rider(pywikibot, site, repo,0, 'Elizabeth', 'Banks'),'Q47295776')
        
    def test_table_reader(self):
        result_dic={
        'Road champ':[-1, 0,''],
        'Road day':[-1, 1,''],
        'Road month':[-1, 2,''],
        'Road year':[-1, 3,''],
        'Road winner':[-1, 4,''],
        'Clm champ':[-1, 5,''],
        'Clm day':[-1, 6,''],
        'Clm month':[-1, 7,''],
        'Clm year':[-1, 8,''],
        'Clm winner':[-1, 9,''],
        }
        
        result_table, row_count, ecart_global=low.table_reader('champ',result_dic, 0, False)
        self.assertTrue(row_count>0)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch, 'test'))
    return suite    

if __name__ == '__main__':
    unittest.main()  
