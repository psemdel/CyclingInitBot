#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
import csv
import numpy as np
import os
from exception import *
from CyclingInitBotLow import *
from classificationImporter import *

def UCIclassificationImporter(pywikibot,site,repo,year, separator,test): #
    resulttable = [[0 for x in range(10)] for y in range(2000)] 
    
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
                print(row)
                for jj in range(len(row)):
 
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
        
        print('table read')
        for nn in range(1000):
            TeamID='0'
            RiderID='0'
            if resulttable[nn][5]!=0:
                TeamID=searchTeam(pywikibot,site,repo,resulttable,nn,5)
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
                   qualifierRank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                   targetQualifier =  pywikibot.WbQuantity(amount=int(resulttable[nn][0]), site=repo)
                   qualifierRank.setTarget(targetQualifier)
                   claim.addQualifier(qualifierRank)
                   qualifierPoints=pywikibot.page.Claim(site, 'P1358', is_qualifier=True)
                   targetQualifier = pywikibot.WbQuantity(amount=float(resulttable[nn][4].replace(",",".")), site=repo)
                   qualifierPoints.setTarget(targetQualifier)
                   claim.addQualifier(qualifierPoints)
    
    
def UCIclassificationCleaner(pywikibot,site,repo,year, separator,test): #
    resulttable = [[0 for x in range(10)] for y in range(2000)] 
    
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
                print(row)
                for jj in range(len(row)):
 
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
        
        print('table read')
        for nn in range(1000):
            TeamID='0'
            RiderID='0'
            if resulttable[nn][5]!=0:
                TeamID=searchTeam(pywikibot,site,repo,resulttable,nn,5)
                RiderID=searchRider(pywikibot,site,repo,resulttable,nn,reversename)
            
            if RiderID!='0' and TeamID!='0' and test==0:
               item =pywikibot.ItemPage(repo, TeamID)
               item.get()
               Addc=1
               
               if(u'P3494' in item.claims): 
                   item.removeClaims(item.claims['P3494'])