# -*- coding: utf-8 -*-

import pywikibot
import unittest
from src.classification_importer import copy_team, put_dnf_in_startlist
from src.cycling_init_bot_low import table_reader

site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()

class Test_f(unittest.TestCase):  
    def test_copy_team(self):
        
        # 0:'2321', #general
        #  1: '2417',#stage
        
        item =pywikibot.ItemPage(repo, "Q79138636")
        item.get()
        startlist=item.claims.get(u'P710')
        target = pywikibot.ItemPage(repo, "Q2870834") #no team
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, "Q2870834")
        self.assertEqual(team, None)
        
        claim=pywikibot.Claim(repo, u'P2417')  
        
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, "Q2870834")
        self.assertEqual(team, None)
        
        target = pywikibot.ItemPage(repo, "Q38823209") #credit mutuel
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, "Q38823209")
        self.assertEqual(team, "Q98931960")
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, "Q38823209")
        self.assertEqual(team, "Q98931960")     
        
        target = pywikibot.ItemPage(repo, "Q98895868") #AUT
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, "Q98895868")
        self.assertEqual(team, "Q74748391")
        
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual( this_starter, "Q98895868")
        self.assertEqual(team, "Q74748391")   

        target = pywikibot.ItemPage(repo, "Q129857") #francois Ier
        claim=pywikibot.Claim(repo, u'P2321')  
        
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, None)
        self.assertEqual(team, None)
        claim=pywikibot.Claim(repo, u'P2417') 
        this_starter, team=copy_team(pywikibot, site, startlist, claim, target, test=True)
        self.assertEqual(this_starter, None)
        self.assertEqual(team, None)

    def test_put_dnf_in_startlist(self):
            item_parent =pywikibot.ItemPage(repo, "Q79138636")
            item_parent.get()
            startlist=item_parent.claims.get(u'P710')
            item =pywikibot.ItemPage(repo, "Q98293556")
            item.get()
            
            result='time'
            
            result_dic={
            'rank':[-1, 0, ''],
            'last name':[-1, 1,''],
            'first name':[-1, 2,''],
            'name':[-1, 3,''],
            'result':[-1, 4,result],
            'points':[-1, 5, 'points'],
            'team code':[-1, 7, ''],
            'ecart':[1,6,''],  #always created, not set on time otherwise makes strange things
            'bib':[-1,8,''] #dossard
            }
            
            result_table, row_count, ecart=table_reader('DNF_test',result_dic,0,False)
            
            starter, stage_nummer=put_dnf_in_startlist(pywikibot, site, repo, 
                             item, startlist, row_count, 
                             result_table, result_dic, test=True)
            
            self.assertEqual(starter.getTarget().getID(), "Q18125995")
            self.assertEqual(stage_nummer, '1')

if __name__ == '__main__':
    unittest.main()
