# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:46:11 2018

@author: maxime delzenne
"""

def ccTable():
    i, j = 20, 100;
    #For Europa
    teamTable = [[0 for x in range(i)] for y in range(j)] 
    
    #Item 1 = Continent name
    #Item 2 = genre
    #Item 3= National championship master
    #item 4= Road race woman
    #item 5= Clm woman
    #item 6= Road race man
    #item 7= Clm man
    #item 8= Road race woman U23
    #item 9= Clm woman U23
    kk = 1
    teamTable[kk][1]=u'monde'
    teamTable[kk][2]=u"du "
    teamTable[kk][3]=506424
    teamTable[kk][4]=934877
    teamTable[kk][5]=2630733
    kk+=1
    
    teamTable[kk][1]=u'Afrique'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=1771238
    teamTable[kk][4]=50064341
    teamTable[kk][5]=50063172
    teamTable[kk][6]=23069702
    kk+=1
    
    teamTable[kk][1]=u'Asie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=4806618
    teamTable[kk][4]=50061750
    teamTable[kk][5]=50062728
    kk+=1
   
    teamTable[kk][1]=u'panaméricains'
    teamTable[kk][2]=u""
    teamTable[kk][3]=18384474
    teamTable[kk][4]=31271454
    teamTable[kk][5]=31271381
    kk+=1
        
    teamTable[kk][1]=u'Océanie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=2954777
    teamTable[kk][4]=54315111
    teamTable[kk][5]=54314912
    teamTable[kk][6]=23889469
    
    kk+=1
    
    teamTable[kk][1]=u'Europe'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=2954514
    teamTable[kk][4]=30894544
    teamTable[kk][5]=30894543
    teamTable[kk][6]=30894537
    teamTable[kk][7]=33315723
    teamTable[kk][8]=3653998
    teamTable[kk][9]=3653993
    
    kk+=1
    
    return [teamTable, kk]