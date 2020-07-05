#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:52:19 2020

@author: maxime
"""
import pywikibot
import unittest
from src.get_rider_tricot import f

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class Test_f(unittest.TestCase):  
    def test_f(self):
        #future
        claim=None
        
        id_rider1='Q38217303'
        this_date1=pywikibot.WbTime(site=site,year=2030, month=10, day=5, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date1,claim,False,test=True),0)
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date1,claim,True,test=True),0)
        #it is the champion
        this_date2=pywikibot.WbTime(site=site,year=2020, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),'Q30332844')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=7, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),'Q30332844')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=6, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),0)
        this_date2=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),0)  
        this_date2=pywikibot.WbTime(site=site,year=2018, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),0)   
        this_date2=pywikibot.WbTime(site=site,year=2017, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),0) 
        
         
        id_rider1='Q16678673'
        this_date2=pywikibot.WbTime(site=site,year=2020, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,True,test=True),'Q30332806')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=12, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,True,test=True),'Q30332806')       
        this_date2=pywikibot.WbTime(site=site,year=2019, month=7, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,True,test=True),'Q30332806')
        this_date2=pywikibot.WbTime(site=site,year=2019, month=6, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,True,test=True),0)    

        id_rider1='Q2870834'
        this_date2=pywikibot.WbTime(site=site,year=2019, month=1, day=1, precision='day')    
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,True,test=True),'Q30332806')
        self.assertEqual(f(pywikibot,site,repo,id_rider1,this_date2,claim,False,test=True),0)
        
if __name__ == '__main__':
    unittest.main()