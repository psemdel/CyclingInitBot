# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdel
"""

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
    [teamTableFemmes, endkk]=nationalTeamTable()
   # [teamTableFemmes, endkk]=nationalTeamTable()
    selector=18

    if selector==0:
        Nationalteamcreator(pywikibot,site,repo,time,teamTableFemmes,endkk)
    elif selector==1:
        NationalChampionshipCreator(pywikibot,site,repo,time,teamTableFemmes,endkk,'clmoff')
    elif selector==2:
        StageRaceCreator(pywikibot,site,repo,time,teamTableFemmes)
    elif selector==3:
        IdTeamPage=u'Q47505580'
        TeamOrOther=u'Comp'
        nameSorter(pywikibot,site,repo,time, IdTeamPage, TeamOrOther)
    elif selector==4:
        IdTeamPage=u'Q44497477'
        TeamOrOther=u'Comp'
        dateSorter(pywikibot,site,repo,time,IdTeamPage,TeamOrOther )
    elif selector==5:
        year=u"2016"
        calendarSymmetrizer(pywikibot,site,repo,time, year)
    elif selector==6:
        masterID=u"Q27684043"
        addUCIcalendar(pywikibot,site,repo,time, masterID)
    else: 
        print('do nothing')
        
if __name__ == '__main__':
    main()
    #if not main():
        #print(__doc__)
