#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:54:17 2019

@author: maxime
"""
from cycling_init_bot_low import *
from race_creator import *
# ==Initialisation==
def UCI_calendar_importer(pywikibot, site, repo, time, team_table, separator, test, race_table):
    #title in table, column in table, column in result_table
    result_dic={
            'date from':[-1, 0,''],
            'date to':[-1, 1,''],
            'name':[-1, 2,''],
            'country':[-1, 3,''],
            'class':[-1,4,'']
            }
    verbose=False
   
    result_table, row_count, ecart_global=table_reader('input/Calendar.csv',separator,result_dic,1)
    if verbose:
        print(result_table)
        
    for kk in range(row_count):
        id_master = '0'
        if result_table[kk][result_dic['name'][1]] != 0:
            #read class
            if result_table[kk][result_dic['class'][1]] != 0:
                classe = result_table[kk][result_dic['class'][1]]

            #look in the list of race available which one it is
            id_master, master_genre =search_race(
                result_table[kk][result_dic['name'][1]], race_table)
            
            if id_master != 0 and id_master != '0' and classe != 0:
                item_master = pywikibot.ItemPage(repo, "Q" + str(id_master))
                item_master.get()
                master_name = item_master.labels["fr"]

                if result_table[kk][result_dic['date from'][1]] != 0:
                    start_date = result_table[kk][result_dic['date from'][1]]
                    table_date = start_date.split("/")
                    year = int(table_date[2])
                    race_begin = pywikibot.WbTime(
                        site=site,
                        year=int(table_date[2]),
                        month=int(table_date[1]),
                        day=int(table_date[0]),
                        precision='day')
                    if classe == "1.1" or classe == "1.2" or classe == "1.WWT" or classe =="1.Pro":
                        single_race=True
                    elif classe == "2.1" or classe == "2.2" or classe == "2.WWT" or classe =="2.Pro":
                        single_race=False
                    if classe == "1.1" or classe == "1.2" or classe == "2.1" or classe == "2.2" or classe =="1.Pro" or classe =="2.Pro":
                        UCI = True
                        WWT = False
                    elif classe == "1.WWT" or classe == "2.WWT":
                        UCI = False
                        WWT = True
                        
                    #note: country is a name which is not correct, make inherit the country
                    #note 2: get edition from last year
                    if single_race:
                        if not test:
                            race_creator(
                                    pywikibot,
                                    site,
                                    repo,
                                    time,
                                    team_table,
                                    master_name,
                                    master_genre,
                                    id_master,
                                    year,
                                    UCI,
                                    WWT,
                                    race_begin,
                                    result_table[kk][result_dic['country'][1]],
                                    classe,
                                    True
                                    )
                    else: #stage race
                        if result_table[kk][result_dic['date to'][1]] != 0:
                            end_date = result_table[kk][result_dic['date to'][1]]
                            table_tate = end_date.split("/")
                            stage_race_end = pywikibot.WbTime(
                                site=site,
                                year=int(table_tate[2]),
                                month=int(table_tate[1]),
                                day=int(table_date[0]),
                                precision='day')

                            if not test:
                                race_creator(
                                    pywikibot,
                                    site,
                                    repo,
                                    time,
                                    team_table,
                                    master_name,
                                    master_genre,
                                    id_master,
                                    year,
                                    UCI,
                                    WWT,
                                    race_begin,
                                    result_table[kk][result_dic['country'][1]],
                                    classe,
                                    False,
                                    end_date=stage_race_end,
                                    only_stages= False,
                                    create_stages=False,
                                    )

            elif classe != "CN" and classe != "CC" and classe !="CRT":
                print(result_table[kk][2])
                print("race not found")

