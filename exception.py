#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:10:26 2019

@author: maxime
"""
def list_of_rider_exception():
    exceptionTable = [['' for x in range(2)] for y in range(200)]
    kk = 0

    exceptionTable[kk][0] = u'Anne Palm'
    exceptionTable[kk][1] = u'Q62121769'
    kk += 1
    exceptionTable[kk][0] = u'paulien rooijakkers'
    exceptionTable[kk][1] = u'Q19577695'
    kk += 1
    exceptionTable[kk][0] = u'margarita victo garcia cañellas'
    exceptionTable[kk][1] = u'Q23907253'
    kk += 1

    exceptionTable[kk][0] = u'Jessica Allen'
    exceptionTable[kk][1] = u'Q27306413'
    kk += 1

    exceptionTable[kk][0] = u'Nikolas Maes'
    exceptionTable[kk][1] = u'Q1991336'
    kk += 1
    exceptionTable[kk][0] = u'jolien d`hoore'
    exceptionTable[kk][1] = u'Q440790'
    kk += 1
    exceptionTable[kk][0] = u'Claire Moore'
    exceptionTable[kk][1] = u'Q63040077'
    kk += 1
    exceptionTable[kk][0] = u'Kelly Murphy'
    exceptionTable[kk][1] = u'Q33083846'
    kk += 1
    exceptionTable[kk][0] = u'Emma Smith'
    exceptionTable[kk][1] = u'Q64143672'
    kk += 1
    exceptionTable[kk][0] = u'Maja Savic'
    exceptionTable[kk][1] = u'Q59185359'
    kk += 1
    exceptionTable[kk][0] = u'Maja Savić'
    exceptionTable[kk][1] = u'Q59185359'
    kk += 1
    exceptionTable[kk][0] = u'Katharine Hall'
    exceptionTable[kk][1] = u'Q17306130'
    kk += 1
    exceptionTable[kk][0] = u'Elizabeth Bennett'
    exceptionTable[kk][1] = u'Q57956663'
    kk += 1
    exceptionTable[kk][0] = u'charlotte mitchell'
    exceptionTable[kk][1] = u'Q66370894'
    kk += 1
    exceptionTable[kk][0] = u'Sandra Gómez'
    exceptionTable[kk][1] = u'Q23785379'
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exceptionTable[:kk]
            
    return  final_table


def list_of_team_name_exception():
    teamList = [['' for x in range(2)] for y in range(100)]
    kk = 0

    teamList[kk][0] = u'CANYON // SRAM RACING'
    teamList[kk][1] = u'Q45536829'
    kk += 1
    teamList[kk][0] = u'WIGGLE HIGH5'
    teamList[kk][1] = u'Q47034223'
    kk += 1
    teamList[kk][0] = u'WAOWDEALS PRO CYCLING TEAM'
    teamList[kk][1] = u'Q45900995'
    kk += 1
    teamList[kk][0] = u'MITCHELTON SCOTT'
    teamList[kk][1] = u'Q43144477'
    
    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exceptionTable[:kk]
            
    return  final_table


def list_of_team_code_exception():
    exceptionTable = [['' for x in range(2)] for y in range(100)]
    kk = 0

    exceptionTable[kk][0] = u'ORS 2017'
    exceptionTable[kk][1] = u'Q27865610'
    kk += 1
    exceptionTable[kk][0] = u'SUN 2017'
    exceptionTable[kk][1] = u'Q28133168'
    kk += 1
    exceptionTable[kk][0] = u'LSL 2017'
    exceptionTable[kk][1] = u'Q28047488'
    kk += 1
    exceptionTable[kk][0] = u'LSL 2019'
    exceptionTable[kk][1] = u'Q56760475'
    kk += 1
    exceptionTable[kk][0] = u'ILU 2019'
    exceptionTable[kk][1] = u'Q61510587'
    kk += 1
    exceptionTable[kk][0] = u'LCW 2019'
    exceptionTable[kk][1] = u'Q61449735'
    kk += 1
    exceptionTable[kk][0] = u'MCC 2019'
    exceptionTable[kk][1] = u'Q61451340'

    final_table = [['' for x in range(2)] for y in range(kk)]
    final_table=exceptionTable[:kk]
            
    return  final_table

