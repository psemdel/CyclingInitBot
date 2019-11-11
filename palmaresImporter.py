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
   #Q31271010
    inputstr="""
|-
| 2006 || [[Evelyn García]] || [[Ana Gabriela Larios]] ||  [[Ana Gabriela Larios]]
|-
| 2007 || [[Evelyn García]] || [[Michelle Ortiz]] || [[Priscila Ramos]]
|-
| 2008 || [[Roxana Ortiz]] || [[Priscila Ramos]] ||  [[Priscila Ramos]] 
|-
| 2009 || [[Evelyn García]] || [[Michelle Ortiz]] || [[Xenia Estrada]]
|-
| 2010 || [[Evelyn García]] || [[Xenia Estrada]] || [[Nathaly Majano]]
|-
| 2011 || [[Evelyn García]] || [[Roxana Ortiz]] || [[Beatriz Quiroz]]
|-
| 2012 || [[Xenia Estrada]] || [[Ana Figueroa]] || [[Nathaly Majano]]
|-
| 2013 || [[Ana Figueroa]] || [[Xenia Estrada]] || [[Karen Cruz]]
|-
| 2014 || [[Xenia Estrada]] || [[Ana Figueroa]] ||[[Ana Figueroa]]
|-
| 2015 || [[Evelyn García]] || [[Aída Turcios]] || [[Ana Figueroa]]
|-
| 2016 || [[Ana Figueroa]] || [[Roxana Ortiz]] || [[Vanessa Serrano]]
|-
| 2017 || [[Evelyn García]] || [[Ana Figueroa]] || [[Xenia Estrada]]
|-
| 2018 || [[Roxana Ortiz]] || [[Brenda Aparicio]] || [[Alejandra Cardona]]
|-
| 2019 || [[Xenia Estrada]] || [[Vanessa Serrano]] || [[Sauking Shi]]
 """
     
    #inputstr=input()
    tableOfwinner=palmaresParsing(inputstr)
    #print(tableOfwinner)
    numberofabsentriders, counterrepeat, tableOfwinnerOut=wikidataelementAnalyser(pywikibot,site,repo,tableOfwinner)
        
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

def wikidataelementAnalyser(pywikibot,site,repo,tableOfwinner):

    #look for riders not created
    counter=0
    counterrepeat=0
    tableOfwinnerOut=tableOfwinner
    exceptionTable=listOfException()
    
    for ii in range(len(tableOfwinner)):
        for jj in range(1,4):
            Idtemp=searchItemRider(pywikibot,site,repo, tableOfwinner[ii][jj] )
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
    
    
    
    