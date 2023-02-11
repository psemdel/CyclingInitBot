#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:28:49 2022

@author: maxime
"""

import pywikibot
import unittest
from src.base import Race

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestRace(unittest.TestCase):
    def test_race_sortkey(self):
        r1=Race(name='Grand Prix du Test')
        self.assertEqual(r1.sortkey, 'grand prix du test')
        r2=Race(name='Championnats du Test')
        self.assertEqual(r2.sortkey, 'test')    

    def test_get_year(self):
        r1=Race(id="Q57277539")
        self.assertEqual(r1.get_year(),2019)
        r1=Race(id="Q19361204")
        self.assertEqual(r1.get_year(),2015)   
        
    def test_get_race_name(self):
        r1=Race(id="Q104640102")
        self.assertEqual(r1.get_race_name(),"Tour féminin du Guatemala")
 
    def test_get_race_begin(self):
        race_begin=pywikibot.WbTime(site=site,year=2020, month=10, day=14, precision='day')    
        r1=Race(id="Q79137942")
        self.assertEqual(r1.get_begin_date(),race_begin)  

    def test_get_end_date(self):
        race_end=pywikibot.WbTime(site=site,year=2020, month=10, day=16, precision='day')    
        r1=Race(id="Q79137942")
        self.assertEqual(r1.get_end_date(),race_end) 

    def test_get_class(self):
        r1=Race(id="Q57163391")
        self.assertEqual(r1.get_class(), "Q22231106")
        r1=Race(id="Q57277539")
        self.assertEqual(r1.get_class(), "Q23005601")
        
    def test_get_is_women(self):
        r1=Race(id="Q115443011")
        self.assertTrue(r1.get_is_women())
        r1=Race(id="Q116148731")
        self.assertFalse(r1.get_is_women())    
        r1=Race(id="Q42053105")
        self.assertTrue(r1.get_is_women())  
        
    def test_get_is_stage(self):
        r1=Race(id="Q116302534")
        self.assertFalse(r1.get_is_stage())    
        r1=Race(id="Q116687807")
        self.assertTrue(r1.get_is_stage())           

if __name__ == '__main__':
    unittest.main()
