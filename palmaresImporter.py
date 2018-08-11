# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:35:54 2018

@author: maxime delzenne
"""
from CyclingInitBotLow import *

#==Initialisation==   
def wikiinit():
    
    import time
    import sys
    sys.path.insert(0, 'C:\\Wikidata2\\core')
    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot')
    sys.path.insert(0, 'C:\\Wikidata2\\core\\pywikibot\\CyclingInitBot')
    import pywikibot
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    import CyclingInitBotSub
    
    return [pywikibot,site,repo,time]


def palmaresImporter():
    [pywikibot,site,repo,time]=wikiinit()
    
    inputstr="""
| 1974 ||[[France Richer]]||[[Marilyn Freeman]] ||[[Jane McVeigh]]
|-
| 1974 ||[[France Richer]]||[[Marilyn Freeman]] ||[[Jane McVeigh]]
|-
| 1975 || [[Karen Strong]] ||[[Jane McVeigh]] ||[[Betty Schepens]]
|-
| 1976 || [[Karen Strong]] ||[[Dora Horbatiuk ]] ||[[Sylvia Burka]]
|-
| 1977 || [[Sylvia Burka]] || [[Karen Strong]]||[[Carole Vanier]]
|-
| 1978 || [[Sylvia Burka]] ||[[J. Stevens]] ||[[M.A. Kokan]]
|-
| 1979 ||[[Karen Strong]] ||[[Sylvia Burka]] ||[[Marie-Claude Audet]]
|-
| 1980 || [[Sylvia Burka]] ||[[Carole Vanier]] ||[[Marie-Claude Audet]]
|-
| 1981 || [[Karen Strong]] ||[[Carole Vanier]] ||[[Geneviève Brunet]]
|-
| 1982 || [[Verena Buhler]] || [[Laural Zilke]] ||[[Karen Strong]]
|-
| 1983 || [[Marie-Claude Audet]] || [[Karen Strong]]|| [[Verena Buhler]]
|-
| 1984 || [[Geneviève Brunet]] ||[[Marie-Claude Audet]] ||[[Laural Zilke]]
|-
| 1985 || [[Barbara Lang]] ||[[Sarah Neil]] || [[Pamela Bryan]]
|-
|1986 || [[Sarah Neil]] ||[[Barbara Lang]] || [[Denise Kelly]]
|-
| 1987 || [[Geneviève Brunet]] ||[[Alison Sydor]] ||  [[Barbara Lang]]
|-
| 1988 || [[Sarah Neil]] || [[Maria Hawkins]]||[[Edie Fischer]]
|-
| 1989 || [[Laurel Zike]] ||[[Maria Hawkins]]||[[Edie Fischer]]
|-
|1990 || [[Alison Sydor]] || [[Maria Hawkins]] || [[Sarah Neil]]
|-
|1991 || [[Alison Sydor]] || [[Denise Kelly]] || [[Maria Hawkins]]
|-
|1992 || [[Clara Hughes]] || [[Susan Palmer-Komar]] || [[Linda Jackson]]
|-
|1993 || [[Alison Sydor]] || [[Clara Hughes]] || [[Megan McKenna]]
|-
|1994 || [[Alison Sydor]] || [[Leslie Tomlinson]] || [[Clara Hughes]]
|-
|1995 || [[Linda Jackson]] || [[Susan Palmer-Komar]] || [[Alison Sydor]]
|-
|1996 || [[Susan Palmer-Komar]] || [[Anne Samplonius]] || [[Leigh Hobson]]
|-
|1997 || [[Linda Jackson]] || [[Julia Farell]] || [[Susan Palmer-Komar]]
|-
|1998 || [[Linda Jackson]] || [[Alison Sydor]] || [[Lyne Bessette]]
|-
|1999 || [[Clara Hughes]] || [[Lyne Bessette]] || [[Sandy Espeseth]]
|-
|2000 || [[Sandy Espeseth]] || [[Mélanie Nadeau]] || [[Leigh Hobson]]
|-
|2001 || [[Lyne Bessette]] || [[Sandy Espeseth]] || [[Geneviève Jeanson]]
|-
|2002 || [[Katy St Laurent]] || [[Julie Pepin]] || [[Sandy Espeseth]]
|-
|2003 || [[Geneviève Jeanson]] || [[Lyne Bessette]] || [[Susan Palmer-Komar]]
|-
|2004 || [[Lyne Bessette]] || [[Manon Jutras]] || [[Erinne Willock]]
|-
|2005 || [[Geneviève Jeanson]] || [[Erinne Willock]] || [[Susan Palmer-Komar]]
|-
|2006 || [[Alexandra Wrubleski]] || [[Anne Samplonius]] || [[Leigh Hobson]]
|-
|2007 || [[Gina Grain]] || [[Marni Hambleton]] || [[Moriah McGregor]]
|-
|2008 || [[Alexandra Wrubleski]] || [[Leigh Hobson]] || [[Felicia Gomez Greer]]
|-
|2009 || [[Alison Testroete]] || [[Gina Grain]] || [[Merrill Collins]]
|-
|2010 || [[Joëlle Numainville]] || [[Tara Whitten]] || [[Alison Testroete]]
|-
|2011 || [[Véronique Fortin]] || [[Lex Albrecht]] || [[Erinne Willock]]
|-
|2012 || [[Denise Ramsden]] || [[Clara Hughes]] || [[Joëlle Numainville]]
|-
|2013 || [[Joëlle Numainville]] || [[Leah Kirchmann]] || [[Lex Albrecht]]
|-
| 2014 || [[Leah Kirchmann]] || [[Denise Ramsden]] || [[Leah Guloien]]
|-
| 2015 || [[Joëlle Numainville]]  || [[Leah Kirchmann]]|| [[Jamie Gilgen]]
|-
| 2016|| [[Annie Foreman-Mackey]]  || [[Joëlle Numainville]]  || [[Leah Kirchmann]]
|-
| 2017 || [[Allison Beveridge]] || [[Kirsti Lay]] || [[Alison Jackson]]
 """
 
    championshipID='Q31096001'
    
    #inputstr=input()
    tableOfwinner=palmaresParsing(inputstr)
    #print(tableOfwinner)
    numberofabsentriders, counterrepeat, tableOfwinnerOut=wikidataelementAnalyser(pywikibot,site,tableOfwinner)
    test=1
        
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
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][1],1)    
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][2],2)    
              addWinner(pywikibot, site,repo,itempresent,tableOfwinner[ii][3],3)

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
    
def riderFastInit():
   [pywikibot,site,repo,time]=wikiinit()
   mydescription={}
   label={}
 
   Name=u"Fatemeh Feizi"
   mydescription['fr']=u'Coureuse cycliste iranienne'
   label['fr']=Name
   
  ## kkinit=teamCIOsearch(teamTableFemmes, u'NAM')
   CountryCIO=u'IRI'
   kk=teamCIOsearch(teamTableFemmes, CountryCIO)
   Idrider=searchItem(pywikibot,site,Name)

   if (Idrider==u'Q0'):  #no rider with this name  
       Id = create_item(pywikibot,site, label)
       item =pywikibot.ItemPage(repo, Id)
       item.get()
       item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
       addValue(pywikibot,repo,item,31,5,u'nature') 
       addValue(pywikibot,repo,item,21,6581072,u'genre') 
       addValue(pywikibot,repo,item,27,teamTableFemmes[kk][3],u'nationality')
       addValue(pywikibot,repo,item,106,2309784,u'cyclist')
  
    
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
    

    return exceptionTable
    
if __name__ == '__main__':
    #print(teamCIOsearch(teamTableFemmes, u'GBR'))
   # print(teamTableFemmes[35][3])
 #palmaresImporter()
 riderFastInit()
    
    
    
    