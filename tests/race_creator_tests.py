# -*- coding: utf-8 -*-

import pywikibot
import unittest
from src.race_creator import UCI_to_calendar_id, stage_label

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class Test_f(unittest.TestCase):  
     def test_calendarUWTID(self):
         res=UCI_to_calendar_id(True, False, False, 2019, "woman")
         self.assertEqual(res, "Q57267790")
         res=UCI_to_calendar_id(True, False, False, 2018, "woman")
         self.assertEqual(res, "Q47005682")
         res=UCI_to_calendar_id(True, False, False, 2019, "man")
         self.assertEqual(res, None)
         res=UCI_to_calendar_id(True, False, False, 2018, "man")  
         self.assertEqual(res, None)
         res=UCI_to_calendar_id(True, True, False, 2019, "woman")
         self.assertEqual(res, "Q57277246")
         res=UCI_to_calendar_id(True, True, False, 2018, "woman")
         self.assertEqual(res, "Q41787783")
         res=UCI_to_calendar_id(True, False, True, 2019, "woman")
         self.assertEqual(res, "Q56966729")
         res=UCI_to_calendar_id(True, False, True, 2018, "woman")
         self.assertEqual(res, "Q42317185")
         
     def test_stage_label(self):
        number=0
        genre="du "
        race_name="Tour de France"
        year=2010
        res=stage_label(number, genre,race_name, year)
        self.assertEqual(res[u'fr'], "Prologue du Tour de France 2010")
        number=1
        res=stage_label(number, genre,race_name, year)
        self.assertEqual(res[u'fr'], "1re étape du Tour de France 2010")