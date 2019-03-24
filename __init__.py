# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:35:56 2018

@author: maxime delzenne
"""
from nationTeamTable import *
from ProTeamTable import *
from ccTable import *
from nameSorter import *
from stageRaceCreator import *
from nationalChampionshipCreator import *
from ccChampionshipCreator import *
from nationalTeamCreator import *
from ProTeamCreator import *
from symmetrizer import *
from calendarList import *
from CyclingInitBotLow import *
from calendarList import*
from classificationImporter import*
from SingleDayRaceCreator import*
from exception import *
from palmaresImporter import *

if __name__ == '__main__':
   [teamTableFemmes, endkk]=nationalTeamTable()
   #from ProTeamTable import AmateurTeamTable
   #[teamTableFemmes, endkk]=ProTeamTable()
   #[teamTableFemmes, endkk]=AmateurTeamTable()
   

   print( teamTableFemmes[35][7]==u'GBR')
