# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:30:20 2018

@author: maxime delzenne
"""
from cycling_init_bot_low import *

def national_championship_creator(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        endkk,
        man_or_woman,
        option,
        start_year,
        end_year,
        country,
        CC):
    
    def national_championship_basic(
        pywikibot,
        repo,
        item,
        site,
        id_master,
        year,
        country_code,
        id_present,
        CC):
    
        add_value(pywikibot, repo, item, 31, id_master, u'Nature')
        add_value(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
        add_to_master(pywikibot,site,repo,id_present,id_master)
        
        if CC==False:
            id_allchamp = searchItem(
                pywikibot,
                site,
                u'Championnats nationaux de cyclisme sur route en ' +
                str(year))
            if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):  
                print(u'Championnats nationaux de cyclisme sur route en ' +
                str(year)+'not found')
            else:
                add_value(pywikibot, repo, item, 361, noQ(id_allchamp), u'part of')
                add_to_master(pywikibot,site,repo,id_present,id_allchamp)
            add_value(pywikibot, repo, item, 17, country_code, u'country')

    def national_championship_race_basic(
            pywikibot,
            repo,
            item,
            site,
            id_champ,
            id_master,
            country_code,
            year,
            id_race,
            enligne, 
            CC):
        
        add_value(pywikibot, repo, item, 31, id_master, u'Nature')
        add_value(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
        add_to_master(pywikibot,site,repo,id_race,id_master)
        add_to_master(pywikibot,site,repo,id_race,id_champ)
        
        if(u'P585' not in item.claims):
            claim = pywikibot.Claim(repo, u'P585')  # date
            date = pywikibot.WbTime(site=site, year=year, precision='year')
            claim.setTarget(date)
            item.addClaim(claim, summary=u'Adding date')
        
        Addc = 1
        list_of_nature = item.claims.get(u'P31')
    
        if CC:
            if id_master == 934877 or id_master == 2630733:
                item_to_add = pywikibot.ItemPage(repo, u'Q23015458')  # CDM
            else:
                item_to_add = pywikibot.ItemPage(repo, u'Q22231118')  # CC
        else:
            item_to_add = pywikibot.ItemPage(repo, u'Q22231119')  # CN
        
        for ii in range(len(list_of_nature)):
            if list_of_nature[ii].getTarget() == item_to_add:  # Already there
                Addc = 0
                print('Item already in the Master list')
    
        if Addc == 1:
            claim = pywikibot.Claim(repo, u'P31')
            target = item_to_add  # pywikibot.ItemPage(repo, u'Q22231119')
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Adding CN')
    
    
        if CC==False:
            if enligne:
                label = u'Course en ligne féminine aux championnats nationaux de cyclisme sur route ' + \
                    str(year)
            else:
                label = u'Contre-la-montre féminin aux championnats nationaux de cyclisme sur route ' + \
                    str(year)
            id_allchamp = searchItem(pywikibot, site, label)
            if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):
                print(label+'not found')
            else:
                add_to_master(pywikibot,site,repo,id_race,id_allchamp)
        
            add_value(pywikibot, repo, item, 361, id_champ, u'part of')
            add_value(pywikibot, repo, item, 17, country_code, u'country')
    
    def national_championship_label(team_table, kk, year, english):
        # input
        country_fr = team_table[kk][1]
        genre_fr = team_table[kk][2]
    
        # declaration
        mylabel = {}
        label_part1_fr = u"Championnats"
        label_part2_fr = u"de cyclisme sur route"
        mylabel[u'fr'] = label_part1_fr + " " + genre_fr + \
            country_fr + " " + label_part2_fr + " " + str(year)
    
        if english!=False:
            countryadj_en = team_table[kk][6]
            label_part2_en = u"National Road Race Championships"
            mylabel[u'en'] = str(year) + " " + countryadj_en + " " + label_part2_en
        return mylabel
    
    def national_championship_race_label(team_table, kk, year, man_or_woman,enligne):
        # input
        country_fr = team_table[kk][1]
        genre_fr = team_table[kk][2]
        
        if enligne:
            firstword=u"Course en ligne "
            if man_or_woman == u'man':
                adj = u'masculine'
            else:
                adj = u'féminine'
        else:
            firstword= u"Contre-la-montre "
            if man_or_woman == u'man':
                adj = u'masculin'
            else:
                adj = u'féminin'
        # declaration
        mylabel = {}
        
        label_part1_fr =  firstword + adj + " aux championnats"
        label_part2_fr = u"de cyclisme sur route"
        mylabel[u'fr'] = label_part1_fr + " " + genre_fr + \
            country_fr + " " + label_part2_fr + " " + str(year)
        return mylabel
  
    # kkinit=teamCIOsearch(team_table,Country)
    kkinit = 1
    if option == 'clmoff':
        clm = False
    else:
        clm = True
            
    for kk in range(kkinit, endkk):  # endkk
        # kk=kkinit
        # if 1==1:
        group = team_table[kk][8]
        if group == 1:
            if CC:
                id_master=team_table[kk][3]
                country_code=0
                if man_or_woman == 'man':
                    index_road_race= 6
                    index_clm_race= 7
                else:
                    index_road_race= 4
                    index_clm_race= 5
            else:
                id_master=team_table[kk][9]
                country_code= team_table[kk][3]
                if man_or_woman == 'man':
                    index_road_race= 12
                    index_clm_race= 13
                else:
                    index_road_race= 10
                    index_clm_race= 11
            
            for year in range(start_year, end_year):
                group = 1
                # Create the championship
                mylabel = {}
                mylabel = national_championship_label(team_table, kk, year,True)
                id_present, item=create_present(mylabel)

                if id_present!='Q1':
                    national_championship_basic(
                        pywikibot,
                        repo,
                        item,
                        site,
                        id_master,
                        year,
                        country_code,
                        id_present,
                        CC)
                
                    name_previous = national_championship_label(
                                    team_table, kk, year-1)
                    name_next = national_championship_label(
                                                        team_table, kk, year+1)
                    link_year(pywikibot, site,id_present,name_previous,name_next)
            
                    # Create the road race
                    if team_table[kk][index_road_race] != 0:
                        mylabel_enligne =  national_championship_race_label(
                                team_table, kk, year, man_or_woman,True)
                        id_enligne_present, item_enligne=create_present(mylabel_enligne)
                        
                        if id_enligne_present!=u'Q1':
                            national_championship_race_basic(
                                pywikibot,
                                repo,
                                item_enligne,
                                site,
                                id_present,
                                team_table[kk][index_road_race],
                                country_code,
                                year,
                                id_enligne_present,
                                True, 
                                CC)
                            name_enligne_previous=national_championship_race_label(
                                team_table, kk, year-1, man_or_woman,True)
                            name_enligne_next=national_championship_race_label(
                                team_table, kk, year+1, man_or_woman,True)
                            link_year(pywikibot, site,id_enligne_present,
                                      name_enligne_previous,name_enligne_next)
                    
                    # Create the Clm
                    if clm and team_table[kk][IndexClmRace] != 0:
                        mylabel_clm =  national_championship_race_label(
                                team_table, kk, year, man_or_woman,False)
                        id_clm_present, item_clm=create_present(mylabel_clm)

                        if id_clm_present!=u'Q1':
                            national_championship_race_basic(
                                pywikibot,
                                repo,
                                item_clm,
                                site,
                                id_present,
                                team_table[kk][index_clm_race],
                                country_code,
                                year,
                                id_clm_present,
                                False, 
                                CC)
                            name_clm_previous=national_championship_race_label(
                                team_table, kk, year-1, man_or_woman,False)
                            name_clm_next=national_championship_race_label(
                                team_table, kk, year+1, man_or_woman,False)
                            link_year(pywikibot, site,id_enligne_present,
                                      name_clm_previous,name_clm_next)


