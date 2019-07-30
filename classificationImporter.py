# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

#oDoc = XSCRIPTCONTEXT.getDocument()

import csv
import numpy as np
import os
from exception import *
from CyclingInitBotLow import *

def timeconverter(input):
    if input==0 or input=='0' or input=='+0' or input=='+00':
        return 0
    else:
        timesplit=input.split(":")
        if len(timesplit)==3:
            return int(timesplit[0])*3600+int(timesplit[1])*60+int(timesplit[2])
        if len(timesplit)==2:
            return int(timesplit[0])*60+int(timesplit[1])
        
        else:
            return int(timesplit[0])

def searchRider(pywikibot,site,repo,resulttable,kk,reversename):
    if reversename==1:
        nameTable=[u'' for x in range(8)] #[ for y in range(j)] 
        jj=0
        inputName=resulttable[kk][1]
        Lastname=""
        Firstname=""
        for ii in range(len(inputName)):
            if inputName[ii]==' ':
                jj=jj+1
            else:
                nameTable[jj]=nameTable[jj]+inputName[ii]
        for ll in range(jj+1):
            if nameTable[ll]==nameTable[ll].upper():
                if Lastname=="":
                    Lastname=nameTable[ll]
                else:
                    Lastname=Lastname+ " "+nameTable[ll]
            else:
                if Firstname=="":
                    Firstname=nameTable[ll]
                else:
                    Firstname=Firstname + " "+nameTable[ll]
    else:
        Firstname=resulttable[kk][2]
        Lastname=resulttable[kk][3]
     
    if Lastname!=0:
        Lastname=Lastname.lower()    
        Firstname=Firstname.lower()
        RiderName=str(Firstname+" "+Lastname)
        exceptionTable=listOfException()
        for ll in range(1,len(exceptionTable)):
            temp=exceptionTable[ll][0]
            if temp!=0:
               temp=temp.lower()
               
            if RiderName==temp:
               return exceptionTable[ll][1]
    else:
      return '0'
    #no exception
    RiderID=searchItemRider(pywikibot,site,repo, RiderName )
    if RiderID=='Q0':
        print(RiderName +' not found')
        return '0'
    elif (RiderID==u'Q1'):
        print(RiderName+' already present several times')
        return '0'
    else:
        return RiderID
    
def searchTeam(pywikibot,site,resulttable,kk,column):
    TeamExceptionTable=listOfTeamException()
    teamCode=resulttable[kk][column]
    
    for ll in range(1,len(TeamExceptionTable)):
        if teamCode==TeamExceptionTable[ll][0]:
            return TeamExceptionTable[ll][1]
    
    TeamID=searchItem(pywikibot,site, teamCode )
    if TeamID=='Q0':
        print(teamCode +'not found')
        return '0'
    elif (TeamID==u'Q1'):
        print(teamCode+' already present several times')
        return '0'
    else:
        return TeamID

def UCIclassificationImporter(pywikibot,site,repo,year, separator,test): #
    resulttable = [[0 for x in range(10)] for y in range(1000)] 
    
    kk=0
    rankrow=-1
    lastnamerow=-1
    firstnamerow=-1
    namerow=-1
    resultrow=-1
    pointsrow=-1
    teamcoderow=-1
    reversename=0

    with open('UCIranking'+year+'.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in spamreader:
            if kk==0:
                for jj in range(len(row)):
                    print(row[jj])
                
                    if row[jj]=='Rank':
                        rankrow=jj
                    elif row[jj]=='Last name':
                        lastnamerow=jj
                    elif row[jj]=='First name':
                        firstnamerow=jj
                    elif row[jj]=='Name':
                        namerow=jj
                    elif row[jj]=='Results' or row[jj]=='Result' :  
                        resultrow=jj
                    elif row[jj]=='Points':  
                        pointsrow=jj
                    elif row[jj]=='Team Code':  
                        teamcoderow=jj 
          
                if firstnamerow==-1 and namerow!=-1:
                    reversename=1
                if rankrow==-1:
                    print('no rank column')
                    return 0
            elif kk!=0:
                resulttable[kk-1][0]=row[rankrow]
                if namerow!=-1:
                    resulttable[kk-1][1]=row[namerow]
                if firstnamerow!=-1:
                    resulttable[kk-1][2]=row[firstnamerow]
                if lastnamerow!=-1:
                    resulttable[kk-1][3]=row[lastnamerow]
                if pointsrow!=-1:
                    resulttable[kk-1][4]=row[pointsrow] #time
                if teamcoderow!=-1:
                    if row[teamcoderow]!=0 and row[teamcoderow]!="":
                        resulttable[kk-1][5]=row[teamcoderow]+" "+year
            kk=kk+1
        for nn in range(1000):
            TeamID='0'
            RiderID='0'
            if resulttable[nn][5]!=0:
                TeamID=searchTeam(pywikibot,site,resulttable,nn,6)
                RiderID=searchRider(pywikibot,site,repo,resulttable,nn,reversename)
            if RiderID!='0' and TeamID!='0' and test==0:
               item =pywikibot.ItemPage(repo, TeamID)
               item.get()
               Addc=1
               
               if(u'P3494' in item.claims):  
                   listOfcomprend=item.claims.get(u'P3494')
                   itemToAdd=pywikibot.ItemPage(repo,RiderID)
                   for ii in range(len(listOfcomprend)):
                       if listOfcomprend[ii].getTarget()==itemToAdd: #Already there
                            Addc=0
                            print('Item already in the Master list')
               
               if Addc==1:
                   claim=pywikibot.Claim(repo, u'P3494') 
                   target = pywikibot.ItemPage(repo, RiderID)
                   claim.setTarget(target)
                   item.addClaim(claim, summary=u'Adding classification')
                   qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                   targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[nn][0]), site=repo)
                   qualifierRank.setTarget(targetQualifier)
                   claim.addQualifier(qualifierRank)
                   qualifierPoints=pywikibot.page.Claim(site, 'P1358', isQualifier=True)
                   targetQualifier = pywikibot.WbQuantity(amount=float(resulttable[nn][4].replace(",",".")), site=repo)
                   qualifierPoints.setTarget(targetQualifier)
                   claim.addQualifier(qualifierPoints)
    

def classificationImporter(pywikibot,site,repo,GeneralOrStage, RaceID,final, separator,maxkk,year):
    filepath='C:\temp\Result\Results.csv'
    #For Europa
    resulttable = [[0 for x in range(20)] for y in range(20)] 
    kk=0
    rankrow=-1
    lastnamerow=-1
    firstnamerow=-1
    namerow=-1
    resultrow=-1
    pointsrow=-1
    teamcoderow=-1
    reversename=0
    
    with open('Results.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in spamreader:
            if kk==0:
                for jj in range(len(row)):
                    if row[jj]=='Rank':
                        rankrow=jj
                    elif row[jj]=='Last name' or row[jj]=='Last Name':
                        lastnamerow=jj
                    elif row[jj]=='First name' or row[jj]=='First Name':
                        firstnamerow=jj
                    elif row[jj]=='Name':
                        namerow=jj
                    elif row[jj]=='Results' or row[jj]=='Result': 
                        resultrow=jj
                    elif row[jj]=='Points':  
                        pointsrow=jj
                    elif row[jj]=='Team Code':
                        teamcoderow=jj 
                    
                if firstnamerow==-1 and namerow!=-1:
                    reversename=1
                if rankrow==-1:
                    print('no rank column')
                    return 0
            elif kk!=0 and kk<11:
                resulttable[kk-1][0]=row[rankrow]
                if namerow!=-1:
                    resulttable[kk-1][1]=row[namerow]
                if firstnamerow!=-1:
                    resulttable[kk-1][2]=row[firstnamerow]
                if lastnamerow!=-1:
                    resulttable[kk-1][3]=row[lastnamerow]
                if teamcoderow!=-1:
                    if row[teamcoderow]!=0 and row[teamcoderow]!="":
                        resulttable[kk-1][6]=row[teamcoderow]+" "+str(year)  
                    
                if pointsrow==-1 and resultrow!=-1: #sometimes the points are in result
                    pointsrow=resultrow
  
                if GeneralOrStage==2 or GeneralOrStage==3 or GeneralOrStage==6 or GeneralOrStage==7 or GeneralOrStage==8: #points or mountains
                    resulttable[kk-1][4]=float(row[pointsrow].replace(",",".")) #points
                else:
                    if kk==1:
                        resulttable[kk-1][4]=timeconverter(row[resultrow]) #time
                        resulttable[kk-1][5]=0 #ecart
                    else:
                        if row[resultrow].find("+")==0:
                            temp=row[resultrow][1:]
                            resulttable[kk-1][5]=timeconverter(temp)
                        else:
                            print(row[resultrow])
                            resulttable[kk-1][4]=timeconverter(row[resultrow]) #time
  
                            if resulttable[kk-1][4]==0:
                                resulttable[kk-1][5]=0
                            else:
                                resulttable[kk-1][5]=resulttable[kk-1][4]-resulttable[0][4]
            kk=kk+1
    item =pywikibot.ItemPage(repo, RaceID)
    item.get()
    
    if GeneralOrStage==1:
        propertyNummer='2417' #stage
    elif GeneralOrStage==2:
        propertyNummer='3494'  #points
    elif GeneralOrStage==3:    
        propertyNummer='4320'  #mountains
    elif GeneralOrStage==4 or GeneralOrStage==7:    
        propertyNummer='4323'#youth 
    elif GeneralOrStage==5:    
        propertyNummer='3497'#teamtime
    elif GeneralOrStage==6:    
        propertyNummer='3496'#team points   
    elif GeneralOrStage==8:    
        propertyNummer='4322'#sprint    
    else: #0
        propertyNummer='2321'  #general
    
    test=0
    if test==0:
        if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
            print(u'Classification already there')
        else: 
            claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
            kk=0
            while kk<maxkk:
                if GeneralOrStage==5 or GeneralOrStage==6: #team
                    TeamID=searchTeam(pywikibot,site,resulttable,kk,6)
                    RiderID=TeamID
                else:
                    RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)
                if RiderID!='0':
                   claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
                   target = pywikibot.ItemPage(repo, RiderID)
                   claim.setTarget(target)
                   item.addClaim(claim, summary=u'Adding classification')
                   qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                   targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                   qualifierRank.setTarget(targetQualifier)
                   claim.addQualifier(qualifierRank)
                   if GeneralOrStage==2 or GeneralOrStage==3 or GeneralOrStage==6 or GeneralOrStage==7:
                       qualifierPoints=pywikibot.page.Claim(site, 'P1358', isQualifier=True)
                       targetQualifier = pywikibot.WbQuantity(amount=int(resulttable[kk][4]), site=repo)
                       qualifierPoints.setTarget(targetQualifier)
                       claim.addQualifier(qualifierPoints)
                   elif resulttable[kk][0]=='1':
                       qualifierTime=pywikibot.page.Claim(site, 'P2781', isQualifier=True)
                       targetQualifier = pywikibot.WbQuantity(amount=int(resulttable[kk][4]), site=repo)
                       qualifierTime.setTarget(targetQualifier)
                       claim.addQualifier(qualifierTime)
                   else:
                       qualifierEcart=pywikibot.page.Claim(site, 'P2911', isQualifier=True)
                       targetQualifier = pywikibot.WbQuantity(amount=int(resulttable[kk][5]), site=repo)
                       qualifierEcart.setTarget(targetQualifier)
                       claim.addQualifier(qualifierEcart)
                   kk=kk+1
                   if GeneralOrStage==0 and final==1:
                       addWinner(pywikibot, site,repo,item,RiderID,int(resulttable[kk-1][0]),GeneralOrStage) 
                       
                else:
                   print(u'interrupted')
                   kk=1000
                   
                   
def riderTricot(pywikibot,site,repo,riderID,timeOfRace,claim,chrono):
    #look for the tricot of rider
    savetable = [[0 for x in range(10)] for y in range(1000)] 
    kk=0
    isroadchamp=0 
    isclmchamp=0
    isworldroadchamp=0
    iseurroadchamp=0
    isworldclmchamp=0
    iseurclmchamp=0
    roadchamp=0
    clmchamp=0
    worldroadchamp=0
    worldclmchamp=0
    eurroadchamp=0
    eurclmchamp=0
    quali=0
    
    with open('Champ.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";", quotechar='|')
        for row in spamreader:
            savetable[kk]=row
            #print(row)
            if kk>1:
                if row[6]==riderID:
                    #the rider won once champ on road
                    timeroad=pywikibot.WbTime(site=site,year=row[5], month=row[4], day=row[3], precision='day')    
                    #timeOfRace>timeofroad and timeOfRace<=timeofroad+1 year
                    if compareDates(timeOfRace,timeroad)==1 and timeOfRace.year<=(timeroad.year+1): #if race after championship
                        print(timeroad.year)
                        print(timeOfRace.year)
                        if u'Q934877'==row[2]:
                            worldroadchamp=row[2]
                        elif u'Q30894544'==row[2]:
                            eurroadchamp=row[2]
                        else:
                            roadchamp=row[2]
                        if timeroad.year==timeOfRace.year:  #then it is clear
                            if u'Q934877'==row[2]:
                                isworldroadchamp=1
                            elif u'Q30894544'==row[2]:
                                iseurroadchamp=1
                            else:
                                isroadchamp=1
                if row[13]==riderID:
                    timeclm=pywikibot.WbTime(site=site,year=row[12], month=row[11], day=row[10], precision='day')    
                    if compareDates(timeOfRace,timeclm)==1:
                        if timeclm.year>(timeOfRace.year):
                            a=1
                        else:
                            if u'Q2630733'==row[9]:
                                worldclmchamp=row[9]
                            elif u'Q30894543'==row[9]:
                                eurclmchamp=row[9] 
                            else:
                                clmchamp=row[9]
                            if timeclm.year==timeOfRace.year:
                                 if u'Q2630733'==row[9]:
                                     isworldclmchamp=1
                                 elif u'Q30894543'==row[9]:     
                                     iseurclmchamp=1
                                 else:
                                     isclmchamp=1
            kk=kk+1
        #print(savetable)
        #print(kk)
        if roadchamp!=0 and isroadchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][2]==roadchamp:
                    timeroad=pywikibot.WbTime(site=site,year=savetable[ii][5], month=savetable[ii][4], day=savetable[ii][3], precision='day')    
                    if timeroad.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeroad)==1:
                             #print('not champ')
                             isroadchamp=-1 #there was another championship
        if clmchamp!=0 and isclmchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][9]==clmchamp:
                    timeclm=pywikibot.WbTime(site=site,year=savetable[ii][12], month=savetable[ii][11], day=savetable[ii][10], precision='day')    
                    if timeclm.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeclm)==1:
                             #print('not champ')
                             isclmchamp=-1 #there was another championship       
        if worldroadchamp!=0 and isworldroadchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][2]==worldroadchamp:
                    timeroad=pywikibot.WbTime(site=site,year=savetable[ii][5], month=savetable[ii][4], day=savetable[ii][3], precision='day')    
                    if timeroad.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeroad)==1:
                             #print('not champ')
                             isworldroadchamp=-1 #there was another championship  
        if worldclmchamp!=0 and isworldclmchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][9]==worldclmchamp:
                    timeclm=pywikibot.WbTime(site=site,year=savetable[ii][12], month=savetable[ii][11], day=savetable[ii][10], precision='day')    
                    if timeclm.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeclm)==1:
                             #print('not champ')
                             isworldclmchamp=-1 #there was another championship                               
        if eurroadchamp!=0 and iseurroadchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][2]==eurroadchamp:
                    timeroad=pywikibot.WbTime(site=site,year=savetable[ii][5], month=savetable[ii][4], day=savetable[ii][3], precision='day')    
                    if timeroad.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeroad)==1:
                             #print('not champ')
                             iseuroadchamp=-1 #there was another championship  
        if eurclmchamp!=0 and iseurclmchamp==0: #check if the champ has already taken place
            for ii in range(1,kk):
                if savetable[ii][9]==eurclmchamp:
                    timeclm=pywikibot.WbTime(site=site,year=savetable[ii][12], month=savetable[ii][11], day=savetable[ii][10], precision='day')    
                    if timeclm.year==timeOfRace.year:
                         if compareDates(timeOfRace,timeclm)==1:
                             #print('not champ')
                             iseurclmchamp=-1 #there was another championship
#prioriy order
#road    
        if isworldroadchamp==1 or (worldroadchamp!=0 and isworldroadchamp!=-1):
            print('this is the world road champ')
            quali=worldroadchamp
        elif iseurroadchamp==1 or (eurroadchamp!=0 and iseurroadchamp!=-1):
           print('this is the european road champ')  
           quali=eurroadchamp
        elif isroadchamp==1 or (roadchamp!=0 and isroadchamp!=-1):
           print('this is the road champ')
           quali=roadchamp
           
        if quali!=0:  
           targetQualifier = pywikibot.ItemPage(repo, quali)
           qualifierTricot=pywikibot.page.Claim(site, 'P2912', isQualifier=True)
           qualifierTricot.setTarget(targetQualifier)
           claim.addQualifier(qualifierTricot)    
           
        quali=0
#clm    
        if chrono=='on':
            if isworldclmchamp==1 or (worldclmchamp!=0 and isworldclmchamp!=-1):
               print('this is the world clm champ')
               quali=worldclmchamp
            elif iseurclmchamp==1 or (eurclmchamp!=0 and iseurclmchamp!=-1):
               print('this is the european clm champ')
               quali=eurclmchamp
            elif isclmchamp==1 or (clmchamp!=0 and isclmchamp!=-1):
               print('this is the clm champ')
               quali=clmchamp
    
            if quali!=0:  
               targetQualifier = pywikibot.ItemPage(repo, quali)
               qualifierTricot=pywikibot.page.Claim(site, 'P2912', isQualifier=True)
               qualifierTricot.setTarget(targetQualifier)
               claim.addQualifier(qualifierTricot)  

def listofstartersimporter (pywikibot,site,repo, prologueorfinal, RaceID, separator,timeOfRace,chrono,test,teamTable):
    filepath='C:\temp\Result\Results.csv'
    #For Europa
    resulttable = [[0 for x in range(10)] for y in range(200)] 
    kk=0
    rankrow=-1
    lastnamerow=-1
    firstnamerow=-1
    namerow=-1
    resultrow=-1
    pointsrow=-1
    teamcoderow=-1
    reversename=0
        
    with open('Results.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in spamreader:
            if kk==0:
                print(row)
                for jj in range(len(row)):
                    if row[jj]=='Rank':
                        rankrow=jj
                    elif row[jj]=='Last name' or row[jj]=='Last Name':
                        lastnamerow=jj
                    elif row[jj]=='First name' or row[jj]=='First Name':
                        firstnamerow=jj
                    elif row[jj]=='Name':
                        namerow=jj
                    elif row[jj]=='Results' or row[jj]=='Result': 
                        resultrow=jj
                    elif row[jj]=='Points':  
                        pointsrow=jj
                    elif row[jj]=='Team Code':  
                        teamcoderow=jj 
                    elif row[jj]=='BIB':  
                        dossardrow=jj     
                    
                if firstnamerow==-1 and namerow!=-1:
                    reversename=1
                if rankrow==-1:
                    print('no rank column')
                    return 0
            elif kk!=0 and row[dossardrow]!='':
                if rankrow!=-1:
                    resulttable[kk-1][0]=row[rankrow]
                if namerow!=-1:
                    resulttable[kk-1][1]=row[namerow]
                if firstnamerow!=-1:
                    resulttable[kk-1][2]=row[firstnamerow]
                if lastnamerow!=-1:
                    resulttable[kk-1][3]=row[lastnamerow]
                if dossardrow!=-1:
                    resulttable[kk-1][4]=row[dossardrow]
            kk=kk+1
    item =pywikibot.ItemPage(repo, RaceID)
    item.get()    
    
    #delete the zeros
    resulttable2 = [[0 for x in range(10)] for y in range(kk-1)] 
    for ii in range(0,kk-1):
        resulttable2[ii]=resulttable[ii]

    #Sort by dossard
    resulttable2=sorted(resulttable2, key=lambda tup: int(tup[4]))
    resulttable=resulttable2
    #check if all riders are already present
    if test==1:
        for kk in range(len(resulttable)):
            RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)

    alreadylist=0
    Year=timeOfRace.year
    if test==0:
        if(u'P'+str('710') in item.claims) and prologueorfinal==0:  #already there do nothing
            print(u'List of starters already there')
        else:   
            #check national team
            nationalteamdetected=0
            allsameteam=1
            for kk in range(len(resulttable)):
                if int(resulttable[kk][4])%10==1:
                    #insert last team
                    if nationalteamdetected==1 and allsameteam==0:
                        print(u'national team detected '+IDtoCIOsearch(teamTable, noQ(nationalteamnation)))
                        for jj in range(nationalteambegin,kk):
                            resulttable[jj][5]=IDtoCIOsearch(teamTable, noQ(nationalteamnation)) + " " + str(Year)
                    nationalteamdetected=1
                    nationalteambegin=kk
                    nationalteamnation=u'reset'
                    proteam=u'reset'
                    allsameteam=1
                if nationalteamdetected!=0:    
                    RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)
                    item =pywikibot.ItemPage(repo, RiderID)
                    item.get()
                    if (u'P27' in item.claims):
                        nationality=item.claims.get(u'P27')
                        if nationalteamnation==u'reset':
                            nationalteamnation=nationality[0].getTarget().getID()
                        else:
                            if nationalteamnation!=nationality[0].getTarget().getID():
                                nationalteamdetected=0
                    team=getPresentTeam(pywikibot,site,repo,RiderID,timeOfRace)
                    if proteam==u'reset':
                        proteam=team
                    else:
                        if proteam!=team:
                            allsameteam=0
            claim=pywikibot.Claim(repo, u'P'+str('710')) 
            if (u'P'+str('710') in item.claims):
                alreadylist=1
            listOfcomprend=item.claims.get(u'P'+str(710))
            if prologueorfinal==1:
                listOfcomprendbool=[0 for x in range(len(listOfcomprend))] 
            for kk in range(len(resulttable)):
                RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)
                if RiderID!='0':
                    target = pywikibot.ItemPage(repo, RiderID)
                    #look for it
                    Addc=-1
                    if alreadylist==1:
                        for ii in range(len(listOfcomprend)):
                           if listOfcomprend[ii].getTarget()==target: #Already there
                                Addc=ii
                                if prologueorfinal==1 or prologueorfinal==2:
                                    listOfcomprendbool[ii]=1
                    if Addc==-1:
                        claim=pywikibot.Claim(repo, u'P'+str('710'))  #reinit everytime
                        claim.setTarget(target)
                        item.addClaim(claim, summary=u'Adding starterlist')
                        qualifierDossard=pywikibot.page.Claim(site, 'P1618', isQualifier=True)
                        targetQualifier =resulttable[kk][4]  #pywikibot.WbQuantity(amount=resulttable[kk][4], site=repo)
                        qualifierDossard.setTarget(targetQualifier)
                        claim.addQualifier(qualifierDossard)
                        if resulttable[kk][5]!=0:
                            Idnationalteam=searchItem(pywikibot,site,resulttable[kk][5])
                            if Idnationalteam!=u'Q0' and Idnationalteam!=u'Q1':
                               print(Idnationalteam)
                               qualifierTeam=pywikibot.page.Claim(site, 'P54', isQualifier=True)
                               qualifierTeam.setTarget(Idnationalteam)
                               claim.addQualifier(qualifierTeam)
                        if prologueorfinal==1 or prologueorfinal==2:
                           if resulttable[kk][0]=='' and prologueorfinal==2:
                               qualifierDNF=pywikibot.page.Claim(site, 'P1534', isQualifier=True)
                               targetQualifier = pywikibot.ItemPage(repo, u'Q1210380')
                               qualifierDNF.setTarget(targetQualifier)
                               claim.addQualifier(qualifierDNF)
                           else:
                               qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                               targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                               qualifierRank.setTarget(targetQualifier)
                               claim.addQualifier(qualifierRank)
                        riderTricot(pywikibot,site,repo,RiderID,timeOfRace,claim,chrono)  
                    else:
                        if prologueorfinal==1 or prologueorfinal==2:
                           listOfcomprend[Addc].setTarget(target) 
                           qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                           targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                           qualifierRank.setTarget(targetQualifier)
                           listOfcomprend[Addc].addQualifier(qualifierRank) #to check
            #all riders are classified, assumption the other are DNF
            if prologueorfinal==1:
                for kk in range(len(listOfcomprend)+1):
                    if listOfcomprendbool[kk]==0:
                         listOfcomprend[kk].setTarget(target) 
                         qualifierDNF=pywikibot.page.Claim(site, 'P1534', isQualifier=True)
                         targetQualifier = pywikibot.ItemPage(repo, u'Q1210380')
                         qualifierDNF.setTarget(targetQualifier)
                         listOfcomprend[kk].addQualifier(qualifierDNF)
                         
                         
def champlistcreator(pywikibot,site,repo,time):
    dic ={'2019': 'Q60015262', '2018' : 'Q43920899', '2017' : 'Q28005879', '2016' : 'Q22021840',
		'2015' : 'Q19296998', '2014' : 'Q15621925', '2013': 'Q3339162',
		'2012' : 'Q1333003', '2011' : 'Q1143844', '2010' : 'Q1568490',
		'2009' : 'Q263224', '2008' : 'Q826505', '2007' : 'Q43286248',
		'2006' : 'Q43286261', '2005' : 'Q1335357', '2004' : 'Q43286272',
		'2003' : 'Q43286289', '2002' : 'Q43286297', '2001' : 'Q43286309'
	}
    
    dicroadrace =['Q934877','Q30894544','Q50064341','Q54315111','Q50061750','Q31271454']
    dicclm=['Q2630733','Q30894543','Q50063172','Q50062728','Q54314912','Q31271381']
    
    startYear=2017
    EndYear=2020
    champtable = [[0 for x in range(15)] for y in range(1000)] 
    ll=-1    

    for ii in range(len(dicroadrace)):
        Idroadrace=dicroadrace[ii]
        masterID=Idroadrace
        itemroadrace =pywikibot.ItemPage(repo, Idroadrace)
        itemroadrace.get()
        if(u'P527' in itemroadrace.claims):
             listOfcomprend=itemroadrace.claims.get(u'P527')
             for jj in range(len(listOfcomprend)):  
                  itemthisyear =listOfcomprend[jj].getTarget()
                  itemthisyear.get()
                  datefound=0
                  invalidprecision=0
                  thereisawinner=0
                  ll=ll+1
                  champtable[ll][2]=masterID
                  
                  if (u'P585' in itemthisyear.claims):
                     listofracedate=itemthisyear.claims.get(u'P585')
                     racedate=listofracedate[0].getTarget()
                     if racedate.day==1 and racedate.month==1:
                         invalidprecision=1
                     else:
                         datefound=1
                  if (u'P1346' in itemthisyear.claims):
                     winners=itemthisyear.claims.get(u'P1346')
                     for mm in range(len(winners)):
                         thisqualID=winners[mm].qualifiers['P642'][0].getTarget().getID()
                         if thisqualID=='Q20882667': #check qualifier
                             tempwinner=winners[mm].getTarget().getID()
                             thereisawinner=1       
                         if datefound==1 and thereisawinner==1:
                             champtable[ll][3]=racedate.day
                             champtable[ll][4]=racedate.month
                             champtable[ll][5]=racedate.year  
                             champtable[ll][6]=tempwinner
                         elif invalidprecision==1 and thereisawinner==1:
                             print(thislabel)
                             print('unsufficient precision')
    ll=-1                          
               
    for ii in range(len(dicclm)):
        Idroadrace=dicclm[ii]
        masterID=Idroadrace
        itemroadrace =pywikibot.ItemPage(repo, Idroadrace)
        itemroadrace.get()
        if(u'P527' in itemroadrace.claims):
             listOfcomprend=itemroadrace.claims.get(u'P527')
             for jj in range(len(listOfcomprend)):  
                  itemthisyear =listOfcomprend[jj].getTarget()
                  itemthisyear.get()
                  datefound=0
                  invalidprecision=0
                  thereisawinner=0
                  ll=ll+1
                  champtable[ll][9]=masterID
                  
                  if (u'P585' in itemthisyear.claims):
                     listofracedate=itemthisyear.claims.get(u'P585')
                     racedate=listofracedate[0].getTarget()
                     if racedate.day==1 and racedate.month==1:
                         invalidprecision=1
                     else:
                         datefound=1
                  if (u'P1346' in itemthisyear.claims):
                     winners=itemthisyear.claims.get(u'P1346')
                     for mm in range(len(winners)):
                         thisqualID=winners[mm].qualifiers['P642'][0].getTarget().getID()
                         if thisqualID=='Q20882667': #check qualifier
                             tempwinner=winners[mm].getTarget().getID()
                             thereisawinner=1       
                         if datefound==1 and thereisawinner==1:
                             champtable[ll][10]=racedate.day
                             champtable[ll][11]=racedate.month
                             champtable[ll][12]=racedate.year  
                             champtable[ll][13]=tempwinner
                         elif invalidprecision==1 and thereisawinner==1:
                             print(thislabel)
                             print('unsufficient precision')   
                             
                             
                             
    print(champtable)                          
    #Look in the national championships
    for ii in range( startYear,EndYear):
        IdallNational=dic[str(ii)]
        itemallNational =pywikibot.ItemPage(repo, IdallNational)
        itemallNational.get()
        if(u'P527' in itemallNational.claims):
             listOfcomprend=itemallNational.claims.get(u'P527')
             for jj in range(len(listOfcomprend)):  
                  itemthisNational =listOfcomprend[jj].getTarget()
                  itemthisNational.get()
                  listOfcomprend2=itemthisNational.claims.get(u'P527')
                  ll=ll+1
                  for kk in range(len(listOfcomprend2)):
                         itemthisRace =listOfcomprend2[kk].getTarget()
                         itemthisRace.get()
                         thislabel=get_label('fr',itemthisRace)
                         #print(thislabel)
                         datefound=0
                         invalidprecision=0
                         thereisawinner=0
                         
                         if thislabel.find("Course en ligne féminine aux")==0:
                             if (u'P31' in itemthisRace.claims):
                                 listofnature=itemthisRace.claims.get(u'P31')
                                 masterID=listofnature[0].getTarget().getID()
                                 champtable[ll][2]=masterID
                             if (u'P585' in itemthisRace.claims):
                                 listofracedate=itemthisRace.claims.get(u'P585')
                                 racedate=listofracedate[0].getTarget()
                                 if racedate.day==1 and racedate.month==1:
                                     invalidprecision=1
                                 else:
                                     datefound=1
                             if (u'P1346' in itemthisRace.claims):
                                 winners=itemthisRace.claims.get(u'P1346')
                                 for mm in range(len(winners)):
                                     thisqualID=winners[mm].qualifiers['P642'][0].getTarget().getID()
                                     if thisqualID=='Q20882667': #check qualifier
                                         tempwinner=winners[mm].getTarget().getID()
                                         thereisawinner=1
                             if datefound==1 and thereisawinner==1:
                                 champtable[ll][3]=racedate.day
                                 champtable[ll][4]=racedate.month
                                 champtable[ll][5]=racedate.year  
                                 champtable[ll][6]=tempwinner
                             elif invalidprecision==1 and thereisawinner==1:
                                 print(thislabel)
                                 print('unsufficient precision')
                         elif thislabel.find("Contre-la-montre féminin aux")==0:
                             if (u'P31' in itemthisRace.claims):
                                 listofnature=itemthisRace.claims.get(u'P31')
                                 masterID=listofnature[0].getTarget().getID()
                                 champtable[ll][9]=masterID
                             if (u'P585' in itemthisRace.claims):
                                 listofracedate=itemthisRace.claims.get(u'P585')
                                 racedate=listofracedate[0].getTarget()
                                 if racedate.day==1 and racedate.month==1:
                                     invalidprecision=1
                                 else:
                                     datefound=1
                             if (u'P1346' in itemthisRace.claims):
                                 winners=itemthisRace.claims.get(u'P1346')
                                 for mm in range(len(winners)):
                                     thisqualID=winners[mm].qualifiers['P642'][0].getTarget().getID()
                                     if thisqualID=='Q20882667': #check qualifier
                                         tempwinner=winners[mm].getTarget().getID()
                                         thereisawinner=1
                             if datefound==1 and thereisawinner==1:
                                 champtable[ll][10]=racedate.day
                                 champtable[ll][11]=racedate.month
                                 champtable[ll][12]=racedate.year  
                                 champtable[ll][13]=tempwinner
                             elif invalidprecision==1 and thereisawinner==1:
                                 print(thislabel)
                                 print('unsufficient precision')      
 

    with open('champ2.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(champtable)
        
def test():
     champtable=[1,2]
     np.savetxt('champ3.csv',champtable, delimiter=';')
     
           
if __name__ == '__main__': 
    [pywikibot,site,repo,time]=wikiinit()          
    print(searchItem(pywikibot,site,'ESP 2019'))
   # test