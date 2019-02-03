# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:23:59 2018

@author: maxime delzenne
"""

def nationalTeamTable():
    i, j = 20, 100;
    #For Europa
    teamTable = [[0 for x in range(i)] for y in range(j)] 
    
    #Item 1 = Country name fr
    #Item 2 = genre
    #Item 3= Element of the country
    #Item 4= Element of the master for the team
    #Item 5= Country name en
    #Item 6= Country adjective en
    #Item 7= CIO code
    #Item 8= Importance group of the country
    #Item 9= National championship master
    #item 10= Road race woman
    #item 11= Clm woman
    #item 12 = Road race man
    #item 13 = Clm man
    
    kk = 1
    
    teamTable[kk][1]=u'Afghanistan'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=889
    teamTable[kk][4]=43092098
    teamTable[kk][5]=u'Afghanistan'
    teamTable[kk][6]=u'Afghan'
    teamTable[kk][7]=u'AFG'
    teamTable[kk][8]=3
    kk+=1
    
    teamTable[kk][1]=u'Albanie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=222
    teamTable[kk][4]=42606434
    teamTable[kk][5]=u'Albania'
    teamTable[kk][6]=u'Albanian'
    teamTable[kk][7]=u'ALB'
    teamTable[kk][8]=2
    kk+=1
    
    teamTable[kk][1]=u'Algérie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=262
    teamTable[kk][4]=43092189
    teamTable[kk][5]=u'Algeria'
    teamTable[kk][6]=u'Algerian'
    teamTable[kk][7]=u'ALG'
    teamTable[kk][8]=2
    kk+=1
        
    teamTable[kk][1]=u'Andorre'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=228
    teamTable[kk][4]=42606593
    teamTable[kk][5]=u'Andorra'
    teamTable[kk][6]=u'Andorran'
    teamTable[kk][7]=u'AND'
    teamTable[kk][8]=2
    kk+=1
    
    teamTable[kk][1]=u'Angola'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=916
    teamTable[kk][4]=43092443
    teamTable[kk][5]=u'Angola'
    teamTable[kk][6]=u'Angolan'
    teamTable[kk][7]=u'ANG'
    teamTable[kk][8]=3
    kk+=1
    
    teamTable[kk][1]=u'Antigua-et-Barbuda'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=781
    teamTable[kk][4]=43092555
    teamTable[kk][5]=u'Antigua and Barbuda'
    teamTable[kk][6]=u'Antiguan'
    teamTable[kk][7]=u'ANT'
    teamTable[kk][8]=3
    kk+=1
    
    teamTable[kk][1]=u'Argentine'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=414
    teamTable[kk][4]=43092731
    teamTable[kk][5]=u'Argentina'
    teamTable[kk][6]=u'Argentinian'
    teamTable[kk][7]=u'ARG'
    teamTable[kk][8]=2
    teamTable[kk][9]=2954341
    teamTable[kk][10]=51332671
    teamTable[kk][11]=51332630
    kk+=1  
  
    teamTable[kk][1]=u'Arménie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=399
    teamTable[kk][4]=42606750
    teamTable[kk][5]=u'Armenia'
    teamTable[kk][6]=u'Armenian'
    teamTable[kk][7]=u'ARM'
    teamTable[kk][8]=3
    kk+=1
    
    teamTable[kk][1]=u'Aruba'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=21203
    teamTable[kk][4]=43092811
    teamTable[kk][5]=u'Aruba'
    teamTable[kk][6]=u'Aruban'
    teamTable[kk][7]=u'ARU'
    teamTable[kk][8]=3
    kk+=1 
    
    teamTable[kk][1]=u'Samoa américaines'
    teamTable[kk][2]=u"des "
    teamTable[kk][3]=16641
    teamTable[kk][4]=43092975
    teamTable[kk][5]=u'American Samoa'
    teamTable[kk][6]=u'American Samoan'
    teamTable[kk][7]=u'ASA'  #to check
    teamTable[kk][8]=3
    kk+=1 
    
    teamTable[kk][1]=u'Australie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=408
    teamTable[kk][4]=26433717
    teamTable[kk][5]=u'Australia'
    teamTable[kk][6]=u'Australian'
    teamTable[kk][7]=u'AUS'
    teamTable[kk][8]=1
    teamTable[kk][9]=2564187
    teamTable[kk][10]=29051258
    teamTable[kk][11]=29043254
    kk+=1
    
    teamTable[kk][1]=u'Autriche'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=40
    teamTable[kk][4]=34679945
    teamTable[kk][5]=u'Austria'
    teamTable[kk][6]=u'Austrian'
    teamTable[kk][7]=u'AUT'
    teamTable[kk][8]=1
    teamTable[kk][9]=129495
    teamTable[kk][10]=31094517
    teamTable[kk][11]=31093255
    kk+=1
    
    teamTable[kk][1]=u'Azerbaïdjan'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=227
    teamTable[kk][4]=42609988
    teamTable[kk][5]=u'Azerbaijan'
    teamTable[kk][6]=u'Azerbaijani'
    teamTable[kk][7]=u'AZE'
    teamTable[kk][8]=1
    teamTable[kk][9]=16538054
    teamTable[kk][10]=43286638
    teamTable[kk][11]=43286663
    kk+=1
    
    teamTable[kk][1]=u'Belgique'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=31
    teamTable[kk][4]=30744085
    teamTable[kk][5]=u'Belgium'
    teamTable[kk][6]=u'Belgian'
    teamTable[kk][7]=u'BEL'
    teamTable[kk][8]=1
    teamTable[kk][9]=1424329
    teamTable[kk][10]=30332924
    teamTable[kk][11]=29642128
    kk+=1
    
    teamTable[kk][1]=u'Belize'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=242
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Belize'
    teamTable[kk][6]=u'Belizean'
    teamTable[kk][7]=u'BIZ'
    teamTable[kk][8]=3
    teamTable[kk][9]=16538226
    teamTable[kk][10]=50404774
    teamTable[kk][11]=50404789
    kk+=1
    
    
    teamTable[kk][1]=u'Biélorussie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=184
    teamTable[kk][4]=43286756
    teamTable[kk][5]=u'Belarus'
    teamTable[kk][6]=u'Belarusian'
    teamTable[kk][7]=u'BLR'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954798
    teamTable[kk][10]=31271624
    teamTable[kk][11]=31271615
    kk+=1
    
    teamTable[kk][1]=u'Bolivie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=750
    teamTable[kk][4]=43306939
    teamTable[kk][5]=u'Bolivia'
    teamTable[kk][6]=u'Bolivian'
    teamTable[kk][7]=u'BOL'
    teamTable[kk][8]=2
    kk+=1
    
    
    
    teamTable[kk][1]=u'Brésil'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=155
    teamTable[kk][4]=43288916
    teamTable[kk][5]=u'Brazil'
    teamTable[kk][6]=u'Brazilian'
    teamTable[kk][7]=u'BRA'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955205
    teamTable[kk][10]=43288961
    teamTable[kk][11]=43288988
    kk+=1
    
    teamTable[kk][1]=u'Bulgarie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=219
    teamTable[kk][4]=43306952
    teamTable[kk][5]=u'Bulgaria'
    teamTable[kk][6]=u'Bulgarian'
    teamTable[kk][7]=u'BUL'
    teamTable[kk][8]=2
    kk+=1

    teamTable[kk][1]=u'Canada'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=16
    teamTable[kk][4]=33505760
    teamTable[kk][5]=u'Canada'
    teamTable[kk][6]=u'Canadian'
    teamTable[kk][7]=u'CAN'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955203
    teamTable[kk][10]=31096609
    teamTable[kk][11]=31096001
    kk+=1
    
    teamTable[kk][1]=u'Chili'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=298
    teamTable[kk][4]=43306977
    teamTable[kk][5]=u'Chili'
    teamTable[kk][6]=u'Chilean'
    teamTable[kk][7]=u'CHI'
    teamTable[kk][8]=2
    teamTable[kk][9]=2955202
    teamTable[kk][10]=31271587
    teamTable[kk][11]=51332422
    kk+=1
    
    teamTable[kk][1]=u'Chine'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=148
    teamTable[kk][4]=43093449
    teamTable[kk][5]=u'China'
    teamTable[kk][6]=u'Chinese'
    teamTable[kk][7]=u'CHN'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954796
    teamTable[kk][10]=43286408
    teamTable[kk][11]=43286449
    kk+=1
    
    teamTable[kk][1]=u'Colombie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=739
    teamTable[kk][4]=33893444
    teamTable[kk][5]=u'Colombia'
    teamTable[kk][6]=u'Colombian'
    teamTable[kk][7]=u'COL'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954810
    teamTable[kk][10]=43307022
    teamTable[kk][11]=43307035
    kk+=1
    
    teamTable[kk][1]=u'Costa Rica'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=800
    teamTable[kk][4]=43307054
    teamTable[kk][5]=u'Costa Rica'
    teamTable[kk][6]=u'Costa Rican'
    teamTable[kk][7]=u'CRC'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955204
    teamTable[kk][10]=33081164
    teamTable[kk][11]=33081846
    kk+=1 
    
    
    teamTable[kk][1]=u'Croatie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=224
    teamTable[kk][4]=43307086
    teamTable[kk][5]=u'Croatia'
    teamTable[kk][6]=u'Croatian'
    teamTable[kk][7]=u'CRO'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954807
    teamTable[kk][10]=30349395
    teamTable[kk][11]=30349411
    kk+=1
    
    teamTable[kk][1]=u'Cuba'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=241
    teamTable[kk][4]=43307111
    teamTable[kk][5]=u'Cuba'
    teamTable[kk][6]=u'Cuban'
    teamTable[kk][7]=u'CUB'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954801
    teamTable[kk][10]=30512013
    teamTable[kk][11]=30511620
    kk+=1
    
    teamTable[kk][1]=u'Chypre'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=229
    teamTable[kk][4]=53869566
    teamTable[kk][5]=u'Cyprus'
    teamTable[kk][6]=u'Cypriot'
    teamTable[kk][7]=u'CYP'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954799
    teamTable[kk][10]=53869580
    teamTable[kk][11]=53869589
    teamTable[kk][12]=24621530
    teamTable[kk][13]=24621627
    kk+=1
    
    teamTable[kk][1]=u'République tchèque'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=213
    teamTable[kk][4]=33895512
    teamTable[kk][5]=u'Czech Republic'
    teamTable[kk][6]=u'Czech'
    teamTable[kk][7]=u'CZE'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955107
    teamTable[kk][10]=31505332
    teamTable[kk][11]=31506358
    kk+=1
        
    teamTable[kk][1]=u'Danemark'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=35
    teamTable[kk][4]=33510054
    teamTable[kk][5]=u'Denmark'
    teamTable[kk][6]=u'Danish'
    teamTable[kk][7]=u'DEN'
    teamTable[kk][8]=1
    teamTable[kk][9]=129483
    teamTable[kk][10]=30349364
    teamTable[kk][11]=30349371
    kk+=1
    
    teamTable[kk][1]=u'Salvador'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=792
    teamTable[kk][4]=43744686
    teamTable[kk][5]=u'El Salvador'
    teamTable[kk][6]=u'Salvadoran'
    teamTable[kk][7]=u'ESA'
    teamTable[kk][8]=2
    teamTable[kk][9]=16538271
    teamTable[kk][10]=43744865
    teamTable[kk][11]=43744788
    kk+=1
        
    teamTable[kk][1]=u'Espagne'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=29
    teamTable[kk][4]=30753078
    teamTable[kk][5]=u'Spain'
    teamTable[kk][6]=u'Spanish'
    teamTable[kk][7]=u'ESP'
    teamTable[kk][8]=1
    teamTable[kk][9]=129656
    teamTable[kk][10]=31271605
    teamTable[kk][11]=31271315
    kk+=1
    
    teamTable[kk][1]=u'Estonie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=191
    teamTable[kk][4]=33987947
    teamTable[kk][5]=u'Estonia'
    teamTable[kk][6]=u'Estonian'
    teamTable[kk][7]=u'EST'
    teamTable[kk][8]=1
    teamTable[kk][9]=129594
    teamTable[kk][10]=43745198
    teamTable[kk][11]=43745136
    kk+=1
    
    teamTable[kk][1]=u'Finlande'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=33
    teamTable[kk][4]=33987956
    teamTable[kk][5]=u'Finland'
    teamTable[kk][6]=u'Finnish'
    teamTable[kk][7]=u'FIN'
    teamTable[kk][8]=1
    teamTable[kk][9]=129570
    teamTable[kk][10]=30332239
    teamTable[kk][11]=30332311
    kk+=1
    
    teamTable[kk][1]=u'France'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=142
    teamTable[kk][4]=26215309
    teamTable[kk][5]=u'France'
    teamTable[kk][6]=u'French'
    teamTable[kk][7]=u'FRA'
    teamTable[kk][8]=1
    teamTable[kk][9]=32435
    teamTable[kk][10]=30332844
    teamTable[kk][11]=30332806
    teamTable[kk][12]=27048419
    teamTable[kk][13]=27048421
    kk+=1
    
    teamTable[kk][1]=u'Grande-Bretagne'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=145
    teamTable[kk][4]=28840624
    teamTable[kk][5]=u'Great Britain'
    teamTable[kk][6]=u'British'
    teamTable[kk][7]=u'GBR'
    teamTable[kk][8]=1
    teamTable[kk][9]=619439
    teamTable[kk][10]=30349468
    teamTable[kk][11]=30349480
    kk+=1
        
    teamTable[kk][1]=u'Allemagne'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=183
    teamTable[kk][4]=33512923
    teamTable[kk][5]=u'Germany'
    teamTable[kk][6]=u'German'
    teamTable[kk][7]=u'GER'
    teamTable[kk][8]=1
    teamTable[kk][9]=80798
    teamTable[kk][10]=30332737
    teamTable[kk][11]=30332699
    kk+=1
    
    teamTable[kk][1]=u'Grèce'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=41
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Greece'
    teamTable[kk][6]=u'Greek'
    teamTable[kk][7]=u'GRE'
    teamTable[kk][8]=3
    teamTable[kk][9]=2955090
    teamTable[kk][10]=55221006
    teamTable[kk][11]=55220999
    kk+=1
    
    teamTable[kk][1]=u'Guatemala'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=774
    teamTable[kk][4]=43775548
    teamTable[kk][5]=u'Guatemala'
    teamTable[kk][6]=u'Guatemalan'
    teamTable[kk][7]=u'GUA'
    teamTable[kk][8]=1
    teamTable[kk][9]=17624434
    teamTable[kk][10]=33082364
    teamTable[kk][11]=33082393
    kk+=1
    
    teamTable[kk][1]=u'Hong Kong'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=8646
    teamTable[kk][4]=33989289
    teamTable[kk][5]=u'Hong Kong'
    teamTable[kk][6]=u'Hong Kong'
    teamTable[kk][7]=u'HKG'
    teamTable[kk][8]=1
    teamTable[kk][9]=16538163
    teamTable[kk][10]=43775863
    teamTable[kk][11]=43775943
    kk+=1
    
    teamTable[kk][1]=u'Hongrie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=28
    teamTable[kk][4]=43776079
    teamTable[kk][5]=u'Hungary'
    teamTable[kk][6]=u'Hungarian'
    teamTable[kk][7]=u'HUN'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955089
    teamTable[kk][10]=32161692
    teamTable[kk][11]=32163348
    kk+=1
    
    teamTable[kk][1]=u'Iran'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=794
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Iran'
    teamTable[kk][6]=u'Iranian'
    teamTable[kk][7]=u'IRI'
    teamTable[kk][8]=3
    teamTable[kk][9]=2912687
    teamTable[kk][10]=55995447
    teamTable[kk][11]=55995576
    kk+=1
    
    teamTable[kk][1]=u'Irlande'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=27
    teamTable[kk][4]=43776389
    teamTable[kk][5]=u'Irland'
    teamTable[kk][6]=u'Irish'
    teamTable[kk][7]=u'IRL'
    teamTable[kk][8]=1
    teamTable[kk][9]=13580466
    teamTable[kk][10]=33083546
    teamTable[kk][11]=33083817
    kk+=1
    
    teamTable[kk][1]=u'Israel'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=801
    teamTable[kk][4]=33989947
    teamTable[kk][5]=u'Israel'
    teamTable[kk][6]=u'Israel'
    teamTable[kk][7]=u'ISR'
    teamTable[kk][8]=1
    teamTable[kk][9]=2954766
    teamTable[kk][10]=30349213
    teamTable[kk][11]=30349222
    kk+=1
    
    teamTable[kk][1]=u'Italie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=38
    teamTable[kk][4]=33514038
    teamTable[kk][5]=u'Italia'
    teamTable[kk][6]=u'Italian'
    teamTable[kk][7]=u'ITA'
    teamTable[kk][8]=1
    teamTable[kk][9]=32213
    teamTable[kk][10]=30332988
    teamTable[kk][11]=30333018
    kk+=1
    
    teamTable[kk][1]=u'Japon'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=17
    teamTable[kk][4]=33994132
    teamTable[kk][5]=u'Japan'
    teamTable[kk][6]=u'Japanese'
    teamTable[kk][7]=u'JPN'  #CIO is JAP
    teamTable[kk][8]=1
    teamTable[kk][9]=80646
    teamTable[kk][10]=30557308
    teamTable[kk][11]=30557246
    kk+=1
    
    teamTable[kk][1]=u'Kazakhstan'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=232
    teamTable[kk][4]=43094028
    teamTable[kk][5]=u'Kazakhstan'
    teamTable[kk][6]=u'Kazakhstani'
    teamTable[kk][7]=u'KAZ'
    teamTable[kk][8]=1
    teamTable[kk][9]=689090
    teamTable[kk][10]=31510394
    teamTable[kk][11]=31529645
    kk+=1
    
 
    
    teamTable[kk][1]=u'Lettonie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=211
    teamTable[kk][4]=44192852
    teamTable[kk][5]=u'Latvia'
    teamTable[kk][6]=u'Latvian'
    teamTable[kk][7]=u'LAT'
    teamTable[kk][8]=1
    teamTable[kk][9]=1983791
    teamTable[kk][10]=30556990
    teamTable[kk][11]=30556121
    kk+=1
    
    teamTable[kk][1]=u'Lituanie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=37
    teamTable[kk][4]=33996970
    teamTable[kk][5]=u'Lithuania'
    teamTable[kk][6]=u'Lithuanian'
    teamTable[kk][7]=u'LTU'
    teamTable[kk][8]=1
    teamTable[kk][9]=129523
    teamTable[kk][10]=32604159
    teamTable[kk][11]=32603438
    kk+=1
    
    teamTable[kk][1]=u'Luxembourg'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=32
    teamTable[kk][4]=33514339
    teamTable[kk][5]=u'Luxembourg'
    teamTable[kk][6]=u'Luxembourgish'
    teamTable[kk][7]=u'LUX'
    teamTable[kk][8]=1
    teamTable[kk][9]=129589
    teamTable[kk][10]=30557561
    teamTable[kk][11]=30557504
    kk+=1    
    
    teamTable[kk][1]=u'Malaisie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=833
    teamTable[kk][4]=33998830
    teamTable[kk][5]=u'Malaysia'
    teamTable[kk][6]=u'Malaysian'
    teamTable[kk][7]=u'MAS'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955092
    teamTable[kk][10]=44193897
    teamTable[kk][11]=44193874
    kk+=1
    
    teamTable[kk][1]=u'Mexique'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=96
    teamTable[kk][4]=33999133
    teamTable[kk][5]=u'Mexico'
    teamTable[kk][6]=u'Mexican'
    teamTable[kk][7]=u'MEX'
    teamTable[kk][8]=1
    teamTable[kk][9]=114396
    teamTable[kk][10]=45083519
    teamTable[kk][11]=45083601
    kk+=1 
  
    teamTable[kk][1]=u'Maurice'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=1027
    teamTable[kk][4]=45083741
    teamTable[kk][5]=u'Mauritius'
    teamTable[kk][6]=u'Mauritian'
    teamTable[kk][7]=u'MRI'
    teamTable[kk][8]=2
    teamTable[kk][9]=17354260
    teamTable[kk][10]=45083914
    teamTable[kk][11]=45083963
    kk+=1 
    
    teamTable[kk][1]=u'Namibie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=1030
    teamTable[kk][4]=48648460
    teamTable[kk][5]=u'Namibia'
    teamTable[kk][6]=u'Namibian'
    teamTable[kk][7]=u'NAM'
    teamTable[kk][8]=1
    teamTable[kk][9]=1826259
    teamTable[kk][10]=31271492
    teamTable[kk][11]=31271499
    kk+=1
    
    
    teamTable[kk][1]=u'Pays-Bas'
    teamTable[kk][2]=u"des "
    teamTable[kk][3]=29999
    teamTable[kk][4]=27701263
    teamTable[kk][5]=u'Netherland'
    teamTable[kk][6]=u'Netherlands'
    teamTable[kk][7]=u'NED'
    teamTable[kk][8]=1
    teamTable[kk][9]=2726103
    teamTable[kk][10]=30333102
    teamTable[kk][11]=30333137
    kk+=1
    
    teamTable[kk][1]=u'Norvège'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=20
    teamTable[kk][4]=33517532
    teamTable[kk][5]=u'Norway'
    teamTable[kk][6]=u'Norwegian'
    teamTable[kk][7]=u'NOR'
    teamTable[kk][8]=1
    teamTable[kk][9]=129519
    teamTable[kk][10]=31271010
    teamTable[kk][11]=31271024
    kk+=1
    
    teamTable[kk][1]=u'Nouvelle-Zélande'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=664
    teamTable[kk][4]=45084426
    teamTable[kk][5]=u'New Zealand'
    teamTable[kk][6]=u'New Zealand'  
    teamTable[kk][7]=u'NZL'
    teamTable[kk][8]=1
    teamTable[kk][9]=2057790
    teamTable[kk][10]=29061811
    teamTable[kk][11]=45084575
    kk+=1
    
    teamTable[kk][1]=u'Paraguay'
    teamTable[kk][2]=u'du '
    teamTable[kk][3]=733
    teamTable[kk][4]=55791200
    teamTable[kk][5]=u'Paraguay'
    teamTable[kk][6]=u'Paraguayan'
    teamTable[kk][7]=u'PAR'  #CIO is PHL
    teamTable[kk][8]=3
    teamTable[kk][9]=2955211
    teamTable[kk][10]=55791222
    teamTable[kk][11]=55791233
    kk+=1
    
    teamTable[kk][1]=u'Philippines'
    teamTable[kk][2]=u"des "
    teamTable[kk][3]=928
    teamTable[kk][4]=42394736
    teamTable[kk][5]=u'Philippines'
    teamTable[kk][6]=u'Philippines'
    teamTable[kk][7]=u'PHI'  #CIO is PHL
    teamTable[kk][8]=3
    teamTable[kk][9]=16538206
    teamTable[kk][10]=55808632
    teamTable[kk][11]=55808642
    kk+=1
    
    teamTable[kk][1]=u'Pologne'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=36
    teamTable[kk][4]=33538045
    teamTable[kk][5]=u'Poland'
    teamTable[kk][6]=u'Polish'
    teamTable[kk][7]=u'POL'
    teamTable[kk][8]=1
    teamTable[kk][9]=2439460
    teamTable[kk][10]=31276622
    teamTable[kk][11]=30456396
    kk+=1
    
    teamTable[kk][1]=u'Portugal'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=45
    teamTable[kk][4]=45084767
    teamTable[kk][5]=u'Portugal'
    teamTable[kk][6]=u'Portuguese'
    teamTable[kk][7]=u'POR'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955216
    teamTable[kk][10]=45084873
    teamTable[kk][11]=45084954
    kk+=1
    
    teamTable[kk][1]=u'Porto Rico'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=1183
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Puerto Rico'
    teamTable[kk][6]=u'Puerto Rican'
    teamTable[kk][7]=u'PUR'
    teamTable[kk][8]=3
    teamTable[kk][9]=17624398
    teamTable[kk][10]=55185809
    teamTable[kk][11]=55185811
    kk+=1
    
    
    
    teamTable[kk][1]=u'Roumanie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=218
    teamTable[kk][4]=42394605
    teamTable[kk][5]=u'Romania'
    teamTable[kk][6]=u'Romanian'
    teamTable[kk][7]=u'ROM'  #CIO is ROU
    teamTable[kk][8]=1
    teamTable[kk][9]=2955100
    teamTable[kk][10]=32609249
    teamTable[kk][11]=32611136
    kk+=1
    
    teamTable[kk][1]=u'Afrique du Sud'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=258
    teamTable[kk][4]=43094142
    teamTable[kk][5]=u'South Africa'
    teamTable[kk][6]=u'South African'
    teamTable[kk][7]=u'RSA'
    teamTable[kk][8]=1
    teamTable[kk][9]=129547
    teamTable[kk][10]=43286073
    teamTable[kk][11]=29034408
    kk+=1
    
    teamTable[kk][1]=u'Russie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=159
    teamTable[kk][4]=33538048
    teamTable[kk][5]=u'Russia'
    teamTable[kk][6]=u'Russian'
    teamTable[kk][7]=u'RUS'
    teamTable[kk][8]=1
    teamTable[kk][9]=129553
    teamTable[kk][10]=31271644
    teamTable[kk][11]=31272638
    kk+=1
    
    teamTable[kk][1]=u'Rwanda'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=1037
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Rwanda'
    teamTable[kk][6]=u'Rwandan'
    teamTable[kk][7]=u'RWA'
    teamTable[kk][8]=3
    teamTable[kk][9]=16538267
    teamTable[kk][10]=55185740
    teamTable[kk][11]=55185725
    kk+=1
    
    teamTable[kk][1]=u'Slovénie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=215
    teamTable[kk][4]=43093898
    teamTable[kk][5]=u'Slovenia'
    teamTable[kk][6]=u'Slovenian'
    teamTable[kk][7]=u'SLO'
    teamTable[kk][8]=1
    teamTable[kk][9]=129650
    teamTable[kk][10]=30332625
    teamTable[kk][11]=30332486
    kk+=1
    
    teamTable[kk][1]=u'Serbie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=403
    teamTable[kk][4]=45171131
    teamTable[kk][5]=u'Serbia'
    teamTable[kk][6]=u'Serbian'
    teamTable[kk][7]=u'SRB'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955114
    teamTable[kk][10]=31298588
    teamTable[kk][11]=31300263
    kk+=1
    
    teamTable[kk][1]=u'Suisse'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=39
    teamTable[kk][4]=30744089
    teamTable[kk][5]=u'Switzerland'
    teamTable[kk][6]=u'Swiss'
    teamTable[kk][7]=u'SUI'
    teamTable[kk][8]=1
    teamTable[kk][9]=129576
    teamTable[kk][10]=31092105
    teamTable[kk][11]=30584268
    kk+=1
    
    teamTable[kk][1]=u'Slovaquie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=214
    teamTable[kk][4]=45171391
    teamTable[kk][5]=u'Slovakia'
    teamTable[kk][6]=u'Slovakian'
    teamTable[kk][7]=u'SVK'
    teamTable[kk][8]=1
    teamTable[kk][9]=129586
    teamTable[kk][10]=45171831
    teamTable[kk][11]=45171898
    kk+=1
        
    teamTable[kk][1]=u'Suède'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=34
    teamTable[kk][4]=33539201
    teamTable[kk][5]=u'Sweden'
    teamTable[kk][6]=u'Swedish'
    teamTable[kk][7]=u'SWE'
    teamTable[kk][8]=1
    teamTable[kk][9]=2465478
    teamTable[kk][10]=30349432
    teamTable[kk][11]=30349441
    kk+=1
    
    teamTable[kk][1]=u'Thaïlande'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=869
    teamTable[kk][4]=34009293
    teamTable[kk][5]=u'Thaïland'
    teamTable[kk][6]=u'Thailandese'
    teamTable[kk][7]=u'THA'
    teamTable[kk][8]=2
    teamTable[kk][9]=17624418
    teamTable[kk][10]=60883855
    teamTable[kk][11]=60883940
    kk+=1
    
    teamTable[kk][1]=u'Taïwan'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=865
    teamTable[kk][4]=33539648
    teamTable[kk][5]=u'Taiwan'
    teamTable[kk][6]=u'Taiwanese'
    teamTable[kk][7]=u'TPE'
    teamTable[kk][8]=1
    teamTable[kk][9]=17624413
    teamTable[kk][10]=45172237
    teamTable[kk][11]=45172232
    kk+=1
    
    teamTable[kk][1]=u'Turquie'
    teamTable[kk][2]=u"de "
    teamTable[kk][3]=43
    teamTable[kk][4]=0
    teamTable[kk][5]=u'Turkey'
    teamTable[kk][6]=u'Turkish'
    teamTable[kk][7]=u'TUR'
    teamTable[kk][8]=2
    kk+=1
    
    teamTable[kk][1]=u'Ukraine'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=212
    teamTable[kk][4]=34010555
    teamTable[kk][5]=u'Ukraine'
    teamTable[kk][6]=u'Ukrainian'
    teamTable[kk][7]=u'UKR'
    teamTable[kk][8]=1
    teamTable[kk][9]=2057230
    teamTable[kk][10]=30577809
    teamTable[kk][11]=30577837
    kk+=1
    
    teamTable[kk][1]=u'États-Unis'
    teamTable[kk][2]=u"des "
    teamTable[kk][3]=30
    teamTable[kk][4]=28869552
    teamTable[kk][5]=u'United States'
    teamTable[kk][6]=u'United States'
    teamTable[kk][7]=u'USA'
    teamTable[kk][8]=1
    teamTable[kk][9]=2955199
    teamTable[kk][10]=30349499
    teamTable[kk][11]=30349507
    kk+=1
  
    teamTable[kk][1]=u'Venezuela'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=717
    teamTable[kk][4]=45173072
    teamTable[kk][5]=u'Venezuela'
    teamTable[kk][6]=u'Venezuelan'
    teamTable[kk][7]=u'VEN'
    teamTable[kk][8]=2
    teamTable[kk][9]=2955217
    teamTable[kk][10]=45172931
    teamTable[kk][11]=45172978
    kk+=1
    
    
    return [teamTable, kk]

if __name__ == '__main__':
    [teamTable, kk]=nationalTeamTable()
    print(teamTable[32][12])