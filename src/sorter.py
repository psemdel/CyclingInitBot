# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:48:04 2018

@author: psemdel
"""
from .cycling_init_bot_low import (delete_value, add_multiple_value, compare_dates,
get_label, checkprop)
from .moo import Race, Cyclist, Team
from .bot_log import Log

#sort the victories by date
def date_sorter(pywikibot, site, repo, time, team_id, property_number,test):
 
    #return the victories sorted by date
    def date_sort(list_of_victories, new_order):
        iimax = len(new_order) - 1
        for ii in range(iimax - 1):
            jjmax = iimax - ii
            table_sorted = True
            for jj in range(jjmax):
                victoire1 = list_of_victories[new_order[jj]]
                victoire2 = list_of_victories[new_order[jj + 1]]
                date1 = victoire1.date
                date2 = victoire2.date
                comparisonTemp = compare_dates(date1, date2)
                if comparisonTemp == 1:  # bad order
                    temp = new_order[jj]
                    new_order[jj] = new_order[jj + 1]
                    new_order[jj + 1] = temp
                    table_sorted = False
            if table_sorted:
                break
        return new_order
    
    log=Log()
    item = pywikibot.ItemPage(repo, team_id)
    item.get()
    
    list_of_races = []

    prop=checkprop(property_number)
    if(prop in item.claims):
        list_of_comprend = item.claims.get(prop)
    
    list_of_qualifiers=['P580','P585','P582']
    
    for ii in range(len(list_of_comprend)): #ii needed below
        this_item = list_of_comprend[ii].getTarget()
        this_item.get()
        
        done=False
        
        for qual in list_of_qualifiers:
            if qual in this_item.claims: 
                 claim_temp = this_item.claims[qual]
                 this_item_date = claim_temp[0].getTarget()
                 done=True
                 break
             
        if done==False:
            log.concat(this_item.labels['fr'] + u' has no date')
            return 0
        else:
            this_race=Race(ii, this_item.labels['fr'], this_item.getID(),this_item_date)
            list_of_races.append(this_race)

    new_order = [x for x in range(len(list_of_comprend))]
    old_order = [x for x in range(len(list_of_comprend))]

    new_order = date_sort(list_of_races, new_order)
    log.concat(new_order)
    order_ok=True
    
    if not test:
        for ii in range(len(new_order)):
            if new_order[ii] != old_order[ii]: #change only from the moment it differs, afterwards everything must be ordered
                order_ok=False
            if not order_ok:
                key = new_order[ii]
                id_item =  list_of_races[key].id_item
        
                delete_value(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    id_item,
                    'race for sorting')
                add_multiple_value(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    id_item,
                    'race for sorting',
                    1)
    return 0, log     

#sort the family name of cyclists
def name_sorter(pywikibot, site, repo, time, team_id, property_number, test):
    item = pywikibot.ItemPage(repo, team_id)
    item.get()

    list_of_objects = []
    list_of_names = []

    list_of_team_cat = [
        "Q6154783", "Q20638319", "Q382927", "Q1756006", 
        "Q23726798", "Q20738667", "Q28492441", "Q20639848", 
        "Q20639847", "Q20652655", "Q20653563", "Q20653564",
        "Q20653566", "Q2466826", "Q26849121", "Q78464255", 
        "Q80425135", "Q53534649"
        ]
    
    log=Log()
    team=False
    raceteam=False
    if u'P31' in item.claims:
        list_of_comprend = item.claims.get(u'P31')
        if list_of_comprend[0].getTarget() in list_of_team_cat:
            team=True

    # Read the list of racers and correct their name
    prop=checkprop(property_number)
    if(prop in item.claims):
        list_of_comprend = item.claims.get(prop)
    if prop ==u"P1923":
        raceteam=True

    list_of_names = [[u'' for x in range(2)] for y in range(len(list_of_comprend))]
    
    for ii in range(len(list_of_comprend)):
        this_item = list_of_comprend[ii].getTarget()
        this_item.get()
        this_label=get_label('fr', this_item)
        if raceteam:
            teamdate=''
            this_object=Team(ii, this_label, this_item.getID(),teamdate,site=site, pywikibot=pywikibot)
        elif team:
            this_object=Cyclist(ii, this_label, this_item.getID())
        else:
            this_object=Race(ii, this_label, this_item.getID(),'',site=site, pywikibot=pywikibot)
            
        list_of_objects.append(this_object)

        list_of_names[ii][0]=ii #remember original place
        list_of_names[ii][1]=this_object.sortkey
    
    sorted_names = sorted(list_of_names, key=lambda tup: tup[1])    
    log.concat('sorted list :')
    log.concat(sorted_names)
    order_ok=True
    
    list_of_qualifiers=['P580','P582']
        
    saved_qualifiers={}
    # delete done later
    if not test:
        for ii in range(len(sorted_names)):
            if sorted_names[ii] != list_of_names[ii]: #change only from the moment it differs, afterwards everything must be ordered
                order_ok=False
            if not order_ok:
                key = sorted_names[ii][0]
                id_item =list_of_objects[key].id_item
                # delete the old one
                allclaims = item.claims[prop]
                claim = allclaims[0]
        
                # Save the qualifiers
                for qual in list_of_qualifiers:
                    if qual in claim.qualifiers:
                        saved_qualifiers[qual]=claim.qualifiers[qual][0].getTarget()
                
                delete_value(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    id_item,
                    'rider for sorting')
                add_multiple_value(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    id_item,
                    'rider for sorting',
                    1)
        
                for qual in list_of_qualifiers: 
                    if qual in saved_qualifiers:
                        this_qual = pywikibot.page.Claim(site, qual, isQualifier=True)
                        this_qual.setTarget(saved_qualifiers[qual])
                        claim.addQualifier(this_qual)
    return 0, log     
