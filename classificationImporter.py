# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

#oDoc = XSCRIPTCONTEXT.getDocument()

import csv
import os
from CyclingInitBotLow import *

def timeconverter(input):
    if input==0 or input=='+00':
        return 0
    else:
        timesplit=input.split(":")
        return int(timesplit[0])*3600+int(timesplit[1])*60+int(timesplit[2])

def listofteam():
    teamList = [[0 for x in range(2)] for y in range(100)] 
    kk = 1
    
    teamList[kk][0]=u'CANYON // SRAM RACING'   
    teamList[kk][1]=u'Q45536829'
    kk+=1    
    teamList[kk][0]=u'WIGGLE HIGH5'   
    teamList[kk][1]=u'Q47034223'
    kk+=1       
    teamList[kk][0]=u'WAOWDEALS PRO CYCLING TEAM'   
    teamList[kk][1]=u'Q45900995'
    kk+=1   
    teamList[kk][0]=u'MITCHELTON SCOTT'   
    teamList[kk][1]=u'Q43144477'
    kk+=1  

def searchRider(pywikibot,site,resulttable,kk,reversename):
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
    RiderID=searchItem(pywikibot,site, RiderName )
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
    
def listOfTeamException():  
    exceptionTable = [[0 for x in range(2)] for y in range(100)] 
    kk = 1
    
    exceptionTable[kk][0]=u'ORS 2017'   
    exceptionTable[kk][1]=u'Q27865610'
    kk+=1
    exceptionTable[kk][0]=u'SUN 2017'   
    exceptionTable[kk][1]=u'Q28133168'
    kk+=1
    exceptionTable[kk][0]=u'LSL 2017'   
    exceptionTable[kk][1]=u'Q28047488'
    kk+=1
    
    return exceptionTable

def listOfException():
    exceptionTable = [[0 for x in range(2)] for y in range(100)] 
    kk = 1
    
    exceptionTable[kk][0]=u'Louis Engel'   
    exceptionTable[kk][1]=u'Q3261842'
    kk+=1
    exceptionTable[kk][0]=u'Anthony Roux'   
    exceptionTable[kk][1]=u'Q512801'
    kk+=1                        
    exceptionTable[kk][0]=u'Jérémy Roy'   
    exceptionTable[kk][1]=u'Q705331'
    kk+=1   
    exceptionTable[kk][0]=u'Pierre Latour'   
    exceptionTable[kk][1]=u'Q17486055'
    kk+=1          
    exceptionTable[kk][0]=u'Émile Engel'   
    exceptionTable[kk][1]=u'Q3112436'
    kk+=1 
    exceptionTable[kk][0]=u'André Raynaud'   
    exceptionTable[kk][1]=u'Q522455'
    kk+=1 
    exceptionTable[kk][0]=u'Paul Maye'  
    exceptionTable[kk][1]=u'Q493674'
    kk+=1     
    exceptionTable[kk][0]=u'Marcel Laurent'   
    exceptionTable[kk][1]=u'Q3289108'
    kk+=1     
    exceptionTable[kk][0]=u'Jean Rey'   
    exceptionTable[kk][1]=u'Q3174287'
    kk+=1     
    exceptionTable[kk][0]=u'Bernard Gauthier'   
    exceptionTable[kk][1]=u'Q822440'
    kk+=1   
    exceptionTable[kk][0]=u'Jacques Dupont'   
    exceptionTable[kk][1]=u'Q275830'
    kk+=1       
    exceptionTable[kk][0]=u'François Mahé'   
    exceptionTable[kk][1]=u'Q2011167'
    kk+=1       
    exceptionTable[kk][0]=u'Georges Groussard'   
    exceptionTable[kk][1]=u'Q1338784'
    kk+=1          
    exceptionTable[kk][0]=u'Michel Périn'   
    exceptionTable[kk][1]=u'Q3310553'
    kk+=1    
    exceptionTable[kk][0]=u'Jean Dumont'   
    exceptionTable[kk][1]=u'Q2018336'
    kk+=1        
    exceptionTable[kk][0]=u'Mariano Martinez'   
    exceptionTable[kk][1]=u'Q2405300'
    kk+=1  
    exceptionTable[kk][0]=u'Raymond Martin'   
    exceptionTable[kk][1]=u'Q2069946'
    kk+=1  
    exceptionTable[kk][0]=u'François Simon'   
    exceptionTable[kk][1]=u'Q1451199'
    kk+=1
    exceptionTable[kk][0]=u'Jan Smith'
    exceptionTable[kk][1]=u'Q54555914'
    kk+=1
    exceptionTable[kk][0]=u'Susan Crow'
    exceptionTable[kk][1]=u'Q54555931'
    kk+=1
    exceptionTable[kk][0]=u'Maxine Johnson'
    exceptionTable[kk][1]=u'Q6795975'
    kk+=1
    exceptionTable[kk][0]=u'Sarah Phillips'
    exceptionTable[kk][1]=u'Q19867752' 
    kk+=1
    exceptionTable[kk][0]=u'Sally Boyden'
    exceptionTable[kk][1]=u'Q7405083' 
    kk+=1   
    exceptionTable[kk][0]=u'Louise Jones'
    exceptionTable[kk][1]=u'Q6688807' 
    kk+=1  
    exceptionTable[kk][0]=u'Emma Davies'
    exceptionTable[kk][1]=u'Q5372774' 
    kk+=1   
    exceptionTable[kk][0]=u'Jessica Allen'
    exceptionTable[kk][1]=u'Q6187080' 
    kk+=1   
    exceptionTable[kk][0]=u'Julia Shaw'
    exceptionTable[kk][1]=u'Q6306728' 
    kk+=1
    exceptionTable[kk][0]=u'María Isabel Moreno'
    exceptionTable[kk][1]=u'Q439421' 
    kk+=1
    exceptionTable[kk][0]=u'Belen Lopez'
    exceptionTable[kk][1]=u'Q16223239' 
    kk+=1
    exceptionTable[kk][0]=u'Belén López'
    exceptionTable[kk][1]=u'Q16223239' 
    kk+=1
    exceptionTable[kk][0]=u'Gloria Rodríguez'
    exceptionTable[kk][1]=u'Q19519085'
    kk+=1
    exceptionTable[kk][0]=u'Alicia González'
    exceptionTable[kk][1]=u'Q19661974'
    kk+=1
    exceptionTable[kk][0]=u'María Mora'
    exceptionTable[kk][1]=u'Q51296237'
    kk+=1
    exceptionTable[kk][0]=u'Ana Fernandez'
    exceptionTable[kk][1]=u'Q55187131'
    kk+=1
    exceptionTable[kk][0]=u'Ana Fernández'
    exceptionTable[kk][1]=u'Q55187131'
    kk+=1
    exceptionTable[kk][0]=u'Yelena Antonova'
    exceptionTable[kk][1]=u'Q19559969'
    kk+=1
    exceptionTable[kk][0]=u'Stephanie Pohl'
    exceptionTable[kk][1]=u'Q2344233'
    kk+=1
    exceptionTable[kk][0]=u'Svetlana Kuznetsova'
    exceptionTable[kk][1]=u'Q21063641'
    kk+=1
    exceptionTable[kk][0]=u'Olga Sokolova'
    exceptionTable[kk][1]=u'Q14552179'
    kk+=1
    exceptionTable[kk][0]=u'Lisa Klein'
    exceptionTable[kk][1]=u'Q15825971'
    kk+=1
    exceptionTable[kk][0]=u'Claudia Lehmann'
    exceptionTable[kk][1]=u'Q15794537'
    kk+=1
    exceptionTable[kk][0]=u'Emilie Aubry'
    exceptionTable[kk][1]=u'Q513806'
    kk+=1
    exceptionTable[kk][0]=u'Maria Heim'
    exceptionTable[kk][1]=u'Q1532305'
    kk+=1
    exceptionTable[kk][0]=u'Lone Larsen'
    exceptionTable[kk][1]=u'Q20830249'
    kk+=1
    exceptionTable[kk][0]=u'Helle Jensen'
    exceptionTable[kk][1]=u'Q55422442'
    kk+=1
    exceptionTable[kk][0]=u'Sara Mustonen'
    exceptionTable[kk][1]=u'Q4968493'
    kk+=1
    exceptionTable[kk][0]=u'Marie Lindberg'
    exceptionTable[kk][1]=u'Q19519692'
    kk+=1
    exceptionTable[kk][0]=u'Eva Johansson'
    exceptionTable[kk][1]=u'Q55754271'
    kk+=1   
    exceptionTable[kk][0]=u'Lauren Hall'
    exceptionTable[kk][1]=u'Q16212170'
    kk+=1      
    exceptionTable[kk][0]=u'Amanda Miller'
    exceptionTable[kk][1]=u'Q18154419'
    kk+=1      
    exceptionTable[kk][0]=u'Brooke Miller'
    exceptionTable[kk][1]=u'Q18154419'
    kk+=1      
    exceptionTable[kk][0]=u'Jessica Phillips'
    exceptionTable[kk][1]=u'Q20715018'
    kk+=1
    exceptionTable[kk][0]=u'Emma White'
    exceptionTable[kk][1]=u'Q24300644'
    kk+=1  
    exceptionTable[kk][0]=u'Linda Stein'
    exceptionTable[kk][1]=u'Q11780418'
    kk+=1 
    exceptionTable[kk][0]=u'Jane Robinson'
    exceptionTable[kk][1]=u'Q55809416'
    kk+=1 
    exceptionTable[kk][0]=u'Linda Jackson'
    exceptionTable[kk][1]=u'Q511699'
    kk+=1
    exceptionTable[kk][0]=u'Geneviève Gauthier'
    exceptionTable[kk][1]=u'Q55814114'
    kk+=1
    exceptionTable[kk][0]=u'Laura Brown'
    exceptionTable[kk][1]=u'Q1807714'
    kk+=1
    exceptionTable[kk][0]=u'Barbara Lang'
    exceptionTable[kk][1]=u'Q55813877'
    kk+=1
    exceptionTable[kk][0]=u'Denise Ramsden'
    exceptionTable[kk][1]=u'Q2240672'
    kk+=1    
    exceptionTable[kk][0]=u'Alison Jackson'
    exceptionTable[kk][1]=u'Q21067366'
    kk+=1
    exceptionTable[kk][0]=u'Ulrike Baumgartner'
    exceptionTable[kk][1]=u'Q25320642'
    kk+=1
    exceptionTable[kk][0]=u'Barbara Mayer'
    exceptionTable[kk][1]=u'Q31095264'
    kk+=1
    exceptionTable[kk][0]=u'Alison Wright'
    exceptionTable[kk][1]=u'Q19757742'
    kk+=1   
    exceptionTable[kk][0]=u'Alexis Rhodes'
    exceptionTable[kk][1]=u'Q468953'
    kk+=1      
    exceptionTable[kk][0]=u'Grace Brown'
    exceptionTable[kk][1]=u'Q39270192'
    kk+=1       
    exceptionTable[kk][0]=u'Margaret Henderson'
    exceptionTable[kk][1]=u'Q57045220'
    kk+=1      
    exceptionTable[kk][0]=u'Kate Perry'
    exceptionTable[kk][1]=u'Q29050111'
    kk+=1    
    exceptionTable[kk][0]=u'Sarah Ulmer'
    exceptionTable[kk][1]=u'Q176489'
    kk+=1     
    exceptionTable[kk][0]=u'Elisa Balsamo'
    exceptionTable[kk][1]=u'Q26903398'
    kk+=1       
    exceptionTable[kk][0]=u'Jessica Roberts'
    exceptionTable[kk][1]=u'Q54807020'
    kk+=1       
    exceptionTable[kk][0]=u'Ingrid Moe'
    exceptionTable[kk][1]=u'Q40760511'
    kk+=1     
    exceptionTable[kk][0]=u'Lauren Murphy'
    exceptionTable[kk][1]=u'Q57905179'
    kk+=1    
    exceptionTable[kk][0]=u'Anna Christian'
    exceptionTable[kk][1]=u'Q18159989'
    kk+=1 
    exceptionTable[kk][0]=u'Anna Kay'
    exceptionTable[kk][1]=u'Q47296652'
    kk+=1     
    exceptionTable[kk][0]=u'elizabeth bennett'
    exceptionTable[kk][1]=u'Q57956663'
    kk+=1 
    exceptionTable[kk][0]=u'jennifer george'
    exceptionTable[kk][1]=u'Q26236413'
    kk+=1 
    exceptionTable[kk][0]=u'Sarah Walker'
    exceptionTable[kk][1]=u'Q2855120'
    kk+=1 
    exceptionTable[kk][0]=u'sophie wright'
    exceptionTable[kk][1]=u'Q26903403'
    kk+=1 
    exceptionTable[kk][0]=u'paulien rooijakkers'
    exceptionTable[kk][1]=u'Q19577695'
    kk+=1     
    exceptionTable[kk][0]=u'jeydy pradera bernal'
    exceptionTable[kk][1]=u'Q47067465'
    kk+=1     
    exceptionTable[kk][0]=u'kendall ryan'
    exceptionTable[kk][1]=u'Q18156942'
    kk+=1 
    exceptionTable[kk][0]=u'margarita victo garcia cañellas'
    exceptionTable[kk][1]=u'Q23907253'
    kk+=1    
    exceptionTable[kk][0]=u'Lily Williams'
    exceptionTable[kk][1]=u'Q29168606'
    kk+=1  
    exceptionTable[kk][0]=u'Elizabeth Banks'
    exceptionTable[kk][1]=u'Q47295776'
    kk+=1   
    exceptionTable[kk][0]=u'maria martins'
    exceptionTable[kk][1]=u'Q47073025'
    kk+=1      
    exceptionTable[kk][0]=u'Fernanda Yapura'
    exceptionTable[kk][1]=u'Q42594667'
    kk+=1     
    exceptionTable[kk][0]=u'Katharine Hall'
    exceptionTable[kk][1]=u'Q17306130'
    kk+=1   
    

    return exceptionTable


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
                TeamID=searchTeam(pywikibot,site,resulttable,nn,5)
                RiderID=searchRider(pywikibot,site,resulttable,nn,reversename)
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
    

def classificationImporter(pywikibot,site,repo,GeneralOrStage, RaceID,final, separator,maxkk):
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
    year=2018
    
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
  
                if GeneralOrStage==2 or GeneralOrStage==3: #points or mountains
                    resulttable[kk-1][4]=float(row[pointsrow].replace(",",".")) #points
                else:
                    resulttable[kk-1][4]=timeconverter(row[resultrow]) #time
                    if kk==1:
                        resulttable[kk-1][5]=0 #ecart
                    else:
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
    elif GeneralOrStage==4:    
        propertyNummer='4323'#youth 
    elif GeneralOrStage==5:    
        propertyNummer='3497'   
    else: #0
        propertyNummer='2321'  #general
    
    #print(resulttable)
    test=0
    if test==0:
        if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
            print(u'Classification already there')
        else: 
            claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
            kk=0
            while kk<maxkk:
                if GeneralOrStage==5: #team
                    TeamID=searchTeam(pywikibot,site,resulttable,kk,6)
                    RiderID=TeamID
                else:
                    RiderID=searchRider(pywikibot,site,resulttable,kk,reversename)
                if RiderID!='0':
                   target = pywikibot.ItemPage(repo, RiderID)
                   claim.setTarget(target)
                   item.addClaim(claim, summary=u'Adding classification')
                   qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                   targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                   qualifierRank.setTarget(targetQualifier)
                   claim.addQualifier(qualifierRank)
                   if GeneralOrStage==2 or GeneralOrStage==3:
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
            if kk>1:
                if row[6]==riderID:
                    #the rider won once champ on road
                    timeroad=pywikibot.WbTime(site=site,year=row[5], month=row[4], day=row[3], precision='day')    
                    if compareDates(timeOfRace,timeroad)==1: #if race after championship
                        if  timeroad.year>(timeOfRace.year+1): #if race too after championship
                            a=1
                        else:  #interesting case
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
                        if timeclm.year>(timeOfRace.year+1):
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

def listofstartersimporter (pywikibot,site,repo, prologueorfinal, RaceID, separator,timeOfRace,chrono,test):
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
    year=2018
    
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
            RiderID=searchRider(pywikibot,site,resulttable,kk,reversename)

    #print(resulttable)
    alreadylist=0
    if test==0:
        if(u'P'+str('710') in item.claims) and prologueorfinal==0:  #already there do nothing
            print(u'List of starters already there')
        else:   
            claim=pywikibot.Claim(repo, u'P'+str('710')) 
            if (u'P'+str('710') in item.claims):
                alreadylist=1
            listOfcomprend=item.claims.get(u'P'+str(710))
            if prologueorfinal==1:
                listOfcomprendbool=[0 for x in range(len(listOfcomprend))] 
            for kk in range(len(resulttable)):
                RiderID=searchRider(pywikibot,site,resulttable,kk,reversename)
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
                        claim.setTarget(target)
                        item.addClaim(claim, summary=u'Adding starterlist')
                        qualifierDossard=pywikibot.page.Claim(site, 'P1618', isQualifier=True)
                        targetQualifier =resulttable[kk][4]  #pywikibot.WbQuantity(amount=resulttable[kk][4], site=repo)
                        qualifierDossard.setTarget(targetQualifier)
                        claim.addQualifier(qualifierDossard)
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
             
