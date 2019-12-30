#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:26:08 2019

@author: maxime
"""

def amateur_team_tab():
    i, j = 20, 100
   
    pro_team_dic={
        'name':1,
        'master':2,
        'country':3,
        'codeUCI':4,
        'group':5,
        'active':6            
        }
    
    kk = 1

    team_table = [[0 for x in range(i)] for y in range(j)]

    # Allemagne
    team_table[kk][1] = u"d.velop cloud–cycle cafe ladies"
    team_table[kk][2] = 29389056
    team_table[kk][3] = u'GER'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Gesundshop24.de"
    team_table[kk][2] = 54257534
    team_table[kk][3] = u'GER'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Maxx-Solar"
    team_table[kk][2] = 25997921
    team_table[kk][3] = u'GER'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Team Stuttgart"
    team_table[kk][2] = 29937736
    team_table[kk][3] = u'GER'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Belgique
    team_table[kk][1] = u"Autoglas Wetteren"
    team_table[kk][2] = 28829541
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Equano"
    team_table[kk][2] = 28869598
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Entente cycliste Wallonie"
    team_table[kk][2] = 50193072
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Hoop Op Zegen Beveren"
    team_table[kk][2] = 28941753
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Isorex"
    team_table[kk][2] = 28829711
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Jos Feron Lady Force"
    team_table[kk][2] = 28869604
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    team_table[kk][1] = u"Keukens Redant"
    team_table[kk][2] = 28829872
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Wielerclub de sprinters Malderen"
    team_table[kk][2] = 28830001
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Illi-Bikes Women"
    team_table[kk][2] = 61507365
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Rogelli-Gyproc"
    team_table[kk][2] = 61747858
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"S-bikes Bodhi"
    team_table[kk][2] = 63759241
    team_table[kk][3] = u'BEL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Pays-Bas
    team_table[kk][1] = u"Adelaar Ladies"
    team_table[kk][2] = 28942865
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"De Jonge Renner Ladies"
    team_table[kk][2] = 28830557
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    team_table[kk][1] = u"Jan van Arckel"
    team_table[kk][2] = 28829796
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    team_table[kk][1] = u"Maaslandster Veris CCN"
    team_table[kk][2] = 47505799
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"NWVG"
    team_table[kk][2] = 28942869
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Regioteam Noord-Holland Dames"
    team_table[kk][2] = 28942924
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Restore"
    team_table[kk][2] = 29550954
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"RWC Ahoy"
    team_table[kk][2] = 52108137
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Swaboladies"
    team_table[kk][2] = 28869582
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Team Drenthe"
    team_table[kk][2] = 28942932
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"TWC de Kempen Dames"
    team_table[kk][2] = 28942937
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Ulysses-Hoorn-West Frisia"
    team_table[kk][2] = 50381444
    team_table[kk][3] = u'NED'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # GB
    team_table[kk][1] = u"Bianchi Dama"
    team_table[kk][2] = 56285471
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Boompods EDCo NRG"
    team_table[kk][2] = 51484136
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Jadan Weldtite"
    team_table[kk][2] = 29608675
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Torelli-Assure"
    team_table[kk][2] = 29551008
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"NJC-Biemme-Echelon"
    team_table[kk][2] = 51484408
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u" Brother UK-Tifosi-OnForm"
    team_table[kk][2] = 51574577
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"YRDP Fred Whitton Challenge"
    team_table[kk][2] = 52107819
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"YRDP Fred Whitton Challenge"
    team_table[kk][2] = 52107819
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Liv Awol"
    team_table[kk][2] = 62123983
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Storey Racing"
    team_table[kk][2] = 29608773
    team_table[kk][3] = u'GBR'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # Brother UK - Fusion RT

    # France
    team_table[kk][1] = u"Breizh Ladies"
    team_table[kk][2] = 30050984
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"DN 17 Nouvelle-Aquitaine"
    team_table[kk][2] = 41483457
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"DN Auvergne-Rhône Alpes"
    team_table[kk][2] = 54208680
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"DN Biofrais"
    team_table[kk][2] = 41483289
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"DN Languedoc Le Boulou"
    team_table[kk][2] = 47505786
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Elles Pays de la Loire"
    team_table[kk][2] = 54207012
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Léopard Normandie"
    team_table[kk][2] = 54209261
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Team féminin Centre Val de Loire"
    team_table[kk][2] = 30051006
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"UC Vern-sur-Seiche"
    team_table[kk][2] = 54207811
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"VC Morteau Montbenoit"
    team_table[kk][2] = 30051000
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Vélo Sprint Bouchain"
    team_table[kk][2] = 51727632
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Crédit mutuel"
    team_table[kk][2] = 67605086
    team_table[kk][3] = u'FRA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Espagne
    team_table[kk][1] = u"Catema.cat"
    team_table[kk][2] = 47505687
    team_table[kk][3] = u'ESP'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Nafarroa-Ermitagana-Navarra"
    team_table[kk][2] = 53573816
    team_table[kk][3] = u'ESP'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Río Miera-Cantabria Deporte"
    team_table[kk][2] = 53573952
    team_table[kk][3] = u'ESP'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Delikia Ginestar"
    team_table[kk][2] = 61819593
    team_table[kk][3] = u'ESP'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Suisse
    team_table[kk][1] = u"Remax"
    team_table[kk][2] = 52108266
    team_table[kk][3] = u'SUI'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Centre mondial du cyclisme féminin"
    team_table[kk][2] = 69900887
    team_table[kk][3] = u'SUI'
    team_table[kk][5] = 1
    team_table[kk][6] = 1
    kk += 1

    # Danemark
    team_table[kk][1] = u"Rytger"
    team_table[kk][2] = 23023574
    team_table[kk][3] = u'DEN'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # USA
    team_table[kk][1] = u"IS Corp-Progress Software"
    team_table[kk][2] = 30053526
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Colavita-Bianchi"
    team_table[kk][2] = 24910599
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Fearless Femme Racing"
    team_table[kk][2] = 30077798
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Feed Hungry Kids Project"
    team_table[kk][2] = 54255993
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Gray Goat Mobile"
    team_table[kk][2] = 54256096
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"LA Sweat"
    team_table[kk][2] = 54256193
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Levine Law Group"
    team_table[kk][2] = 54256271
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Ortho Carolina"
    team_table[kk][2] = 30053774
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Papa John’s"
    team_table[kk][2] = 30077734
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Team Colombia"
    team_table[kk][2] = 54256409
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Meteor-Intelligentsia"
    team_table[kk][2] = 54256658
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Wolfpack"
    team_table[kk][2] = 54256834
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"DNA"
    team_table[kk][2] = 24185125
    team_table[kk][3] = u'USA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # Pologne
    team_table[kk][1] = u"Bcm Nowatex Ziemia Darlo"
    team_table[kk][2] = 50945907
    team_table[kk][3] = u'POL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Mat Atom Deweloper"
    team_table[kk][2] = 30329897
    team_table[kk][3] = u'POL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"TKK Pacific"
    team_table[kk][2] = 56846135
    team_table[kk][3] = u'POL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # Canada
    team_table[kk][1] = u"Desjardins Ford"
    team_table[kk][2] = 54256494
    team_table[kk][3] = u'CAN'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Macogep"
    team_table[kk][2] = 54210079
    team_table[kk][3] = u'CAN'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # New-Zealand

    team_table[kk][1] = u"RoxSolt Attaquer"
    team_table[kk][2] = 30077864
    team_table[kk][3] = u'NZL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # Mexique
    team_table[kk][1] = u"Durango-Specialized-IED"
    team_table[kk][2] = 30053023
    team_table[kk][3] = u'MEX'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Brésil
    team_table[kk][1] = u"Memorial Santos-Fupes"
    team_table[kk][2] = 52107994
    team_table[kk][3] = u'BRA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    # Italie
    team_table[kk][1] = u"ACS Cycling Chirio"
    team_table[kk][2] = 1437873
    team_table[kk][3] = u'ITA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Born to Win"
    team_table[kk][2] = 66386504
    team_table[kk][3] = u'ITA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    teamTable[kk][1] = u"Vallerbike"
    teamTable[kk][2] = 41430368
    teamTable[kk][3] = u'ITA'
    teamTable[kk][5] = 2
    teamTable[kk][6] = 0
    kk += 1

    teamTable[kk][1] = u"Andy Schleck Cycles-Immo Losch"
    teamTable[kk][2] = 61967168
    teamTable[kk][3] = u'LUX'
    teamTable[kk][5] = 2
    teamTable[kk][6] = 0
    kk += 1

    teamTable[kk][1] = u"Mike Greer Homes"
    team_table[kk][2] = 61125738
    team_table[kk][3] = u'NZL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    return [team_table, kk, pro_team_dic]