"""
Created on Thu Jan  4 15:28:39 2018

@author: psemdel
"""
from .cycling_init_bot_low import (add_multiple_value, add_value, add_Qvalue,
add_to_master,
get_description, get_alias, create_present, CIOtoIDsearch, link_year)                                  
from .bot_log import Log
from .language_list  import load 
all_langs=load()

def f(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        nation_table,
        team_dic,
        year):
    
    def team_alias(team_table, kk, year, team_dic):
        # input
        alias = {}
        if team_table[kk][team_dic['UCIcode']] != u'':
            alias['fr'] = [team_table[kk][team_dic['UCIcode']] + u" " + str(year)]  # UCI code + year
            alias['en'] =  alias['fr']
            for lang in all_langs:
                alias[lang] = alias[u'fr']
            
        return alias

    def team_basic(
            pywikibot,
            repo,
            item,
            siteIn,
            team_name,
            country_code,
            year,
            id_master,
            id_present,
            UCI_code
            ):
        # No need for the table here
    
        if UCI_code != u"":
            #add_value(pywikibot, repo, item, 31, 2466826, u'Nature')
            add_value(pywikibot, repo, item, "P1998", UCI_code, u'UCI code')
       # else:
            #add_value(pywikibot, repo, item, 31, 26849121, u'Nature')
        add_multiple_value(pywikibot, repo, item, "P31", "Q53534649", u'Season', 0)
        add_Qvalue(pywikibot, repo, item, "P641", "Q3609", u'cyclisme sur route')
    
        add_Qvalue(pywikibot, repo, item, "P17", country_code, u'country')
        add_Qvalue(pywikibot, repo, item, "P361", id_master, u'part of')
        add_to_master(pywikibot,site,repo,id_present,id_master)
    
        if(u'P580' not in item.claims):
            claim = pywikibot.Claim(repo, u'P580')  # date de début
            startdate = pywikibot.WbTime(
                site=siteIn,
                year=year,
                month=1,
                day=1,
                precision='day')
            claim.setTarget(startdate)
            item.addClaim(claim, summary=u'Adding starting date')
    
        if(u'P582' not in item.claims):
            claim = pywikibot.Claim(repo, u'P582')  # date de fin
            enddate = pywikibot.WbTime(
                site=siteIn,
                year=year,
                month=12,
                day=31,
                precision='day')
            claim.setTarget(enddate)
            item.addClaim(claim, summary=u'Adding ending date')
    
        if(u'P1448' not in item.claims):
            claim = pywikibot.Claim(repo, u'P1448')  # nom officiel
            official_name = pywikibot.WbMonolingualText(
                text=team_name, language='fr')
            claim.setTarget(official_name)
            item.addClaim(claim, summary=u'Adding official name')
    
    
    def team_intro(item, team_table, kk, year, team_dic):
        item.get()
        if get_description('fr', item) == '':
            mydescription = team_description(team_table, kk, year)
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
    
        if get_alias('fr', item) == '':
            myalias = team_alias(team_table, kk, year, team_dic)
            item.editAliases(aliases=myalias, summary=u'Setting Aliases')
    
    def team_label(team_table, kk, year):
        # declaration
        mylabel = {}
    
        # Teamlabel_fr
        mylabel[u'fr'] = team_table[kk][1] + " " + str(year)
        mylabel[u'en'] = mylabel[u'fr']
        
        for lang in all_langs:
            mylabel[lang] = mylabel[u'fr']
        # Teamlabel_en
        return mylabel
    
    def team_description(team_table, kk, year):
        # declaration
        mydescription = {}
    
        # mydescription_fr
        description_part1_fr = u'Saison'
        description_part2_fr = u"de l'équipe cycliste"
        mydescription[u'fr'] = description_part1_fr + " " + \
            str(year) + " " + description_part2_fr + " " + team_table[kk][1]
        return mydescription
    
    try:
        kkinit = 1
        endkk=len(team_table)
        log=Log()
        
        if True:
            for kk in range(kkinit, endkk): 
                if team_table[kk][team_dic['active']] == 1:
    
                    mylabel = {}
                    mylabel = team_label(team_table, kk, year)
                    id_present, item=create_present(pywikibot, site,repo,time,mylabel)
                    
                    if id_present!=u'Q1':
                        log.concat("team id: " + id_present)
                        team_intro(item, team_table, kk, year, team_dic)
                        team_basic(
                            pywikibot,
                            repo,
                            item,
                            site,
                            team_table[kk][team_dic['name']],
                            CIOtoIDsearch(
                                nation_table,
                                team_table[kk][team_dic['country']]),
                            year,
                            team_table[kk][team_dic['master']],
                            id_present,
                            team_table[kk][team_dic['UCIcode']]
                            )
                         # Link the other to the new item
                        name_previous=team_label(team_table, kk, year-1)
                        name_next=team_label(team_table, kk, year+1)
                        link_year(pywikibot, site,repo, id_present,name_previous[u'fr'],name_next[u'fr'])
        return 0, log, id_present
    except:
        log.concat("General Error in team creator")
        return 10, log, "Q1"