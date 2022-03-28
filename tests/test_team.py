#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:35:27 2022

@author: maxime
"""

import pywikibot
import unittest
from src.base import Team

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestTeam(unittest.TestCase):
    def test_team_sortkey(self):
        t1=Team(name='Orica AIS 2020')
        self.assertEqual(t1.sortkey, 'orica ais 2020')
        t2=Team(name='equipe de France')
        self.assertEqual(t2.sortkey, 'france')    
        t3=Team(name='SC Michela Fanini 2000')
        self.assertEqual(t3.sortkey, 'sc michela fanini 2000')

if __name__ == '__main__':
    unittest.main()