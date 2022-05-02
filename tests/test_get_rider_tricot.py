#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:52:19 2020

@author: maxime
"""
import pywikibot
import unittest
from src.get_rider_tricot import GetRiderTricot

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestGetRiderTricot(unittest.TestCase):  
    def test_f(self):
        #future
        id_rider1='Q38217303'
        this_date1=pywikibot.WbTime(site=site,year=2030, month=10, day=5, precision='day') 
        
        grt=GetRiderTricot(id_rider1,this_date1,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0)
        grt=GetRiderTricot(id_rider1,this_date1,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),0)  

        #it is the champion
        this_date2=pywikibot.WbTime(site=site,year=2020, month=1, day=1, precision='day')  
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332844')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=7, day=1, precision='day')
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332844')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=6, day=1, precision='day')
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0)
        this_date2=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')  
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0)
        this_date2=pywikibot.WbTime(site=site,year=2018, month=1, day=1, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0) 
        this_date2=pywikibot.WbTime(site=site,year=2017, month=1, day=1, precision='day')    
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0)
        
        #Chrono
        id_rider1='Q16678673'
        this_date2=pywikibot.WbTime(site=site,year=2020, month=1, day=1, precision='day')  
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332806')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=12, day=1, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332806')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=7, day=1, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332806')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=6, day=1, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),0)

        id_rider1='Q289826'
        this_date2=pywikibot.WbTime(site=site,year=2021, month=3, day=6, precision='day')  
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30894544') 

        #test chrono
        id_rider1='Q2870834'
        this_date2=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')  
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30332806')
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),0)
        
        id_rider1='Q563737'
        this_date2=pywikibot.WbTime(site=site,year=2020, month=8, day=25, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),'Q30333102')
        id_rider1='Q289826'
        grt=GetRiderTricot(id_rider1,this_date2,None,False,u'woman',test=True)
        self.assertEqual(grt.main(),'Q934877')
        
        #test double champ        
        id_rider1='Q563737'
        this_date2=pywikibot.WbTime(site=site,year=2020, month=10, day=1, precision='day') 
        grt=GetRiderTricot(id_rider1,this_date2,None,True,u'woman',test=True)
        self.assertEqual(grt.main(),'Q934877')
        
if __name__ == '__main__':
    unittest.main()

