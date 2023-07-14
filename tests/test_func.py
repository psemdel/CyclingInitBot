#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:40:34 2022

@author: maxime
"""

import pywikibot
import unittest

from src.func import (is_website, get_single_or_stage,date_finder,
                      time_converter, float_to_int, define_article,
                      table_reader, get_fc_dic

             )         

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestFunc(unittest.TestCase):
    def test_is_website(self):
        self.assertFalse(is_website())
        
    def test_get_single_or_stage(self):
        self.assertEqual(get_single_or_stage("1.1"),True)
        self.assertEqual(get_single_or_stage("2.1"),False)
        self.assertEqual(get_single_or_stage(21),True) 
        self.assertEqual(get_single_or_stage("abc"),True)

    def test_date_finder(self):
        #easy case
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=4, precision='day')    
       
        number=1
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=3, precision='day')    
        self.assertEqual(res,exp)
        #check that the function does not change the value of race_begin
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        res=date_finder(1,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,exp)
        
        res=date_finder(4,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=4, precision='day')    
        self.assertEqual(res,exp)  
        self.assertEqual(res,race_end)  
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=6, precision='day') 
        res=date_finder(4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  

        #not possible
        number=0
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        
        #prologue
        first_stage=0
        number=0
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        number=1
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        self.assertEqual(res,exp)
        
        #month limit, january
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=1, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=2, day=2, precision='day')    
        number=1
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=31, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=2, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  
        
        #month limit, april
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2015, month=4, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=5, day=3, precision='day')    
        number=1
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=5, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=5, day=2, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)       
        
        #year limit
        first_stage=1
        last_stage=4
        race_begin=pywikibot.WbTime(site=site,year=2014, month=12, day=30, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2015, month=1, day=2, precision='day')    
        number=1
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
        res=date_finder(2,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2014, month=12, day=31, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(3,first_stage,last_stage, race_begin,race_end)
        exp=pywikibot.WbTime(site=site,year=2015, month=1, day=1, precision='day')    
        self.assertEqual(res,exp)
        res=date_finder(4,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_end)  

        #case thailand
        first_stage=1
        last_stage=3
        number=1
        race_begin=pywikibot.WbTime(site=site,year=2020, month=10, day=14, precision='day')    
        race_end=pywikibot.WbTime(site=site,year=2020, month=10, day=16, precision='day')  
        res=date_finder(number,first_stage,last_stage, race_begin,race_end)
        self.assertEqual(res,race_begin)
    
    def test_time_converter(self):
        res=time_converter("03:38'05''",0)
        self.assertEqual(res,(13085))
        res=time_converter("03:38:05",0)
        self.assertEqual(res,(13085))  
        res=time_converter("+00:00:05",100)
        self.assertEqual(res,(105))  
        res=time_converter("00.03.09",0)
        self.assertEqual(res,(189))
        
    def test_float_to_int(self):
        self.assertEqual( float_to_int('1149.67'),1149)  
        self.assertEqual( float_to_int("1149.67"),1149)  
        self.assertEqual( float_to_int("1149.07"),1149)  
        self.assertEqual( float_to_int(1149.67),1149)  
        self.assertEqual( float_to_int(1149),1149)  
        self.assertEqual( float_to_int(''),0)  #exception management
        self.assertEqual( float_to_int(""),0)
        self.assertEqual( float_to_int('1149,67'),1149)  
        self.assertEqual( float_to_int("1149,67"),1149)  
        self.assertEqual( float_to_int("1149,07"),1149)  
        
    def test_define_article(self):
        self.assertEqual(define_article(None),("", ""))
        self.assertEqual(define_article("La Classique des Alpes"),("de la ", "Classique des Alpes"))
        self.assertEqual(define_article("Women's Tour"),("du ", "Women's Tour"))
        self.assertEqual(define_article("Tour of the Gila"),("du ", "Tour of the Gila"))
        self.assertEqual(define_article("Le Samyn des Dames"),("du ", "Samyn des Dames"))
        self.assertEqual(define_article("Chrono des nations"),("du ", "Chrono des nations"))
        self.assertEqual(define_article("Flèche wallonne"),("de la ", "Flèche wallonne"))
        self.assertEqual(define_article("Amstel Gold Race"),("de l'", "Amstel Gold Race"))
                
    def test_table_reader(self):
        df,_,_,_= table_reader('champ',None)
        self.assertTrue(len(df)>0)
        self.assertTrue("Champ" in df.columns)
        self.assertTrue("Winner" in df.columns)
        self.assertTrue("WorldCC" in df.columns)
        self.assertTrue("Clm" in df.columns)
        
        df,_,_,_= table_reader('Results',9058,year=2023)
        self.assertTrue("Pos" in df.columns)
        self.assertTrue("Time" in df.columns)
        self.assertTrue("Rider_ID" in df.columns)
        self.assertEqual(df["Rider"].values[0],"Annemiek van Vleuten")
        self.assertEqual(df["Team"].values[0],"Movistar Team")
        
        df,_,_,_= table_reader('Results',9058,year=2023,general_or_stage=0)
        self.assertTrue("Pos" in df.columns)
        self.assertTrue("Time" in df.columns)
        self.assertTrue("Rider_ID" in df.columns)
        self.assertEqual(df["Rider"].values[0],"Annemiek van Vleuten")
        self.assertEqual(df["Team"].values[0],"Movistar Team")
        
    def test_get_fc_dic(self):
        keys=get_fc_dic(9058,year=2023)
        self.assertEqual(keys,[0,2,3,5])
        keys=get_fc_dic(9058,year=2023,stage_num=-1)
        self.assertEqual(keys,[0,2,3,5])
        
        keys=get_fc_dic(9064,year=2005,stage_num=-1)
        self.assertEqual(keys,[0,2,3,4])
        
        keys=get_fc_dic(17,year=2022)
        self.assertEqual(keys,[0,2,3,4])
        
        keys=get_fc_dic(17,year=2023,stage_num=1)
        self.assertEqual(keys,[1,0,4,2,3,5])
        
        keys=get_fc_dic(17,year=2022,stage_num=1)
        self.assertEqual(keys,[1,0,4,2,5])

        keys=get_fc_dic(9064,year=2005,stage_num=0)
        self.assertEqual(keys,[1,0])
        
        keys=get_fc_dic(9064,year=2005,stage_num=1)
        self.assertEqual(keys,[1,0]) 

        keys=get_fc_dic(9062,year=2015,stage_num=-1)
        self.assertEqual(keys,[0,2,3,4,8])
        
        keys=get_fc_dic(9049,year=2015,stage_num=-1)
        self.assertEqual(keys,[0])
        
        keys=get_fc_dic(9049,year=2023,stage_num=-1)
        self.assertEqual(keys,[0])
        
        
if __name__ == '__main__':
    unittest.main()        
