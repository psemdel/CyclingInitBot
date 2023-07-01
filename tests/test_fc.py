#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:40:34 2022

@author: maxime
"""

import pywikibot
import unittest

from src.FirstCyclingAPI.first_cycling_api.combi import combi_results_startlist

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestFC(unittest.TestCase):
    def test_startlist(self):
        df= combi_results_startlist(9045,2023).results_table

        sub_df=df[df["Inv name"]=="wiebes lorena"]
        self.assertEqual(sub_df.iloc[0]["Rider"],"Lorena Wiebes")
        self.assertEqual(sub_df.iloc[0]["Pos"],"1")
        self.assertEqual(sub_df.iloc[0]["BIB"],1.0)
    
        sub_df=df[df["Inv name"]=="bredewold mischa"]
        
        self.assertEqual(sub_df.iloc[0]["Rider"],"Mischa Bredewold")
        self.assertEqual(sub_df.iloc[0]["Pos"],"38")
        self.assertEqual(sub_df.iloc[0]["BIB"],2.0)
    
        sub_df=df[df["Inv name"]=="cecchini elena"]
        
        self.assertEqual(sub_df.iloc[0]["Rider"],"Elena Cecchini")
        self.assertEqual(sub_df.iloc[0]["Pos"],"DNF")
        self.assertEqual(sub_df.iloc[0]["BIB"],3.0)  
        
        sub_df=df[df["Inv name"]=="franz heidi"]
        
        self.assertEqual(sub_df.iloc[0]["Rider"],"Heidi Franz")
        self.assertEqual(sub_df.iloc[0]["Pos"],"62")
        self.assertEqual(sub_df.iloc[0]["BIB"],201.0)          

    
if __name__ == '__main__':
    unittest.main()        
