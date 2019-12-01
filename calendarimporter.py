#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:54:17 2019

@author: maxime
"""

import csv


import sys
import os
#from CyclingInitBotSub import *

# ==Initialisation==


def wikiinit():

    import time
    import sys
    sys.path.insert(0, '/disque1/Python/pywikibot')
    sys.path.insert(0, '/disque1/Python')
    sys.path.insert(0, '/disque1/Python/CyclingInitBot')
    import pywikibot
   ## import CyclingInitBotSub
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    ##import CyclingInitBotSub

    return [pywikibot, site, repo, time]


def RaceList():
    raceTable = [[0 for x in range(20)] for y in range(1000)]

    # 1: part 1 of the name
    # 2: part 2 of the name
    # 3: master
    # 4: genre

    kk = 1

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
    raceTable[kk][4] = u"de la "
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
    raceTable[kk][2] = u"Isbergue"
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

    raceTable[kk][1] = u'Lotto'
    raceTable[kk][2] = u"Belgium"
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

    raceTable[kk][1] = u'GP'
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

    raceTable[kk][1] = u'GP'
    raceTable[kk][2] = u"Plouay"
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

    return raceTable


def racesearch(name, raceTable):
    result = 0, 0

    for ii in range(len(raceTable)):
        if raceTable[ii][1] != 0 and raceTable[ii][2] != 0:
            if name.find(raceTable[ii][1]) != -1:
                if name.find(raceTable[ii][2]) != -1:
                    return raceTable[ii][3], raceTable[ii][4]

    return result


def UCIcalendarImporter(pywikibot, site, repo, teamTable, separator, test):
    raceTable = RaceList()
    resulttable = [[0 for x in range(10)] for y in range(2000)]

    kk = 0
    startdaterow = -1
    enddaterow = -1
    namerow = -1
    countryrow = -1
    classrow = -1

    with open('Calendar.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in spamreader:
            if kk == 1:
                print(row)
                for jj in range(len(row)):

                    if row[jj] == 'Date From':
                        startdaterow = jj
                    elif row[jj] == 'Date To':
                        enddaterow = jj
                    elif row[jj] == 'Name':
                        namerow = jj
                    elif row[jj] == 'Country':
                        countryrow = jj
                    elif row[jj] == 'Class':
                        classrow = jj
            elif kk != 0 and kk != 1:
                if startdaterow != -1:
                    resulttable[kk - 1][0] = row[startdaterow]
                if enddaterow != -1:
                    resulttable[kk - 1][1] = row[enddaterow]
                if namerow != -1:
                    resulttable[kk - 1][2] = row[namerow]
                if countryrow != -1:
                    resulttable[kk - 1][3] = row[countryrow]
                if classrow != -1:
                    resulttable[kk - 1][4] = row[classrow]  # time
            kk = kk + 1

        print('table read')
        for nn in range(kk + 1):
            MasterID = '0'
            if resulttable[nn][2] != 0:
                if resulttable[nn][4] != 0:
                    Class = resulttable[nn][4]

                MasterID, Mastergenre = racesearch(
                    resulttable[nn][2], raceTable)
                if MasterID != 0 and MasterID != '0' and Class != 0:
                    itemMaster = pywikibot.ItemPage(repo, "Q" + str(MasterID))
                    itemMaster.get()
                    Mastername = itemMaster.labels["fr"]

                    if resulttable[nn][0] != 0:
                        startdate = resulttable[nn][0]
                        tableDate = startdate.split("/")
                        Year = tableDate[2]
                        StageRaceBegin = pywikibot.WbTime(
                            site=site,
                            year=tableDate[2],
                            month=tableDate[1],
                            day=tableDate[0],
                            precision='day')

                        if Class == "1.1" or Class == "1.2" or Class == "1.WWT":
                            singlestagerace = 0
                        elif Class == "2.1" or Class == "2.2" or Class == "2.WWT":
                            singlestagerace = 1
                        if Class == "1.1" or Class == "1.2" or Class == "2.1" or Class == "2.2":
                            UCI = u"yes"
                            WWT = u"no"
                        elif Class == "1.WWT" or Class == "2.WWT":
                            UCI = u"no"
                            WWT = u"yes"
                        Onlystages = u"no"
                        Createstage = u"no"

                        if singlestagerace == 1:
                            if resulttable[nn][1] != 0:
                                enddate = resulttable[nn][0]
                                tableDate = enddate.split("/")
                                StageRaceEnd = pywikibot.WbTime(
                                    site=site,
                                    year=tableDate[2],
                                    month=tableDate[1],
                                    day=tableDate[0],
                                    precision='day')
                                FirstStage = 1
                                LastStage = 1
                                if test == 0:
                                    StageRaceCreator(
                                        pywikibot,
                                        site,
                                        repo,
                                        time,
                                        teamTable,
                                        Mastername,
                                        Mastergenre,
                                        MasterID,
                                        Year,
                                        UCI,
                                        StageRaceBegin,
                                        StageRaceEnd,
                                        FirstStage,
                                        LastStage,
                                        resulttable[nn][3],
                                        Createstage,
                                        Class,
                                        Onlystages,
                                        MasterID)
                        else:
                            if test == 0:
                                SingleDayRaceCreator(
                                    pywikibot,
                                    site,
                                    repo,
                                    time,
                                    teamTable,
                                    Mastername,
                                    Mastergenre,
                                    MasterID,
                                    Year,
                                    UCI,
                                    StageRaceBegin,
                                    resulttable[nn][3],
                                    Class)
                elif Class != "CN" and Class != "CC":
                    print(resulttable[nn][2])
                    print("race not found")


if __name__ == '__main__':
    from nationTeamTable import nationalTeamTable
    [pywikibot, site, repo, time] = wikiinit()
    [teamTable, endkk] = nationalTeamTable()
    raceTable = RaceList()
    UCIcalendarImporter(pywikibot, site, repo, teamTable, ";", 1)
