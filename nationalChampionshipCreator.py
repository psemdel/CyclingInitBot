# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:30:20 2018

@author: maxime delzenne
"""
from CyclingInitBotLow import *


def nationalChampionshipBasic(pywikibot,repo,item,siteIn,Master,Year,country_code,Idpresent): 
  
    addValue(pywikibot,repo,item,31,Master,u'Nature') 
    Idchamp=searchItem(pywikibot,siteIn,u'Championnats nationaux de cyclisme sur route en '+str(Year))
    if (Idchamp==u'Q0')or(Idchamp==u'Q1'):  #no previous or several
           a=1
    else:
        addValue(pywikibot,repo,item,361,noQ(Idchamp),u'part of') 
        itemMaster= pywikibot.ItemPage(repo, Idchamp)
        itemMaster.get()
        addMultipleValue(pywikibot,repo,itemMaster,527,noQ(Idpresent),u'link year',0)
        
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
    addValue(pywikibot,repo,item,17,country_code,u'country')   
    
def nationalChampionshipEnLigneBasic(pywikibot,repo,item,siteIn,Master,country_code,Year):
   addValue(pywikibot,repo,item,31,Master,u'Nature') 
   Addc=1
    
   listOfNature=item.claims.get(u'P31')
   itemToAdd=pywikibot.ItemPage(repo,u'Q22231119') #CN
   for ii in range(len(listOfNature)):
       if listOfNature[ii].getTarget()==itemToAdd: #Already there
            Addc=0
            print('Item already in the Master list')
    
   if Addc==1:  
       claim=pywikibot.Claim(repo, u'P31') 
       target = pywikibot.ItemPage(repo, u'Q22231119')
       claim.setTarget(target)
       item.addClaim(claim, summary=u'Adding CN') 
    
   addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
   addValue(pywikibot,repo,item,17,country_code,u'country')

   if(u'P585' in item.claims):
        a=1
   else:
        claim=  pywikibot.Claim(repo, u'P585') #date
        date=pywikibot.WbTime(site=siteIn,year=Year, precision='year') 
        claim.setTarget(date)    
        item.addClaim(claim, summary=u'Adding date')
        
def nationalChampionshipLabel(teamTable,kk,Year):
    #input
    country_fr =teamTable[kk][1]
    genre_fr =teamTable[kk][2]
        
    countryadj_en =teamTable[kk][6]
    
    #declaration
    mylabel={}
    label_part1_fr = u"Championnats"
    label_part2_fr = u"de cyclisme sur route"
    mylabel[u'fr']=label_part1_fr + " " + genre_fr + country_fr + " " + label_part2_fr + " "+ str(Year)

    label_part2_en = u"National Road Race Championships"
    mylabel[u'en']= str(Year) + " "+ countryadj_en + " "+ label_part2_en 
    return mylabel


def nationalChampionshipEnLigneLabel(teamTable,kk,Year, ManOrWoman):
    #input
    country_fr =teamTable[kk][1]
    genre_fr =teamTable[kk][2]
    
    if ManOrWoman==u'man':
        adj=u'masculine'
    else:
        adj=u'féminine'
        
    #declaration
    mylabel={}
    label_part1_fr = u"Course en ligne "+adj+" aux championnats"
    label_part2_fr = u"de cyclisme sur route"
    mylabel[u'fr']=label_part1_fr + " " + genre_fr +country_fr + " " + label_part2_fr + " "+ str(Year)
    return mylabel


def nationalChampionshipClmLabel(teamTable,kk,Year, ManOrWoman):
    #input
    country_fr =teamTable[kk][1]
    genre_fr =teamTable[kk][2]
    
    if ManOrWoman==u'man':
        adj=u'masculin'
    else:
        adj=u'féminin'
    
    #declaration
    mylabel={}
    label_part1_fr = u"Contre-la-montre "+adj+" aux championnats"
    label_part2_fr = u"de cyclisme sur route"
    mylabel[u'fr']=label_part1_fr + " " + genre_fr + country_fr + " " + label_part2_fr + " "+ str(Year)
    return mylabel

def NationalChampionshipCreator(pywikibot,site,repo,time,teamTable,endkk,ManOrWoman, option, startYear,EndYear,Country):
    kkinit=teamCIOsearch(teamTable,Country)
    
    if option=='clmoff':
        clm=0
    else:
        clm=1
        
    if ManOrWoman=='man':
        IndexRoadRace=12
        IndexClmRace=13
    else:
        IndexRoadRace=10
        IndexClmRace=11
        
    #print(kkinit)
    for kk in range(kkinit,endkk):  #endkk
    ##kk=kkinit
        ##if 1==1:
        group=teamTable[kk][8]
        if group==1:
            for ii in range( startYear,EndYear):
                Year=ii
                group=1
                #Create the championship
                mylabel={}
                mylabel=nationalChampionshipLabel(teamTable,kk,Year)
                #print(mylabel)
                Idpresent=searchItem(pywikibot,site,mylabel['fr'])
                if (Idpresent==u'Q0'):
                    print(mylabel['fr']+ ' created')
                        #Type code
                    Idpresent = create_item(pywikibot,site, mylabel)
                    
                elif (Idpresent==u'Q1'):
                    print(mylabel['fr']+' already present several times')
                else:    
                    print(mylabel['fr']+' already present')
            
                item =pywikibot.ItemPage(repo, Idpresent)
                item.get()
                nationalChampionshipBasic(pywikibot,repo,item,site,teamTable[kk][9],Year,teamTable[kk][3],Idpresent)
                
                #Search previous
                Yearprevious= Year-1
                mylabelprevious=nationalChampionshipLabel(teamTable,kk,Yearprevious)
                Idprevious=searchItem(pywikibot,site,mylabelprevious['fr'])
                if (Idprevious==u'Q0')or(Idprevious==u'Q1'):  #no previous or several
                   a=1
                else:
                    addValue(pywikibot,repo,item,155,noQ(Idprevious),u'link previous') 
                        #Link to the previous
                    itemPrevious=pywikibot.ItemPage(repo, Idprevious)
                    itemPrevious.get()
                    addValue(pywikibot,repo,itemPrevious,156,noQ(Idpresent),u'link next')
                         
                #Search next   
                Yearnext= Year+1
                mylabelnext=nationalChampionshipLabel(teamTable,kk,Yearnext)
                Idnext=searchItem(pywikibot,site,mylabelnext['fr'])
                
                time.sleep(1.0)
                if (Idnext==u'Q0')or(Idnext==u'Q1'):  #no next or 
                    a=1
                else:
                   addValue(pywikibot,repo,item,156,noQ(Idnext),u'link next')  
                   #Link to the next
                   itemNext=pywikibot.ItemPage(repo, Idnext)
                   itemNext.get()
                   addValue(pywikibot,repo,itemNext,155,noQ(Idpresent),u'link previous')
                 
                #Link the new item to the other    
                #link to master
                itemMaster= pywikibot.ItemPage(repo, u'Q'+ str(teamTable[kk][9]))
                itemMaster.get()
                addMultipleValue(pywikibot,repo,itemMaster,527,noQ(Idpresent),u'link year '+ str(Year),0) 
                
                #Create the road race
                time.sleep(1.0)
                mylabelEnLigne=nationalChampionshipEnLigneLabel(teamTable,kk,Year,ManOrWoman)
                IdEnLignepresent=searchItem(pywikibot,site,mylabelEnLigne['fr'])
                if (IdEnLignepresent==u'Q0'):
                    print(mylabelEnLigne['fr']+ ' created')
                        #Type code
                    IdEnLignepresent = create_item(pywikibot,site, mylabelEnLigne)
                
                elif (IdEnLignepresent==u'Q1'):
                    print(mylabelEnLigne['fr']+' already present several times')
                else:    
                    print(mylabelEnLigne['fr']+' already present')
            
                itemEnLigne =pywikibot.ItemPage(repo, IdEnLignepresent)
                itemEnLigne.get()
                nationalChampionshipEnLigneBasic(pywikibot,repo,itemEnLigne,site,teamTable[kk][IndexRoadRace],teamTable[kk][3],Year)

                #Link to previous
                mylabelEnLigneprevious=nationalChampionshipEnLigneLabel(teamTable,kk,Yearprevious,ManOrWoman)
              
                IdEnLigneprevious=searchItem(pywikibot,site,mylabelEnLigneprevious['fr'])
                if (IdEnLigneprevious==u'Q0')or(IdEnLigneprevious==u'Q1'):  #no previous or several
                   a=1
                else:
                    addValue(pywikibot,repo,itemEnLigne,155,noQ(IdEnLigneprevious),u'link previous') 
                        #Link to the previous
                    itemEnLignePrevious=pywikibot.ItemPage(repo, IdEnLigneprevious)
                    itemEnLignePrevious.get()
                    addValue(pywikibot,repo,itemEnLignePrevious,156,noQ(IdEnLignepresent),u'link next')
                
                #Link to next
                mylabelEnLignenext=nationalChampionshipEnLigneLabel(teamTable,kk,Yearnext,ManOrWoman)
                IdEnLignenext=searchItem(pywikibot,site,mylabelEnLignenext['fr'])
                 
                
                time.sleep(1.0)
                if (IdEnLignenext==u'Q0')or(IdEnLignenext==u'Q1'):  #no next or 
                    a=1
                else:
                   addValue(pywikibot,repo,itemEnLigne,156,noQ(IdEnLignenext),u'link next')  
                   #Link to the next
                   itemEnLigneNext=pywikibot.ItemPage(repo, IdEnLignenext)
                   itemEnLigneNext.get()
                   addValue(pywikibot,repo,itemEnLigneNext,155,noQ(IdEnLignepresent),u'link previous')
                
                #Link to master (En ligne...)
                
                itemEnLigneMaster= pywikibot.ItemPage(repo, u'Q'+ str(teamTable[kk][IndexRoadRace]))
                itemEnLigneMaster.get()
                addMultipleValue(pywikibot,repo,itemEnLigneMaster,527,noQ(IdEnLignepresent),u'link year '+ str(Year),0)
                
                #Link to master (championship...)
                addMultipleValue(pywikibot,repo,item,527,noQ(IdEnLignepresent),u'link course en ligne',0)
                
                 #Create the Clm
                time.sleep(1.0)
                if clm==1:
                    mylabelClm=nationalChampionshipClmLabel(teamTable,kk,Year,ManOrWoman)
                    IdClmpresent=searchItem(pywikibot,site,mylabelClm['fr'])
                    if (IdClmpresent==u'Q0'):
                        print(mylabelClm['fr']+' created')
                            #Type code
                        IdClmpresent = create_item(pywikibot,site, mylabelClm)
                    
                    elif (IdClmpresent==u'Q1'):
                        print(mylabelClm['fr']+' already present several times')
                    else:    
                        print(mylabelClm['fr']+' already present')
                
                    itemClm =pywikibot.ItemPage(repo, IdClmpresent)
                    itemClm.get()
                    #Same function as EnLigne
                    nationalChampionshipEnLigneBasic(pywikibot,repo,itemClm,site,teamTable[kk][IndexClmRace],teamTable[kk][3],Year)
                   
                    #Link to previous
                    mylabelClmprevious=nationalChampionshipClmLabel(teamTable,kk,Yearprevious,ManOrWoman)
                    IdClmprevious=searchItem(pywikibot,site,mylabelClmprevious['fr'])
                    if (IdClmprevious==u'Q0')or(IdClmprevious==u'Q1'):  #no previous or several
                       a=1
                    else:
                        addValue(pywikibot,repo,itemClm,155,noQ(IdClmprevious),u'link previous') 
                            #Link to the previous
                        itemClmPrevious=pywikibot.ItemPage(repo, IdClmprevious)
                        itemClmPrevious.get()
                        addValue(pywikibot,repo,itemClmPrevious,156,noQ(IdClmpresent),u'link next')
                    
                    #Link to next
                    mylabelClmnext=nationalChampionshipClmLabel(teamTable,kk,Yearnext,ManOrWoman)
                    IdClmnext=searchItem(pywikibot,site,mylabelClmnext['fr'])
                    
                    time.sleep(1.0)
                    if (IdClmnext==u'Q0')or(IdClmnext==u'Q1'):  #no next or 
                        a=1
                    else:
                       addValue(pywikibot,repo,itemClm,156,noQ(IdClmnext),u'link next')  
                       #Link to the next
                       itemClmNext=pywikibot.ItemPage(repo, IdClmnext)
                       itemClmNext.get()
                       addValue(pywikibot,repo,itemClmNext,155,noQ(IdClmpresent),u'link previous')
                    
                    #Link to master (clm...)
                    itemClmMaster= pywikibot.ItemPage(repo, u'Q'+ str(teamTable[kk][IndexClmRace]))
                    itemClmMaster.get()
                    addMultipleValue(pywikibot,repo,itemClmMaster,527,noQ(IdClmpresent),u'link year '+ str(Year),0)
                     
                    #Link to master (championship...)
                    addMultipleValue(pywikibot,repo,item,527,noQ(IdClmpresent),u'link clm',0)


if __name__ == '__main__':
   #from nationTeamTable import nationalTeamTable 
   [teamTable, endkk]=nationalTeamTable()
   print(teamTable[32][12])

   