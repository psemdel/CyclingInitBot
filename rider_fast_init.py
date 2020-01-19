#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:05:33 2019

@author: maxime
"""
from cycling_init_bot_low import *
from exception import *

def rider_fast_init(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        name,
        CountryCIO):
    
    def create_fr_description(CountryCIO,team_table):
        mydescription = {}
        adj=u''
        for ii in range(len(team_table)):
            if team_table[ii][7] == CountryCIO:
                adj = team_table[ii][16]
                break
        mydescription['fr'] = 'coureuse cycliste ' + adj
        return mydescription

    
    mydescription=create_fr_description(CountryCIO,team_table)
    label = {}
    label['fr'] = name

    ## kkinit=teamCIOsearch(team_table, u'NAM')
    kk = teamCIOsearch(team_table, CountryCIO)
    id_rider = search_rider(pywikibot, site, repo,name,'','')

    if (id_rider == u'Q0'):  # no rider with this name
        id_rider = create_item(pywikibot, site, label)
        print(id_rider)
        item = pywikibot.ItemPage(repo, id_rider)
        item.get()
        
        item.editDescriptions(mydescription,
                              summary=u'Setting/updating descriptions.')
        add_value(pywikibot, repo, item, 31, 5, u'nature')
        add_value(pywikibot, repo, item, 21, 6581072, u'genre')
        add_value(
            pywikibot,
            repo,
            item,
            27,
            team_table[kk][3],
            u'nationality')
        add_value(pywikibot, repo, item, 106, 2309784, u'cyclist')