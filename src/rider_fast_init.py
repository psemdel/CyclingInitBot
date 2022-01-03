#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:05:33 2019

@author: maxime
"""
#from  import cycling_init_bot_low
#from Bot import cycling_init_bot_low
from .cycling_init_bot_low import (search_rider,  teamCIOsearch, create_item, 
                                   add_Qvalue)

from .bot_log import Log
from .language_list  import load 
all_langs=load()
                             
def f(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        name,
        CountryCIO,
        man_or_woman):
    
    def create_fr_description(CountryCIO,team_table,man_or_woman):
        mydescription = {}
        adj=u''
        for ii in range(len(team_table)):
            if team_table[ii][7] == CountryCIO:
                if man_or_woman==u'man':
                    adj = team_table[ii][17]
                else:
                    adj = team_table[ii][16]
                break
        if man_or_woman==u'man':
            mydescription['fr'] = 'coureur cycliste ' + adj
        else:   
            mydescription['fr'] = 'coureuse cycliste ' + adj
        return mydescription
    
    try:
        print("rider_fast_init")
        verbose=True
        log=Log()
        mydescription=create_fr_description(CountryCIO,team_table,man_or_woman)
        if verbose:
            print("description ok")
        label = {}
        label['fr'] = name
        label['en'] = name
                
        for lang in all_langs:
            label[lang] = label[u'fr']
            
        if verbose:
            print("label ok")
    
        ## kkinit=teamCIOsearch(team_table, u'NAM')
        kk = teamCIOsearch(team_table, CountryCIO)
        if verbose:
            print("teamCIO ok")
            print(pywikibot is None)
            print(site is None)
            print(repo is None)
            print(name is None)
            
        id_rider = search_rider(pywikibot, site, repo,name,'','')
        if verbose:
            print("search rider ok")

        if (id_rider == u'Q0'):  # no rider with this name
            id_rider = create_item(pywikibot, site, label)
            
            log.concat("new id rider")
            log.concat(id_rider)
            item = pywikibot.ItemPage(repo, id_rider)
            item.get()
            
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
            add_Qvalue(pywikibot, repo, item, "P31", "Q5", u'nature')
            if man_or_woman==u'man':
                add_Qvalue(pywikibot, repo, item, "P21", "Q6581097", u'genre')
            else:
                add_Qvalue(pywikibot, repo, item, "P21", "Q6581072", u'genre')
            add_Qvalue(
                pywikibot,
                repo,
                item,
                "P27",
                team_table[kk][3],
                u'nationality')
            add_Qvalue(pywikibot, repo, item, "P106", "Q2309784", u'cyclist')
        else:
            log.concat("AlreadyThere with id " +id_rider)
            return 1, log, "Q1"
        return 0, log, id_rider
    except Exception as msg:
        print(msg)
        log.concat("General Error in rider_fast_init")
        return 10, log, "Q1"

