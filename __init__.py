# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:35:56 2018

@author: maxime delzenne
"""
from nationTeamTable import nationalTeamTable 
from nameSorter import *
from stageRaceCreator import *
from nationalChampionshipCreator import *
from nationalTeamCreator import *
from symmetrizer import *
from calendarList import *
from CyclingInitBotLow import *
from calendarList import*

if __name__ == '__main__':
   [teamTableFemmes, endkk]=nationalTeamTable()
   print(endkk)
   print(teamCIOsearch(teamTableFemmes,'FRA'))

   
