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
|-
| 1959 || [[Beryl Burton]] || [[Millie Robinson]] || [[Sheila Holmes]]
|-
| 1960 || [[Beryl Burton]] || [[Sheila Holmes]] || [[Val Baxendine]]
|-
| 1961 || [[Jo Bowers]] || [[Beryl Burton]] || [[Jan Smith]]
|-
| 1962 || [[Jo Bowers]] || [[Pat Pepper]] || [[Cynthia Cary]]
|-
| 1963 || [[Beryl Burton]] || [[Pat Pepper]] || [[Jo Bowers]]
|-
| 1964 || [[Val Rushworth]] || [[Sylvia Beardon]] || [[Ann Illingworth]]
|-
| 1965 || [[Beryl Burton]] || [[Susan Crow]] || [[Joan Kershaw]]
|-
| 1966 || [[Beryl Burton]] || [[Christine Goodfellow]] || [[Ann Illingworth]]
|-
| 1967 || [[Beryl Burton]] || [[Barbara Mapplebeck]] || [[Pat Pepper]]
|-
| 1968 || [[Beryl Burton]] || [[Barbara Mapplebeck]] || [[Sylvia Beardon]]
|-
| 1969 || [[Ann Horswell]] || [[Bernadette Swinnerton]] || [[Pat Pepper]]
|-
| 1970 || [[Beryl Burton]] || [[Joan Kershaw]] || [[Brenda Brown]]
|-
| 1971 || [[Beryl Burton]] || [[Bernadette Swinnerton]] || [[Ann Bailey]]
|-
| 1972 || [[Beryl Burton]] || [[Ann Bailey]] || [[Pat Pepper]]
|-
| 1973 || [[Beryl Burton]] || [[Denise Burton]] || [[Christine Goodfellow]]
|-
| 1974 || [[Beryl Burton]] || [[Carol Barton]] || [[Christine Goodfellow]]
|-
| 1975 || [[Jayne Westbury]] || [[Denise Burton]] || [[Cath Swinnerton]]
|-
| 1976 || [[Denise Burton]] || [[Beryl Burton]] || [[Carol Barton]]
|-
| 1977 || [[Cath Swinnerton]] || [[Faith Murray]] || [[Josie Randall]]
|-
| 1978 || [[Brenda Atkinson]] || [[Denise Burton]] || [[Cathy Swinnerton]]
|-
| 1979 || [[Brenda Atkinson]] || [[Cath Swinnerton]] || [[Bernadette Griffiths]]
|-
| 1980 || [[Jill Bishop]] || [[Julie Earnshaw]] || [[Brenda Atkinson]]
|-
| 1981 || [[Mandy Jones]] || [[Julie Earnshaw]] || [[Vicki Thomas]]
|-
| 1982 || [[Brenda Atkinson]] || [[Cath Swinnerton]] || [[Cath Swinnerton]]
|-
| 1983 || [[Mandy Jones]] || [[Judith Painter]] || [[Linda Gornall]]
|-
| 1984 || [[Cath Swinnerton]] || [[Maria Blower]] || [[Muriel Sharp]]
|-
| 1985 || [[Brenda Tate]] || [[Lisa Bramani]] || [[Vicki Thomas]]
|-
| 1986 || [[Lisa Bramani]] || [[Vicki Thomas]] || [[Linda Flavell]]
|-
| 1987 || [[Lisa Bramani]] || [[Sally Hodge]] || [[Linda Gornall]]
|-
| 1988 || [[Lisa Bramani]] || [[Sally Hodge]] || [[Maria Blower]]
|-
| 1989 || [[Lisa Bramani]] || [[Sue Wright]] || [[Maria Blower]]
|-
| 1990 || [[Marie Purvis]] || [[Alison Butler]] || [[Maxine Johnson]]
|-
| 1991 || [[Marie Purvis]] || [[Clare Greenwood]] || [[Linda Gornall]]
|-
| 1992 || [[Marie Purvis]] || [[Sarah Phillips]] || [[Clare Greenwood]]
|-
| 1993 || [[Marie Purvis]] || [[Maxine Johnson]] || [[Sarah Phillips]]
|-
| 1994 || [[Maxine Johnson]] || [[Jenny Kershaw]] || [[Sally Boyden]]
|-
| 1995 || [[Marie Purvis]] || [[Ann Plant]] || [[Jenny Kershaw]]
|-
| 1996 || [[Maria Lawrence]] || [[Ann Plant]] || [[Angela Hunter]]
|-
| 1997 || [[Maria Lawrence]] || [[Isla Rowntree]] || [[Angela Hunter]]
|-
| 1998 || [[Megan Huges]] || [[Louise Jones]] || [[Sally Boyden]]
|-
| 1999 || [[Nicole Cooke]] || [[Yvonne McGregor]] || [[Ceris Gilfillan]]
|-
| 2000 || [[Ceris Gilfillan]] || [[Caroline Alexander]] || [[Yvonne McGregor]]
|-
| 2001 || [[Nicole Cooke]] || [[Ceris Gilfillan]] || [[Sara Symington]]
|-
| 2002 || [[Nicole Cooke]] || [[Rachel Heal]] || [[Melanie Sears]]
|-
| 2003 || [[Nicole Cooke]] || [[Rachel Heal]] || [[Vicki Pincombe]]
|-
| 2004 || [[Nicole Cooke]] || [[Rachel Heal]] || [[Vicki Pincombe]]
|-
| 2005 || [[Nicole Cooke]] || [[Rachel Heal]] || [[Emma Davies]]
|-
| 2006 || [[Nicole Cooke]] || [[Lorna Webb]] || [[Joanna Rowsell]]
|-
| 2007 || [[Nicole Cooke]] || [[Rachel Heal]] || [[Helen Wyman]]
|-
| 2008 || [[Nicole Cooke]] || [[Emma Pooley]] || [[Joanna Rowsell]]
|-
| 2009 || [[Nicole Cooke]] || [[Elizabeth Armitstead]] || [[Emma Pooley]]
|-
| 2010 || [[Emma Pooley]] || [[Elizabeth Armitstead]] || [[Nicole Cooke]]
|-
| 2011 || [[Elizabeth Armitstead]] || [[Nicole Cooke]] || [[Sharon Laws]]
|-
| 2012 || [[Sharon Laws]] || [[Elizabeth Armitstead]] || [[Emma Pooley]]
|-
| 2013 || [[Elizabeth Armitstead]] || [[Laura Trott]] || [[Danielle King]]
|-
| 2014||[[Laura Trott]]||[[Danielle King]]||[[Elizabeth Armitstead]]
|-
| 2015||[[Elizabeth Armitstead]]||[[Alice Barnes ]]||[[Laura Trott]]
|-
| 2016||[[Hannah Barnes]]||[[Alice Barnes]]||[[Lucy Garner]]
|-
| 2017 || [[Elizabeth Armitstead]] || [[Katie Archibald]] || [[Hannah Barnes]] 
 """
 
    championshipID='Q27048419'
    
    #inputstr=input()
    tableOfwinner=palmaresParsing(inputstr)
    #print(tableOfwinner)
    numberofabsentriders, tableOfwinnerOut=wikidataelementAnalyser(pywikibot,site,tableOfwinner)
    test=1
        
    if numberofabsentriders==0 and test==0:
        palmaresFilling(pywikibot,site,repo,tableOfwinner,championshipID)
    
    
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
        #linksplit1=tempforyear[1].split("[[")  
        #link=linksplit1[1].split("]]") 
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
                for ll in range(1,len(exceptionTable)):
                    if tableOfwinner[ii][jj]==exceptionTable[ll][0]:
                        tableOfwinnerOut[ii][jj]=exceptionTable[ll][1]
                if tableOfwinner[ii][jj]==0:  
                    print(tableOfwinner[ii][jj]+ ' found several times')
   
            else:
                tableOfwinnerOut[ii][jj]=Idtemp
                 
    if counter==0:
        print('All riders found!!')
    else:
        print(str(counter)+' riders not found')
    return counter, tableOfwinnerOut
    
def riderFastInit():
   [pywikibot,site,repo,time]=wikiinit()
   mydescription={}
   label={}
   
   Name=u"Flor Aparecida Palma Dos Santos"
   mydescription['fr']=u'Coureuse cycliste chilienne'
   label['fr']=Name
   
  ## kkinit=teamCIOsearch(teamTableFemmes, u'NAM')
   CountryCIO=u'CHI'
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
    
    

    return exceptionTable
    
if __name__ == '__main__':
    #palmaresImporter()
    riderFastInit()
    
    
    
    