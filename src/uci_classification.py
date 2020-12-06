#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
from .cycling_init_bot_low import (cyclists_table_reader, table_reader, search_team_by_code,
                                   search_team_by_code_man)
from .bot_log import Log

def f(
        pywikibot,
        site,
        repo,
        year,
        id_master_UCI,
        filename,
        cleaner,
        test,
        man_or_woman,
        UCIranking,
        bypass
        ):
 
    try:
        result_dic={
        'rank':[-1, 0, ''],
        'last name':[-1, 1,''],
        'first name':[-1, 2,''],
        'name':[-1, 3,''],
        'result':[-1, 4,'points'],
        'points':[-1, 5, 'points'],
        'team code':[-1, 7, ''],
        'ecart':[1,6,'time'],  #always created
        'bib':[-1,8,''] #dossard
        }
        verbose=False
        log=Log()
        
        result_table, row_count, ecart=table_reader(filename , result_dic,0,verbose)
        #post-processing
        for ii in range(row_count):
            if result_table[ii][result_dic['points'][1]]==0:
                result_table[ii][result_dic['points'][1]]=result_table[ii][result_dic['result'][1]]
            if result_table[ii][result_dic['team code'][1]]!=0 and result_table[ii][result_dic['team code'][1]]!="":
                result_table[ii][result_dic['team code'][1]]=result_table[ii][result_dic['team code'][1]]+" "+str(year)  

        log.concat('result_table created')
        search_team=UCIranking
        list_of_cyclists, all_riders_found, cycling_log, list_of_teams, all_teams_found=cyclists_table_reader(pywikibot, site, repo,result_table,
                                                                                                result_dic,
                                                                                                search_team=search_team,
                                                                                           man_or_woman=man_or_woman)

        if not all_riders_found and bypass==False:
            log.concat(u'Not all riders found, request stopped')
            return 1, log
        
        if (not all_teams_found and UCIranking) and bypass==False:
            log.concat(u'Not all teams found, request stopped')
            return 1, log           
        
        #fill the rider
       
        if not test:
            for ii in range(len(list_of_cyclists)):
                this_rider=list_of_cyclists[ii]
                if this_rider.id_item!='Q0' and this_rider.id_item!='Q1':
                    if cleaner!=True:
                        #action in the rider 
                        Addc=True
                        if(u'P1344' in this_rider.item.claims):
                             list_of_comprend = this_rider.item.claims.get(u'P1344')
                             item_to_add = pywikibot.ItemPage(repo, id_master_UCI)
                             for in_comprend in list_of_comprend:
                                if in_comprend.getTarget() == item_to_add:  # Already there
                                    Addc = False
                                    log.concat('Item already in the Master list')
                             if Addc:
                                #add the calendar to P1344
                                claim = pywikibot.Claim(repo, u'P1344')
                                claim.setTarget(item_to_add)
                                this_rider.item.addClaim(claim, summary=u'Adding classification')
                                
                                qualifier_rank = pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                                target_qualifier = pywikibot.WbQuantity(amount=this_rider.rank, site=repo)
                                qualifier_rank.setTarget(target_qualifier)
                                claim.addQualifier(qualifier_rank)
                                
                                qualifier_points = pywikibot.page.Claim(
                                    site, 'P1358', is_qualifier=True)
                                target_qualifier = pywikibot.WbQuantity(amount=result_table[ii][result_dic['points'][1]],
                                                                        site=repo)
                                qualifier_points.setTarget(target_qualifier)
                                claim.addQualifier(qualifier_points)
        
                    #action in the team, only for UCI ranking up to now
                        if result_table[ii][result_dic['team code'][1]]!=0 and result_table[ii][result_dic['team code'][1]]!="" and UCIranking:
                            this_team=list_of_teams[ii]
                            id_team= this_team.id_item
                            if id_team!='Q0' and id_team!='Q1':
                                item_team= pywikibot.ItemPage(repo, id_team)
                                item_team.get()
                                
                                Addc=True
                                item_to_add =this_rider.item
                                if(u'P3494' in item_team.claims):
                                    if cleaner:
                                        Addc=False
                                        item_team.removeClaims(this_rider.item.claims['P3494'])
                                    else: #not clear
                                        list_of_comprend = item_team.claims.get(u'P3494')
                                        for in_comprend in list_of_comprend:
                                            if in_comprend.getTarget() == item_to_add:  # Already there
                                                Addc = False
                                                log.concat('Item already in the Master list')
                                #no property or not there
                                if Addc:
                                   claim = pywikibot.Claim(repo, u'P3494')
                                   claim.setTarget(item_to_add)
                                   item_team.addClaim(claim, summary=u'Adding classification')
                                   
                                   qualifier_rank = pywikibot.page.Claim(
                                           site, 'P1352', is_qualifier=True)
                                   target_qualifier = pywikibot.WbQuantity(
                                           amount=this_rider.rank, site=repo)
                                   qualifier_rank.setTarget(target_qualifier)
                                   claim.addQualifier(qualifier_rank)
                                   
                                   qualifier_points = pywikibot.page.Claim(
                                           site, 'P1358', is_qualifier=True)
                                   target_qualifier = pywikibot.WbQuantity(amount=result_table[ii][result_dic['points'][1]],
                                                                           site=repo)
                                   qualifier_points.setTarget(target_qualifier)
                                   claim.addQualifier(qualifier_points)
            return 0, log
    except Exception as msg:
        print(msg)
        log.concat("General Error in UCI ranking")
        return 10, log        
