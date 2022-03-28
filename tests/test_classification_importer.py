# -*- coding: utf-8 -*-

import pywikibot
import unittest

from src.func import table_reader
from src.classification_importer import ClassificationImporter


site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestClassificationImporter(unittest.TestCase):  
    def test_copy_team(self):
        
        # 0:'2321', #general
        #  1: '2417',#stage
        cl=ClassificationImporter(0, "Q79138636", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist()
        
        target = pywikibot.ItemPage(repo, "Q2870834") #no team
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q2870834")
        self.assertEqual(team, None)
        
        claim=pywikibot.Claim(repo, u'P2417')  
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q2870834")
        self.assertEqual(team, None)
        
        target = pywikibot.ItemPage(repo, "Q38823209") #credit mutuel
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q38823209")
        self.assertEqual(team, "Q98931960")
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q38823209")
        self.assertEqual(team, "Q98931960")     
        
        target = pywikibot.ItemPage(repo, "Q98895868") #AUT
        claim=pywikibot.Claim(repo, u'P2321')  
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q98895868")
        self.assertEqual(team, "Q74748391")
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual( this_starter, "Q98895868")
        self.assertEqual(team, "Q74748391")   

        target = pywikibot.ItemPage(repo, "Q26792853") #AUT
        claim=pywikibot.Claim(repo, u'P2321')  

        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, "Q26792853")
        self.assertEqual(team, "Q74748391")
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual( this_starter, "Q26792853")
        self.assertEqual(team, "Q74748391") 

        target = pywikibot.ItemPage(repo, "Q129857") #francois Ier
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, None)
        self.assertEqual(team, None)
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=cl.copy_team(claim, target)
        self.assertEqual(this_starter, None)
        self.assertEqual(team, None)

    def test_put_dnf_in_startlist(self):
            
        cl=ClassificationImporter(0, "Q98293556", False, 10, test=True)
        cl.is_there_a_startlist()

        df, _,_,log=table_reader('DNF_test',rider=True)
        starter, stage_nummer=cl.put_dnf_in_startlist(df)
       
        self.assertEqual(starter.getTarget().getID(), "Q18125995")
        self.assertEqual(stage_nummer, '1')

    def test_is_there_a_startlist(self):

        cl=ClassificationImporter(0, "Q98293689", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist()
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, True)
        #stage race, with startlist
        cl=ClassificationImporter(0, "Q79138636", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist()
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False)

         #single day race, with startlist
        cl=ClassificationImporter(0, "Q57277525", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False)       
        
        #single day race, without startlist
        cl=ClassificationImporter(0, "Q24575332", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is None)
        self.assertEqual(in_parent, False) 

        #stage, with startlist
        cl=ClassificationImporter(1, "Q98293689", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, True)
        
        #stage race, with startlist
        cl=ClassificationImporter(1, "Q79138636", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False) 
       
         #single day race, with startlist
        cl=ClassificationImporter(1,"Q57277525", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False) 
 
        #single day race, without startlist
        cl=ClassificationImporter(1,"Q24575332", False, 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is None)
        self.assertEqual(in_parent, False) 
        
if __name__ == '__main__':
    unittest.main()
