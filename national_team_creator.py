# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: maxime delzenne
"""
def national_team_creator(
        pywikibot,
        site,
        repo,
        time,
        team_table,
        endkk,
        man_or_woman):
   
    # ==Get==
    def national_team_alias(teamTable, kk, Year):
        # input
        alias = {}
        alias['fr'] = [teamTable[kk][7] + u" " + str(Year)]
        alias['en'] = alias['fr']
        alias['es'] = alias['fr']
        return alias

    def national_team_basic(
            pywikibot,
            repo,
            item,
            siteIn,
            country_name,
            country_code,
            year,
            master,
            CIO):
        # No need for the table here
        add_value(pywikibot, repo, item, 31, 23726798, u'Nature')
        add_value(pywikibot, repo, item, 1998, CIO, u'CIO code')
        add_value(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
        add_value(pywikibot, repo, item, 17, country_code, u'country')
        add_value(pywikibot, repo, item, 361, master, u'part of')
    
        if(u'P580' not in item.claims):
            claim = pywikibot.Claim(repo, u'P580')  # date de début
            start_date = pywikibot.WbTime(
                site=siteIn,
                year=year,
                month=1,
                day=1,
                precision='day')
            claim.setTarget(start_date)
            item.addClaim(claim, summary=u'Adding starting date')
    
        if(u'P582' not in item.claims):
            claim = pywikibot.Claim(repo, u'P582')  # date de fin
            end_date = pywikibot.WbTime(
                site=siteIn,
                year=year,
                month=12,
                day=31,
                precision='day')
            claim.setTarget(end_date)
            item.addClaim(claim, summary=u'Adding ending date')
    
        if(u'P1448' not in item.claims):
            claim = pywikibot.Claim(repo, u'P1448')  # nom officiel
            official_name = pywikibot.WbMonolingualText(
                text=country_name, language='fr')
            claim.setTarget(official_name)
            item.addClaim(claim, summary=u'Adding official name')


    def national_team_intro(item, teamTable, kk, Year):
        item.get()
        if get_description('fr', item) == '':
            mydescription = national_team_description(teamTable, kk, Year)
            item.editDescriptions(mydescription,
                                  summary=u'Setting/updating descriptions.')
    
        if get_alias('fr', item) == '':
            myalias = national_team_alias(teamTable, kk, Year)
            item.editAliases(
                aliases=myalias,
                summary=u'Setting Aliases')  # Not working yet


    def national_team_label(teamTable, kk, Year, man_or_woman):
        # input
        country_fr = teamTable[kk][1]
        genre_fr = teamTable[kk][2]
    
        countryadj_en = teamTable[kk][6]
    
        if man_or_woman == u'man':
            adj = u''
            adjen = u'men'
            adjes = u''
        else:
            adj = u'féminine '
            adjen = u'women'
            adjes = u' femenino'
        # declaration
        mylabel = {}
    
        # Teamlabel_fr
        label_part1_fr = u"équipe"
        label_part2_fr = adj + u"de cyclisme sur route"
        mylabel[u'fr'] = label_part1_fr + " " + genre_fr + \
            country_fr + " " + label_part2_fr + " " + str(Year)
    
        # Teamlabel_en
        label_part2_en = adjen + u"'s national road cycling team"
        mylabel[u'en'] = countryadj_en + " " + label_part2_en + " " + str(Year)
    
        # Teamlabel_es
        countryname_es = teamTable[kk][15]
        if countryname_es != '':
            mylabel[u'es'] = u"Equipo nacional" + adjes + " de " + \
                countryname_es + " de ciclismo en ruta" + " " + str(Year)
    
        return mylabel


    def national_team_description(teamTable, kk, Year):
        # input
        country_fr = teamTable[kk][1]
        genre_fr = teamTable[kk][2]
    
        # declaration
        mydescription = {}
    
        # mydescription_fr
        description_part1_fr = u'saison'
        description_part2_fr = u"de l'équipe"
        description_part3_fr = u"de cyclisme sur route"
        mydescription[u'fr'] = description_part1_fr + " " + \
            str(Year) + " " + description_part2_fr + " " + genre_fr + country_fr + " " + description_part3_fr
    
        return mydescription
    
    ### begin main ###
    kkinit = teamCIOsearch(team_table, u'GUA')

    if man_or_woman == 'man':
        IndexTeam = 14
    else:
        IndexTeam = 4

    # kk=kkinit
    # print(kkinit)
    # if kk==kkinit:
    for kk in range(kkinit, endkk):  #
        group = team_table[kk][8]
        if group == 1:
            for ii in range(2020, 2021):  # range(1990,2019)
                Year = ii
                if team_table[kk][IndexTeam] != 0:
                    mylabel = {}
                    mylabel = national_team_label(
                        team_table, kk, Year, man_or_woman)
                    
                    id_present, item=create_present(pywikibot, site,repo,time,mylabel)
        
                    if id_present!=u'Q1':
                        national_team_intro(item, team_table, kk, Year)
                        time.sleep(1.0)
                        national_team_basic(
                            pywikibot,
                            repo,
                            item,
                            site,
                            team_table[kk][1],
                            team_table[kk][3],
                            Year,
                            team_table[kk][IndexTeam],
                            team_table[kk][7])
                        time.sleep(1.0)
                    # Link the other to the new item

                        # Search previous
                        mylabel_previous = national_team_label(
                            team_table, kk, year-1, man_or_woman)
                        mylabel_next = national_team_label(
                            team_table, kk, year+1, man_or_woman)
                        
                        link_year(pywikibot, site,repo, id_present, mylabel_previous,mylabel_next)
                    # link to master
                    if team_table[kk][4] != 0:
                        item_master = pywikibot.ItemPage(
                            repo, u'Q' + str(team_table[kk][4]))
                        item_master.get()
                        add_multiple_value(
                            pywikibot,
                            repo,
                            item_master,
                            527,
                            noQ(id_present),
                            u'link year ' +
                            str(year),
                            0)