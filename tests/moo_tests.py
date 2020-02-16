#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:10:48 2020

@author: maxime
"""

import unittest

class TestMoo(unittest.TestCase):
    def test_contagen(self):
        test_table=['anna','van','der','breggen']
        self.assertEqual(concaten(test_table,1), 'van der breggen')
        self.assertEqual(concaten(test_table,2), 'der breggen')
    
    
    def test_lower(self):
        tested_name1=ThisName('Anna van der Breggen')
        tested_name2=ThisName('anna van der breggen')
        tested_name3=ThisName('anna van der Breggen')
        self.assertEqual(tested_name1.name_cor, 'anna van der breggen')
        self.assertEqual(tested_name2.name_cor, 'anna van der breggen')
        self.assertEqual(tested_name3.name_cor, 'anna van der breggen')
    
    def test_accent(self):
        tested_name1=ThisName('Mia Radotić')
        tested_name2=ThisName('Olga Zabelinskaïa')
        tested_name3=ThisName('Edita Pučinskaitė')
        self.assertEqual(tested_name1.name_cor, 'mia radotic')
        self.assertEqual(tested_name2.name_cor, 'olga zabelinskaia')
        self.assertEqual(tested_name3.name_cor, 'edita pucinskaite')
      
    def test_check_and_revert(self):
        tested_name1=ThisName('anna van der breggen')
        tested_name2=ThisName('Anna van der Breggen')
        tested_name3=ThisName('Anna VAN DER BREGGEN')
        tested_name4=ThisName('VAN DER BREGGEN Anna')
        self.assertEqual(tested_name1.name_cor, 'anna van der breggen')
        self.assertEqual(tested_name2.name_cor, 'anna van der breggen')
        self.assertEqual(tested_name3.name_cor, 'anna van der breggen')
        self.assertEqual(tested_name4.name_cor, 'anna van der breggen')
        
    def test_cyclist_inherit(self):
        tested_cyclist1=Cyclist(1, 'Mia Radotić', 'item')
        tested_cyclist2=Cyclist(1,'Olga Zabelinskaïa','item')
        tested_cyclist3=Cyclist(1,'Edita Pučinskaitė','item')
        self.assertEqual(tested_cyclist1.name_cor, 'mia radotic')
        self.assertEqual(tested_cyclist2.name_cor, 'olga zabelinskaia')
        self.assertEqual(tested_cyclist3.name_cor, 'edita pucinskaite')
        
    def test_cyclist_sortkey(self):
        tested_cyclist1=Cyclist(1,'anna breggen','item')
        self.assertEqual(tested_cyclist1.sortkey, 'breggen')
        tested_cyclist2=Cyclist(1,'anna van breggen','item')
        self.assertEqual(tested_cyclist2.sortkey, 'van breggen')      
      #  tested_cyclist3=Cyclist(1,'anna mo breggen','item')
        #a console is expected
       # self.assertEqual(tested_cyclist3.sortkey, 'mo breggen')  

    def test_race_sortkey(self):
        tested_race1=Race(1,'Grand Prix du Test','item','date')
        self.assertEqual(tested_race1.sortkey, 'grand prix du test')
        tested_race2=Race(1,'Championnats du Test','item','date')
        self.assertEqual(tested_race2.sortkey, 'test')    

    def test_team_sortkey(self):
        tested_team1=Team(1,'Orica AIS 2020','item','date')
        self.assertEqual(tested_team1.sortkey, 'orica ais 2020')
        tested_team2=Team(1,'equipe de France','item','date')
        self.assertEqual(tested_team2.sortkey, 'france')    

    
if __name__ == '__main__':
    unittest.main()