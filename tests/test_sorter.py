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

from src.sorter import NameSorter
from src.base import PyItem

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestNameSorter(unittest.TestCase):  
    def test_team(self):
        n=NameSorter("Q100595064","P123")
        self.assertTrue(n.check_if_team())
        n=NameSorter("Q27538420","P123")  
        self.assertFalse(n.check_if_team())     

    def test_main(self):
        id_team='Q4115189'
        prop="P1923" # 'has part (P527)', 'participating team (P1923)'
        
        f= NameSorter(
            id_team, 
            prop,
            test=False)
        f.main()  
        
if __name__ == '__main__':
    unittest.main()
