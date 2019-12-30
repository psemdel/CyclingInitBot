#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:44:28 2019

@author: maxime
"""
import csv
import numpy as np
import os
from exception import *


def UCI_classification_importer(
        pywikibot,
        site,
        repo,
        year,
        id_master_UCI,
        filename,
        cleaner,
        test,
        ):
 
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
    
    result_table, row_count, ecart=table_reader('input/' + filename + year + '.csv', result_dic,0)
    
    #post-processing
    for ii in range(row_count):
        if result_table[ii][result_dic['points'][1]]==0:
            result_table[ii][result_dic['points'][1]]=result_table[ii][result_dic['result'][1]]
    
    print('result_table created')
    list_of_cyclists=cyclists_table_reader(pywikibot, site, repo, result_table,result_dic)

    #fill the rider
    if not test:
        for ii in range(len(list_of_cyclists)):
            this_rider=list_of_cyclists[ii]
            
            if this_rider!='Q0' and this_rider!='Q1':
                if cleaner!=True:
                    #action in the rider 
                    Addc=True
                    if(u'P1344' in this_rider.item.claims):
                         list_of_comprend = this_rider.item.claims.get(u'P1344')
                         item_to_add = pywikibot.ItemPage(repo, id_master_UCI)
                         for in_comprend in list_of_comprend:
                            if in_comprend.getTarget() == item_to_add:  # Already there
                                Addc = False
                                print('Item already in the Master list')
                         if Addc:
                            #add the calendar to P1344
                            claim = pywikibot.Claim(repo, u'P1344')
                            claim.setTarget(item_to_add)
                            item.addClaim(claim, summary=u'Adding classification')
                            
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
    
                #action in the team
                if resulttable[ii][result_dic['team code'][1]] != 0:
                    id_team=search_team_by_code(pywikibot, site, result_table[ii][result_dic['team code'][1]])
                   
                    if id_team!='Q0' and id_team!='Q1':
                        item_team= pywikibot.ItemPage(repo, id_team)
                        item_team.get()
                        
                        Addc=True
                        if(u'P3494' in item_team.claims):
                            if cleaner:
                                this_rider.item.removeClaims(item.claims['P3494'])
                            else: #not clear
                                list_of_comprend = item.claims.get(u'P3494')
                                item_to_add =this_rider.item
                                for in_comprend in list_of_comprend:
                                    if in_comprend.getTarget() == item_to_add:  # Already there
                                        Addc = False
                                        print('Item already in the Master list')
            
                                if Addc:
                                   claim = pywikibot.Claim(repo, u'P3494')
                                   claim.setTarget(item_to_add)
                                   item.addClaim(claim, summary=u'Adding classification')
                                   
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

        
