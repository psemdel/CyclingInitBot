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
|[[1951]]|| [[Nantes]]||[[Lucienne Benoît]]||[[Georgette Rodet]]||[[Jeannine Lemaire]]
|-
|[[1952]]|| [[Montlhéry]]||[[Jeannine Lemaire]]||[[Gaby Guillard]]||[[Huguette Luneau]]
|-
|[[1953]]|| [[Nantes]]||[[Jeannine Lemaire]]||[[Gaby Guillard]]||[[Reine Lacave]]
|-
|[[1954]]|| [[Roanne]]|| [[Noelle Naulot]]||[[Jeannine Lemaire]]||[[Joséphine Bardelet]]
|-
|[[1955]]|| [[Montlhéry]]||[[Lydia Brein-Haritonides]] ||[[Marie-Jeanne Donabedian]]||[[Simone Demory]]
|-
|[[1956]]|| [[Longwy]]||[[Lily Herse]]||[[Marie-Jeanne Donabedian]]||[[Renée Vissac]]
|-
|[[1957]]|| [[Bourg-en-Bresse]]||[[Jeannine Meriau]]||[[Pierrette Soupiret]]||[[Marie-Jeanne Donabedian]] 
|-
|[[1958]]|| [[Montlhéry]]||[[Lily Herse]]||[[Renée Vissac]]||[[Gilberte Rocaboy]]
|-
|[[1959]]|| [[Landivisiau]]||[[Lily Herse]]||[[Renée Vissac]]||[[Simone Demory]]
|-
|[[1960]]|| [[Annemasse]]||[[Renée Vissac]]||[[Lily Herse]]||[[Andrée Vaudel]]
|-
|[[1961]]|| [[Louvroil]]||[[Lily Herse]]||[[Simone Heutte]]||[[Renée Vissac]]
|-
|[[1962]]|| [[Saint-Hilaire-du-Harcouët]]||[[Lily Herse]]||[[Andrée Flageolet]]||[[Renée Vissac]]
|-
|[[1963]]|| [[Sancerre]]||[[Lily Herse]]||[[Renée Thuin]]||[[Andrée Flageolet]]
|-
|[[1964]]|| [[Coutances]]||[[Andrée Flageolet]]||[[Lily Herse]]||[[Renée Vissac]]
|-
|[[1965]]|| [[Bully-les-Mines]]||[[Lily Herse]]||[[Renée Vissac]] ||[[Simone Boubechiche]]
|-
|[[1966]]|| [[Le Havre]]||[[Gisèle Caille]]||[[Claude Bordujenko]] ||[[Lily Herse]]
|-
|[[1967]]|| [[Xertigny]]||[[Lily Herse]] ||[[Christiane Rousseau]]||[[Renée Vissac]]
|-
|[[1968]]|| [[Port-de-Bouc]]||[[Chantal N'Guyen]]||[[Jacky Barbedette]]||[[Micheline Le Moigne]]
|-
|[[1969]]|| [[Rouen-les-Essarts]]||[[Geneviève Gambillon]]||[[Danièle Piton]]||[[Micheline Le Moigne]]
|-
|[[1970]]|| [[Serent]]||[[Geneviève Gambillon]]||[[Micheline Le Moigne]]||[[Chantal Heuveline]]
|-
|[[1971]]|| [[Jeumont]]||[[Annick Chapron]]||[[Geneviève Gambillon]]||[[Béatrice Vachet]]
|-
|[[1972]]|| [[Vitteaux]]||[[Geneviève Gambillon]]||[[Josiane Bost]]||[[Sylviane Junal]]
|-
|[[1973]]|| [[Dax]]||[[Élisabeth Camus]]||[[Mauricette Carpentier]]||[[Geneviève Gambillon]]
|-
|[[1974]]|| [[Montpinchon]]||[[Geneviève Gambillon]]||[[Annick Chapron]]||[[Élisabeth Camus]]
|-
|[[1975]]|| [[Callac]]||[[Geneviève Gambillon]]||[[Josiane Bost]]||[[Jeanine Martin-Leborgne]]
|-
|[[1976]]|| [[Lignac]]||[[Geneviève Gambillon]]||[[Nicole Verzier]]||[[Josiane Bost]]
|-
|[[1977]]|| [[Pomport]]||[[Geneviève Gambillon]]||[[Josiane Bost]]||[[Nicole Verzier]]
|-
|[[1978]]|| [[Escoussens]]||[[Chantal Fortier]]||[[Colette Savary-Davaine]]||[[Élisabeth Camus]]
|-
|[[1979]]|| [[Neufchâtel-en-Saosnois]]||[[Jeannie Longo]]||[[Élisabeth Camus]]||[[Nathalie Diart]]
|-
|[[1980]]|| [[Villié-Morgon]]||[[Jeannie Longo]]||[[Chantal Fortier]]||[[Sylvie Brémond]]
|-
|[[1981]]|| [[Charleville-Mézières]]||[[Jeannie Longo]]||[[Fabienne Amedro]]||[[Valérie Simonnet]]
|-
|[[1982]]|| [[Bressuire]]||[[Jeannie Longo]]||[[Fabienne Amedro]]||[[Chantal Pouline]]
|-
|[[1983]]|| [[Wintzenheim]]||[[Jeannie Longo]]||[[Corinne Crunelle]]||[[Dominique Damiani]]
|-
|[[1984]]|| [[Berck (Pas-de-Calais)|Berck]]||[[Jeannie Longo]]||[[Isabelle Nicoloso]]||[[Nathalie Pelletier]]
|-
|[[1985]]|| [[Chailley]]||[[Jeannie Longo]]||[[Valérie Simonnet]]||[[Dominique Damiani]]
|-
|[[1986]]|| [[Châteaulin]]||[[Jeannie Longo-Ciprelli]]||[[Valérie Simonnet]]||[[Isabelle Nicoloso|Isabelle Nicoloso-Verger]]
|-
|[[1987]]|| [[Lugny (Saône-et-Loire)|Lugny]]||[[Jeannie Longo-Ciprelli]]||[[Valérie Simonnet]]||[[Martine L'Haridon]]
|-
|[[1988]]|| [[Saint-Étienne]]||[[Jeannie Longo-Ciprelli]]||[[Valérie Simonnet]]||[[Dominique Damiani]]
|-
|[[1989]]|| [[Montluçon]]||[[Jeannie Longo-Ciprelli]]||[[Valérie Simonnet]]||[[Sandrine Lestrade]]
|-
|[[1990]]|| [[Saint-Saulge]]||[[Catherine Marsal]]||[[Elisabeth Mahaut]]||[[Barbara Aulnette]]
|-
|[[1991]]|| [[Saint-Saulge]]||[[Marion Clignet]]||[[Nathalie Cantet]]||[[Sandrine Lestrade]]
|-
|[[1992]]|| [[Avize]]||[[Jeannie Longo-Ciprelli]]||[[Marion Clignet]]||[[Laurence Leboucher]]
|-
|[[1993]]|| [[Châtellerault]]||[[Marion Clignet]]||[[Catherine Marsal]]||[[Corinne Legal]]
|-
|[[1994]]|| [[Fontenay-le-Comte]]||[[Chantal Gorostegui]]||[[Jocelyne Hugi-Messori]]||[[Catherine Marsal]]
|-
|[[1995]]|| [[La Cluse-et-Mijoux]]||[[Jeannie Longo-Ciprelli]]||[[Catherine Marsal]]||[[Élisabeth Chevanne-Brunel]]
|-
|[[1996]]|| [[Castres]]||[[Catherine Marsal]]||[[Jeannie Longo-Ciprelli]]||[[Jocelyne Hugi-Messori]]
|-
|[[1997]]|| [[Montlhéry]]||[[Sylvie Riedle]]||[[Emmanuelle Farcy]]||[[Catherine Marsal]]
|-
|[[1998]]|| [[Clermont-Ferrand]]||[[Jeannie Longo-Ciprelli]]||[[Séverine Desbouys]]||[[Fany Lecourtois]]
|-
|[[1999]]|| [[Clermont-Ferrand]]||[[Jeannie Longo-Ciprelli]]||[[Géraldine Jehl-Loewenguth]]||[[Séverine Desbouys]]
|-
|[[2000]]|| [[Le Poiré-sur-Vie]]||[[Jeannie Longo-Ciprelli]]||[[Catherine Marsal]]||[[Magali Le Floc'h]]
|-
|[[2001]]|| [[Argenton-sur-Creuse]]||[[Jeannie Longo-Ciprelli]]||[[Sonia Huguet]]||[[Catherine Marsal]]
|-
|[[2002]] ||[[Briançon]]||[[Magali Le Floc'h]]||[[Edwige Pitel]]||[[Béatrice Thomas]]
|-
|[[2003]]|| [[Plumelec]]||[[Sonia Huguet]]||[[Maryline Salvetat]]||[[Delphine Guille]]
|-
|[[2004]]|| [[Pont-du-Fossé]]||[[Jeannie Longo-Ciprelli]]||[[Élisabeth Chevanne-Brunel]]||[[Sandrine Marcuz-Moreau]]
|-
|[[2005]]|| [[Boulogne-sur-Mer]]||[[Magali Le Floc'h]]||[[Sandrine Marcuz-Moreau]]||[[Karine Gautard-Roussel]]
|-
|[[2006]]|| [[Chantonnay]]||[[Jeannie Longo-Ciprelli]]||[[Béatrice Thomas]]||[[Élodie Touffet]]
|-
|[[2007]]|| [[Aurillac]]||[[Edwige Pitel]]||[[Jeannie Longo-Ciprelli]]||[[Marina Jaunatre]]
|-
|[[2008]]|| [[Semur-en-Auxois]]||[[Jeannie Longo]]||[[Christel Ferrier-Bruneau]]||[[Edwige Pitel]]
|-
|[[2009]]|| [[Saint-Brieuc]]||[[Christel Ferrier-Bruneau]]||[[Marina Jaunatre]]|| [[Jeannie Longo]]
|-
|[[2010]]|| [[Chantonnay]]||[[Mélodie Lesueur]]||[[Amélie Rivat]]||[[Jeannie Longo]]
|-
|[[2011]]|| [[Boulogne-sur-Mer]]||[[Christel Ferrier-Bruneau]]||[[Jeannie Longo]]||[[Magdalena de Saint-Jean]]
|-
|[[2012]] || [[Saint-Amand-les-Eaux]] || [[Marion Rousse]] || [[Julie Krasniak]] || [[Fanny Riberot]]
|-
|[[2013]] || [[Communauté de communes de Plabennec et des Abers|Pays des Abers]] || [[Élise Delzenne ]] || [[Amélie Rivat]] || [[Aude Biannic]]
|-
|[[2014]] || [[Futuroscope]] || [[Pauline Ferrand-Prévot]] || [[Mélodie Lesueur]] || [[Fanny Riberot]]
|-
|[[2015]] || [[Chantonnay]] || [[Pauline Ferrand-Prévot]] || [[Audrey Cordon]] || [[Amélie Rivat]]
|-
|[[2016]] || [[Vesoul]] || [[Edwige Pitel]] || [[Marjolaine Bazin]] || [[Audrey Cordon]]
|-
|[[2017]] || [[Saint-Omer (Pas-de-Calais)|Saint Omer]] || [[Charlotte Bravard]] || [[Amélie Rivat]] || [[Marjolaine Bazin]]
|}"""

    
    championshipID='Q30332844'
    
    #inputstr=input()
    tableOfwinner=palmaresParsing(inputstr)
    print(tableOfwinner)
    numberofabsentriders, tableOfwinnerOut=wikidataelementAnalyser(pywikibot,site,tableOfwinner)
   
    if numberofabsentriders==0:
        palmaresFilling(pywikibot,site,repo,tableOfwinner,championshipID)
    
    
def palmaresParsing(inputstr):
    #parsing of the raw input
    tableofRow=inputstr.split("|-")
    ColumnOfwinner=2
    tableOfwinner = [[0 for x in range(4)] for y in range(len(tableofRow)-1)] 
    
    for ii in range(0,len(tableofRow)-1):#range(len(tableofRow))
        tableofCell={}
        tableofCell=tableofRow[1+ii].split("||")
        #get the year
        tempforyear=tableofCell[0].split("|")
        linksplit1=tempforyear[1].split("[[")  
        link=linksplit1[1].split("]]") 
        tableOfwinner[ii][0]=int(link[0])
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
    
    for ii in range(len(tableOfwinner)):
        for jj in range(1,4):
            Idtemp=searchItem(pywikibot,site,tableOfwinner[ii][jj])
            if (Idtemp==u'Q0'):  #no previous or several
                print(tableOfwinner[ii][jj]+ ' not found')
                counter=counter+1
            elif (Idtemp==u'Q1'):
                print(tableOfwinner[ii][jj]+ ' found several times')
                #list of exceptions
                if tableOfwinner[ii][jj]=='JG':
                    tableOfwinnerOut[ii][jj]='Q112'
                
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
   
   Name=u"Béatrice Vachet"
   mydescription['fr']=u'Coureuse cycliste française'
   label['fr']=Name
   
  ## kkinit=teamCIOsearch(teamTableFemmes, u'NAM')
   CountryCIO=u'FRA'
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
  

if __name__ == '__main__':
    #palmaresImporter()
    riderFastInit()
    
    
    
    