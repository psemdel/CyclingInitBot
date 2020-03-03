#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:34:29 2019

@author: maxime
"""
from cycling_init_bot_low import * 
from get_rider_tricot import *

def startlist_importer (pywikibot,site,repo, prologue_or_final, id_race, time_of_race,chrono,test,nation_table):
     #0=prologue, 1=final, 2=one day race
    verbose=False
    
    result_dic={
    'rank':[-1, 0, ''],
    'last name':[-1, 1,''],
    'first name':[-1, 2,''],
    'name':[-1, 3,''],
    'result':[-1, 4,'time'],  #startlist only with time
    'points':[-1, 5, 'points'],
    'team code':[-1, 7, ''],
    'ecart':[1,6,'time'],  #always created
    'bib':[-1,8,''] #dossard
    }
    
    result_table, row_count, ecart=table_reader('Results', result_dic,0,True)
    #Sort by dossard
    result_table=sorted(result_table, key=lambda tup: int(tup[8]))
    print('table read and sorted')
    
    list_of_cyclists=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, nosortkey=True)
    row_count=len(list_of_cyclists)
    
    if not test:
         item =pywikibot.ItemPage(repo, id_race)
         item.get() 
         already_list=False
         year=time_of_race.year
         if(u'P'+str('710') in item.claims) and prologue_or_final==0:  #already there do nothing
            print(u'List of starters already there')
         else:   
            #check national team
            national_team_detected=False
            all_same_team=True
            for ii in range(row_count):
                if result_table[ii][result_dic['bib'][1]]%10==1:
                    #insert last team
                    print('national_team_detected')
                    print(national_team_detected)
                    print(all_same_team)
                    
                    if national_team_detected and all_same_team<0:
                        print(u'national team detected '+IDtoCIOsearch(nation_table, noQ(national_team_nation)))
                        #insert the team
                        for jj in range(national_team_begin,ii):
                            national_team_code=IDtoCIOsearch(nation_table, noQ(national_team_nation)) + " " + str(year)
                            id_national_team=search_item(pywikibot,site,national_team_code)
                            if id_national_team!=u'Q0' and id_national_team!=u'Q1':
                                list_of_cyclists[jj].team=id_national_team
                            #result_table[jj][result_dic['team code'][1]]
                    #re-init the variable
                    national_team_detected=True
                    national_team_begin=ii
                    national_team_nation=u'reset'
                    proteam=u'reset'
                    all_same_team=1 #if all_same_team is 1 then it is probably not a national team
                   
                if national_team_detected and prologue_or_final!=1: 
                    item_rider=list_of_cyclists[ii].item
                    id_rider=list_of_cyclists[ii].id_item
                    #get nationality
                    if (u'P27' in item_rider.claims):
                        nationality=item_rider.claims.get(u'P27')
                        list_of_cyclists[ii].nationality=nationality
                        if national_team_nation==u'reset':
                            national_team_nation=nationality[0].getTarget().getID()
                        else:
                            if national_team_nation!=nationality[0].getTarget().getID(): 
                                #not the same nation --> not a national team
                                print('different nation')
                                national_team_detected=False 
                    team=get_present_team(pywikibot,site,repo,id_rider,time_of_race)
                    if proteam==u'reset':
                        proteam=team
                    else:
                        if team!='Q1' and proteam!=team: 
                            all_same_team=all_same_team-1
                            print('all_same_team')
                            print(all_same_team)
            
            #last team
            if national_team_detected and all_same_team<0:
                 print(u'national team detected '+IDtoCIOsearch(nation_table, noQ(national_team_nation)))
                        #insert the team
                 for jj in range(national_team_begin,row_count):
                    national_team_code=IDtoCIOsearch(nation_table, noQ(national_team_nation)) + " " + str(year)
                    id_national_team=search_item(pywikibot,site,national_team_code)
                    if id_national_team!=u'Q0' and id_national_team!=u'Q1':
                        list_of_cyclists[jj].team=id_national_team                        
            if (u'P'+str('710') in item.claims):
                already_list=True
                list_of_comprend=item.claims.get(u'P'+str(710))
            if prologue_or_final==1:
                list_of_comprendbool=[False for x in range(len(list_of_comprend))] 
                
            qualifier_DNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
            qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
            qualifier_dossard=pywikibot.page.Claim(site, 'P1618', is_qualifier=True)
            qualifier_team=pywikibot.page.Claim(site, 'P54', is_qualifier=True)
            target_DNFqual = pywikibot.ItemPage(repo, u'Q1210380')
            
            for ii in range(row_count):
                if list_of_cyclists[ii].id_item!='Q0' and list_of_cyclists[ii].id_item!='Q1':
                    this_rider=list_of_cyclists[ii]
                    item_rider=this_rider.item 
                    #look for it
                    Addc=-1
                    if already_list:
                        for jj in range(len(list_of_comprend)):
                           if list_of_comprend[jj].getTarget()==item_rider: #Already there
                                Addc=jj
                                if prologue_or_final==1:
                                    list_of_comprendbool[jj]=True
                    if Addc==-1:  ##create the rider
                        if prologue_or_final==1:
                            print('rider not found'+str(id_rider))
                        claim=pywikibot.Claim(repo, u'P'+str('710'))  #reinit everytime
                        claim.setTarget(item_rider)
                        item.addClaim(claim, summary=u'Adding starterlist')
                  
                        qualifier_dossard.setTarget(str(this_rider.dossard))
                        claim.addQualifier(qualifier_dossard)
                        if this_rider.team!='': #national team
                            target_qualifier = pywikibot.ItemPage(repo, this_rider.team)
                            qualifier_team.setTarget(target_qualifier)
                            claim.addQualifier(qualifier_team)
                        if prologue_or_final==1 or prologue_or_final==2:
                           if this_rider.rank==0: #no ranking
                               qualifier_DNF.setTarget(target_DNFqual)
                               claim.addQualifier(qualifier_DNF)
                           else:
                               target_qualifier =  pywikibot.WbQuantity(amount=this_rider.rank, site=repo)
                               qualifier_rank.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_rank)
                        get_rider_tricot(pywikibot,site,repo,this_rider.id_item,time_of_race,claim,chrono)
                    else: ##rider already there
                        if prologue_or_final==1 or prologue_or_final==2:
                           if this_rider.rank==0: #no ranking
                               qualnotfound=True
                               for qual in list_of_comprend[Addc].qualifiers.get('P1534', []):
                                   qualnotfound=False
                               if qualnotfound:
                                   qualifier_DNF.setTarget(target_DNFqual)
                                  # list_of_comprend[Addc].setTarget(item_rider) 
                                   list_of_comprend[Addc].addQualifier(qualifier_DNF)
                           else:
                               qualnotfound=True
                               for qual in list_of_comprend[Addc].qualifiers.get('P1352', []):
                                   qualnotfound=False
                               if qualnotfound:
                                   target_qualifier =   pywikibot.WbQuantity(amount=this_rider.rank, site=repo)
                                   qualifier_rank.setTarget(target_qualifier)
                                   #list_of_comprend[Addc].setTarget(target) 
                                   list_of_comprend[Addc].addQualifier(qualifier_rank)
            #all riders are classified, assumption the other are DNF
            if prologue_or_final==1:
                for kk in range(len(list_of_comprend)):
                    if list_of_comprendbool[kk]==False: ##rider not found in this result sheet
                         #list_of_comprend[kk].setTarget(item_rider) 
                         qualifier_DNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)#useful?
                         qualnotfound=True
                         for qual in list_of_comprend[kk].qualifiers.get('P1534', []):
                             qualnotfound=False
                         if qualnotfound:
                             qualifier_DNF.setTarget(target_DNFqual)
                             list_of_comprend[kk].addQualifier(qualifier_DNF)