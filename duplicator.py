#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:17:17 2019

@author: maxime
"""


def fillchamp(pywikibot, site, repo, time):
    prefix = u'Course en ligne féminine '
    #prefix=u'Contre-la-montre féminin '
    sufix = u'aux championnats nationaux de cyclisme sur route '
    startYear = 2011
    EndYear = 2018

    for ii in range(startYear, EndYear):
        Year = ii
        mylabel = {}
        mylabel[u'fr'] = prefix + sufix + str(Year)
        Idpresent = searchItem(pywikibot, site, mylabel['fr'])
        item = pywikibot.ItemPage(repo, Idpresent)
        item.get()

        if(u'P527' in item.claims):
            listOfcomprend = item.claims.get(u'P527')
            for ii in range(len(listOfcomprend)):
                itemthisChampionship = listOfcomprend[ii].getTarget()
                itemthisChampionship.get()
                thislabel = get_label('fr', itemthisChampionship)
                Idchamp = searchItem(
                    pywikibot, site, thislabel[thislabel.find('championnats'):])
                if (Idpresent == u'Q0'or Idpresent == u'Q1'):
                    print(thislabel + "not found")
                else:
                    addValue(
                        pywikibot,
                        repo,
                        itemthisChampionship,
                        361,
                        noQ(Idchamp),
                        u'link master')


def duplicator(pywikibot, site, repo, time):
    mastername = u'championnats nationaux de cyclisme sur route en '

    #prefix=u'Course en ligne féminine '
    prefix = u'Contre-la-montre féminin '
    sufix = u'aux championnats nationaux de cyclisme sur route '
    startYear = 2010
    EndYear = 2019

    for ii in range(startYear, EndYear):
        Year = ii
        mylabel = {}
        mylabel[u'fr'] = mastername + str(Year)
        print(mylabel[u'fr'])
        Idmaster = searchItem(pywikibot, site, mylabel['fr'])
        if (Idmaster == u'Q0'):
            print('master not found')
            return
        item = pywikibot.ItemPage(repo, Idmaster)
        item.get()

        mylabel = {}
        mylabel[u'fr'] = prefix + sufix + str(Year)
        Idpresent = searchItem(pywikibot, site, mylabel['fr'])
        if (Idpresent == u'Q0'):
            print(mylabel['fr'] + ' created')
            # Type code
            Idpresent = create_item(pywikibot, site, mylabel)

        elif (Idpresent == u'Q1'):
            print(mylabel['fr'] + ' already present several times')
        else:
            print(mylabel['fr'] + ' already present')

        itemson = pywikibot.ItemPage(repo, Idpresent)
        itemson.get()
        addValue(pywikibot, repo, itemson, 361, noQ(Idmaster), u'link master')

        # Search previous
        Yearprevious = Year - 1
        mylabelprevious = {}
        mylabelprevious['fr'] = prefix + sufix + str(Yearprevious)
        Idprevious = searchItem(pywikibot, site, mylabelprevious['fr'])
        if (Idprevious == u'Q0')or(Idprevious ==
                                   u'Q1'):  # no previous or several
            a = 1
        else:
            addValue(
                pywikibot,
                repo,
                itemson,
                155,
                noQ(Idprevious),
                u'link previous')
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
        mylabelnext = {}
        mylabelnext['fr'] = prefix + sufix + str(Yearnext)
        Idnext = searchItem(pywikibot, site, mylabelnext['fr'])

        time.sleep(1.0)
        if (Idnext == u'Q0')or(Idnext == u'Q1'):  # no next or
            a = 1
        else:
            addValue(pywikibot, repo, itemson, 156, noQ(Idnext), u'link next')
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

        if(u'P527' in item.claims):
            listOfcomprend = item.claims.get(u'P527')
            for ii in range(len(listOfcomprend)):
                itemthisChampionship = listOfcomprend[ii].getTarget()
                itemthisChampionship.get()
                if(u'P527' in itemthisChampionship.claims):
                    listOfcomprendchamp = itemthisChampionship.claims.get(
                        u'P527')
                    for jj in range(len(listOfcomprendchamp)):
                        itemthisrace = listOfcomprendchamp[jj].getTarget()
                        itemthisrace.get()
                        racelabel = get_label('fr', itemthisrace)
                        if racelabel.find(prefix) == 0:
                            itemthisraceID = listOfcomprendchamp[jj].getTarget(
                            ).getID()
                            addMultipleValue(
                                pywikibot, repo, itemson, 527, noQ(itemthisraceID), u'duplicate', 0)


if __name__ == '__main__':
    [pywikibot, site, repo, time] = wikiinit()
    # duplicator(pywikibot,site,repo,time)
    fillchamp(pywikibot, site, repo, time)
