# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: psemdel
"""
from CyclingInitBotLow import *


#==Get==
def proTeamAlias(teamTable,kk, Year):
    #input
    alias={}
    alias['fr'] =[teamTable[kk][4]+ u" " + str(Year)] #UCI code + Year
    return alias

#==High level functions==
def proTeamBasic(pywikibot,repo,item,siteIn,team_name,country_code, Year,Master,UCI,proamateur):
#No need for the table here 
    
    if proamateur==1:
        addValue(pywikibot,repo,item,31,2466826,u'Nature') 
        addValue(pywikibot,repo,item,1998,UCI,u'UCI code') 
    else:
        addValue(pywikibot,repo,item,31,26849121,u'Nature')
    addMultipleValue(pywikibot,repo,item,31,53534649,u'Season',0)  
    addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
   
    addValue(pywikibot,repo,item,17,country_code,u'country')
    addValue(pywikibot,repo,item,361,Master,u'part of')
    
    if(u'P580' in item.claims):
        a=1
    else:
        claim=  pywikibot.Claim(repo, u'P580') #date de début
        startdate=pywikibot.WbTime(site=siteIn,year=Year, month=1, day=1, precision='day') 
        claim.setTarget(startdate)
        item.addClaim(claim, summary=u'Adding starting date')  
    
    if(u'P582' in item.claims):
        a=1
    else:
        claim=  pywikibot.Claim(repo, u'P582') #date de fin
        enddate=pywikibot.WbTime(site=siteIn,year=Year, month=12, day=31, precision='day') 
        claim.setTarget(enddate)    
        item.addClaim(claim, summary=u'Adding ending date') 
    
    if(u'P1448' in item.claims):
        a=1
    else:
        claim=  pywikibot.Claim(repo, u'P1448') #nom officiel
        officialname=pywikibot.WbMonolingualText(text=team_name, language='fr')
        claim.setTarget(officialname)    
        item.addClaim(claim, summary=u'Adding official name') 
        
def proTeamIntro(item,teamTable,kk,Year,proamateur):
    item.get()
    if get_description('fr',item)=='':
       mydescription=proTeamDescription(teamTable,kk,Year)
       item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
    
    if proamateur==1:     
        if get_alias('fr',item)=='':
           myalias=proTeamAlias(teamTable,kk,Year)
           item.editAliases(aliases=myalias, summary=u'Setting Aliases') 
       
       
def proTeamLabel(teamTable,kk,Year):
    #input
    name =teamTable[kk][1]
    #declaration
    mylabel={}
    
    #Teamlabel_fr
    mylabel[u'fr']=name + " "+ str(Year)
    mylabel[u'en']=mylabel[u'fr']
    #Teamlabel_en
    return mylabel

def proTeamDescription(teamTable,kk,Year):
    #input
    name =teamTable[kk][1]
    
    #declaration
    mydescription={}
    
    #mydescription_fr
    description_part1_fr = u'Saison'
    description_part2_fr = u"de l'équipe cycliste"
    mydescription[u'fr']=description_part1_fr + " "+  str(Year)+ " "+description_part2_fr+" " + name  
    return mydescription
 

def proteamcreator(pywikibot,site,repo,time,teamTableFemmes,nationalTeamTable,endkk,proamateur,countrytocreate):
    Year=2019
    kkinit=1
    for Year in range(2011,2020):
    #if kk==kkinit:
        for kk in range(kkinit,endkk):  #endkk
            if (proamateur==1 and teamTableFemmes[kk][6]==1) or (proamateur==0 and teamTableFemmes[kk][5]==1): #
            #teamTableFemmes[kk][5]==0 or    
                mylabel={}
                mylabel=proTeamLabel(teamTableFemmes,kk,Year)
                Idpresent=searchItem(pywikibot,site,mylabel['fr'])
                if (Idpresent==u'Q0'):
                    print(mylabel['fr']+' created')
                    #Type code
                    Idpresent = create_item(pywikibot,site, mylabel)
                    
                elif (Idpresent==u'Q1'):
                    print(mylabel['fr']+' already present several times')
                else:    
                    print(mylabel['fr']+' already present')
            
                item =pywikibot.ItemPage(repo, Idpresent)
                item.get()
                proTeamIntro(item,teamTableFemmes,kk,Year,proamateur)
                time.sleep(1.0)
                proTeamBasic(pywikibot,repo,item,site,teamTableFemmes[kk][1],CIOtoIDsearch(nationalTeamTable,teamTableFemmes[kk][3]),Year,teamTableFemmes[kk][2],teamTableFemmes[kk][4],proamateur)
                time.sleep(1.0)
                #Link the other to the new item
                
                #Search previous
                Yearprevious= Year-1
                mylabelprevious=proTeamLabel(teamTableFemmes,kk,Yearprevious)
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
                mylabelnext=proTeamLabel(teamTableFemmes,kk,Yearnext)
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
                itemMaster= pywikibot.ItemPage(repo, u'Q'+ str(teamTableFemmes[kk][2]))
                itemMaster.get()
                addMultipleValue(pywikibot,repo,itemMaster,527,noQ(Idpresent),u'link year '+ str(Year),0) 

if __name__ == '__main__':
   from ProTeamTable import AmateurTeamTable
   #[teamTableFemmes, endkk]=ProTeamTable()
   [teamTableFemmes, endkk]=AmateurTeamTable()
   #CIOtoIDsearch(nationalTeamTable,teamTableFemmes[kk][3])
   print(endkk)

   