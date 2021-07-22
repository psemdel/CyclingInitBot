# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:30:20 2018

@author: maxime delzenne
"""
from .cycling_init_bot_low import (add_value, add_Qvalue, add_to_master, 
search_item, teamCIOsearch, create_present, link_year)
from .bot_log import Log

def f(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        man_or_woman,
        option,
        start_year,
        end_year,
        CC, 
        **kwargs):
    
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
    
        add_Qvalue(pywikibot, repo, item, "P31", id_master, u'Nature')
        add_Qvalue(pywikibot, repo, item, "P641", "Q3609", u'cyclisme sur route')
        add_to_master(pywikibot,site,repo,id_present,id_master)
        
        if CC==False:
            id_allchamp = search_item(
                pywikibot,
                site,
                u'Championnats nationaux de cyclisme sur route en ' +
                str(year))
            if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):  
                print(u'Championnats nationaux de cyclisme sur route en ' +
                str(year)+' not found')
                return 1
            else:
                add_Qvalue(pywikibot, repo, item, "P361", id_allchamp, u'part of')
                add_to_master(pywikibot,site,repo,id_present,id_allchamp)
            add_Qvalue(pywikibot, repo, item, "P17", country_code, u'country')
        return 0

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
            CC,
            man_or_woman):
        
        add_Qvalue(pywikibot, repo, item, "P31", id_master, u'Nature')
        add_Qvalue(pywikibot, repo, item, "P641", "Q3609", u'cyclisme sur route')
        add_to_master(pywikibot,site,repo,id_race,id_master)
        add_to_master(pywikibot,site,repo,id_race,id_champ)
        
        if(u'P585' not in item.claims):
            claim = pywikibot.Claim(repo, u'P585')  # date
            date = pywikibot.WbTime(
                site=site,
                year=year,
                month=1,
                day=1,
                precision='day')
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
            if man_or_woman==u"woman":
                if enligne:
                    label = u'Course en ligne féminine aux championnats nationaux de cyclisme sur route ' + \
                        str(year)
                else:
                    label = u'Contre-la-montre féminin aux championnats nationaux de cyclisme sur route ' + \
                        str(year)
            else:
                if enligne:
                    label = u'Course en ligne masculine aux championnats nationaux de cyclisme sur route ' + \
                        str(year)
                else:
                    label = u'Contre-la-montre masculin aux championnats nationaux de cyclisme sur route ' + \
                        str(year)
            id_allchamp = search_item(pywikibot, site, label)
            if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):
                print(label+' not found')
                return 1
            else:
                add_to_master(pywikibot,site,repo,id_race,id_allchamp)
        
            add_Qvalue(pywikibot, repo, item, "P361", id_champ, u'part of')
            add_Qvalue(pywikibot, repo, item, "P17", country_code, u'country')
        return 0
        
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
            elif man_or_woman == u'woman':
                adj = u'féminine'
            elif man_or_woman == u'manU':
                adj = u'masculine espoirs'
            elif man_or_woman == u'womanU':
                adj = u'féminine espoirs'    
            elif man_or_woman == u'manJ':
                adj = u'masculine juniors'
            elif man_or_woman == u'womanJ':
                adj = u'féminine juniors'    
        else:
            firstword= u"Contre-la-montre "
            if man_or_woman == u'man':
                adj = u'masculin'
            elif man_or_woman == u'woman':
                adj = u'féminin'
            elif man_or_woman == u'manU':
                adj = u'masculin espoirs'
            elif man_or_woman == u'womanU':
                adj = u'féminin espoirs'    
            elif man_or_woman == u'manJ':
                adj = u'masculin juniors'
            elif man_or_woman == u'womanJ':
                adj = u'féminin juniors'        
                
        # declaration
        mylabel = {}
        
        label_part1_fr =  firstword + adj + " aux championnats"
        label_part2_fr = u"de cyclisme sur route"
        mylabel[u'fr'] = label_part1_fr + " " + genre_fr + \
            country_fr + " " + label_part2_fr + " " + str(year)
        return mylabel
    
    #Main function
    try:
        if CC:
            kkinit =1
            endkk= len(team_table)
        else:
            country=kwargs.get('country',False)
            if country:
                kkinit = teamCIOsearch(team_table, country)
                endkk = kkinit+1
            else:
                kkinit =1
                endkk= len(team_table)
            
        if option == 'clmoff':
            clm = False
        else:
            clm = True
        
        gender_dic=["woman","man","womanU","manU","womanJ","manJ"] 
        
        if man_or_woman in gender_dic:
            gender_dic=[man_or_woman]
        elif man_or_woman == u"both":   
            gender_dic=["woman","man"]    
        elif man_or_woman == u"all": 
            gender_dic=["woman","man","womanU","manU","womanJ","manJ"]    
        else:
            gender_dic=["woman"]
            
           
        log=Log()    
        for m_or_w in gender_dic:
            log.concat( "championships creation for gender: " + m_or_w)
            for kk in range(kkinit, endkk):  
                group = team_table[kk][8]
                if group == 1 or group == 2:
                    if CC:
                        id_master=team_table[kk][3]
                        country_code=0
                        if m_or_w == u"man":
                            index_road_race= 6
                            index_clm_race= 7
                        elif m_or_w==u"woman":
                            index_road_race= 4
                            index_clm_race= 5
                    else:
                        id_master=team_table[kk][9]
                        country_code= team_table[kk][3]
                        if m_or_w == u"man":
                            index_road_race= 12
                            index_clm_race= 13
                        elif m_or_w==u"woman":
                            index_road_race= 10
                            index_clm_race= 11
                        elif m_or_w==u"womanU":
                            index_road_race= 18
                            index_clm_race= 19
                        elif m_or_w==u"womanJ":    
                            index_road_race= 20
                            index_clm_race= 21
                        elif m_or_w==u"manU":
                            index_road_race= 22
                            index_clm_race= 23
                        elif m_or_w==u"manJ":
                            index_road_race= 24
                            index_clm_race= 25
                    
                    log.concat( "championships creation for country: Q" + str(country_code))
                    
                    for year in range(start_year, end_year+1):
                        log.concat( "championships creation for year: " + str(year))    
                        # Create the championship
                        mylabel = {}
                        mylabel = national_championship_label(team_table, kk, year,True)
                        id_present, item=create_present(pywikibot, site,repo,time, mylabel)
        
                        if id_present!='Q1':
                            res=national_championship_basic(
                                pywikibot,
                                repo,
                                item,
                                site,
                                id_master, #champ of one country
                                year,
                                country_code,
                                id_present,
                                CC)
                            if res==1:
                                log.concat(u'Championnats nationaux de cyclisme sur route en ' + str(year)+' not found')
                                log.concat(u'Code interrupted')
                                return 10, log
                                
                            name_previous = national_championship_label(
                                            team_table, kk, year-1, True)
                            name_next = national_championship_label(
                                                                team_table, kk, year+1,True)
                            link_year(pywikibot, site,repo, id_present,name_previous,name_next)
                            # Create the road race
                            if team_table[kk][index_road_race] != 0:
                                mylabel_enligne =  national_championship_race_label(
                                        team_table, kk, year, m_or_w,True)
                                id_enligne_present, item_enligne=create_present(pywikibot, site,repo,time,mylabel_enligne)
                                
                                if id_enligne_present!=u'Q1':
                                    res=national_championship_race_basic(
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
                                        CC,
                                        m_or_w)
                                    if res==1:
                                        log.concat(u'Course en ligne masculine/féminine de cyclisme sur route en ' + str(year)+' not found')
                                        log.concat(u'Code interrupted')
                                        return 10, log
                                    name_enligne_previous=national_championship_race_label(
                                        team_table, kk, year-1, m_or_w,True)
                                    name_enligne_next=national_championship_race_label(
                                        team_table, kk, year+1, m_or_w,True)
                                    link_year(pywikibot, site,repo, id_enligne_present,
                                              name_enligne_previous,name_enligne_next)
                            
                            # Create the Clm
                            if clm and team_table[kk][index_clm_race] != 0:
                                mylabel_clm =  national_championship_race_label(
                                        team_table, kk, year, m_or_w,False)
                                id_clm_present, item_clm=create_present(pywikibot, site,repo,time,mylabel_clm)
        
                                if id_clm_present!=u'Q1':
                                    res=national_championship_race_basic(
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
                                        CC,
                                        m_or_w)
                                    if res==1:
                                        log.concat(u'Contre-la-montre masculin/féminin de cyclisme sur route en ' + str(year)+' not found')
                                        log.concat(u'Code interrupted')
                                        return 10, log
                                    name_clm_previous=national_championship_race_label(
                                        team_table, kk, year-1, m_or_w,False)
                                    name_clm_next=national_championship_race_label(
                                        team_table, kk, year+1, m_or_w,False)
                                    link_year(pywikibot, site,repo, id_enligne_present,
                                              name_clm_previous,name_clm_next)
        return 0, log
    except:
        log.concat("General Error in national team creator")
        return 10, log

