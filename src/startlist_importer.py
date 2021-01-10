#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:34:29 2019

@author: maxime
"""
from .cycling_init_bot_low import (table_reader, cyclists_table_reader, 
IDtoCIOsearch, search_item, get_present_team, noQ, get_label, get_items,
get_nationality)                               
from . import get_rider_tricot 
from .bot_log import Log


def find_sortkey(label, words):
    for word in words:
        if label.find(word)!=-1:
            return True
    return False

def search_item_national_team(pywikibot, site, repo, search_string, dic,dic_neg,**kwargs): #For Team and rider
    from pywikibot.data import api
    
    wikidata_entries = get_items(api, site, search_string)
    if(wikidata_entries['search'] == []):
        # no result
        return u'Q0'
    elif len(wikidata_entries['search'])==1:
        #search by alias has no search-continue
        wikidataSearchresult = wikidata_entries['search']
        wikidataSearchresult1 = wikidataSearchresult[0]
        id_national_team = wikidataSearchresult1['id']
        item = pywikibot.ItemPage(repo, id_national_team)
        item.get()
        this_label=get_label('fr', item)
        if find_sortkey(this_label, dic) and not find_sortkey(this_label, dic_neg):
            return id_national_team 
        else:
            return u'Q0'
    else:
        all_results = wikidata_entries['search']
        for result in all_results:
            id_national_team=result['id']   
            item = pywikibot.ItemPage(repo, id_national_team)
            item.get()
            this_label=get_label('fr', item)
           
            if find_sortkey(this_label, dic) and not find_sortkey(this_label, dic_neg):
                return id_national_team 
        return u'Q0' 


def get_national_team_id(pywikibot,site, repo,nation_table, country_id, year, man_or_woman):
    if man_or_woman==u'woman':
        dic=['féminine de cyclisme']
        dic_neg=[]
    elif man_or_woman=='manU':
        dic=['espoirs de cyclisme'] 
        dic_neg=[]
    elif  man_or_woman=='man':
        dic=['de cyclisme']
        dic_neg=['féminine de cyclisme','espoirs de cyclisme']
    else:
        return 'Q0'
    
    national_team_code=IDtoCIOsearch(nation_table, noQ(country_id)) + " " + str(year)
    return search_item_national_team(pywikibot,site,repo, national_team_code, dic, dic_neg)

def find_national_team(pywikibot,site,repo,list_of_cyclists, 
                       result_table, result_dic, row_count, nation_table, 
                       force_nation_team, year, log, man_or_woman,
                       time_of_race):
    
    verbose=False
    national_team_detected=False #otherwise insert nothing during first loop
    all_same_team=1
    national_team_nation=u'reset'
    national_team_begin=0
    for ii in range(row_count):
        #check national team
        if not force_nation_team:
            if result_table[ii][result_dic['bib'][1]]%10==1:
                        #insert last team
                if (national_team_detected and all_same_team<0):
                    print(u'national team detected '+IDtoCIOsearch(nation_table, noQ(national_team_nation)))
                    #insert the team
                    for jj in range(national_team_begin,ii):
                        id_national_team=get_national_team_id(pywikibot,site, repo,nation_table, national_team_nation, year, man_or_woman) 
                        if id_national_team!=u'Q0':
                            list_of_cyclists[jj].team=id_national_team
                            list_of_cyclists[jj].national_team=True #for testing
                #re-init the variable
                national_team_detected=True
                national_team_begin=ii
                national_team_nation=u'reset'
                proteam=u'reset'
                all_same_team=1 #if all_same_team is 1 then it is probably not a national team
               
            if national_team_detected: 
                
                item_rider=list_of_cyclists[ii].item
                id_rider=list_of_cyclists[ii].id_item
                if verbose:
                    print(list_of_cyclists[ii].dossard)
                #get nationality
                nationality=get_nationality(pywikibot, repo, site, id_rider, time_of_race)    
                if nationality !="Q0":
                    if verbose:
                        print("nationality: "+ nationality)
                    list_of_cyclists[ii].nationality=nationality   
                    if national_team_nation==u'reset':
                        national_team_nation=nationality   
                    else:
                        if national_team_nation!=nationality   : 
                            #not the same nation --> not a national team
                            if verbose:
                                print("different nation")
                            national_team_detected=False 
                team=get_present_team(pywikibot,site,repo,id_rider,time_of_race)
                if verbose:
                    print("team: "+ team)
                if proteam==u'reset':
                    if team!="Q1":
                        proteam=team
                else:
                    if team!='Q1' and proteam!=team: 
                        all_same_team=all_same_team-1
                    elif team=='Q1':
                        all_same_team=all_same_team-1
            #last team
        else: #force_nation_team, then only look at nation value
            item_rider=list_of_cyclists[ii].item
            id_rider=list_of_cyclists[ii].id_item
            nationality=get_nationality(pywikibot, repo, site, id_rider, time_of_race)    
            national_team_nation=nationality
            id_national_team=get_national_team_id(pywikibot,site, repo,nation_table, national_team_nation, year, man_or_woman) 
            if id_national_team!=u'Q0':
                list_of_cyclists[ii].team=id_national_team
                list_of_cyclists[ii].national_team=True #for testing

     
    if not force_nation_team and national_team_detected and all_same_team<0:
         print("last")
         print(u'national team detected '+IDtoCIOsearch(nation_table, noQ(national_team_nation)))
                #insert the team
         for jj in range(national_team_begin,row_count):
            id_national_team=get_national_team_id(pywikibot,site, repo,nation_table, national_team_nation, year, man_or_woman) 
            if id_national_team!=u'Q0':
                list_of_cyclists[jj].team=id_national_team   
                list_of_cyclists[jj].national_team=True #for testing

    return list_of_cyclists, log          
                       
def f(pywikibot,site,repo, prologue_or_final, id_race, 
      time_of_race,chrono,test,nation_table,man_or_woman, force_nation_team,**kwargs):
     #0=prologue, 1=final, 2=one day 
    try:
        verbose=False
        log=Log()
        
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
        
        file=kwargs.get('file','Results')
        result_table, row_count, ecart=table_reader(file, result_dic,0,True)
        #Sort by dossard
        result_table=sorted(result_table, key=lambda tup: int(tup[8]))
        log.concat('table read and sorted')
        
        list_of_cyclists, all_riders_found, cycling_log, list_of_teams, all_teams_found=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, nosortkey=True)
        log.concat(cycling_log)
        if not all_riders_found:
            log.concat(u'Not all riders found, request stopped')
            return 1, log
        else:
            log.concat(u'all riders found, ok')
        row_count=len(list_of_cyclists)
        
        if not test:
             item =pywikibot.ItemPage(repo, id_race)
             item.get() 
             already_list=False
             year=time_of_race.year
             if((u'P'+str('710') in item.claims) 
                and (prologue_or_final==0 or prologue_or_final==2)):  #already there do nothing
                 log.concat("warning ")
                 log.concat(u'List of starters already there')
             if True:   
                
                if prologue_or_final!=1: #for prologue_or_final==1 no detection
                    log.concat(u'looking for national team')
                    list_of_cyclists, log=find_national_team(pywikibot,site,
                                                        repo,
                                                        list_of_cyclists,
                                                        result_table, 
                                                        result_dic,
                                                        row_count,
                                                        nation_table, 
                                                        force_nation_team,
                                                        year, 
                                                        log,
                                                        man_or_woman,
                                                        time_of_race)
                             
                if (u'P'+str('710') in item.claims):
                    already_list=True
                    list_of_comprend=item.claims.get(u'P710')
                if prologue_or_final==1:
                    list_of_comprendbool=[False for x in range(len(list_of_comprend))] 
                    
                target_DNFqual = pywikibot.ItemPage(repo, u'Q1210380')
                
                log.concat(u'inserting start list')
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
                                log.concat('rider not found'+str(list_of_cyclists[ii].id_item))
                            claim=pywikibot.Claim(repo, u'P710')  #reinit everytime
                            claim.setTarget(item_rider)
                            item.addClaim(claim, summary=u'Adding starterlist')
                            qualifier_dossard=pywikibot.page.Claim(site, 'P1618', is_qualifier=True)
                            qualifier_dossard.setTarget(str(this_rider.dossard))
                            claim.addQualifier(qualifier_dossard)
                            if this_rider.team!='': #national team
                                target_qualifier = pywikibot.ItemPage(repo, this_rider.team)
                                qualifier_team=pywikibot.page.Claim(site, 'P54', is_qualifier=True)
                                qualifier_team.setTarget(target_qualifier)
                                claim.addQualifier(qualifier_team)
                            if prologue_or_final==1 or prologue_or_final==2:
                               if this_rider.rank==0: #no ranking
                                   qualifier_DNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                                   qualifier_DNF.setTarget(target_DNFqual)
                                   claim.addQualifier(qualifier_DNF)
                               else:
                                   target_qualifier =  pywikibot.WbQuantity(amount=this_rider.rank, site=repo)
                                   qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                                   qualifier_rank.setTarget(target_qualifier)
                                   claim.addQualifier(qualifier_rank)
                            if not force_nation_team: #when only national team, no national tricot
                                get_rider_tricot.f(pywikibot,site,repo,this_rider.id_item,time_of_race,claim,chrono,man_or_woman)
                        else: ##rider already there
                            if prologue_or_final==1 or prologue_or_final==2:
                               if this_rider.rank==0: #no ranking
                                   qualnotfound=True
                                   for qual in list_of_comprend[Addc].qualifiers.get('P1534', []):
                                       qualnotfound=False
                                   if qualnotfound:
                                       qualifier_DNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                                       qualifier_DNF.setTarget(target_DNFqual)
                                      # list_of_comprend[Addc].setTarget(item_rider) 
                                       list_of_comprend[Addc].addQualifier(qualifier_DNF)
                               else:
                                   qualnotfound=True
                                   for qual in list_of_comprend[Addc].qualifiers.get('P1352', []):
                                       qualnotfound=False
                                   if qualnotfound:
                                       target_qualifier =   pywikibot.WbQuantity(amount=this_rider.rank, site=repo)
                                       qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
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
        return 0, log                          
    except Exception as msg:
            print(msg)
            log.concat("General Error in classification_importer")
            return 10, log     
