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

                                   
def f(
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
    
    try:
        print("rider_fast_init")
        mydescription=create_fr_description(CountryCIO,team_table)
        label = {}
        label['fr'] = name
    
        ## kkinit=teamCIOsearch(team_table, u'NAM')
        kk = teamCIOsearch(team_table, CountryCIO)
        id_rider = search_rider(pywikibot, site, repo,name,'','')
        print("id_rider")
        print(id_rider)
        if (id_rider == u'Q0'):  # no rider with this name
            id_rider = create_item(pywikibot, site, label)
            print(id_rider)
            item = pywikibot.ItemPage(repo, id_rider)
            item.get()
            
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
            add_Qvalue(pywikibot, repo, item, "P31", "Q5", u'nature')
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
            raise Exception("AlreadyThere")

    except:
        raise Exception("General Error in rider_fast_init")
        
if __name__ == '__main__' :
    from . import pywikibot
    from . import nation_team_table
    import time

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    
    nation_table= nation_team_table.load()
    name="Marianne Vos"
    countryCIO="NED" 
    
    try:
        f(pywikibot, site, repo, time, nation_table, name, countryCIO)
    except Exception as msg:
        print(msg)
