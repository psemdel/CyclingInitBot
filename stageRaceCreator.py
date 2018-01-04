# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
import cyclingInitBotLow

def StageRaceBasic(pywikibot,repo,item,siteIn,country_code,Master,StartDate, EndDate):
#No need for the table here    
       
    addValue(pywikibot,repo,item,31,Master,u'Nature') 
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
    addValue(pywikibot,repo,item,17,country_code,u'country')

    if(u'P580' in item.claims):
        a=1
    else:
        claim=  pywikibot.Claim(repo, u'P580') #date de début
        claim.setTarget(StartDate)
        item.addClaim(claim, summary=u'Adding starting date')  
        
    if(u'P582' in item.claims):
        a=1
    else:
        claim=  pywikibot.Claim(repo, u'P582') #date de fin
        claim.setTarget(EndDate)
        item.addClaim(claim, summary=u'Adding ending date') 
        
def StageBasic(pywikibot,repo,item,site,Number,country_code,Master,StageRaceBegin):

    if Number==0:
        addValue(pywikibot,repo,item,31,485321,u'Nature')  #prologue
    else:
        addValue(pywikibot,repo,item,31,18131152,u'Nature')  #étape   
    
    
    addValue(pywikibot,repo,item,361,Master,u'part of')
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
    addValue(pywikibot,repo,item,17,country_code,u'country')
    addValue(pywikibot,repo,item,1545,str(Number),u'order')
    
    #StageRaceBegin later   
    
def StageLabel(Number, Genre, StageRaceName, Year):
    mylabel={}
        
    if Number==0:
        label_part1_fr = u"Prologue"
    elif Number==1:
        label_part1_fr = u"1re étape"
    else:
        label_part1_fr = str(Number)+u"e étape"
        
    mylabel[u'fr']= label_part1_fr+" " + Genre + StageRaceName + " "+ str(Year)
    return mylabel


def StageRaceCreator(pywikibot,site,repo,time,teamTableFemmes):   
    StageRaceName=u"Santos Women's Tour"
    StageRaceGenre=u'du ' #+space
    StageRaceMasterId=22661614
    Year=2018
    StageRaceBegin=pywikibot.WbTime(site=site,year=Year, month=1, day=11, precision='day')
    StageRaceEnd=pywikibot.WbTime(site=site,year=Year, month=1, day=14, precision='day')
    FirstStage=1
    LastStage=4
    CountryCIO=u'AUS'
    mydescription={}
    #StageRaceEnd=pywikibot.WbTime(site=siteIn,year=2017, month=1, day=1, precision='day')
    
    #Create Item
    kk=teamCIOsearch(teamTableFemmes, CountryCIO)
    
    mylabel={}
    mylabel[u'fr']=StageRaceName + " " + str(Year)
    
    Idpresent=searchItem(pywikibot,site,mylabel['fr'])
    if (Idpresent==u'Q0'):
        print(mylabel[u'fr']+' created')
            #Type code
        Idpresent = create_item(pywikibot,site, mylabel)
    elif (Idpresent==u'Q1'):
        print(mylabel['fr']+' already present several times')
    else:    
        print(mylabel['fr']+' already present')

    item =pywikibot.ItemPage(repo, Idpresent)
    item.get()
    
    if get_description('fr',item)=='':
        mydescription[u'fr']=u'édition ' + str(Year) + StageRaceGenre + StageRaceName
        item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
    
    StageRaceBasic(pywikibot,repo,item,site,teamTableFemmes[kk][3],StageRaceMasterId,StageRaceBegin,StageRaceEnd)
    
    #Search previous
    Yearprevious= Year-1
    mylabelprevious=StageRaceName + " " + str(Yearprevious)
    Idprevious=searchItem(pywikibot,site,mylabelprevious)
    if (Idprevious==u'Q0')or(Idprevious==u'Q1'):  #no previous or several
       a=1
    else:
        addValue(pywikibot,repo,item,155,noQ(Idprevious),u'link previous') 
            #Link to the previous
        itemPrevious=pywikibot.ItemPage(repo, Idprevious)
        itemPrevious.get()
        addValue(pywikibot,repo,itemPrevious,156,noQ(Idpresent),u'link next')
             
    #Search next   
    Yearnext= Year+1
    mylabelnext=StageRaceName + " " + str(Yearnext)
    Idnext=searchItem(pywikibot,site,mylabelnext)
    
    time.sleep(1.0)
    if (Idnext==u'Q0')or(Idnext==u'Q1'):  #no next or 
        a=1
    else:
       addValue(pywikibot,repo,item,156,noQ(Idnext),u'link next')  
       #Link to the next
       itemNext=pywikibot.ItemPage(repo, Idnext)
       itemNext.get()
       addValue(pywikibot,repo,itemNext,155,noQ(Idpresent),u'link previous')
    
    #link to master
    itemMaster= pywikibot.ItemPage(repo, u'Q'+ str(StageRaceMasterId))
    itemMaster.get()
    addComprend(pywikibot,repo,itemMaster,noQ(Idpresent),u'link year '+ str(Year)) 
    
    #Create the stages
    stageLabel={}  
        
    for ii in range(FirstStage,LastStage+1):
        stageLabel=StageLabel(ii, StageRaceGenre, StageRaceName, Year)
        
        IdStagepresent=searchItem(pywikibot,site,stageLabel['fr'])
        if (IdStagepresent==u'Q0'):
            print(stageLabel['fr']+' created')
                #Type code
            IdStagepresent = create_item(pywikibot,site, stageLabel)
          
        elif (Idpresent==u'Q1'):
            print(stageLabel['fr']+' already present several times')
        else:    
            print(stageLabel['fr']+' already present')
    
        itemStagePresent=pywikibot.ItemPage(repo, IdStagepresent)
        itemStagePresent.get()
        if get_description('fr',itemStagePresent)=='':
            mydescription[u'fr']=u'étape'+" " + StageRaceGenre + StageRaceName + " "+ str(Year)
            itemStagePresent.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
        StageBasic(pywikibot,repo,itemStagePresent,site,ii,teamTableFemmes[kk][3],noQ(Idpresent),StageRaceBegin)
         #Link to previous
        if ii==0:
            lookforprevious=0
        else:   
            if ii==1:
                if FirstStage==0:
                    lookforprevious=1
                else:
                    lookforprevious=0
            else:
                lookforprevious=1
        
        if lookforprevious==1:
            stageLabelprevious=StageLabel(ii-1, StageRaceGenre, StageRaceName, Year)
            IdStageprevious=searchItem(pywikibot,site,stageLabelprevious['fr'])
            if (IdStageprevious==u'Q0')or(IdStageprevious==u'Q1'):  #no previous or several
                a=1
            else:
                addValue(pywikibot,repo,itemStagePresent,155,noQ(IdStageprevious),u'link previous') 
                    #Link to the previous
                itemStagePrevious=pywikibot.ItemPage(repo, IdStageprevious)
                itemStagePrevious.get()
                addValue(pywikibot,repo,itemStagePrevious,156,noQ(IdStagepresent),u'link next')
        
        #Link to the master for this year, so item
        addComprend(pywikibot,repo,item,noQ(IdStagepresent),u'link stage '+str(ii)) 
        #Link to next
        #Not required 