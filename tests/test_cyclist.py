#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:19:50 2022

@author: maxime
"""

import pywikibot
import unittest
from src.base import Cyclist

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestCyclist(unittest.TestCase):
    def test_cyclist_inherit(self):
        c1=Cyclist(name='Mia Radotić')
        c2=Cyclist(name='Olga Zabelinskaïa')
        c3=Cyclist(name='Edita Pučinskaitė')
        self.assertEqual(c1.name_cor, 'mia radotic')
        self.assertEqual(c2.name_cor, 'olga zabelinskaia')
        self.assertEqual(c3.name_cor, 'edita pucinskaite')
        
    def test_cyclist_sortkey(self):
        c1=Cyclist(name='anna breggen')
        self.assertEqual(c1.sortkey, 'breggen')
        c2=Cyclist(name='anna van breggen')
        self.assertEqual(c2.sortkey, 'van breggen')   
        c3=Cyclist(name='Kaswanto')
        self.assertEqual(c3.sortkey, 'kaswanto')

    def test_get_present_team(self):
        c1=Cyclist(id="Q563737")
        this_date1=pywikibot.WbTime(site=site,year=2009, month=12, day=31, precision='day') 
        self.assertEqual(c1.get_present_team(this_date1), "Q604919")
        this_date1=pywikibot.WbTime(site=site,year=2009, month=1, day=1, precision='day')  
        self.assertEqual(c1.get_present_team(this_date1), "Q604919")
        this_date1=pywikibot.WbTime(site=site,year=2010, month=12, day=31, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q1")
        this_date1=pywikibot.WbTime(site=site,year=2012, month=1, day=1, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q17011604")
        this_date1=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day') 
        self.assertEqual(c1.get_present_team(this_date1), "Q1886678")
        this_date1=pywikibot.WbTime(site=site,year=2017, month=1, day=1, precision='day') 
        self.assertEqual(c1.get_present_team(this_date1), "Q2651858")
        this_date1=pywikibot.WbTime(site=site,year=2018, month=1, day=1, precision='day') 
        self.assertEqual(c1.get_present_team(this_date1), "Q2651858")
        this_date1=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q2651858")  
        
        c1=Cyclist(id="Q58454725")
        this_date1=pywikibot.WbTime(site=site,year=2022, month=3, day=30, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q21484669")  
        c1=Cyclist(id="Q61480155")
        this_date1=pywikibot.WbTime(site=site,year=2022, month=3, day=30, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q21484669")                    
        c1=Cyclist(id="Q98923509")
        this_date1=pywikibot.WbTime(site=site,year=2022, month=3, day=30, precision='day')    
        self.assertEqual(c1.get_present_team(this_date1), "Q21484669")          

    def test_get_nationality(self):
        c1=Cyclist(id="Q13893333")
        this_date1=pywikibot.WbTime(site=site,year=2009, month=12, day=31, precision='day')    
        self.assertEqual(c1.get_nationality(this_date1),"Q142")
        c1=Cyclist(id="Q16215626")
        self.assertEqual(c1.get_nationality(this_date1),"Q212")
        c1=Cyclist(id="Q270555")
        self.assertEqual(c1.get_nationality(this_date1),"Q35")
        this_date2=pywikibot.WbTime(site=site,year=2019, month=12, day=31, precision='day')  
        self.assertEqual(c1.get_nationality(this_date2),"Q664")
        
if __name__ == '__main__':
    unittest.main()
