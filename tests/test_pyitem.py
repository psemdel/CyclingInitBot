#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:37:14 2022

@author: maxime
"""

import pywikibot
import unittest
from src.base import PyItem

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestRace(unittest.TestCase):
    def test_get_country(self):
        p1=PyItem(id="Q57277539")
        self.assertEqual(p1.get_country(), "Q31")
        p1=PyItem(id="Q75")
        self.assertEqual(p1.get_country(), None)
        p1=PyItem(id="Q104640102")
        self.assertEqual(p1.get_country(), "Q774")

    def test_link_year(self):
        p1=PyItem(id="Q110369548")
        id_master, id_previous, id_next=p1.link_year(2022,test=True)
        self.assertEqual(id_master,"Q1757136")
        self.assertEqual(id_previous,"Q104523104")
        self.assertEqual(id_next,"Q115729649")
        
        p1=PyItem(id="Q110369548")
        id_master, id_previous, id_next=p1.link_year(2022,id_master="Q1757136",test=True)
        self.assertEqual(id_master,"Q1757136")
        self.assertEqual(id_previous,"Q104523104")
        self.assertEqual(id_next,"Q115729649")
        
        p1=PyItem(id="Q104523104")
        id_master, id_previous, id_next=p1.link_year(2021,test=True)
        self.assertEqual(id_master,"Q1757136")
        self.assertEqual(id_previous,"Q74725319")
        self.assertEqual(id_next,"Q110369548")
        
        p1=PyItem(id="Q105142737")
        id_master, id_previous, id_next=p1.link_year(2021,test=True)
        self.assertEqual(id_master,"Q17037135")
        self.assertEqual(id_previous,"Q74725071")
        self.assertEqual(id_next,"Q110794327")

if __name__ == '__main__':
    unittest.main()
