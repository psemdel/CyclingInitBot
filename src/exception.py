#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:10:26 2019

@author: maxime
"""
def list_of_rider_exception():
    exception_table = [['' for x in range(2)] for y in range(200)]
    kk = 0

    exception_table[kk][0] = u'Anne Palm'
    exception_table[kk][1] = u'Q62121769'
    kk += 1
    exception_table[kk][0] = u'paulien rooijakkers'
    exception_table[kk][1] = u'Q19577695'
    kk += 1
    exception_table[kk][0] = u'GARCIA CAÑELLAS Margarita Victo'
    exception_table[kk][1] = u'Q23907253'
    kk += 1
    
    exception_table[kk][0] = u'margarita victo garcia cañellas'
    exception_table[kk][1] = u'Q23907253'
    kk += 1
    
    exception_table[kk][0] = u'margarita victo garcia canellas'
    exception_table[kk][1] = u'Q23907253'
    kk += 1   

    exception_table[kk][0] = u'Jessica Allen'
    exception_table[kk][1] = u'Q27306413'
    kk += 1

    exception_table[kk][0] = u'Nikolas Maes'
    exception_table[kk][1] = u'Q1991336'
    kk += 1
    exception_table[kk][0] = u'jolien d`hoore'
    exception_table[kk][1] = u'Q440790'
    kk += 1
    exception_table[kk][0] = u'jolien dhoore'
    exception_table[kk][1] = u'Q440790'
    kk += 1
    exception_table[kk][0] = u'Claire Moore'
    exception_table[kk][1] = u'Q63040077'
    kk += 1
    exception_table[kk][0] = u'Kelly Murphy'
    exception_table[kk][1] = u'Q33083846'
    kk += 1
    exception_table[kk][0] = u'Emma Smith'
    exception_table[kk][1] = u'Q64143672'
    kk += 1
    exception_table[kk][0] = u'Maja Savic'
    exception_table[kk][1] = u'Q59185359'
    kk += 1
    exception_table[kk][0] = u'Maja Savić'
    exception_table[kk][1] = u'Q59185359'
    kk += 1
    exception_table[kk][0] = u'Katharine Hall'
    exception_table[kk][1] = u'Q17306130'
    kk += 1
    exception_table[kk][0] = u'Elizabeth Bennett'
    exception_table[kk][1] = u'Q57956663'
    kk += 1
    exception_table[kk][0] = u'charlotte mitchell'
    exception_table[kk][1] = u'Q66370894'
    kk += 1
    exception_table[kk][0] = u'Sandra Gómez'
    exception_table[kk][1] = u'Q23785379'
    kk += 1
    exception_table[kk][0] = u'1501996785028 ERIC'
    exception_table[kk][1] = u'Q19661759'
    kk += 1     
    exception_table[kk][0] = u'ERIĆ 1501996785028'
    exception_table[kk][1] = u'Q19661759'
    kk += 1    
    exception_table[kk][0] = u'1501996785028 ERIĆ'
    exception_table[kk][1] = u'Q19661759'
    kk += 1     
    exception_table[kk][0] = u'1501996785028 ERIĆ 1501996785028 ERIĆ'
    exception_table[kk][1] = u'Q19661759'
    kk += 1  
    exception_table[kk][0] = u'ERIĆ 1501996785028 ERIĆ 1501996785028'
    exception_table[kk][1] = u'Q19661759'
    kk += 1      

    #men
    exception_table[kk][0] = u'Felix Gross'
    exception_table[kk][1] = u'Q39885866'
    kk += 1
    
    
    
    
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exception_table[:kk]
            
    return  final_table


def list_of_team_name_exception():
    exception_table = [['' for x in range(2)] for y in range(100)]
    kk = 0

    exception_table[kk][0] = u'CANYON // SRAM RACING'
    exception_table[kk][1] = u'Q45536829'
    kk += 1
    exception_table[kk][0] = u'WIGGLE HIGH5'
    exception_table[kk][1] = u'Q47034223'
    kk += 1
    exception_table[kk][0] = u'WAOWDEALS PRO CYCLING TEAM'
    exception_table[kk][1] = u'Q45900995'
    kk += 1
    exception_table[kk][0] = u'MITCHELTON SCOTT'
    exception_table[kk][1] = u'Q43144477'
    kk += 1
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exception_table[:kk]
         
    return  final_table

#woman
def list_of_team_code_exception():
    exception_table = [['' for x in range(2)] for y in range(100)]
    kk = 0

    exception_table[kk][0] = u'ORS 2017'
    exception_table[kk][1] = u'Q27865610'
    kk += 1
    exception_table[kk][0] = u'SUN 2017'
    exception_table[kk][1] = u'Q28133168'
    kk += 1
    exception_table[kk][0] = u'LSL 2017'
    exception_table[kk][1] = u'Q28047488'
    kk += 1
    exception_table[kk][0] = u'LSL 2019'
    exception_table[kk][1] = u'Q56760475'
    kk += 1
    exception_table[kk][0] = u'ILU 2019'
    exception_table[kk][1] = u'Q61510587'
    kk += 1
    exception_table[kk][0] = u'LCW 2019'
    exception_table[kk][1] = u'Q61449735'
    kk += 1
    exception_table[kk][0] = u'MCC 2019'
    exception_table[kk][1] = u'Q61451340'
    kk += 1
    exception_table[kk][0] = u'MTS 2020'
    exception_table[kk][1] = u'Q74725715'    
    kk += 1
    exception_table[kk][0] = u'TFS 2020'
    exception_table[kk][1] = u'Q82315001'   
    kk += 1
    exception_table[kk][0] = u'SUN 2020'
    exception_table[kk][1] = u'Q74726068'   
    kk += 1
    exception_table[kk][0] = u'CCC 2020'
    exception_table[kk][1] = u'Q74726282'   
    kk += 1  
    exception_table[kk][0] = u'LSL 2020'
    exception_table[kk][1] = u'Q74725666'   
    kk += 1   
    exception_table[kk][0] = u'MOV 2020'
    exception_table[kk][1] = u'Q74725765'   
    kk += 1
    exception_table[kk][0] = u'ARK 2020'
    exception_table[kk][1] = u'Q83972829'   
    kk += 1   
    exception_table[kk][0] = u'MCC 2020'
    exception_table[kk][1] = u'Q85546997'   
    kk += 1       
    exception_table[kk][0] = u'ILU 2020'
    exception_table[kk][1] = u'Q86102811'   
    kk += 1       
    exception_table[kk][0] = u'TFS 2021'
    exception_table[kk][1] = u'Q104525637'   
    kk += 1       
    exception_table[kk][0] = u'MOV 2021'
    exception_table[kk][1] = u'Q104525417'   
    kk += 1 
    exception_table[kk][0] = u'BEX 2021'
    exception_table[kk][1] = u'Q104523283'   
    kk += 1   
    exception_table[kk][0] = u'DSM 2021'
    exception_table[kk][1] = u'Q104525447'   
    kk += 1      
    exception_table[kk][0] = u'ARK 2021'
    exception_table[kk][1] = u'Q104889619'   
    kk += 1      
    exception_table[kk][0] = u'CCM 2021'
    exception_table[kk][1] = u'Q106474502'   
    kk += 1     
    exception_table[kk][0] = u'MCC 2021'
    exception_table[kk][1] = u'Q105811484'   
    kk += 1     
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exception_table[:kk]
            
    return  final_table

def list_of_team_code_exception_man():
    exception_table = [['' for x in range(2)] for y in range(100)]
    kk = 0

    exception_table[kk][0] = u'MTS 2020'
    exception_table[kk][1] = u'Q78075331'    
    kk += 1
    exception_table[kk][0] = u'TFS 2020'
    exception_table[kk][1] = u'Q78075353'      
    kk += 1
    exception_table[kk][0] = u'SUN 2020'
    exception_table[kk][1] = u'Q78075349'   
    kk += 1
    exception_table[kk][0] = u'CCC 2020'
    exception_table[kk][1] = u'Q78075307'   
    kk += 1
    exception_table[kk][0] = u'MOV 2020'
    exception_table[kk][1] = u'Q78075334'   
    kk += 1
    exception_table[kk][0] = u'ARK 2020'
    exception_table[kk][1] = u'Q79434602'   
    kk += 1
    exception_table[kk][0] = u'MCC 2020'
    exception_table[kk][1] = u'Q85537002'   
    kk += 1    
    exception_table[kk][0] = u'ILU 2020'
    exception_table[kk][1] = u'Q83016986'   
    kk += 1     
    exception_table[kk][0] = u'TFS 2021'
    exception_table[kk][1] = u'Q102115546'   
    kk += 1     
    exception_table[kk][0] = u'MOV 2021'
    exception_table[kk][1] = u'Q102248307'   
    kk += 1  
    exception_table[kk][0] = u'BEX 2021'
    exception_table[kk][1] = u'Q102247786'   
    kk += 1   
    exception_table[kk][0] = u'DSM 2021'
    exception_table[kk][1] = u'Q102248403'   
    kk += 1     
    exception_table[kk][0] = u'ARK 2021'
    exception_table[kk][1] = u'Q104537408'   
    kk += 1      
    exception_table[kk][0] = u'CCM 2021'
    exception_table[kk][1] = u'Q105410552'   
    kk += 1     
    exception_table[kk][0] = u'MCC 2021'
    exception_table[kk][1] = u'Q105333983'   
    kk += 1     
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exception_table[:kk]
            
    return  final_table
