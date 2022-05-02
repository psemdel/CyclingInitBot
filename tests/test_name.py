#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:10:48 2020

@author: maxime
"""

import pywikibot
import unittest
from src.name import (concaten, Name, CyclistName)

class TestName(unittest.TestCase):
    def test_contagen(self):
        test_table=['anna','van','der','breggen']
        self.assertEqual(concaten(test_table,1), 'van der breggen')
        self.assertEqual(concaten(test_table,2), 'der breggen')
    
    def test_lower(self):
        n1=CyclistName('Anna van der Breggen')
        n2=CyclistName('anna van der breggen')
        n3=CyclistName('anna van der Breggen')
        self.assertEqual(n1.name_cor, 'anna van der breggen')
        self.assertEqual(n2.name_cor, 'anna van der breggen')
        self.assertEqual(n3.name_cor, 'anna van der breggen')
    
    def test_accent(self):
        n1=CyclistName('Mia Radotić')
        n2=CyclistName('Olga Zabelinskaïa')
        n3=CyclistName('Edita Pučinskaitė')
        self.assertEqual(n1.name_cor, 'mia radotic')
        self.assertEqual(n2.name_cor, 'olga zabelinskaia')
        self.assertEqual(n3.name_cor, 'edita pucinskaite')
        n1=CyclistName('Felix Groß')
        self.assertEqual(n1.name_cor, 'felix gross')
      
    def test_check_and_revert(self):
        n1=CyclistName('anna van der breggen')
        n2=CyclistName('Anna van der Breggen')
        n3=CyclistName('Anna VAN DER BREGGEN')
        n4=CyclistName('VAN DER BREGGEN Anna')
        self.assertEqual(n1.name_cor, 'anna van der breggen')
        self.assertEqual(n2.name_cor, 'anna van der breggen')
        self.assertEqual(n3.name_cor, 'anna van der breggen')
        self.assertEqual(n4.name_cor, 'anna van der breggen')
        n1=CyclistName('SORGHO W. Mathias')
        self.assertEqual(n1.name_cor, 'w. mathias sorgho')
        n1=CyclistName('W. Mathias Sorgho')
        self.assertEqual(n1.name_cor, 'w. mathias sorgho')
        n1=CyclistName('GROß Felix')
        self.assertEqual(n1.name_cor, 'felix gross') #replace ß through ss

        n1=Name('GP')
        self.assertEqual(n1.name_cor, 'gp')
        n1=Name('Grand Prix')
        self.assertEqual(n1.name_cor, 'grand prix')
    
if __name__ == '__main__':
    unittest.main()
