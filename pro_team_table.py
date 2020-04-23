# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:30:17 2018

@author: psemdel
"""

def load():
    team_table = [[0 for x in range(20)] for y in range(100)]
    # Item 1 = name
    # Item 2 = master
    # Item 3 = country
    # Item 4 = code UCI
    # item 5 =group (priority)
    # item 6= active
    
    pro_team_dic={
            'name':1,
            'master':2,
            'country':3,
            'UCIcode':4,
            'group':5,
            'active':6            
            }
    
    kk = 0

    team_table[kk][1] = u"Alasayl"
    team_table[kk][2] = 47466174
    team_table[kk][3] = u'UAE'
    team_table[kk][4] = u'ACT'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u'Alé BTC Ljubljana'
    team_table[kk][2] = 1420281
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'ALE'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u'Aromitalia Vaiano'
    team_table[kk][2] = 17037135
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'VAI'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Astana Women's"
    team_table[kk][2] = 1208086
    team_table[kk][3] = u'KAZ'
    team_table[kk][4] = u'ASA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"BePink"
    team_table[kk][2] = 812812
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'BPK'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Bizkaia-Durango"
    team_table[kk][2] = 8248375
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'BDM'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Boels Dolmans"
    team_table[kk][2] = 2651858
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'DLT'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"BTC City Ljubljana"
    team_table[kk][2] = 47086699
    team_table[kk][3] = u'SLO'
    team_table[kk][4] = u'BTC'
    team_table[kk][5] = 0
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Canyon-SRAM Racing"
    team_table[kk][2] = 1757136
    team_table[kk][3] = u'GER'
    team_table[kk][4] = u'CSR'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Bigla"
    team_table[kk][2] = 15727996
    team_table[kk][3] = u'DEN'
    team_table[kk][4] = u'CBT'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Biehler Krush"
    team_table[kk][2] = 28869582
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'BKP'  
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    
    team_table[kk][1] = u"Cams Tifosi"
    team_table[kk][2] = 51574577
    team_table[kk][3] = u'GBR'
    team_table[kk][4] = u'CAT'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Casa Dorada"
    team_table[kk][2] = 81936382
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'not available'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1  
    
    

    team_table[kk][1] = u"Charente-Maritime Women Cycling"
    team_table[kk][2] = 41483457
    team_table[kk][3] = u'FRA'
    team_table[kk][4] = u'CMW'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1


    team_table[kk][1] = u"China Liv Pro Cycling"
    team_table[kk][2] = 16921675
    team_table[kk][3] = u'CHN'
    team_table[kk][4] = u'GPC'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Cogeas"
    team_table[kk][2] = 47450893
    team_table[kk][3] = u'RUS'
    team_table[kk][4] = u'CGS'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Conceria Zabri-Fanini"
    team_table[kk][2] = 28652712
    team_table[kk][3] = u'ALB'
    team_table[kk][4] = u'CZF'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Ciclotel"
    team_table[kk][2] = 81933532
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'CTL'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1   

    team_table[kk][1] = u"Cylance"
    team_table[kk][2] = 21450809
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'CPC'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"DNA"
    team_table[kk][2] = 24185125
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'DNA'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Doltcini-Van Eyck Sport"
    team_table[kk][2] = 21823219
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'DVE'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Eneicat-RBH"
    team_table[kk][2] = 60817976
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'EIC'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1    

    team_table[kk][1] = u"Eurotarget-Bianchi-Vittoria"
    team_table[kk][2] = 30330282
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'SBT'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Experza-Footlogix"
    team_table[kk][2] = 2443570
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'EXP'
    team_table[kk][5] = 0
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"FDJ-Nouvelle Aquitaine-Futuroscope"
    team_table[kk][2] = 15711596
    team_table[kk][3] = u'FRA'
    team_table[kk][4] = u'FDJ'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Hitec Products"
    team_table[kk][2] = 1290628
    team_table[kk][3] = u'NOR'
    team_table[kk][4] = u'HPU'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Illuminate"
    team_table[kk][2] = 28344643
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'ILU'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Instafund La Prima"
    team_table[kk][2] = 85337551
    team_table[kk][3] = u'CAN'
    team_table[kk][4] = u'ILP'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Lotto Soudal Ladies"
    team_table[kk][2] = 1686506
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'LSL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Lviv Women"
    team_table[kk][2] = 61449725
    team_table[kk][3] = u'UKR'
    team_table[kk][4] = u'LCW'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1   
    
    team_table[kk][1] = u"Macogep Tornatech Girondins de Bordeaux"
    team_table[kk][2] = 54210079
    team_table[kk][3] = u'CAN'
    team_table[kk][4] = u'MTG'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Massi Tactic"
    team_table[kk][2] = 47505687
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'MAT'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1  
    
    # Brésil
    team_table[kk][1] = u"Memorial Santos-Fupes"
    team_table[kk][2] = 52107994
    team_table[kk][3] = u'BRA'
    team_table[kk][4] = u'MEM'
    team_table[kk][5] = 2
    team_table[kk][6] = 1
    kk += 1

    team_table[kk][1] = u"Minsk Cycling Club"
    team_table[kk][2] = 28503589
    team_table[kk][3] = u'BLR'
    team_table[kk][4] = u'MCC'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Mitchelton-Scott"
    team_table[kk][2] = 2030459
    team_table[kk][3] = u'AUS'
    team_table[kk][4] = u'MTS'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Movistar Women"
    team_table[kk][2] = 41425184
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'MOV'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Multum Accountants-LSK"
    team_table[kk][2] = 28829541
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'MUL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"NXTG Racing"
    team_table[kk][2] = 84086763
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'NXG'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Parkhotel Valkenburg-Destil"
    team_table[kk][2] = 21484669
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'PHV'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Rally"
    team_table[kk][2] = 16985323
    team_table[kk][3] = u'CAN'
    team_table[kk][4] = u'RLW'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"SC Michela Fanini"
    team_table[kk][2] = 17010791
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'MIC'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Servetto-Piumate-Beltrami TSA"
    team_table[kk][2] = 17011701
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'SER'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Sho-Air Twenty20"
    team_table[kk][2] = 16974684
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'T20'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Sestroretsk"
    team_table[kk][2] = 86099803
    team_table[kk][3] = u'RUS'
    team_table[kk][4] = u'SSR'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1
   

    team_table[kk][1] = u"Sopela"
    team_table[kk][2] = 5978395
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'SWT'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Sunweb Women"
    team_table[kk][2] = 2292295
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'SUN'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Swapit Agolico"
    team_table[kk][2] = 43145400
    team_table[kk][3] = u'MEX'
    team_table[kk][4] = u'SWA'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Team Dukla Praha Women"
    team_table[kk][2] = 30330301
    team_table[kk][3] = u'CZE'
    team_table[kk][4] = u'TDP'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Thailand Women's Cycling Team"
    team_table[kk][2] = 28790089
    team_table[kk][3] = u'THA'
    team_table[kk][4] = u'TWC'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Tibco-Silicon Valley Bank"
    team_table[kk][2] = 537946
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'TIB'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Top Girls Fassa Bortolo"
    team_table[kk][2] = 3739967
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'TOP'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Drops"
    team_table[kk][2] = 23005923
    team_table[kk][3] = u'GBR'
    team_table[kk][4] = u'DRP'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Valcar Cylance"
    team_table[kk][2] = 28790149
    team_table[kk][3] = u'ITA'
    team_table[kk][4] = u'VAL'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"CCC-Liv"
    team_table[kk][2] = 1886678
    team_table[kk][3] = u'NED'
    team_table[kk][4] = u'CCC'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"WNT-Rotor Pro Cycling"
    team_table[kk][2] = 26001161
    team_table[kk][3] = u'GBR'
    team_table[kk][4] = u'WNT'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1

    # Dead
    team_table[kk][1] = u"Virtu Cycling Women"
    team_table[kk][2] = 22079749
    team_table[kk][3] = u'DEN'
    team_table[kk][4] = u'TVC'
    team_table[kk][5] = 0
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Wiggle High5"
    team_table[kk][2] = 47034223
    team_table[kk][3] = u'GBR'
    team_table[kk][4] = u'WHT'
    team_table[kk][5] = 3
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"UnitedHealthcare Women's"
    team_table[kk][2] = 16985991
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'UHC'
    team_table[kk][5] = 3
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Hagens Berman-Supermint"
    team_table[kk][2] = 23022363
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'HBS'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1

    team_table[kk][1] = u"Health Mate-Cyclelive Team"
    team_table[kk][2] = 47073038
    team_table[kk][3] = u'BEL'
    team_table[kk][4] = u'HCT'
    team_table[kk][5] = 2
    team_table[kk][6] = 0
    kk += 1
    
    team_table[kk][1] = u"Trek-Segafredo Women"
    team_table[kk][2] = 55478420
    team_table[kk][3] = u'USA'
    team_table[kk][4] = u'TFS'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1  
    
    team_table[kk][1] = u"Vib natural greatness"
    team_table[kk][2] = 84708639
    team_table[kk][3] = u'ESP'
    team_table[kk][4] = u'VIB'
    team_table[kk][5] = 1
    team_table[kk][6] = 0
    kk += 1     
    
    
    
    final_table = [['' for x in range(7)] for y in range(kk)]
    final_table=team_table[:kk]

    return [final_table, pro_team_dic]



