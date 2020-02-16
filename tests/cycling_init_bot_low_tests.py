#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:31 2020

@author: maxime
"""

import unittest

class TestSearch(unittest.TestCase):  
    def test_search_race(self):
        race_table, race_dic = race_list()
        result1, result2 = search_race('Tour Santos Women', race_table,race_dic)
        self.assertEqual(result1, 22661614)
        self.assertEqual(result2 , "du ")
        result1, result2 = search_race('Santos Women Tour', race_table,race_dic)
        self.assertEqual(result1, 22661614)
        self.assertEqual(result2 , "du ")    
        result1, result2 = search_race('Sintos Women Tour', race_table,race_dic)
        self.assertEqual(result1, 0 )
        self.assertEqual(result2 , 0)     
        
    def test_other(self):
        [pywikibot,site,repo,time]=wiki_init()  
        self.assertFalse(is_it_a_cyclist(pywikibot, repo, 'Q38222'))
        self.assertTrue(is_it_a_cyclist(pywikibot, repo, 'Q563737'))
        
        self.assertEqual(search_item(pywikibot, site, 'Anna van der Breggen'),'Q563737')
        self.assertEqual(search_item(pywikibot, site, 'Anna'),'Q1')
        self.assertEqual(search_item(pywikibot, site, 'zz14563465465wuichWRUPIUDGCOIUWR'),'Q0')
        self.assertEqual(search_item(pywikibot, site, 'Elizabeth Banks'),'Q1')
        
        self.assertEqual(search_rider(pywikibot, site, repo,'Anna van der Breggen','',''),'Q563737')
        self.assertEqual(search_rider(pywikibot, site, repo,'Elizabeth Banks','',''),'Q47295776')
        self.assertEqual(search_rider(pywikibot, site, repo,0, 'Elizabeth', 'Banks'),'Q47295776')
        
    
if __name__ == '__main__':
    unittest.main()