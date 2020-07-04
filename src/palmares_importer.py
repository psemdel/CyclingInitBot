# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:35:54 2018

@author: maxime delzenne
"""
from .cycling_init_bot_low import search_item, get_label, add_winner
                                  
import exception 

def f(pywikibot, site, repo, id_championship, test):
   # Q31271010
    inputstr = """
|-
| 2006 || [[Evelyn García]] || [[Ana Gabriela Larios]] ||  [[Ana Gabriela Larios]]
|-
| 2007 || [[Evelyn García]] || [[Michelle Ortiz]] || [[Priscila Ramos]]
|-
| 2008 || [[Roxana Ortiz]] || [[Priscila Ramos]] ||  [[Priscila Ramos]]
|-
| 2009 || [[Evelyn García]] || [[Michelle Ortiz]] || [[Xenia Estrada]]
|-
| 2010 || [[Evelyn García]] || [[Xenia Estrada]] || [[Nathaly Majano]]
|-
| 2011 || [[Evelyn García]] || [[Roxana Ortiz]] || [[Beatriz Quiroz]]
|-
| 2012 || [[Xenia Estrada]] || [[Ana Figueroa]] || [[Nathaly Majano]]
|-
| 2013 || [[Ana Figueroa]] || [[Xenia Estrada]] || [[Karen Cruz]]
|-
| 2014 || [[Xenia Estrada]] || [[Ana Figueroa]] ||[[Ana Figueroa]]
|-
| 2015 || [[Evelyn García]] || [[Aída Turcios]] || [[Ana Figueroa]]
|-
| 2016 || [[Ana Figueroa]] || [[Roxana Ortiz]] || [[Vanessa Serrano]]
|-
| 2017 || [[Evelyn García]] || [[Ana Figueroa]] || [[Xenia Estrada]]
|-
| 2018 || [[Roxana Ortiz]] || [[Brenda Aparicio]] || [[Alejandra Cardona]]
|-
| 2019 || [[Xenia Estrada]] || [[Vanessa Serrano]] || [[Sauking Shi]]
 """

    def palmaresParsing(inputstr):
        # parsing of the raw input
        tableofRow = inputstr.split("|-")
        column_of_winner = 1
        table_of_winners = [[0 for x in range(4)] for y in range(len(tableofRow) - 1)]
    
        for ii in range(0, len(tableofRow) - 1):  # range(len(tableofRow))
            tableofCell = {}
            tableofCell = tableofRow[1 + ii].split("||")
            # get the year
            tempforyear = tableofCell[0].split("|")
            table_of_winners[ii][0] = int(tempforyear[1])  # link[0]
            # get first winner
            for jj in range(column_of_winner, column_of_winner + 3):
                linksplit1 = tableofCell[jj].split("[[")
                link = linksplit1[1].split("]]")
                table_of_winners[ii][jj - column_of_winner + 1] = link[0]
    
        return table_of_winners
        # print(table_of_winners)
    
    
    def palmaresFilling(pywikibot, site, repo, table_of_winners, id_championship):
        item_master = pywikibot.ItemPage(repo, id_championship)
        item_master.get()
        masterlabel = get_label('fr', item_master)
    
        for ii in range(len(table_of_winners)):  # range(len(table_of_winners))
            year = table_of_winners[ii][0]
            print(year)
            present_label = masterlabel + " " + str(year)
            # look for the race
            present_id = search_item(pywikibot, site, present_label)
            if (present_id == u'Q0'):
                print(present_label  + ' not present')
            elif (present_id == u'Q1'):
                print(present_label  + ' present several times')
            else:  # good
                item_present = pywikibot.ItemPage(repo, present_id)
                item_present.get()
                add_winner(
                    pywikibot,
                    site,
                    repo,
                    item_present,
                    table_of_winners[ii][1],
                    1,
                    0)
                add_winner(
                    pywikibot,
                    site,
                    repo,
                    item_present,
                    table_of_winners[ii][2],
                    2,
                    0)
                add_winner(
                    pywikibot,
                    site,
                    repo,
                    item_present,
                    table_of_winners[ii][3],
                    3,
                    0)
                
    def wikidataelementAnalyser(pywikibot, site, repo, table_of_winners):
        # look for riders not created
        counter = 0
        counterrepeat = 0
        table_of_winnersOut = table_of_winners
        exception_table = exception.listOfException()
    
        for ii in range(len(table_of_winners)):
            for jj in range(1, 4):
                Idtemp = search_item(
                    pywikibot, site, table_of_winners[ii][jj])
                if (Idtemp == u'Q0'):  # no previous or several
                    print(table_of_winners[ii][jj] + ' not found')
                    counter = counter + 1
                elif (Idtemp == u'Q1'):
                    # list of exceptions
                    exceptionfound = 0
                    for ll in range(1, len(exception_table)):
                        if table_of_winners[ii][jj] == exception_table[ll][0]:
                            table_of_winnersOut[ii][jj] = exception_table[ll][1]
                            exceptionfound = 1
                    if exceptionfound == 0:
                        print(table_of_winners[ii][jj])
                        print(table_of_winners[ii][jj] + ' found several times')
                        counterrepeat += 1
                else:
                    table_of_winnersOut[ii][jj] = Idtemp

        if counter == 0 and counterrepeat == 0:
            print('All riders found!!')
        elif counterrepeat == 0:
            print(str(counter) + ' riders not found')
        else:
            print(str(counterrepeat) + ' riders found several times')
    
        return counter, counterrepeat, table_of_winnersOut            
                
    # inputstr=input()
    table_of_winners = palmaresParsing(inputstr)
    # print(table_of_winners)
    numberofabsentriders, counterrepeat, table_of_winnersOut = wikidataelementAnalyser(
        pywikibot, site, repo, table_of_winners)

    if numberofabsentriders == 0 and test == 0 and counterrepeat == 0:
        palmaresFilling(
            pywikibot,
            site,
            repo,
            table_of_winnersOut,
            id_championship)

