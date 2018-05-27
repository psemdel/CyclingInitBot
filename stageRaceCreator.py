# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
from CyclingInitBotLow import *
from symmetrizer import *

def StageRaceBasic(pywikibot,repo,item,siteIn,country_code,Master,StartDate, EndDate, UCI, year):
#No need for the table here    
       
    addValue(pywikibot,repo,item,31,Master,u'Nature') 
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
    addValue(pywikibot,repo,item,17,country_code,u'country') 

    addDate(pywikibot,repo,item,580,StartDate,u'starting date')
    addDate(pywikibot,repo,item,582,EndDate,u'ending date')
    
    if UCI==u"yes":
        calendarID=calendaruciID(str(year))
        addValue(pywikibot,repo,item,361,noQ(calendarID),u'part of') #
        
def StageBasic(pywikibot,repo,item,site,Number,country_code,Master,inputDate):

    if Number==0:
        addValue(pywikibot,repo,item,31,485321,u'Nature')  #prologue
    else:
        addValue(pywikibot,repo,item,31,18131152,u'Nature')  #étape   
    
    addValue(pywikibot,repo,item,361,Master,u'part of')
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
    addValue(pywikibot,repo,item,17,country_code,u'country') 
    addValue(pywikibot,repo,item,1545,str(Number),u'order')
    #StageRaceBegin later 
    

def DateFinder(pywikibot,repo,site,Number,FirstStage,LastStage, StageRaceBegin,StageRaceEnd):
    
    daysInMonth = [0 for x in range(13)] #Start at 1
    daysInMonth[1]=31
    daysInMonth[2]=28
    daysInMonth[3]=31
    daysInMonth[4]=30
    daysInMonth[5]=31
    daysInMonth[6]=30
    daysInMonth[7]=31
    daysInMonth[8]=31
    daysInMonth[9]=30
    daysInMonth[10]=31
    daysInMonth[11]=30
    daysInMonth[12]=31
    if Number==FirstStage:
         OutputDate=StageRaceBegin
    elif Number==LastStage:
         OutputDate=StageRaceEnd
    else:
         dayBegin=StageRaceBegin.day
         monthBegin=StageRaceBegin.month
         yearBegin=StageRaceBegin.year
         OutputDate=pywikibot.WbTime(site=site,year=yearBegin, month=1, day=1, precision='day')
         #YearonlyDate=pywikibot.WbTime(site=site,year=yearBegin)
         print(Number)
         dayTemp=dayBegin+(Number-FirstStage)
         print(dayTemp)
         if dayTemp>daysInMonth[monthBegin]:
             dayTemp=dayTemp-daysInMonth[monthBegin]
             monthTemp=monthBegin+1
             if monthTemp>12:
                 yearTemp=yearBegin+1
                 monthTemp=monthTemp-12
             else:
                 yearTemp=yearBegin
         else:
                 monthTemp=monthBegin
                 yearTemp=yearBegin
         OutputDate.day=dayTemp
         OutputDate.month=monthTemp
         OutputDate.year=yearTemp

    return OutputDate         
         

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
    StageRaceName=u"Tour de Uppsala"
    StageRaceGenre=u' du ' #+space
    StageRaceMasterId=52456674
    Year=2018
    UCI=u"yes"
    StageRaceBegin=pywikibot.WbTime(site=site,year=Year, month=5, day=10, precision='day')
    StageRaceEnd=pywikibot.WbTime(site=site,year=Year, month=5, day=11, precision='day')
    FirstStage=1
    LastStage=2
    CountryCIO=u'SWE'
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
    
    StageRaceBasic(pywikibot,repo,item,site,teamTableFemmes[kk][3],StageRaceMasterId,StageRaceBegin,StageRaceEnd, UCI, Year)
    
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
    addMultipleValue(pywikibot,repo,itemMaster,527,noQ(Idpresent),u'link year '+ str(Year),0) 
    
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
        print(IdStagepresent)
        itemStagePresent=pywikibot.ItemPage(repo, IdStagepresent)
        itemStagePresent.get()
        if get_description('fr',itemStagePresent)=='':
            mydescription[u'fr']=u'étape'+" " + StageRaceGenre + StageRaceName + " "+ str(Year)
            itemStagePresent.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
        StageBasic(pywikibot,repo,itemStagePresent,site,ii,teamTableFemmes[kk][3],noQ(Idpresent),StageRaceBegin)
        
        print(StageRaceBegin)
        stageDate=DateFinder(pywikibot,repo,site,ii,FirstStage,LastStage, StageRaceBegin,StageRaceEnd)
        addDate(pywikibot,repo,itemStagePresent,585,stageDate,u'date')
        
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
        addMultipleValue(pywikibot,repo,item,527,noQ(IdStagepresent),u'link stage '+str(ii),0) 
        #Link to next
        #Not required 
  

    
