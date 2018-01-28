# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:57:25 2018

@author: maxime delzenne
"""

def addUCIcalendar(pywikibot,site,repo,time, masterID):
   
    
    classestotest={u"Q22231109",u"Q22231110",u"Q22231111",u"Q22231112",u"Q22231113",u"Q22231118"}
      
    itemmaster =pywikibot.ItemPage(repo, masterID)
    itemmaster.get()
    #get the list of the races
    if(u'P527'in itemmaster.claims):  #already there do nothing
        listOfcomprend=itemmaster.claims.get(u'P527')

    #read all races
    for ii in range(len(listOfcomprend)):
        item=listOfcomprend[ii].getTarget()
        item.get()
        classeOK=0
        
        #check that it is 1.1, 1.2...
        if(u'P31'in item.claims): 
            claimTemp=item.claims[u'P31']
            for jj in range(len(claimTemp)):
                classTemp=claimTemp[jj].getTarget()
                classTempID=classTemp.getID()
                for cc in classestotest:
                    if classTempID==cc:
                        classeOK=1
                   
        if classeOK==1:
            #check the date
            if(u'P585'in item.claims): 
                 claimTemp=item.claims[u'P585']
                 dateTemp=claimTemp[0].getTarget()
            elif (u'P580' in item.claims): #course à étapes
                 claimTemp=item.claims[u'P580']
                 dateTemp=claimTemp[0].getTarget()     
            else:
                 print(item.labels['fr'] + u' has no date')
                 return 0     
    
            Year=str(dateTemp.year)
            calendarID=calendaruciID(pywikibot,site,repo,time, Year)
            if calendarID!=u"Q0":
                print(u"add UCI calendar to edition "+ Year)
                addMultipleValue(pywikibot,repo,item,361,noQ(calendarID),'add uci calendar',0)            
            else:
                print(u"no UCI calendar found for year "+ Year)
        else:
           print(u"edition not UCI " + item.getID())

def calendaruciID(pywikibot,site,repo,time, year):  
    if  year == "2018":
        calendarID="Q47005682"
    elif year == "2017":
        calendarID="Q27765666"	
    elif year == "2016": 
        calendarID="Q22696468"
    elif year == "2015": 
        calendarID="Q18348936"
    elif year == "2014": 
        calendarID="Q15831496"	
    elif year == "2013": 
        calendarID="Q6425932"	
    elif year == "2012": 
        calendarID="Q2466796"	
    elif year == "2011": 
        calendarID="Q2466792"
    elif year == "2010": 
        calendarID="Q2933831"
    elif year == "2009": 
        calendarID="Q2933830"
    elif year == "2008": 
        calendarID="Q2933828"
    elif year == "2007": 
        calendarID="Q3650627"	
    elif year == "2006": 
        calendarID="Q16154659"  
    else:
        calendarID="Q0"
        
    return calendarID
        
def calendarSymmetrizer(pywikibot,site,repo,time, year):
    from pywikibot import pagegenerators 
    
    calendarID=calendaruciID(pywikibot,site,repo,time, year)

    #use the query
    query = "SELECT DISTINCT ?item WHERE {?item wdt:P361 wd:" + calendarID +"}"
    ListOfItem = pagegenerators.WikidataSPARQLPageGenerator(query, site=repo)
        
    itemCalendar =pywikibot.ItemPage(repo, calendarID)
    itemCalendar.get()
    SumAddc=0
    
    for item in ListOfItem:
        valueTemp=item.getID()
        SumAddc=SumAddc+addMultipleValue(pywikibot,repo,itemCalendar,527,noQ(valueTemp),'add races',0)
    
  #      print(item)
    if SumAddc!=0:
        dateSorter(pywikibot,site,repo,time,calendarID,u'Comp')



