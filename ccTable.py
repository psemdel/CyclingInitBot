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
    

    
    kk = 1
    
    teamTable[kk][1]=u'Océanie'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=2954777
    teamTable[kk][4]=54315111
    teamTable[kk][5]=54314912
    kk+=1
    
    teamTable[kk][1]=u'Europe'
    teamTable[kk][2]=u"d'"
    teamTable[kk][3]=2954514
    teamTable[kk][4]=30894544
    teamTable[kk][5]=30894543
    kk+=1
    
    return [teamTable, kk]