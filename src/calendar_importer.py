#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:54:17 2019

@author: maxime
"""
from .cycling_init_bot_low import (noQ, table_reader, search_race, search_item,
                                   get_single_or_stage, get_country, get_label)
from src import race_creator
from .bot_log import Log

# ==Initialisation==
def f(pywikibot, site, repo, team_table, test, 
      race_table, race_dic, man_or_woman, filename, year):
    #title in table, column in table, column in result_table
    result_dic={
            'date from':[-1, 0,''],
            'date to':[-1, 1,''],
            'name':[-1, 2,''],
            'country':[-1, 3,''],
            'class':[-1,4,'']
            }
    verbose=False
    log=Log()

    result_table, row_count, ecart_global=table_reader(filename,result_dic,1,verbose)
    if verbose:
        log.concat(result_table)
        
    for kk in range(row_count):
        if result_table[kk][result_dic['name'][1]] != 0:
            #read class
            if result_table[kk][result_dic['class'][1]] != 0:
                classe = result_table[kk][result_dic['class'][1]]

            #look in the list of race available which one it is
            id_master, master_genre =search_race(
                result_table[kk][result_dic['name'][1]], race_table, race_dic)
            
            if id_master != "Q0" and classe != 0:
                item_master = pywikibot.ItemPage(repo, id_master)
                item_master.get()
                #same form as in national_table
                id_country=get_country(pywikibot, repo, id_master) #else Q0
               #     id_country=noQ(country_list[0].getTarget().getID())
     
                master_name =get_label('fr', item_master)
               # item_master.labels["fr"]

                if result_table[kk][result_dic['date from'][1]] != 0:
                    start_date = result_table[kk][result_dic['date from'][1]]
                    if "." in start_date:
                        table_date = start_date.split(".")
                    elif "/" in start_date:
                        table_date = start_date.split("/")
                    else:
                        print("date separator not recognized, please check")
                        return 10, log
                    year = int(table_date[2])
                    race_begin = pywikibot.WbTime(
                        site=site,
                        year=int(table_date[2]),
                        month=int(table_date[1]),
                        day=int(table_date[0]),
                        precision='day')
                    single_race=get_single_or_stage(classe) 

                    id_previous = search_item(pywikibot, site, master_name + " " +str(year-1))
                    edition_nr=''

                    if id_previous!=u'Q0' and id_previous!=u'Q1':
                        item_previous = pywikibot.ItemPage(repo,id_previous)
                        item_previous .get()
                        if(u'P393' in item_previous.claims): #edition
                            edition_list = item_previous.claims.get(u'P393')
                            edition_nr=int(edition_list[0].getTarget())+1
                    #note: country is a name which is not correct, make inherit the country
                    #note 2: get edition from last year
                    if single_race:
                        if not test:
                             status, log, res_id=race_creator.f(pywikibot,site,repo,
                                  team_table,
                                  master_name,
                                  single_race,
                                  man_or_woman,
                                  race_begin=race_begin,
                                  edition_nr=edition_nr,
                                  id_race_master=id_master,
                                  countryCIO=id_country,
                                  classe=classe,
                                  year=year
                                  )
                    else: #stage race
                        if result_table[kk][result_dic['date to'][1]] != 0:
                            end_date = result_table[kk][result_dic['date to'][1]]
                            if "." in end_date:
                                table_date = end_date.split(".")
                            elif "/" in start_date:
                                table_date = end_date.split("/")
                            else:
                                print("date separator not recognized, please check")
                                return 10, log
                            stage_race_end = pywikibot.WbTime(
                                site=site,
                                year=int(table_date[2]),
                                month=int(table_date[1]),
                                day=int(table_date[0]),
                                precision='day')

                            if not test:
                                status, log, res_id=race_creator.f(pywikibot,site,repo,
                                      team_table,
                                      master_name,
                                      single_race,
                                      man_or_woman,
                                      race_begin=race_begin,
                                      edition_nr=edition_nr,
                                      id_race_master=id_master,
                                      countryCIO=id_country,
                                      classe=classe,
                                      end_date=stage_race_end,
                                      only_stages=False,
                                      create_stages=False,
                                      year=year
                                      )

            elif classe != "CN" and classe != "CC" and classe !="CRT":
                log.concat(result_table[kk][2])
                log.concat("race not found")
    return 0, log   
