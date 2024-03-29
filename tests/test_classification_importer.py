# -*- coding: utf-8 -*-

import pywikibot
import unittest

from src.func import table_reader
from src.classification_importer import ClassificationImporter
from src.base import PyItem

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class TestClassificationImporter(unittest.TestCase):  
    def test_copy_team(self):
        
        # 0:'2321', #general
        #  1: '2417',#stage
        cl=ClassificationImporter(0, "Q79138636", 10, test=True)
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
            
        cl=ClassificationImporter(0, "Q98293556", 10, test=True)
        cl.is_there_a_startlist()

        df, _,_,log=table_reader('DNF_test',None,rider=True)
        starter, stage_nummer=cl.put_dnf_in_startlist(df)
       
        self.assertEqual(starter.getTarget().getID(), "Q18125995")
        self.assertEqual(stage_nummer, '1')

    def test_is_there_a_startlist(self):

        cl=ClassificationImporter(0, "Q98293689", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist()
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, True)
        #stage race, with startlist
        cl=ClassificationImporter(0, "Q79138636", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist()
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False)

         #single day race, with startlist
        cl=ClassificationImporter(0, "Q57277525", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False)       
        
        #single day race, without startlist
        #cl=ClassificationImporter(0, "Q24575332", 10, test=True)
        #startlist, in_parent=cl.is_there_a_startlist() 
        #self.assertTrue(startlist is None)
        #self.assertEqual(in_parent, False) 

        #stage, with startlist
        cl=ClassificationImporter(1, "Q98293689", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, True)
        
        #stage race, with startlist
        cl=ClassificationImporter(1, "Q79138636", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False) 
       
         #single day race, with startlist
        cl=ClassificationImporter(1,"Q57277525", 10, test=True)
        startlist, in_parent=cl.is_there_a_startlist() 
        self.assertTrue(startlist is not None)
        self.assertEqual(in_parent, False) 
 
        #single day race, without startlist
        #cl=ClassificationImporter(1,"Q24575332", 10, test=True)
        #startlist, in_parent=cl.is_there_a_startlist() 
        #self.assertTrue(startlist is None)
        #self.assertEqual(in_parent, False) 
    
    def test_main(self):
        id_race='Q4115189' #sandbox
        stage_or_general=1# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, 
        #5 team, #6 team points, #7 youth points, #8 == sprints, #9 == all
        maxkk=10
        
        pyItem=PyItem(id=id_race)
        pyItem.add_value("P2094","Q1451845","add women cycling")
        
        f=ClassificationImporter(
            stage_or_general,
            id_race,
            maxkk, 
            test=False,
            startliston=True,
            fc=9064, 
            stage_num=1, #only for stage, put -1 otherwise for the main race
            year=2005)
        
        if stage_or_general==9:
            print("run all")
            f.run_all()
        else:
            f.main()
        
if __name__ == '__main__':
    unittest.main()
