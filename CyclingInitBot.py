# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:12:10 2017

@author: psemdel
"""

#==Initialisation==   
def wikiinit():
    import pywikibot
    import time
    import sys
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
   
    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot\\CyclingInitBot')
    import nationTeamTable
    import stageRaceCreator
    import nationalChampionshipCreator
    import nationalTeamCreator
    
    return [pywikibot,site,repo,time]

def main():
    [pywikibot,site,repo,time]=wikiinit()
    [teamTableFemmes, endkk]=nationalTeamTable()

   # [teamTableFemmes, endkk]=nationalTeamTable()
    selector=2
    
    if selector==0:
        Nationalteamcreator(pywikibot,site,repo,time,teamTableFemmes,endkk)
    elif selector==1:
        NationalChampionshipCreator(pywikibot,site,repo,time,teamTableFemmes,endkk)
    elif selector==2:
        StageRaceCreator(pywikibot,site,repo,time,teamTableFemmes)
    else:
        print('nothing to do')
    
    
if __name__ == '__main__':
    main()
    #if not main():
        #print(__doc__)
