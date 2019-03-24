# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:35:54 2018

@author: maxime delzenne
"""
from CyclingInitBotLow import *
from exception import *
#==Initialisation==   
#def wikiinit():
    
 #   import time
#    import sys
# #   sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot')
#    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot\\CyclingInitBot')
#    import pywikibot
    #site = pywikibot.Site("wikidata", "wikidata")
    #repo = site.data_repository()
   # i#mport CyclingInitBotSub
    
    #return [pywikibot,site,repo,time]

#|-
#| 1982 || [[Claudia Tohermes]] || [[Geneviève Brunet]]|| [[C. Baril]]
def palmaresImporter(pywikibot,site,repo,championshipID,test):
   
    inputstr="""
| 2004 || [[Veronika Jeger]] || [[Mónika Király]] || [[Marta Vajda]] 
|-
| 2004 || [[Veronika Jeger]] || [[Mónika Király]] || [[Marta Vajda]] 
|- 
| 2006 || [[Mónika Király]] || [[Diana Szuromine-Pulsfort]] || [[Andrea Fülöp]]
|-
| 2007 || [[Mónika Király]] || [[Diana Szuromine-Pulsfort]] || [[Gabriella Palotai]]
|-
| 2008 || [[Anita Rita Kenyó]] || [[Mónika Király]] || [[Veronika Katonane Simon]]
|-
| 2009 || [[Mónika Király]] || [[Anita Rita Kenyó]]|| [[Veronika Katonane Simon]]
|-
| 2010 || [[Krisztina Fay]] || [[Sara Vidakovich]]|| [[Enikó Papp]]
|-
| 2011 || [[Anita Rita Kenyó]] || [[Krisztina Fay]]|| [[Veronika Anna Kormos]]
|-
| 2012 || [[Anita Rita Kenyó]] || [[Eszter Dosa]] || [[Veronika Anna Kormos]]
|-
| 2013 || [[Diana Szuromine-Pulsfort]] || [[Leila Al Saidi]] || [[Fruzsina Jakocs]]
|-
| 2014 || [[Diana Szuromine-Pulsfort]] || [[Barbara Benkó]] || [[Veronika Anna Kormos]]
|-
| 2015 || [[Diana Szuromine-Pulsfort]] || [[Mónika Király]] || [[Barbara Benkó]]
|-
| 2016 || [[Mónika Király]] || [[Barbara Benkó]] || [[Dorottya Kanti]]
|-
| 2017 || [[Mónika Király]] || [[Szonja Kapott]] || [[Eszter Temela]]
 """
     
    #inputstr=input()
    tableOfwinner=palmaresParsing(inputstr)
    #print(tableOfwinner)
    numberofabsentriders, counterrepeat, tableOfwinnerOut=wikidataelementAnalyser(pywikibot,site,tableOfwinner)
        
    if numberofabsentriders==0 and test==0 and counterrepeat==0:
        palmaresFilling(pywikibot,site,repo,tableOfwinnerOut,championshipID)
    
    
def palmaresParsing(inputstr):
    #parsing of the raw input
    tableofRow=inputstr.split("|-")
    ColumnOfwinner=1
    tableOfwinner = [[0 for x in range(4)] for y in range(len(tableofRow)-1)] 
    
    for ii in range(0,len(tableofRow)-1):#range(len(tableofRow))
        tableofCell={}
        tableofCell=tableofRow[1+ii].split("||")
        #get the year
        tempforyear=tableofCell[0].split("|")
        tableOfwinner[ii][0]=int(tempforyear[1]) #link[0]
        #get first winner
        for jj in range(ColumnOfwinner,ColumnOfwinner+3):
              linksplit1=tableofCell[jj].split("[[")
              link=linksplit1[1].split("]]") 
              tableOfwinner[ii][jj-ColumnOfwinner+1]=link[0]
        
    return tableOfwinner    
    #print(tableOfwinner)
    
def palmaresFilling(pywikibot,site,repo,tableOfwinner,championshipID ):
      itemmaster =pywikibot.ItemPage(repo, championshipID)
      itemmaster.get()
      masterlabel=get_label('fr', itemmaster)
      
      for ii in range(len(tableOfwinner)):  #range(len(tableOfwinner))
          year=tableOfwinner[ii][0]
          print(year)
          presentlabel = masterlabel + " "+ str(year)
          #look for the race
          Idpresent=searchItem(pywikibot,site,presentlabel)
          if (Idpresent==u'Q0'):
              print(presentlabel+ ' not present')
          elif (Idpresent==u'Q1'):
              print(presentlabel+' present several times')
          else:  #good
              itempresent =pywikibot.ItemPage(repo, Idpresent)
              itempresent.get()
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][1],1,0)    
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][2],2,0)    
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][3],3,0)

def wikidataelementAnalyser(pywikibot,site,tableOfwinner):

    #look for riders not created
    counter=0
    counterrepeat=0
    tableOfwinnerOut=tableOfwinner
    exceptionTable=listOfException()
    
    for ii in range(len(tableOfwinner)):
        for jj in range(1,4):
            Idtemp=searchItem(pywikibot,site,tableOfwinner[ii][jj])
            if (Idtemp==u'Q0'):  #no previous or several
                print(tableOfwinner[ii][jj]+ ' not found')
                counter=counter+1
            elif (Idtemp==u'Q1'):
                #list of exceptions
                exceptionfound=0
                for ll in range(1,len(exceptionTable)):
                    if tableOfwinner[ii][jj]==exceptionTable[ll][0]:
                        tableOfwinnerOut[ii][jj]=exceptionTable[ll][1]
                        exceptionfound=1
                if exceptionfound==0:
                    print(tableOfwinner[ii][jj])
                    print(tableOfwinner[ii][jj]+ ' found several times')
                    counterrepeat+=1
            else:
                tableOfwinnerOut[ii][jj]=Idtemp
                 
    if counter==0 and counterrepeat==0:
        print('All riders found!!')
    elif counterrepeat==0:
        print(str(counter)+' riders not found')
    else:
        print(str(counterrepeat)+' riders found several times')
        
    return counter, counterrepeat, tableOfwinnerOut
   

def riderFastInit(pywikibot,site,repo,time,teamTableFemmes, name,description,CountryCIO):
   mydescription={}
   label={}
 
   mydescription['fr']=description
   label['fr']=name
   
  ## kkinit=teamCIOsearch(teamTableFemmes, u'NAM')
   kk=teamCIOsearch(teamTableFemmes, CountryCIO)
   Idrider=searchItem(pywikibot,site,name)

   if (Idrider==u'Q0'):  #no rider with this name  
       Id = create_item(pywikibot,site, label)
       item =pywikibot.ItemPage(repo, Id)
       item.get()
       item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
       addValue(pywikibot,repo,item,31,5,u'nature') 
       addValue(pywikibot,repo,item,21,6581072,u'genre') 
       addValue(pywikibot,repo,item,27,teamTableFemmes[kk][3],u'nationality')
       addValue(pywikibot,repo,item,106,2309784,u'cyclist')
  
    

    
if __name__ == '__main__':
    #print(teamCIOsearch(teamTableFemmes, u'GBR'))
   # print(teamTableFemmes[35][3])
 palmaresImporter()
 #riderFastInit()
    
    
    
    