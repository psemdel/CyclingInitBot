# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
from CyclingInitBotLow import *
from symmetrizer import *


def SingleDayRaceBasic(
        pywikibot,
        repo,
        item,
        siteIn,
        country_code,
        Master,
        Date,
        UCI,
        year):
    # No need for the table here

    addValue(pywikibot, repo, item, 31, Master, u'Nature')
    addValue(pywikibot, repo, item, 641, 3609, u'cyclisme sur route')
    if country_code != 0:
        addValue(pywikibot, repo, item, 17, country_code, u'country')
    addDate(pywikibot, repo, item, 585, Date, u' date')

    if UCI == u"yes":
        calendarID = calendaruciID(str(year))
        addValue(pywikibot, repo, item, 361, noQ(calendarID), u'part of')
    elif WWT == u'yes':
        calendarID = calendarWWTID(str(year))
        addValue(pywikibot, repo, item, 361, noQ(calendarID), u'part of')


def SingleDayRaceCreator(
        pywikibot,
        site,
        repo,
        time,
        teamTableFemmes,
        StageRaceName,
        StageRaceGenre,
        StageRaceMasterId,
        Year,
        UCI,
        StageRaceDate,
        CountryCIO,
        Class):
    mydescription = {}

    mylabel = {}
    mylabel[u'fr'] = StageRaceName + " " + str(Year)

    Idpresent = searchItem(pywikibot, site, mylabel['fr'])
    if (Idpresent == u'Q0'):
        print(mylabel[u'fr'] + ' created')
        # Type code
        Idpresent = create_item(pywikibot, site, mylabel)
    elif (Idpresent == u'Q1'):
        print(mylabel['fr'] + ' already present several times')
    else:
        print(mylabel['fr'] + ' already present')

    item = pywikibot.ItemPage(repo, Idpresent)
    item.get()

    if get_description('fr', item) == '':
        mydescription[u'fr'] = u'édition ' + \
            str(Year) + " " + StageRaceGenre + StageRaceName
        item.editDescriptions(mydescription,
                              summary=u'Setting/updating descriptions.')

    SingleDayRaceBasic(
        pywikibot,
        repo,
        item,
        site,
        CIOtoIDsearch(
            teamTableFemmes,
            CountryCIO),
        StageRaceMasterId,
        StageRaceDate,
        UCI,
        Year)

    if Class == "1.1":
        ClassId = 22231110
    elif Class == "2.1":
        ClassId = 22231112
    elif Class == "1.2":
        ClassId = 22231111
    elif Class == "2.2":
        ClassId = 22231113
    elif Class == "1.WWT":
        ClassId = 23005601
    elif Class == "2.WWT":
        ClassId = 23005603

    if ClassId:
        addMultipleValue(pywikibot, repo, item, 31, ClassId, u'Class', 0)
    # Search previous
    Yearprevious = Year - 1
    mylabelprevious = StageRaceName + " " + str(Yearprevious)
    Idprevious = searchItem(pywikibot, site, mylabelprevious)
    if (Idprevious == u'Q0')or(Idprevious == u'Q1'):  # no previous or several
        a = 1
    else:
        addValue(pywikibot, repo, item, 155, noQ(Idprevious), u'link previous')
        # Link to the previous
        itemPrevious = pywikibot.ItemPage(repo, Idprevious)
        itemPrevious.get()
        addValue(
            pywikibot,
            repo,
            itemPrevious,
            156,
            noQ(Idpresent),
            u'link next')

    # Search next
    Yearnext = Year + 1
    mylabelnext = StageRaceName + " " + str(Yearnext)
    Idnext = searchItem(pywikibot, site, mylabelnext)

    time.sleep(1.0)
    if (Idnext == u'Q0')or(Idnext == u'Q1'):  # no next or
        a = 1
    else:
        addValue(pywikibot, repo, item, 156, noQ(Idnext), u'link next')
        # Link to the next
        itemNext = pywikibot.ItemPage(repo, Idnext)
        itemNext.get()
        addValue(
            pywikibot,
            repo,
            itemNext,
            155,
            noQ(Idpresent),
            u'link previous')

    # link to master
    itemMaster = pywikibot.ItemPage(repo, u'Q' + str(StageRaceMasterId))
    itemMaster.get()
    addMultipleValue(
        pywikibot,
        repo,
        itemMaster,
        527,
        noQ(Idpresent),
        u'link year ' +
        str(Year),
        0)
