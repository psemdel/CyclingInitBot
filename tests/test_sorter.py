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
import os
from src.sorter import (check_if_team)

from src.bot_log import Log
from src import race_list
from src import nation_team_table

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class NameSorter(unittest.TestCase):  
    def test_team(self):
        item = pywikibot.ItemPage(repo, "Q100595064")
        item.get()
        self.assertTrue(check_if_team(item))
        item = pywikibot.ItemPage(repo, "Q27538420")
        item.get()
        self.assertFalse(check_if_team(item))
        
        
        
        
if __name__ == '__main__':
    unittest.main()
