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
        team_table,
        nation_table,
        endkk,
        pro_or_amateur,
        team_dic,
        year):
    
    def pro_team_alias(team_table, kk, year, team_dic):
        # input
        alias = {}
        alias['fr'] = [team_table[kk][team_dic['UCIcode']] + u" " + str(year)]  # UCI code + year
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
            pro_or_amateur):
        # No need for the table here
    
        if pro_or_amateur == 1:
            #add_value(pywikibot, repo, item, 31, 2466826, u'Nature')
            add_value(pywikibot, repo, item, 1998, UCI_code, u'UCI code')
       # else:
            #add_value(pywikibot, repo, item, 31, 26849121, u'Nature')
        add_multiple_value(pywikibot, repo, item, 31, 53534649, u'Season', 0)
        add_value(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
    
        add_value(pywikibot, repo, item, 17, country_code, u'country')
        add_value(pywikibot, repo, item, 361, id_master, u'part of')
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
    
    
    def pro_team_intro(item, team_table, kk, year, pro_or_amateur,team_dic):
        item.get()
        if get_description('fr', item) == '':
            mydescription = pro_team_description(team_table, kk, year)
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
    
        if pro_or_amateur == 1:
            if get_alias('fr', item) == '':
                myalias = pro_team_alias(team_table, kk, year, team_dic)
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
    
    kkinit = 1
       
    # for year in range(2011,2020):
    # if kk==kkinit:
    if True:
        for kk in range(kkinit, endkk):  # endkk
            if team_table[kk][team_dic['active']] == 1:

                mylabel = {}
                mylabel = pro_team_label(team_table, kk, year)
                id_present, item=create_present(pywikibot, site,repo,time,mylabel)
                
                if id_present!=u'Q1':
                    print(id_present)
                    pro_team_intro(item, team_table, kk, year, pro_or_amateur,team_dic)
                    pro_team_basic(
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
                        team_table[kk][team_dic['UCIcode']],
                        pro_or_amateur)
                     # Link the other to the new item
                    name_previous=pro_team_label(team_table, kk, year-1)
                    name_next=pro_team_label(team_table, kk, year+1)
                    link_year(pywikibot, site,repo, id_present,name_previous[u'fr'],name_next[u'fr'])

