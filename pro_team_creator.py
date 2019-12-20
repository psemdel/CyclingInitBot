# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: psemdel
"""
from cycling_init_bot_low import *
from exception import *

def pro_team_creator(
        pywikibot,
        site,
        repo,
        time,
        team_table_femmes,
        national_team_table,
        endkk,
        proamateur,
        countrytocreate):
    
    def pro_team_alias(team_table, kk, year):
        # input
        alias = {}
        alias['fr'] = [team_table[kk][4] + u" " + str(year)]  # UCI code + year
        return alias

    def pro_team_basic(
            pywikibot,
            repo,
            item,
            siteIn,
            team_name,
            country_code,
            year,
            id_master,
            id_present,
            UCI_code,
            proamateur):
        # No need for the table here
    
        if proamateur == 1:
            addValue(pywikibot, repo, item, 31, 2466826, u'Nature')
            addValue(pywikibot, repo, item, 1998, UCI_code, u'UCI code')
        else:
            addValue(pywikibot, repo, item, 31, 26849121, u'Nature')
        addMultipleValue(pywikibot, repo, item, 31, 53534649, u'Season', 0)
        addValue(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
    
        addValue(pywikibot, repo, item, 17, country_code, u'country')
        addValue(pywikibot, repo, item, 361, id_master, u'part of')
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
    
    
    def pro_team_intro(item, team_table, kk, year, proamateur):
        item.get()
        if get_description('fr', item) == '':
            mydescription = pro_team_description(team_table, kk, year)
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
    
        if proamateur == 1:
            if get_alias('fr', item) == '':
                myalias = pro_team_alias(team_table, kk, year)
                item.editAliases(aliases=myalias, summary=u'Setting Aliases')
    
    def pro_team_label(team_table, kk, year):
        # declaration
        mylabel = {}
    
        # Teamlabel_fr
        mylabel[u'fr'] = team_table[kk][1] + " " + str(year)
        mylabel[u'en'] = mylabel[u'fr']
        # Teamlabel_en
        return mylabel
    
    def pro_team_description(team_table, kk, year):
        # declaration
        mydescription = {}
    
        # mydescription_fr
        description_part1_fr = u'Saison'
        description_part2_fr = u"de l'équipe cycliste"
        mydescription[u'fr'] = description_part1_fr + " " + \
            str(year) + " " + description_part2_fr + " " + team_table[kk][1]
        return mydescription
    
    year = 2020
    kkinit = 1
    # for year in range(2011,2020):
    # if kk==kkinit:
    if True:
        for kk in range(kkinit, endkk):  # endkk
            if (proamateur == 1 and team_table_femmes[kk][6] == 1) or (
                    proamateur == 0 and team_table_femmes[kk][5] == 1):
                # team_table_femmes[kk][5]==0 or
                mylabel = {}
                mylabel = pro_team_label(team_table_femmes, kk, year)
                id_present, item=create_present(mylabel)
                
                if id_present!=u'Q1':
                    pro_team_intro(item, team_table_femmes, kk, year, proamateur)
                    pro_team_basic(
                        pywikibot,
                        repo,
                        item,
                        site,
                        team_table_femmes[kk][1],
                        CIOtoIDsearch(
                            national_team_table,
                            team_table_femmes[kk][3]),
                        year,
                        team_table_femmes[kk][2],
                        id_present,
                        team_table_femmes[kk][4],
                        proamateur)
                     # Link the other to the new item
                    name_previous=proTeamLabel(team_table_femmes, kk, year-1)
                    name_next=proTeamLabel(team_table_femmes, kk, year+1)
                    link_year(pywikibot, site,id_present,name_previous,name_next)

