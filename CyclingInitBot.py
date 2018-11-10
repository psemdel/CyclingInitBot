# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdely
"""
import sys, os
from CyclingInitBotSub import *

#==Initialisation==   
def wikiinit():
    
    import time
    import sys
    sys.path.insert(0, 'C:\\Wikidata2\\core')
    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot')
    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot\\CyclingInitBot')
    import pywikibot
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    import CyclingInitBotSub

    return [pywikibot,site,repo,time]

def main():
    [pywikibot,site,repo,time]=wikiinit()
    [teamTable, endkk]= nationalTeamTable()
    [tempccTable, ccendkk]=ccTable()
    [proteamTable, proendkk]=ProTeamTable()
    [amateurteamTable, amateurendkk]=AmateurTeamTable()
   # [teamTable, endkk]=nationalTeamTable()
    selector=13

    if selector==0:
        Nationalteamcreator(pywikibot,site,repo,time,teamTable,endkk)
    elif selector==1:
        ManOrWoman=u'woman'
        Option=u'clmon' #'clmoff'
        startYear=1995
        EndYear=2010
        Country=u'NZL'        
        NationalChampionshipCreator(pywikibot,site,repo,time,teamTable,endkk,ManOrWoman,Option, startYear,EndYear,Country)
    elif selector==2:
        StageRaceName=u"Tour du Costa Rica féminin"
        StageRaceGenre=u'du ' #+space
        StageRaceMasterId=16960754
        Year=2018
        UCI=u"yes"
        StageRaceBegin=pywikibot.WbTime(site=site,year=Year, month=11, day=7, precision='day')
        StageRaceEnd=pywikibot.WbTime(site=site,year=Year, month=11, day=9, precision='day')
        FirstStage=1
        LastStage=3
        CountryCIO=u'CRC'
        StageRaceCreator(pywikibot,site,repo,time,teamTable,StageRaceName,StageRaceGenre,StageRaceMasterId,Year,UCI,StageRaceBegin,StageRaceEnd,FirstStage,LastStage,CountryCIO)
    elif selector==3:
        IdTeamPage=u'Q57983448'
        TeamOrOther=u'Team'
        nameSorter(pywikibot,site,repo,time, IdTeamPage, TeamOrOther)
    elif selector==4:
        IdTeamPage=u'Q44497477'
        TeamOrOther=u'Comp'
        dateSorter(pywikibot,site,repo,time,IdTeamPage,TeamOrOther )
    elif selector==5:
        calendarID=u"Q41787783"
        calendarSymmetrizer(pywikibot,site,repo,time, calendarID)
    elif selector==6:
        masterID=u"Q27684043"
        addUCIcalendar(pywikibot,site,repo,time, masterID)
    elif selector==7:
        calendarSymmetrizerMass(pywikibot,site,repo,time)
    elif selector==8: 
       proamateur=1 #1 is pro
       group=1 #group to create
       countrytocreate=u'GER'
       if proamateur==1:
           proteamcreator(pywikibot,site,repo,time,proteamTable,teamTable,proendkk,proamateur, countrytocreate)
       else:
           proteamcreator(pywikibot,site,repo,time,amateurteamTable,teamTable,amateurendkk,proamateur, countrytocreate)
    elif selector==9:
       ManOrWoman=u'woman'
       Option=u'clmon' #'clmoff'
       ccChampionshipCreator(pywikibot,site,repo,time,tempccTable,ccendkk,ManOrWoman, Option)
    elif selector==10:
         StageRaceName=u"Tour de Toscane féminin-Mémorial Michela Fanini"
         StageRaceGenre=u"du "
         StageRaceMasterId=369183
         Year=2018
         UCI=u"yes"
         StageRaceDate=pywikibot.WbTime(site=site,year=Year, month=7, day=7, precision='day')
         CountryCIO=u'CAN'
         SingleDayRaceCreator(pywikibot,site,repo,time,teamTable,StageRaceName,StageRaceGenre,StageRaceMasterId,Year,UCI,StageRaceDate,CountryCIO)
    elif selector==11:
        RaceID='Q57968196'
        StageOrGeneral=0 #1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team
        final=0
        separator=";"
        maxkk=10
        classificationImporter(pywikibot,site,repo,StageOrGeneral,RaceID,final,separator,maxkk)
    elif selector==12: 
        year=u'2018'
        separator=";"
        test=0
        UCIclassificationImporter(pywikibot,site,repo,year,separator,test)
    elif selector==13:
        RaceID='Q55638555'
        prologueorfinal=1 #0=prologue, 1=final, 2=one day race
        separator=";"
        chrono="on"
        test=0
        timeofrace=pywikibot.WbTime(site=site,year=2018, month=7, day=19, precision='day')    
        listofstartersimporter (pywikibot,site,repo, prologueorfinal, RaceID, separator,timeofrace,chrono,test)    
    else: 
        print('do nothing')
        
if __name__ == '__main__':
    main()
    #if not main():
        #print(__doc__)
