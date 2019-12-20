# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:48:04 2018

@author: psemdel
"""
from cycling_init_bot_low import *
from moo import *


#sort the victories by date
def date_sorter(pywikibot, site, repo, time, team_id, victory,test):
 
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
                comparisonTemp = compareDates(date1, date2)
                if comparisonTemp == 1:  # bad order
                    temp = new_order[jj]
                    new_order[jj] = new_order[jj + 1]
                    new_order[jj + 1] = temp
                    table_sorted = False
            if table_sorted:
                break
        return new_order
    
    
    item = pywikibot.ItemPage(repo, team_id)
    item.get()
    
    list_of_races = []

    if victory:
        property_number = 2522  # victoire
    else:
        property_number = 527  # comprend

    if(u'P' + str(property_number) in item.claims):
        list_of_comprend = item.claims.get(u'P' + str(property_number))
    
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
            print(this_item.labels['fr'] + u' has no date')
            return 0
        else:
            this_race=Race(ii, this_item.labels['fr'], this_item.getID(),this_item_date)
            list_of_races.append(this_race)

    new_order = [x for x in range(len(list_of_comprend))]
    old_order = [x for x in range(len(list_of_comprend))]

    new_order = date_sort(list_of_races, new_order)
    print(new_order)
    order_ok=True
    
    if not test:
        for ii in range(len(new_order)):
    #        print(new_order[ii])
    #        print(old_order[ii])
    #        print(new_order[ii] != old_order[ii])
            if new_order[ii] != old_order[ii]: #change only from the moment it differs, afterwards everything must be ordered
                order_ok=False
            if not order_ok:
                key = new_order[ii]
                id_item =  list_of_races[key].id_item
        
                deleteValue(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    noQ(id_item),
                    'race for sorting')
                addMultipleValue(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    noQ(id_item),
                    'race for sorting',
                    1)

#sort the family name of cyclists
def name_sorter(pywikibot, site, repo, time, team_id, team, champ, test):
    item = pywikibot.ItemPage(repo, team_id)
    item.get()

    list_of_objects = {}
    list_of_names = []

    if team or champ:
        property_number = 527  # comprend
    else:
        property_number = 1923  # liste des équipes participantes

    # Read the list of racers and correct their name
    if(u'P' + str(property_number) in item.claims):
        list_of_comprend = item.claims.get(u'P' + str(property_number))
    
    list_of_names = [[u'' for x in range(2)] for y in range(len(list_of_comprend))]
    
    for ii in range(len(list_of_comprend)):
        this_item = list_of_comprend[ii].getTarget()
        this_item.get()
        
        if team:
            this_object=Cyclist(ii, list_item.labels['fr'], this_item.getID())
        else:
            this_object=Race(ii, list_item.labels['fr'], this_item.getID(),'',site=site)
            
        list_of_objects.append(this_object)
        list_of_names[ii][0]=ii #remember original place
        list_of_names[ii][1]=this_object.sortkey
    
    
    sorted_names = sorted(list_of_names, key=lambda tup: tup[1])    
    print('sorted list :')
    print(sorted_names)
    order_ok=True
    
    if team:
        list_of_qualifiers=['P580','P582']
    else:
        list_of_qualifiers=[]
        
    saved_qualifiers={}
    # delete done later
    if not test:
        for ii in range(len(sortedName)):
            if sorted_names[ii] != list_of_names[ii]: #change only from the moment it differs, afterwards everything must be ordered
                order_ok=False
            if not order_ok:
                key = sorted_names[ii][0]
                id_item =list_of_objects[key].id_item
                # delete the old one
                allclaims = item.claims[u'P' + str(property_number)]
                claim = allclaims[0]
        
                # Save the qualifiers
                for qual in list_of_qualifiers:
                    if qual in claim.qualifiers:
                        saved_qualifiers[qual]=claim.qualifiers[list_of_qualifiers[kk]][0].getTarget()
                
                deleteValue(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    noQ(id_item),
                    'rider for sorting')
                addMultipleValue(
                    pywikibot,
                    repo,
                    item,
                    property_number,
                    noQ(id_item),
                    'rider for sorting',
                    1)
        
                for qual in list_of_qualifiers: 
                    if qual in saved_qualifiers:
                        this_qual = pywikibot.page.Claim(site, qual, isQualifier=True)
                        this_qual.setTarget(saved_qualifiers[qual])
                        claim.addQualifier(this_qual)

