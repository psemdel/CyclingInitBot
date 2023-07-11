#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:10:27 2020

@author: maxime
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:16:31 2020

@author: maxime
"""
import pywikibot
import unittest

from src.team_importer import TeamImporter
from src.base import PyItem

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestNameSorter(unittest.TestCase):  
    def test_main(self):
        id_race='Q4115189'
        pyItem=PyItem(id=id_race)
        pyItem.add_value("P2094","Q1451845","add women cycling")
        
        f=TeamImporter(
            id_race, 
            test=False,
            fc=9064)
        f.main()
        
if __name__ == '__main__':
    unittest.main()
