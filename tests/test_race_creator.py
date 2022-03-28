# -*- coding: utf-8 -*-

import pywikibot
import unittest
from src.race_creator import RaceCreator

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestRaceCreator(unittest.TestCase):  
     def test_calendarUWTID(self):
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=False, year=2019, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(),"Q57267790")
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=False, year=2018, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(),"Q47005682")
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=False, year=2019, man_or_woman="man")
         self.assertEqual(r.UCI_to_calendar_id(),None)
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=False, year=2018, man_or_woman="man")
         self.assertEqual(r.UCI_to_calendar_id(),None)        
         r=RaceCreator(single_race=True, UCI=True, WWT=True,UWT=False, year=2019, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(),"Q57277246")
         r=RaceCreator(single_race=True, UCI=True, WWT=True,UWT=False, year=2018, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(), "Q41787783")
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=True, year=2019, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(),  "Q56966729")
         r=RaceCreator(single_race=True, UCI=True, WWT=False,UWT=True, year=2018, man_or_woman="woman")
         self.assertEqual(r.UCI_to_calendar_id(),  "Q42317185")
         
     def test_stage_label(self):
        r=RaceCreator(single_race=True, race_name="Tour de France",year=2010)
        res=r.stage_label(0)
        self.assertEqual(res[u'fr'], "Prologue du Tour de France 2010")
        res=r.stage_label(1)
        self.assertEqual(res[u'fr'], "1re étape du Tour de France 2010")

if __name__ == '__main__':
    unittest.main()
