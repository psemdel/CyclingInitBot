# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdely
"""
import sys, os
#from CyclingInitBotSub import *

#==Initialisation==   
def wikiinit():
 
    import time
    import sys
    sys.path.insert(0, '/disque1/Python/pywikibot')
    sys.path.insert(0, '/disque1/Python')
    sys.path.insert(0, '/disque1/Python/CyclingInitBot')
    import pywikibot
   ## import CyclingInitBotSub 
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    ##import CyclingInitBotSub

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
        #CC=u'no'
        startYear=2016
        EndYear=2018
        Country=u'RWA'  
        #if CC=="yes":
        #    tempTable=continentalTable
        #    endkk=endkk2
        #else:
        #    tempTable=teamTable
        NationalChampionshipCreator(pywikibot,site,repo,time,teamTable,endkk,ManOrWoman,Option, startYear,EndYear,Country,u'no')    
    elif selector==2:
        StageRaceName=u"Boels Ladies Tour"
        StageRaceGenre=u"du "  
        StageRaceMasterId=1572063
        StageRaceMaster=57277611  #only for onlystages
        Year=2019
        UCI=u"yes"
        Onlystages=u"yes"
        Createstage=u"yes"
        StageRaceBegin=pywikibot.WbTime(site=site,year=Year, month=9, day=3, precision='day')
        StageRaceEnd=pywikibot.WbTime(site=site,year=Year, month=9, day=8, precision='day')
        FirstStage=0
        LastStage=6
        CountryCIO=u'NED'
        Class=21
        StageRaceCreator(pywikibot,site,repo,time,teamTable,StageRaceName,StageRaceGenre,StageRaceMasterId,Year,UCI,StageRaceBegin,
                         StageRaceEnd,FirstStage,LastStage,CountryCIO,Createstage,Class,Onlystages,StageRaceMaster)
    elif selector==3:        
        IdTeamPage=u'Q57277611'
        TeamOrOther=u'Comp'
        nameSorter(pywikibot,site,repo,time, IdTeamPage, TeamOrOther)
    elif selector==4:
        IdTeamPage=u'Q44497477'
        TeamOrOther=u'Comp'
        dateSorter(pywikibot,site,repo,time,IdTeamPage,TeamOrOther )
    elif selector==5:
        calendarID=u"Q57267790"
        calendarSymmetrizer(pywikibot,site,repo,time, calendarID)
    elif selector==6:
        masterID=u"Q27684043"
        addUCIcalendar(pywikibot,site,repo,time, masterID)
    elif selector==7:
        calendarSymmetrizerMass(pywikibot,site,repo,time)
    elif selector==8: 
       proamateur=0 #1 is pro
       group=1 #group to create
       countrytocreate=u'SUI'
       if proamateur==1:
           proteamcreator(pywikibot,site,repo,time,proteamTable,teamTable,proendkk,proamateur, countrytocreate)
       else:
           proteamcreator(pywikibot,site,repo,time,amateurteamTable,teamTable,amateurendkk,proamateur, countrytocreate)
    elif selector==9:
       ManOrWoman=u'woman'
       Option=u'clmon' #'clmoff'
       ccChampionshipCreator(pywikibot,site,repo,time,tempccTable,ccendkk,ManOrWoman, Option)
    elif selector==10:
         StageRaceName=u"Grand Prix d'Isbergues féminin"
         StageRaceGenre=u"du "
         StageRaceMasterId=56703296
         Year=2019
         UCI=u"yes"
         StageRaceDate=pywikibot.WbTime(site=site,year=Year, month=9, day=22, precision='day')
         CountryCIO=u'FRA'
         Class=12
         SingleDayRaceCreator(pywikibot,site,repo,time,teamTable,StageRaceName,StageRaceGenre,StageRaceMasterId,Year,UCI,StageRaceDate,CountryCIO,Class)
    elif selector==11:
        RaceID='Q60964419'
        StageOrGeneral=4# 1 == stage, #0 == general, #2 == point, #3 mountains,#4 youth, #5 team, #6 team ponts, #7 youth points
        #8 == sprints
        final=0
        separator=";"
        maxkk=10
        year=2019
        classificationImporter(pywikibot,site,repo,StageOrGeneral,RaceID,final,separator,maxkk,year)
    elif selector==12: 
        year=u'2018'
        separator=";"
        test=0
        UCIclassificationImporter(pywikibot,site,repo,year,separator,test)
    elif selector==13:
        RaceID='Q60964419'
        prologueorfinal=0 #0=prologue, 1=final, 2=one day race
        separator=";"
        chrono="on"
        test=0
        timeofrace=pywikibot.WbTime(site=site,year=2019, month=7, day=18, precision='day')    
        listofstartersimporter (pywikibot,site,repo, prologueorfinal, RaceID, separator,timeofrace,chrono,test,teamTable)    
    elif selector==14:
        name="Janette Uwineza"
        description='coureuse cycliste rwandaise' #française
        CountryCIO=u'RWA'
        riderFastInit(pywikibot,site,repo,time,teamTableFemmes, name,description,CountryCIO)
    elif selector==15:
        championshipID='Q65372007'
        test=0
        palmaresImporter(pywikibot,site,repo,championshipID,test)
    elif selector==16:
        champlistcreator(pywikibot,site,repo,time)
    else: 
        print('do nothing')
        
if __name__ == '__main__':
 main()
    #if not main():
        #print(__doc__)
