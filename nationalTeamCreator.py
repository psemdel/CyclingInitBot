# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: maxime delzenne
"""

import cyclingInitBotLow

#==Get==
def nationalTeamAlias(teamTable,kk, Year):
    #input
    alias={}
    alias['fr'] =[teamTable[kk][7]+ u" " + str(Year)]
    return alias

#==High level functions==
def nationalTeamBasic(pywikibot,repo,item,siteIn,country_name,country_code, Year,Master,CIO):
#No need for the table here    
    addValue(pywikibot,repo,item,31,23726798,u'Nature') 
    addValue(pywikibot,repo,item,1998,CIO,u'CIO code') 
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
        officialname=pywikibot.WbMonolingualText(text=country_name, language='fr')
        claim.setTarget(officialname)    
        item.addClaim(claim, summary=u'Adding official name') 
        
def nationalTeamIntro(item,teamTable,kk,Year):
    item.get()
    if get_description('fr',item)=='':
       mydescription=nationalTeamDescription(teamTable,kk,Year)
       item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
       
    if get_alias('fr',item)=='':
       myalias=nationalTeamAlias(teamTable,kk,Year)
       item.editAliases(aliases=myalias, summary=u'Setting Aliases') #Not working yet
       
       
def nationalTeamLabel(teamTable,kk,Year):
    #input
    country_fr =teamTable[kk][1]
    genre_fr =teamTable[kk][2]
        
    countryadj_en =teamTable[kk][6]
    
    #declaration
    mylabel={}
    
    #Teamlabel_fr
    label_part1_fr = u"Équipe"
    label_part2_fr = u"féminine de cyclisme sur route"
    mylabel[u'fr']=label_part1_fr + " " + genre_fr + country_fr + " " + label_part2_fr + " "+ str(Year)
     
    #Teamlabel_en
    label_part2_en = u"women's national road cycling team"
    mylabel[u'en']=countryadj_en + " "+ label_part2_en + " "+ str(Year)
    
    return mylabel

def nationalTeamDescription(teamTable,kk,Year):
    #input
    country_fr =teamTable[kk][1]
    genre_fr =teamTable[kk][2]
    
    #declaration
    mydescription={}
    
    #mydescription_fr
    description_part1_fr = u'Saison'
    description_part2_fr = u"de l'équipe"
    description_part3_fr = u"de cyclisme sur route"
    mydescription[u'fr']=description_part1_fr + " "+  str(Year)+ " "+description_part2_fr+" " +genre_fr + country_fr +" "+description_part3_fr  
    
    return mydescription
 

def Nationalteamcreator(pywikibot,site,repo,time,teamTableFemmes,endkk):
    kkinit=teamCIOsearch(teamTableFemmes, u'USA')
    print(kkinit)
    for kk in range(kkinit,endkk):  #endkk
        group=teamTableFemmes[kk][8]
        if group==1:
            for ii in range(1990,2019):
                Year=ii
                 
                mylabel={}
                mylabel=nationalTeamLabel(teamTableFemmes,kk,Year)
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
                nationalTeamIntro(item,teamTableFemmes,kk,Year)
                time.sleep(1.0)
                nationalTeamBasic(pywikibot,repo,item,site,teamTableFemmes[kk][1],teamTableFemmes[kk][3],Year,teamTableFemmes[kk][4],teamTableFemmes[kk][7])
                time.sleep(1.0)
                #Link the other to the new item
                
                #Search previous
                Yearprevious= Year-1
                mylabelprevious=nationalTeamLabel(teamTableFemmes,kk,Yearprevious)
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
                mylabelnext=nationalTeamLabel(teamTableFemmes,kk,Yearnext)
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
                itemMaster= pywikibot.ItemPage(repo, u'Q'+ str(teamTableFemmes[kk][4]))
                itemMaster.get()
                addComprend(pywikibot,repo,itemMaster,noQ(Idpresent),u'link year '+ str(Year)) 

