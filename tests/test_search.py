#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:59:49 2022

@author: maxime
"""
import unittest

from src.base import Search

class TestSearch(unittest.TestCase):  
    def test_search_race(self):
        s=Search('Tour Santos Women')
        r1, r2 = s.race()
        self.assertEqual(r1, "Q22661614")
        self.assertEqual(r2 , "du ")
        
        s=Search('Santos Women Tour')
        r1, r2 = s.race()
        self.assertEqual(r1, "Q22661614")
        self.assertEqual(r2 , "du ")
        
        s=Search('Suntos Women Tour')
        r1, r2 =  s.race()
        self.assertEqual(r1, "Q0")
        self.assertEqual(r2 , "")
        
        s=Search("Grand Prix International d'Isbergues")
        r1, r2 =  s.race()
        self.assertEqual(r1, "Q56703296")
        self.assertEqual(r2 , "du ")
        
        s=Search("GP de Plouay - Lorient- Agglomération Trophée CERATIZIT")
        r1, r2 =  s.race()
        self.assertEqual(r1, "Q1110856")
        self.assertEqual(r2 , "du ")
        
    def test_search_team_by_name(self):
        s=Search("vrienden van het platteland 2005")
        self.assertEqual(s.team_by_name(),'Q83155030')
        s=Search("Team Bigla 2005")
        self.assertEqual(s.team_by_name(),'Q82342943') 
        
    def test_search_team_by_name_man(self):        
        s=Search("Trek-Segafredo 2020")
        self.assertEqual(s.team_by_name(man_or_woman="man"),'Q78075353')  
        s=Search("Trek-Segafredo 2020")
        self.assertEqual(s.team_by_name(is_women=False),'Q78075353') 
        
    def test_search_team_by_code(self):
        s=Search("MTS 2020")
        self.assertEqual(s.team_by_code(),'Q74725715')
        s=Search("ASA 2020")
        self.assertEqual(s.team_by_code(),'Q74725122')
        s=Search("TFS 2020")
        self.assertEqual(s.team_by_code(),'Q82315001')
        s=Search("BTW 2021")
        self.assertEqual(s.team_by_code(),'Q105530407')
        s=Search("LSL 2021")
        self.assertEqual(s.team_by_code(),'Q105451626')
        s=Search("COF 2022")
        self.assertEqual(s.team_by_code(),'Q110629530')

    def test_search_team_by_code_man(self):
        s=Search("TFS 2020")
        self.assertEqual(s.team_by_code(man_or_woman="man"),'Q78075353')
        s=Search("DQT 2020")
        self.assertEqual(s.team_by_code(man_or_woman="man"),'Q78075314')
        s=Search("COF 2022")
        self.assertEqual(s.team_by_code(man_or_woman="man"),'Q109109760')
        s=Search("TFS 2020")
        self.assertEqual(s.team_by_code(is_women=False),'Q78075353')
        s=Search("DQT 2020")
        self.assertEqual(s.team_by_code(is_women=False),'Q78075314')
        s=Search("COF 2022")
        self.assertEqual(s.team_by_code(is_women=False),'Q109109760')        
        
        

    def test_is_it_a_cyclist(self):
        s=Search("TFS 2020")
        self.assertFalse(s.is_it_a_cyclist('Q38222'))
        self.assertTrue(s.is_it_a_cyclist('Q563737'))
        self.assertTrue(s.is_it_a_cyclist('Q47295776'))
        self.assertFalse(s.is_it_a_cyclist('Q75271148'))
        
    def test_is_it_a_teamseason(self):
        s=Search("TFS 2020")
        self.assertTrue(s.is_it_a_teamseason('Q78075314'))
        self.assertTrue(s.is_it_a_teamseason('Q82315001'))
        self.assertFalse(s.is_it_a_teamseason('Q563737'))
        self.assertFalse(s.is_it_a_teamseason('Q27123005'))   
        s=Search("BWB 2021")
        self.assertTrue(s.is_it_a_teamseason('Q104537501'))
        
    def test_is_it_a_menteam(self):
        s=Search("BWB 2021")
        self.assertTrue(s.is_it_a_menteam('Q104537501'))
        s=Search("IGD 2021")
        self.assertTrue(s.is_it_a_menteam('Q102247949'))
        s=Search("COF 2022")
        self.assertTrue(s.is_it_a_menteam('Q109109760'))
        self.assertFalse(s.is_it_a_menteam('Q110629530'))
        
    def test_is_it_a_womenteam(self):
        s=Search("COF 2022")
        self.assertFalse(s.is_it_a_womenteam('Q109109760'))
        self.assertTrue(s.is_it_a_womenteam('Q110629530'))

    def test_find_sortkey(self):
        list_=['féminine de cyclisme']
        s=Search("TFS 2020")
        self.assertTrue(s.find_sortkey('équipe de France féminine de cyclisme sur route 2019',list_))
        self.assertFalse(s.find_sortkey('équipe de France de cyclisme sur route 2019',list_))
        self.assertFalse(s.find_sortkey('équipe de France espoirs de cyclisme sur route 2018',list_))

        list_=['espoirs de cyclisme']
        self.assertFalse(s.find_sortkey('équipe de France féminine de cyclisme sur route 2019',list_))
        self.assertFalse(s.find_sortkey('équipe de France de cyclisme sur route 2019',list_))
        self.assertTrue(s.find_sortkey('équipe de France espoirs de cyclisme sur route 2018',list_))

        list_=['de cyclisme']
        self.assertTrue(s.find_sortkey('équipe de France féminine de cyclisme sur route 2019',list_))
        self.assertTrue(s.find_sortkey('équipe de France de cyclisme sur route 2019',list_))
        self.assertTrue(s.find_sortkey('équipe de France espoirs de cyclisme sur route 2018',list_))

    def test_national_team(self):
         s=Search("FRA 2019")
         positive_list=['féminine de cyclisme']
         negative_list=[]
         self.assertEqual(s.national_team(positive_list,negative_list),'Q56887783')
         
         positive_list=['de cyclisme']
         negative_list=['féminine de cyclisme','espoirs de cyclisme']
         self.assertEqual(s.national_team(positive_list,negative_list),'Q60418112')
         
         positive_list=['espoirs de cyclisme']
         negative_list=[]
         self.assertEqual(s.national_team(positive_list,negative_list),'Q1')      
         
         s=Search("équipe de France féminine de cyclisme sur route 2019")
         positive_list=['féminine de cyclisme']
         negative_list=[]
         self.assertEqual(s.national_team(positive_list,negative_list),'Q56887783')   

    def test_search_item(self):
        s=Search('Anna van der Breggen')
        self.assertEqual(s.simple(),'Q563737')
        s=Search('Anna')
        self.assertEqual(s.simple(),'Q1')
        s=Search('zz14563465465wuichWRUPIUDGCOIUWR')
        self.assertEqual(s.simple(),'Q0')
        s=Search('Elizabeth Banks')
        self.assertEqual(s.simple(),'Q1')
     
    def test_search_rider(self):
        s=Search('Anna van der Breggen')
        self.assertEqual(s.rider('',''),'Q563737')
        s=Search('Elizabeth Banks')
        self.assertEqual(s.rider('',''),'Q47295776')
        s=Search('Elizabeth Banks')
        self.assertEqual(s.rider(None,None),'Q47295776')
        s=Search('')
        self.assertEqual(s.rider('Elizabeth','Banks'),'Q47295776')
        s=Search(0)
        self.assertEqual(s.rider('Elizabeth','Banks'),'Q47295776')        
        s=Search(None)
        self.assertEqual(s.rider('Elizabeth','Banks'),'Q47295776')
        
        s=Search(None)
        self.assertEqual(s.rider('Felix', 'GROß'),'Q39885866')
        s=Search(None)
        self.assertEqual(s.rider('felix', 'groß'),'Q39885866')
        s=Search(None)
        self.assertEqual(s.rider('Felix', 'Groß'),'Q39885866')
        s=Search(None)
        self.assertEqual(s.rider('Felix', 'GROß'),'Q39885866')
        
        s=Search('W. Mathias Sorgho')
        self.assertEqual(s.rider('',''),'Q27644062')
        
        s=Search(None)
        self.assertEqual(s.rider('Belen', 'GONZALEZ SIMON'),'Q111941173')
        self.assertEqual(s.rider('Belen', 'GONZALEZ  SIMON'),'Q111941173')
        
        
        #exception
        s=Search(None)
        self.assertEqual(s.rider('1501996785028', 'ERIC'),'Q19661759')
        s=Search('GARCIA CAÑELLAS Margarita Victo')
        self.assertEqual(s.rider('', ''),'Q23907253')
        s=Search('GONZÁLEZ Roberto')
        self.assertEqual(s.rider('', ''),'Q28048282')
        
    def test_search_fc_id(self):
        s=Search('Anna van der Breggen')
        self.assertEqual(s.search_fc_id(fc_id=89434),"Q289826")

if __name__ == '__main__':
    unittest.main()
