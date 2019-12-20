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
        teamTableFemmes,
        name,
        description,
        CountryCIO):
    mydescription = {}
    label = {}

    mydescription['fr'] = description
    label['fr'] = name

    ## kkinit=teamCIOsearch(teamTableFemmes, u'NAM')
    kk = teamCIOsearch(teamTableFemmes, CountryCIO)
    id_rider = searchItem(pywikibot, site, name)

    if (id_rider == u'Q0'):  # no rider with this name
        id_rider = create_item(pywikibot, site, label)
        item = pywikibot.ItemPage(repo, id_rider)
        item.get()
        
        item.editDescriptions(mydescription,
                              summary=u'Setting/updating descriptions.')
        addValue(pywikibot, repo, item, 31, 5, u'nature')
        addValue(pywikibot, repo, item, 21, 6581072, u'genre')
        addValue(
            pywikibot,
            repo,
            item,
            27,
            teamTableFemmes[kk][3],
            u'nationality')
        addValue(pywikibot, repo, item, 106, 2309784, u'cyclist')