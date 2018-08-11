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
    
def searchTeam(pywikibot,site,resulttable,kk):
    TeamExceptionTable=listOfTeamException()
    teamCode=resulttable[kk][5]
    
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
    exceptionTable[kk][0]=u'Elisa Balsamo'
    exceptionTable[kk][1]=u'Q26903398'
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
    exceptionTable[kk][0]=u'Jessica Pratt'
    exceptionTable[kk][1]=u'Q39172812'
    kk+=1
    exceptionTable[kk][0]=u'Anna Christian'
    exceptionTable[kk][1]=u'Q18159989'
    kk+=1
    exceptionTable[kk][0]=u'margarita garcia'
    exceptionTable[kk][1]=u'Q23907253'
    kk+=1
    exceptionTable[kk][0]=u'elizabeth williams'
    exceptionTable[kk][1]=u'Q18165763'
    kk+=1
    exceptionTable[kk][0]=u'lauren hall'
    exceptionTable[kk][1]=u'Q16212170'
    kk+=1
    exceptionTable[kk][0]=u'Kendall Ryan'
    exceptionTable[kk][1]=u'Q18156942'
    kk+=1
    exceptionTable[kk][0]=u'Jennifer George'
    exceptionTable[kk][1]=u'Q26236413'
    kk+=1
    exceptionTable[kk][0]=u'Lucy Martin'
    exceptionTable[kk][1]=u'Q6698416'
    kk+=1
    
    
    return exceptionTable


def UCIclassificationImporter(pywikibot,site,repo,year): #
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
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
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
                    elif row[jj]=='Results':  
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
        test=0
        for nn in range(1000):
            TeamID='0'
            RiderID='0'
            if resulttable[nn][5]!=0:
                TeamID=searchTeam(pywikibot,site,resulttable,nn)
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
    

def classificationImporter(pywikibot,site,repo,GeneralOrStage, RaceID,final):
    filepath='C:\temp\Result\Results.csv'
    #For Europa
    resulttable = [[0 for x in range(10)] for y in range(10)] 
    kk=0
    rankrow=-1
    lastnamerow=-1
    firstnamerow=-1
    namerow=-1
    resultrow=-1
    pointsrow=-1
    reversename=0
    
    with open('Results.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
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
                
                if GeneralOrStage==2:
                    resulttable[kk-1][4]=row[pointsrow] #time
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
    else:
        propertyNummer='2321'  #general
    
    #print(resulttable)
    test=0
    if test==0:
        if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
            print(u'Classification already there')
        else: 
            claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
            kk=0
            while kk<10:
                RiderID=searchRider(pywikibot,site,resulttable,kk,reversename)
                if RiderID!='0':
                   target = pywikibot.ItemPage(repo, RiderID)
                   claim.setTarget(target)
                   item.addClaim(claim, summary=u'Adding classification')
                   qualifierRank=pywikibot.page.Claim(site, 'P1352', isQualifier=True)
                   targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                   qualifierRank.setTarget(targetQualifier)
                   claim.addQualifier(qualifierRank)
                   if GeneralOrStage==2:
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
                       addWinner(pywikibot, site,repo,item,RiderID,int(resulttable[kk-1][0]))   
                else:
                   print(u'interrupted')
                   kk=1000
          


