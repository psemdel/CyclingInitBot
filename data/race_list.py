#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:15:59 2019

@author: maxime
"""

def load():
    raceTable = [[0 for x in range(5)] for y in range(1000)]

    # 1: part 1 of the name
    # 2: part 2 of the name
    # 3: master
    # 4: genre
    
    race_dic={
        'name1':1,
        'name2':2,
        'master':3,
        'genre':4,
        }
    

    kk = 1
    
    raceTable[kk][1] = u'Valli'
    raceTable[kk][2] = u"Varesine"
    raceTable[kk][3] = 104637824
    raceTable[kk][4] = u"des "
    kk += 1 
  
    raceTable[kk][1] = u'Tour'
    raceTable[kk][2] = u"Suisse"
    raceTable[kk][3] = 104637798
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u'Delta'
    raceTable[kk][2] = u"Road Race"
    raceTable[kk][3] = 28232668
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u'Vårgårda'
    raceTable[kk][2] = u"TTT"
    raceTable[kk][3] = 26266060
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u'Vårgårda'
    raceTable[kk][2] = u"RR"
    raceTable[kk][3] = 26266059
    raceTable[kk][4] = u"de la "
    kk += 1  
    
    raceTable[kk][1] = u'Paris'
    raceTable[kk][2] = u"Roubaix"
    raceTable[kk][3] = 96053083
    raceTable[kk][4] = u"de "
    kk += 1     
    
    raceTable[kk][1] = u'Scheldeprijs'
    raceTable[kk][2] = u""
    raceTable[kk][3] = 104637738
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u'Grand Prix'
    raceTable[kk][2] = u"Chambéry"
    raceTable[kk][3] = 16763629
    raceTable[kk][4] = u"du "
    kk += 1  
   
    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Eco-Struct"
    raceTable[kk][3] = 79034830
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Oetingen"
    raceTable[kk][3] = 104637723
    raceTable[kk][4] = u"du "
    kk += 1  
   
    raceTable[kk][1] = u'Tour'
    raceTable[kk][2] = u"Zhoushan"
    raceTable[kk][3] = 13362122
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u'Tour'
    raceTable[kk][2] = u"Wenzhou"
    raceTable[kk][3] = 104637782
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u'Santos Women'
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 22661614
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Belek"
    raceTable[kk][3] = 78487585
    raceTable[kk][4] = u"du "
    kk += 1    

    raceTable[kk][1] = u"Race"
    raceTable[kk][2] = u"Torquay"
    raceTable[kk][3] = 78655433
    raceTable[kk][4] = u"de la "
    kk += 1  
    
    raceTable[kk][1] = u"Vuelta CV"
    raceTable[kk][2] = u"Feminas"
    raceTable[kk][3] = 60965701
    raceTable[kk][4] = u"de la "
    kk += 1     
    
    raceTable[kk][1] = u"Vuelta"
    raceTable[kk][2] = u"Castellon"
    raceTable[kk][3] = 79030956
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Manavgat"
    raceTable[kk][3] = 79031111
    raceTable[kk][4] = u"du "
    kk += 1   
   

    raceTable[kk][1] = u"Dubai"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 78657185
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u'Strade'
    raceTable[kk][2] = u"Bianche"
    raceTable[kk][3] = 19605976
    raceTable[kk][4] = u"des "
    kk += 1

    raceTable[kk][1] = u'Gran Premio'
    raceTable[kk][2] = u"ICODER"
    raceTable[kk][3] = 57966675
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Vuelta'
    raceTable[kk][2] = u"Costa Rica"
    raceTable[kk][3] = 16960754
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Chrono'
    raceTable[kk][2] = u"Nations"
    raceTable[kk][3] = 41944204
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Tour'
    raceTable[kk][2] = u"Nanxijiang"
    raceTable[kk][3] = 71731311
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Gran Premio'
    raceTable[kk][2] = u"Beghelli"
    raceTable[kk][3] = 27031552
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Giro'
    raceTable[kk][2] = u"Emilia"
    raceTable[kk][3] = 22008975
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Grand Prix'
    raceTable[kk][2] = u"Isbergues"
    raceTable[kk][3] = 56703296
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Giro'
    raceTable[kk][2] = u"Marche "
    raceTable[kk][3] = 68029340
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Tour'
    raceTable[kk][2] = u"Ardèche"
    raceTable[kk][3] = 1729875
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Madrid'
    raceTable[kk][2] = u"Vuelta"
    raceTable[kk][3] = 21030967
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u'Challenge'
    raceTable[kk][2] = u"Vuelta"
    raceTable[kk][3] = 21030967
    raceTable[kk][4] = u"de la "
    kk += 1


    raceTable[kk][1] = u'Ladies'
    raceTable[kk][2] = u"Belgium"
    raceTable[kk][3] = 6685041
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u'Lotto'
    raceTable[kk][2] = u"Belgium Tour"
    raceTable[kk][3] = 6685041
    raceTable[kk][4] = u"du "
    kk += 1
    

    raceTable[kk][1] = u'Scenic Avenue'
    raceTable[kk][2] = u"Race I"
    raceTable[kk][3] = 67205061
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u'Scenic Avenue'
    raceTable[kk][2] = u"Race I"
    raceTable[kk][3] = 67205154
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u'Chrono'
    raceTable[kk][2] = u"Champenois"
    raceTable[kk][3] = 1088090
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Féminine'
    raceTable[kk][2] = u"Fourmies"
    raceTable[kk][3] = 61013887
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Giro'
    raceTable[kk][2] = u"Toscana"
    raceTable[kk][3] = 369183
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u'Boels'
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 1572063
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u'Simac'
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 1572063
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Plouay"
    raceTable[kk][3] = 1110856
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Lorient Agglomération"
    raceTable[kk][3] = 1110856
    raceTable[kk][4] = u"du "
    kk += 1    
    
    raceTable[kk][1] = u'Picto'
    raceTable[kk][2] = u"Charentaise"
    raceTable[kk][3] = 61013883
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Colorado"
    raceTable[kk][2] = u"Classic"
    raceTable[kk][3] = 66777548
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Norway"
    raceTable[kk][3] = 17619325
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Battle"
    raceTable[kk][2] = u"North"
    raceTable[kk][3] = 17619325
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u"Vårgårda"
    raceTable[kk][2] = u"RR"
    raceTable[kk][3] = 26266059
    raceTable[kk][4] = u"de l'"
    kk += 1

    raceTable[kk][1] = u"Vårgårda"
    raceTable[kk][2] = u"TTT"
    raceTable[kk][3] = 26266060
    raceTable[kk][4] = u"de l'"
    kk += 1

    raceTable[kk][1] = u"Périgord"
    raceTable[kk][2] = u"Ladies"
    raceTable[kk][3] = 61013879
    raceTable[kk][4] = u"de la "
    kk += 1
    
    raceTable[kk][1] = u"Flanders"
    raceTable[kk][2] = u"De Vuyst"
    raceTable[kk][3] = 47044489
    raceTable[kk][4] = u"de la "
    kk += 1
    
    raceTable[kk][1] = u"MerXem"
    raceTable[kk][2] = u"Classic"
    raceTable[kk][3] = 61013876
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Vuelta"
    raceTable[kk][2] = u"Tica"
    raceTable[kk][3] = 66385803
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Women"
    raceTable[kk][2] = u"Scotland"
    raceTable[kk][3] = 60964473
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u"Clásica"
    raceTable[kk][2] = u"506"
    raceTable[kk][3] = 66250138
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Clásica"
    raceTable[kk][2] = u"Esencial"
    raceTable[kk][3] = 66309379
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"San"
    raceTable[kk][2] = u"Sebastian"
    raceTable[kk][3] = 60882083
    raceTable[kk][4] = u"de la "
    kk += 1
    
    raceTable[kk][1] = u"Itzulia"
    raceTable[kk][2] = u"Women"
    raceTable[kk][3] =60882083
    raceTable[kk][4] = u"de la "
    kk += 1  

    raceTable[kk][1] = u"Erondegemse"
    raceTable[kk][2] = u"Pijl"
    raceTable[kk][3] = 16974973
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"RideLondon"
    raceTable[kk][2] = u"Classique"
    raceTable[kk][3] = 26143122
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Kreiz"
    raceTable[kk][2] = u"Breizh"
    raceTable[kk][3] = 55754205
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u"Clasica"
    raceTable[kk][2] = u"Navarra"
    raceTable[kk][3] = 66076050
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Classics"
    raceTable[kk][2] = u"Navarra"
    raceTable[kk][3] = 66076050
    raceTable[kk][4] = u"de la "
    kk += 1

    raceTable[kk][1] = u"Nafarroako"
    raceTable[kk][2] = u"Klasikoa"
    raceTable[kk][3] = 66015725
    raceTable[kk][4] = u"de la "
    kk += 1
    
    raceTable[kk][1] = u"Nafarroako"
    raceTable[kk][2] = u"Classics"
    raceTable[kk][3] = 66015725
    raceTable[kk][4] = u"de la "
    kk += 1
    
    raceTable[kk][1] = u"BeNe"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 16911866
    raceTable[kk][4] = u"du "
    kk += 1

    raceTable[kk][1] = u"Baloise"
    raceTable[kk][2] = u"Ladies Tour"
    raceTable[kk][3] = 16911866
    raceTable[kk][4] = u"du "
    kk += 1


    raceTable[kk][1] = u"La Course"
    raceTable[kk][2] = u"Tour de France"
    raceTable[kk][3] = 17348758
    raceTable[kk][4] = u"de "
    kk += 1    

    raceTable[kk][1] = u"Tour de Feminin"
    raceTable[kk][2] = u"cenu"
    raceTable[kk][3] = 1463076
    raceTable[kk][4] = u"du "
    kk += 1   
  
    raceTable[kk][1] = u"Tour de Feminin"
    raceTable[kk][2] = u""
    raceTable[kk][3] = 1463076
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Sparkassen"
    raceTable[kk][2] = u"Giro"
    raceTable[kk][3] = 75628179
    raceTable[kk][4] = u"du "
    kk += 1    
   
    
    raceTable[kk][1] = u"Giro"
    raceTable[kk][2] = u"Italia"
    raceTable[kk][3] = 1526999
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u"Chrono"
    raceTable[kk][2] = u"Armstrong"
    raceTable[kk][3] = 55523189
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Thailand"
    raceTable[kk][3] = 17063894
    raceTable[kk][4] = u"du "
    kk += 1 
    
    
    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"Het Nieuwsblad"
    raceTable[kk][3] = 2973966
    raceTable[kk][4] = u"du "
    kk += 1   

    raceTable[kk][1] = u"Samyn"
    raceTable[kk][2] = u"Dames"
    raceTable[kk][3] = 13060354
    raceTable[kk][4] = u" "
    kk += 1     
 
    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"Hageland"
    raceTable[kk][3] = 3882248
    raceTable[kk][4] = u"de l'"
    kk += 1  

    raceTable[kk][1] = u"Drentse"
    raceTable[kk][2] = u"Acht"
    raceTable[kk][3] = 28938662
    raceTable[kk][4] = u"du "
    kk += 1      
    
    raceTable[kk][1] = u"Ronde"
    raceTable[kk][2] = u"Drenthe"
    raceTable[kk][3] = 23015336
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"Trofeo"
    raceTable[kk][2] = u"Binda"
    raceTable[kk][3] = 641769
    raceTable[kk][4] = u"du "
    kk += 1    

    raceTable[kk][1] = u"Driedaagse"
    raceTable[kk][2] = u"De Panne"
    raceTable[kk][3] = 42052559
    raceTable[kk][4] = u"des "
    kk += 1 
    
    raceTable[kk][1] = u"Classic"
    raceTable[kk][2] = u"De Panne"
    raceTable[kk][3] = 42052559
    raceTable[kk][4] = u"des "
    kk += 1   
    
    
    raceTable[kk][1] = u"Gent"
    raceTable[kk][2] = u"Wevelgem"
    raceTable[kk][3] = 19828524
    raceTable[kk][4] = u"de "
    kk += 1 
    
    raceTable[kk][1] = u"Dwars"
    raceTable[kk][2] = u"Vlaanderen"
    raceTable[kk][3] = 28872927
    raceTable[kk][4] = u"d'"
    kk += 1 
             
    raceTable[kk][1] = u"Ronde"
    raceTable[kk][2] = u"Vlaanderen"
    raceTable[kk][3] = 1637189
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Diamond"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 17064522
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"White"
    raceTable[kk][2] = u"Spot"
    raceTable[kk][3] = 28232668
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"V4 Ladies"
    raceTable[kk][2] = u"Pannonhalma"
    raceTable[kk][3] = 61003351
    raceTable[kk][4] = u"de la "
    kk += 1 

    raceTable[kk][1] = u"V4 Ladies"
    raceTable[kk][2] = u"Zalaegerszeg"
    raceTable[kk][3] = 61004019
    raceTable[kk][4] = u"de la "
    kk += 1     


    raceTable[kk][1] = u"OVO Energy Women"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 16679864
    raceTable[kk][4] = u" "
    kk += 1 
 
 #too dangerous!!   
    
   # raceTable[kk][1] = u"Women's Tour"
  #  raceTable[kk][2] = u""
   # raceTable[kk][3] = 16679864
  #  raceTable[kk][4] = u" "
 #   kk += 1 
    
    raceTable[kk][1] = u"Dwars"
    raceTable[kk][2] = u"Westhoek"
    raceTable[kk][3] = 3716807
    raceTable[kk][4] = u"de "
    kk += 1 
    
    raceTable[kk][1] = u"Vuelta"
    raceTable[kk][2] = u"Guatemala"
    raceTable[kk][3] = 55739408
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Bretagne"
    raceTable[kk][3] =1628953
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Veenendaal"
    raceTable[kk][2] = u"Classic"
    raceTable[kk][3] =56257178
    raceTable[kk][4] = u"de la "
    kk += 1    
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Euromat"
    raceTable[kk][3] =79034830
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Grote Prijs"
    raceTable[kk][2] = u"Euromat"
    raceTable[kk][3] =79034830
    raceTable[kk][4] = u"du "
    kk += 1
    
    
    raceTable[kk][1] = u"Horizon Park"
    raceTable[kk][2] = u"Race"
    raceTable[kk][3] =30051111
    raceTable[kk][4] = u"de la "
    kk += 1    

    raceTable[kk][1] = u"Kievskaya"
    raceTable[kk][2] = u"Challenge"
    raceTable[kk][3] =30051111
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"IJsseldelta"
    raceTable[kk][3] =23843462
    raceTable[kk][4] = u"de l'"
    kk += 1 
    
    

    raceTable[kk][1] = u"Chrono"
    raceTable[kk][2] = u"Gatineau"
    raceTable[kk][3] =1088102
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Gatineau"
    raceTable[kk][3] =3775093
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Gatineau"
    raceTable[kk][3] =3775093
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Ljubljana"
    raceTable[kk][2] = u"TT"
    raceTable[kk][3] =17099191
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Thüringen"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] =314687
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Plumelec"
    raceTable[kk][3] =16982488
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Morbihan"
    raceTable[kk][3] =16982488
    raceTable[kk][4] = u"du "
    kk += 1     
    
    
    raceTable[kk][1] = u"Classique"
    raceTable[kk][2] = u"Morbihan"
    raceTable[kk][3] =24262795
    raceTable[kk][4] = u"de la "
    kk += 1    
    
    raceTable[kk][1] = u"Winston Salem"
    raceTable[kk][2] = u"Classic"
    raceTable[kk][3] =16987217
    raceTable[kk][4] = u"de la "
    kk += 1      
    
    raceTable[kk][1] = u"VR Women"
    raceTable[kk][2] = u"ITT"
    raceTable[kk][3] =30051105
    raceTable[kk][4] = u"du "
    kk += 1      

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Taiyuan"
    raceTable[kk][3] =61003704
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"GP"
    raceTable[kk][2] = u"Cham-Hagendorn"
    raceTable[kk][3] =29983421
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Emakumeen"
    raceTable[kk][2] = u"Bira"
    raceTable[kk][3] =1334580
    raceTable[kk][4] = u"de l'"
    kk += 1 
    
    raceTable[kk][1] = u"Kiev Olimpic"
    raceTable[kk][2] = u"Ring"
    raceTable[kk][3] =61013868
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Trofee"
    raceTable[kk][2] = u"Maarten Wynants"
    raceTable[kk][3] =22008927
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Chongming"
    raceTable[kk][3] =15666441
    raceTable[kk][4] = u"du "
    kk += 1    

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Uppsala"
    raceTable[kk][3] =52456674
    raceTable[kk][4] = u"du "
    kk += 1    

    raceTable[kk][1] = u"Liège"
    raceTable[kk][2] = u"Bastogne"
    raceTable[kk][3] =27538455
    raceTable[kk][4] = u"de "
    kk += 1 

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Yorkshire"
    raceTable[kk][3] =24009981
    raceTable[kk][4] = u"du "
    kk += 1     

    raceTable[kk][1] = u"Island II"
    raceTable[kk][2] = u"Zhoushan"
    raceTable[kk][3] =13362122
    raceTable[kk][4] = u"du "
    kk += 1     

    raceTable[kk][1] = u"Durango"
    raceTable[kk][2] = u"Saria"
    raceTable[kk][3] =3716453
    raceTable[kk][4] = u"de la "
    kk += 1     

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Venezuela 2"
    raceTable[kk][3] =63976580
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"Vuelta"
    raceTable[kk][2] = u"Burgos"
    raceTable[kk][3] =60963675
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Elsy"
    raceTable[kk][2] = u"Jacobs"
    raceTable[kk][3] =2364254
    raceTable[kk][4] = u"du "
    kk += 1    
  
    raceTable[kk][1] = u"Gracia"
    raceTable[kk][2] = u"Gracia"
    raceTable[kk][3] =1332724
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Gila"
    raceTable[kk][3] =29054378
    raceTable[kk][4] = u"du "
    kk += 1    
    
    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"Borsele"
    raceTable[kk][3] =2973988
    raceTable[kk][4] = u"du "
    kk += 1    
 
    raceTable[kk][1] = u"Flèche"
    raceTable[kk][2] = u"Wallonne"
    raceTable[kk][3] =508838
    raceTable[kk][4] = u"de la "
    kk += 1
 
    raceTable[kk][1] = u"Amstel"
    raceTable[kk][2] = u"Gold"
    raceTable[kk][3] =3614690
    raceTable[kk][4] = u"de l'"
    kk += 1
    
    raceTable[kk][1] = u"Brabantse"
    raceTable[kk][2] = u"Pijl"
    raceTable[kk][3] =51717210
    raceTable[kk][4] = u"de la "
    kk += 1    

    raceTable[kk][1] = u"Healthy"
    raceTable[kk][2] = u"Ageing"
    raceTable[kk][3] =1341486
    raceTable[kk][4] = u"de l'"
    kk += 1
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Dottignies"
    raceTable[kk][3] =3774953
    raceTable[kk][4] = u"du "
    kk += 1    

    raceTable[kk][1] = u"Joe Martin"
    raceTable[kk][2] = u"Race"
    raceTable[kk][3] =29060753
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u"Aphrodite"
    raceTable[kk][2] = u"Sanctuary"
    raceTable[kk][3] =61014201
    raceTable[kk][4] = u"de l'"
    kk += 1     
    
    raceTable[kk][1] = u"Aphrodite"
    raceTable[kk][2] = u"Time"
    raceTable[kk][3] =62577415
    raceTable[kk][4] = u"de l'"
    kk += 1        
    
    raceTable[kk][1] = u"Nokere"
    raceTable[kk][2] = u"Koerse"
    raceTable[kk][3] =60821013
    raceTable[kk][4] = u"de la "
    kk += 1    

    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"Westhoek"
    raceTable[kk][3] =50281020
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"Justiniano"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =65042342
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Velo Alanya"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =47531313
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Arava"
    raceTable[kk][3] =61003023
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Scorpions"
    raceTable[kk][2] = u"ITT"
    raceTable[kk][3] =61002924
    raceTable[kk][4] = u"du "
    kk += 1  
   
    raceTable[kk][1] = u"Setmana"
    raceTable[kk][2] = u"Valenciana"
    raceTable[kk][3] =28752781
    raceTable[kk][4] = u"de la "
    kk += 1 

    raceTable[kk][1] = u"Alanya"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =60965348
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Cappadocia"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =79031829
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Occitanie"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] =79032374
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Develi"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =79031767
    raceTable[kk][4] = u"du "
    kk += 1    
    
    raceTable[kk][1] = u"Central Anatolia"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =79032793
    raceTable[kk][4] = u"du "
    kk += 1    
        
    raceTable[kk][1] = u"Trophée"
    raceTable[kk][2] = u"Grimpeuses"
    raceTable[kk][3] =79032472
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u"Grote prijs"
    raceTable[kk][2] = u"Beerens"
    raceTable[kk][3] =77559206
    raceTable[kk][4] = u"du "
    kk += 1 
     
    raceTable[kk][1] = u"Watersley"
    raceTable[kk][2] = u"Challenge"
    raceTable[kk][3] =79032687
    raceTable[kk][4] = u"du "
    kk += 1      

   
    raceTable[kk][1] = u"Kayseri"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =79031695
    raceTable[kk][4] = u"du "
    kk += 1
 
    raceTable[kk][1] = u"Grand Prix Erciyes"
    raceTable[kk][2] = u"Grand Prix Erciyes"
    raceTable[kk][3] =79032136
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Velo Erciyes"
    raceTable[kk][3] =79033022
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Mount Erciyes"
    raceTable[kk][3] =79033120
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"High Altitude"
    raceTable[kk][3] =79033205
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Malaysia"
    raceTable[kk][3] =79033337
    raceTable[kk][4] = u"du "
    kk += 1
    
    raceTable[kk][1] = u"Chabany"
    raceTable[kk][2] = u"Race"
    raceTable[kk][3] =79031524
    raceTable[kk][4] = u"de la "
    kk += 1   

    raceTable[kk][1] = u"Ciudad"
    raceTable[kk][2] = u"Eibar"
    raceTable[kk][3] =79032029
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Gazipasa"
    raceTable[kk][2] = u"Grand Prix"
    raceTable[kk][3] =60965049
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Herald Sun"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] =47509863
    raceTable[kk][4] = u"du "
    kk += 1   

    raceTable[kk][1] = u"Cadel Evans"
    raceTable[kk][2] = u"Race"
    raceTable[kk][3] =28536664
    raceTable[kk][4] = u"de la "
    kk += 1   
    
    raceTable[kk][1] = u"Gravel"
    raceTable[kk][2] = u"Tar"
    raceTable[kk][3] =60642923
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"Gran Premio"
    raceTable[kk][2] = u"Comite Olimpico"
    raceTable[kk][3] =57967831
    raceTable[kk][4] = u"du "
    kk += 1  
    
    raceTable[kk][1] = u"Ronde"
    raceTable[kk][2] = u"Mouscron"
    raceTable[kk][3] =77558798
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u"Districtenpijl"
    raceTable[kk][2] = u"Districtenpijl"
    raceTable[kk][3] =77559070
    raceTable[kk][4] = u"de la "
    kk += 1 
   
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Beerens"
    raceTable[kk][3] =77559206
    raceTable[kk][4] = u"du "
    kk += 1 
   
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Guangxi"
    raceTable[kk][3] =42394196
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u"Bloeizone"
    raceTable[kk][2] = u"Fryslan"
    raceTable[kk][3] =110763940
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"Trofeo"
    raceTable[kk][2] = u"Oro in Euro"
    raceTable[kk][3] =110764022
    raceTable[kk][4] = u"du "
    kk += 1    
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Mediterrennean"
    raceTable[kk][3] =105811175
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"GRAN PREMIO"
    raceTable[kk][2] = u"LIBERAZIONE"
    raceTable[kk][3] =3774541
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u"Leiedal"
    raceTable[kk][2] = u"Koerse"
    raceTable[kk][3] =110764040
    raceTable[kk][4] = u"de la "
    kk += 1  
  
    raceTable[kk][1] = u"Andalucia"
    raceTable[kk][2] = u"Ruta Del Sol"
    raceTable[kk][3] =110764063
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"Omloop"
    raceTable[kk][2] = u"Kempen"
    raceTable[kk][3] =110764076
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Estonia"
    raceTable[kk][3] =110764090
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Kyiv"
    raceTable[kk][2] = u"Cup"
    raceTable[kk][3] =110764507
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u"Kyiv"
    raceTable[kk][2] = u"Green Race"
    raceTable[kk][3] =110764558
    raceTable[kk][4] = u"de la "
    kk += 1 
    
    raceTable[kk][1] = u"Belgrade"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 107233692
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Monica"
    raceTable[kk][2] = u"Bandini"
    raceTable[kk][3] = 110764703
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"Alpes"
    raceTable[kk][2] = u"Gresivaudan"
    raceTable[kk][3] = 110764826
    raceTable[kk][4] = u"de la "
    kk += 1   

    raceTable[kk][1] = u"GP"
    raceTable[kk][2] = u"Schelkens"
    raceTable[kk][3] = 110764947
    raceTable[kk][4] = u"du "
    kk += 1     

    raceTable[kk][1] = u"Mont Ventoux"
    raceTable[kk][2] = u"Challenges"
    raceTable[kk][3] = 110322011
    raceTable[kk][4] = u"du "
    kk += 1  

    raceTable[kk][1] = u"GP"
    raceTable[kk][2] = u"Slovakia"
    raceTable[kk][3] = 110765084
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"Visegrad"
    raceTable[kk][2] = u"Hungary"
    raceTable[kk][3] = 110765104
    raceTable[kk][4] = u"du "
    kk += 1    
    
    raceTable[kk][1] = u"Tour de France"
    raceTable[kk][2] = u"Femmes"
    raceTable[kk][3] = 1542952
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Anna Vasa"
    raceTable[kk][2] = u"Race"
    raceTable[kk][3] = 110765120
    raceTable[kk][4] = u"de la "
    kk += 1 

    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Kalmar"
    raceTable[kk][3] = 110765135
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Yahyalı"
    raceTable[kk][3] = 110765155
    raceTable[kk][4] = u"du "
    kk += 1 
 
    raceTable[kk][1] = u"Coupe d'Europe"
    raceTable[kk][2] = u"Grimpeurs"
    raceTable[kk][3] = 110765167
    raceTable[kk][4] = u"de la "
    kk += 1 

    raceTable[kk][1] = u"Vuelta"
    raceTable[kk][2] = u"Colombia"
    raceTable[kk][3] = 27684043
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"GP"
    raceTable[kk][2] = u"Yvonne Reynders"
    raceTable[kk][3] = 110765321
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Grote Prijs"
    raceTable[kk][2] = u"Yvonne Reynders"
    raceTable[kk][3] = 110765321
    raceTable[kk][4] = u"du "
    kk += 1 

    raceTable[kk][1] = u"La Route"
    raceTable[kk][2] = u"Géantes"
    raceTable[kk][3] = 110765379
    raceTable[kk][4] = u"de "
    kk += 1 
    
    raceTable[kk][1] = u"Grand Prix"
    raceTable[kk][2] = u"Wallonie"
    raceTable[kk][3] = 110765400
    raceTable[kk][4] = u"du "
    kk += 1     

    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Semois"
    raceTable[kk][3] = 79032472
    raceTable[kk][4] = u"du "
    kk += 1   
    
    raceTable[kk][1] = u"Binche"
    raceTable[kk][2] = u"Chimay"
    raceTable[kk][3] = 110765414
    raceTable[kk][4] = u"du "
    kk += 1
      
    raceTable[kk][1] = u"Syrian"
    raceTable[kk][2] = u"Tour"
    raceTable[kk][3] = 110765437
    raceTable[kk][4] = u"du "
    kk += 1 
    
    raceTable[kk][1] = u"Tour"
    raceTable[kk][2] = u"Romandie"
    raceTable[kk][3] = 110765449
    raceTable[kk][4] = u"du "
    kk += 1     
    
    raceTable[kk][1] = u"Travers"
    raceTable[kk][2] = u"Hauts de France"
    raceTable[kk][3] = 110765397
    raceTable[kk][4] = u"d'"
    kk += 1    

    final_table = [['' for x in range(5)] for y in range(kk)]
    final_table=raceTable[:kk]
    
    return final_table, race_dic