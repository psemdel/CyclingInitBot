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
        log=Log()
        mydescription=create_fr_description(CountryCIO,team_table,man_or_woman)
        label = {}
        label['fr'] = name
    
        ## kkinit=teamCIOsearch(team_table, u'NAM')
        kk = teamCIOsearch(team_table, CountryCIO)
        id_rider = search_rider(pywikibot, site, repo,name,'','')

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
            return 1, log
        return 0, log, id_rider
    except:
        log.concat("General Error in rider_fast_init")
        return 10, log

