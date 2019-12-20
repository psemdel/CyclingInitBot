# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:35:56 2018

@author: maxime delzenne
"""
import sys, os, time, csv

#table and constant
from nation_team_table import *
from pro_team_table import *
from amateur_team_table import *
from cc_table import *
from race_list import *
from calendar_list import*
from exception import *

#low functions
from moo import *
from cycling_init_bot_low import *

#main function
from sorter import *
from race_creator import *
from national_championship_creator import *
from national_team_creator import *
from pro_team_creator import *
from classification_importer import*
from palmares_importer import *
from uci_classification import *
from calendar_importer import *
from rider_fast_init import *
from startlist_importer import *
from get_rider_tricot import *

#==Initialisation==   
def wikiinit():
    dirpath = os.path.dirname(__file__)
    upperdir= os.path.dirname(dirpath)
    sys.path.insert(0, upperdir)
    sys.path.insert(0, upperdir + '/pywikibot')
    sys.path.insert(0, dirpath + '/input')

    import pywikibot
   ## import CyclingInitBotSub 
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    ##import CyclingInitBotSub

    return [pywikibot,site,repo,time]

if __name__ == '__main__':
    wikiinit()