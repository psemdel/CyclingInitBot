#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:35:53 2019

@author: maxime
"""

from cycling_init_bot_low import get_label
import csv

def f(pywikibot,site,repo,time):
    dic ={'2019': 'Q60015262', '2018' : 'Q43920899', '2017' : 'Q28005879', '2016' : 'Q22021840',
		'2015' : 'Q19296998', '2014' : 'Q15621925', '2013': 'Q3339162',
		'2012' : 'Q1333003', '2011' : 'Q1143844', '2010' : 'Q1568490',
		'2009' : 'Q263224', '2008' : 'Q826505', '2007' : 'Q43286248',
		'2006' : 'Q43286261', '2005' : 'Q1335357', '2004' : 'Q43286272',
		'2003' : 'Q43286289', '2002' : 'Q43286297', '2001' : 'Q43286309'
	}
    
    dicroadrace =['Q934877','Q30894544','Q50064341','Q54315111','Q50061750','Q31271454']
    dicclm=['Q2630733','Q30894543','Q50063172','Q50062728','Q54314912','Q31271381']
    
    startYear=2001
    EndYear=2020
    champtable = [[0 for x in range(15)] for y in range(1000)] 
    ll=-1    

    for ii in range(len(dicroadrace)):
        Idroadrace=dicroadrace[ii]
        masterID=Idroadrace
        itemroadrace =pywikibot.ItemPage(repo, Idroadrace)
        itemroadrace.get()
        
        if(u'P527' in itemroadrace.claims):
             list_of_comprend=itemroadrace.claims.get(u'P527')
             for jj in range(len(list_of_comprend)):  
                  itemthisyear =list_of_comprend[jj].getTarget()
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
                             print(itemroadrace.get_label)
                             print('unsufficient precision')
    ll=-1                          
               
    for ii in range(len(dicclm)):
        Idroadrace=dicclm[ii]
        masterID=Idroadrace
        itemroadrace =pywikibot.ItemPage(repo, Idroadrace)
        itemroadrace.get()
        if(u'P527' in itemroadrace.claims):
             list_of_comprend=itemroadrace.claims.get(u'P527')
             for jj in range(len(list_of_comprend)):  
                  itemthisyear =list_of_comprend[jj].getTarget()
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
                             print(itemroadrace.get_label)
                             print('unsufficient precision')   
                             
                             
                             
    print(champtable)                          
    #Look in the national championships
    for ii in range( startYear,EndYear):
        IdallNational=dic[str(ii)]
        itemallNational =pywikibot.ItemPage(repo, IdallNational)
        itemallNational.get()
        if(u'P527' in itemallNational.claims):
             list_of_comprend=itemallNational.claims.get(u'P527')
             for jj in range(len(list_of_comprend)):  
                  itemthisNational =list_of_comprend[jj].getTarget()
                  itemthisNational.get()
                  list_of_comprend2=itemthisNational.claims.get(u'P527')
                  ll=ll+1
                  for kk in range(len(list_of_comprend2)):
                         itemthisRace =list_of_comprend2[kk].getTarget()
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
