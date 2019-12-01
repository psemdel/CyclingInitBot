# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:48:04 2018

@author: psemdel
"""
from CyclingInitBotLow import *


def nameParser(inputName):
    nameTable = [u'' for x in range(12)]  # [ for y in range(j)]
    jj = 0

    for ii in range(len(inputName)):
        if inputName[ii] == ' ' or inputName[ii] == "'":
            jj = jj + 1
        else:
            nameTable[jj] = nameTable[jj] + inputName[ii]

    return nameTable


def nameInterpreter(inputName):
    # Useful only for human
    # Try to find the Name
    familyName = u''
    if inputName[2] == u'':  # if only two words, then the second is the name
        familyName = inputName[1]
    elif inputName[1] == u'van' or inputName[1] == u'de':  # van is the beginning of a name
        familyName = completeTheName(1, inputName)
    else:  # it is not easy it has to be manual
        print(inputName)
        index = input('Index of the family name : ')
        familyName = completeTheName(int(index), inputName)

    return familyName


def checkTeam(inputName):
    temp1 = inputName.find(u"equipe d'")
    temp2 = inputName.find(u"equipe des")
    temp3 = inputName.find(u"equipe du")
    temp4 = inputName.find(u"equipe de")
    temp5 = inputName.find(u"championnats d'")
    temp6 = inputName.find(u"championnats des")
    temp7 = inputName.find(u"championnats du")
    temp8 = inputName.find(u"championnats de")
    outputName = u''

    if temp1 != -1 or temp2 != -1 or temp3 != -1 or temp4 != - \
            1 or temp5 != -1 or temp6 != -1 or temp7 != -1 or temp8 != -1:
        parsedName = nameParser(inputName)
        for ii in range(2, 11):
            if parsedName[ii] == u'':
                a = 1
            else:
                if outputName == u'':
                    outputName = parsedName[ii]
                else:
                    outputName = outputName + u' ' + parsedName[ii]
    else:
        outputName = inputName
    # print(outputName)
    return outputName


def completeTheName(index, inputName):
    familyName = inputName[index]
    for ii in range(index + 1, 7):
        if inputName[ii] == u'':
            a = 1
        else:
            familyName = familyName + u' ' + inputName[ii]

    return familyName


class CyclistName:
    def __init__(self, initialName):
        self.initialName = initialName

    def correct_name(self):
        self.initialName = self.initialName.lower()
        self.finalName = self.supprime_accent()

    def supprime_accent(self):
        """ supprime les accents du texte source """
        ligne = self.initialName
        accents = {'a': ['à', 'ã', 'á', 'â', 'ä'],
                   'e': ['é', 'è', 'ê', 'ë'],
                   'i': ['î', 'ï'],
                   'u': ['ù', 'ü', 'û'],
                   'o': ['ô', 'ö'],
                   's': ['š'],
                   'n': ['ñ']}
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        return ligne


class Cyclist:
    def __init__(self, id, fullName, item):
        self.key = id
        self.fullName = fullName
        self.item = item
        self.itemID = item.getID()
        #  self.familyName = familyName


class Victoire:
    def __init__(self, id, date, item):
        self.key = id
        self.date = date
        self.item = item
        self.itemID = item.getID()


def dateSort(listeDesVictoires, newOrder):
    iimax = len(newOrder) - 1
    for ii in range(iimax - 1):
        jjmax = iimax - ii
        table_sorted = 1
        for jj in range(jjmax):
            victoire1 = listeDesVictoires[newOrder[jj]]
            victoire2 = listeDesVictoires[newOrder[jj + 1]]
            date1 = victoire1.date
            date2 = victoire2.date
            comparisonTemp = compareDates(date1, date2)
            if comparisonTemp == 1:  # bad order
                temp = newOrder[jj]
                newOrder[jj] = newOrder[jj + 1]
                newOrder[jj + 1] = temp
                table_sorted = 0
        if table_sorted == 1:
            break
    return newOrder


def dateSorterEmpty(
        pywikibot,
        site,
        repo,
        time,
        IdTeamPage,
        VicOrComp,
        listOfItem):
    item = pywikibot.ItemPage(repo, IdTeamPage)
    item.get()
    listeDesVictoires = []

    if VicOrComp == u'Victoire':
        propertyNumber = 2522  # victoire
    else:
        propertyNumber = 527  # comprend

    for ii in range(len(listOfItem)):
        listOfItem[ii].get()

        if (u'P' + str(580) in listOfItem[ii].claims):  # course à étapes
            claimTemp = listOfItem[ii].claims[u'P' + str(580)]
            dateTemp = claimTemp[0].getTarget()
            print(dateTemp)
        elif(u'P' + str(585) in listOfItem[ii].claims):  # course d'un jour
            claimTemp = listOfItem[ii].claims[u'P' + str(585)]
            dateTemp = claimTemp[0].getTarget()
        elif (u'P' + str(582) in listOfItem[ii].claims):  # course à étapes
            claimTemp = listOfItem[ii].claims[u'P' + str(582)]
            dateTemp = claimTemp[0].getTarget()
        else:
            print(listOfItem[ii].labels['fr'] + u' has no date')
            return 0
        victoireTemp = Victoire(ii, dateTemp, listOfItem[ii])
        listeDesVictoires.append(victoireTemp)

    newOrder = [0 for x in range(len(listOfcomprend))]
    for x in range(len(listOfcomprend)):
        newOrder[x] = x
    newOrder = dateSort(listeDesVictoires, newOrder)
    print(newOrder)

    for ii in range(len(newOrder)):
        key = newOrder[ii]
        itemID = listeDesVictoires[key].itemID
        # delete the old one
        # allclaims=item.claims[u'P'+str(propertyNumber)]
        claim = allclaims[0]
        addMultipleValue(
            pywikibot,
            repo,
            item,
            propertyNumber,
            noQ(itemID),
            'race for sorting',
            1)
#


def dateSorter(pywikibot, site, repo, time, IdTeamPage, VicOrComp):
    item = pywikibot.ItemPage(repo, IdTeamPage)
    item.get()
    listOfItem = {}
    listeDesVictoires = []

    if VicOrComp == u'Victoire':
        propertyNumber = 2522  # victoire
    else:
        propertyNumber = 527  # comprend

    if(u'P' + str(propertyNumber) in item.claims):
        listOfcomprend = item.claims.get(u'P' + str(propertyNumber))
    for ii in range(len(listOfcomprend)):
        listOfItem[ii] = listOfcomprend[ii].getTarget()
        listOfItem[ii].get()
        if(u'P' + str(580) in listOfItem[ii].claims):  # course à étapes
            claimTemp = listOfItem[ii].claims[u'P' + str(580)]
            dateTemp = claimTemp[0].getTarget()
        elif (u'P' + str(585) in listOfItem[ii].claims):  # course d'un jour
            claimTemp = listOfItem[ii].claims[u'P' + str(585)]
            dateTemp = claimTemp[0].getTarget()
        else:
            print(listOfItem[ii].labels['fr'] + u' has no date')
            return 0
        victoireTemp = Victoire(ii, dateTemp, listOfItem[ii])
        listeDesVictoires.append(victoireTemp)

    newOrder = [0 for x in range(len(listOfcomprend))]
    oldOrder = [0 for x in range(len(listOfcomprend))]
    for x in range(len(listOfcomprend)):
        newOrder[x] = x
        oldOrder[x] = x
    newOrder = dateSort(listeDesVictoires, newOrder)
    print(newOrder)
    reorder = 1
    orderfine = 1

    if reorder == 1:
        for ii in range(len(newOrder)):
            # when the first has to be moved all have to be moved
            if newOrder[ii] != oldOrder[ii]:
                if ii == 0:
                    #confirm=input('First race changed confirm (1) : ')
                    # if confirm==1:
                    orderfine = 0
                    # else:
                    #    break
                else:
                    orderfine = 0

            if orderfine == 0:
                key = newOrder[ii]
                itemID = listeDesVictoires[key].itemID
                # delete the old one
                # allclaims=item.claims[u'P'+str(propertyNumber)]
                # claim=allclaims[0]

                deleteValue(
                    pywikibot,
                    repo,
                    item,
                    propertyNumber,
                    noQ(itemID),
                    'race for sorting')
                addMultipleValue(
                    pywikibot,
                    repo,
                    item,
                    propertyNumber,
                    noQ(itemID),
                    'race for sorting',
                    1)


def nameSorter(pywikibot, site, repo, time, IdTeamPage, TeamOrOther):
    # Page to sort
    # import

    item = pywikibot.ItemPage(repo, IdTeamPage)
    item.get()
    listOfItem = {}
    listeDesCyclistes = []
    nameToParseInput = []

    if TeamOrOther == u'Team' or TeamOrOther == u'Champ':
        propertyNumber = 527  # comprend
    else:
        propertyNumber = 1923  # liste des équipes participantes

    # Read the list of racers and correct their name
    if(u'P' + str(propertyNumber) in item.claims):
        listOfcomprend = item.claims.get(u'P' + str(propertyNumber))
    for ii in range(len(listOfcomprend)):
        listOfItem[ii] = listOfcomprend[ii].getTarget()
        listOfItem[ii].get()
        fullNametemp = listOfItem[ii].labels['fr']  # temp because not saved
        cyclistNametemp = CyclistName(fullNametemp)
        cyclistNametemp.correct_name()
        cyclisttemp = Cyclist(ii, cyclistNametemp.finalName, listOfItem[ii])
        listeDesCyclistes.append(cyclisttemp)
        nameToParseInput.append(cyclistNametemp.finalName)

  # print(listeDesCyclistes[0].fullName)

    # nameToParseInput=['maxime delzenne','tom boonen','anna van der breggen', 'nel de crits','ann-sophie duyck']#sortedName
    # Create a list to sort it
    nameToParse = [[u'' for x in range(3)]
                   for y in range(len(nameToParseInput))]
    for x in range(len(nameToParseInput)):
        nameToParse[x][0] = x
        nameToParse[x][1] = nameToParseInput[x]

    if TeamOrOther == u'Team':
        parsedName = [u'' for x in range(len(nameToParseInput))]
        familyName = [u'' for x in range(len(nameToParseInput))]
        for ii in range(len(parsedName)):
            parsedName[ii] = nameParser(nameToParse[ii][1])
            familyName[ii] = nameInterpreter(parsedName[ii])
            nameToParse[ii][2] = familyName[ii]
    else:  # If not human no need to do all this stuff
        for ii in range(len(nameToParse)):
            nameToParse[ii][1] = checkTeam(nameToParse[ii][1])
            nameToParse[ii][2] = nameToParse[ii][1]

    sortedName = sorted(nameToParse, key=lambda tup: tup[2])
    print('sorted list :')
    print(sortedName)

    # delete done later
    for ii in range(len(sortedName)):
        key = sortedName[ii][0]
        itemID = listeDesCyclistes[key].itemID
        # delete the old one
        allclaims = item.claims[u'P' + str(propertyNumber)]
        claim = allclaims[0]

        # Save the qualifiers
        Datedebutbool = 0
        Datefinbool = 0
        if(u'P' + str(580) in claim.qualifiers):
            Datedebutbool = 1
            Datedebutsave = claim.qualifiers[u'P580'][0].getTarget()
        if(u'P' + str(582) in claim.qualifiers):
            Datefinbool = 1
            Datefinsave = claim.qualifiers[u'P582'][0].getTarget()

        deleteValue(
            pywikibot,
            repo,
            item,
            propertyNumber,
            noQ(itemID),
            'rider for sorting')
        addMultipleValue(
            pywikibot,
            repo,
            item,
            propertyNumber,
            noQ(itemID),
            'rider for sorting',
            1)

        # The claim has to be redefined
        # allclaims=item.claims[u'P'+str(propertyNumber)]
        # claim=allclaims[0]
        #addDatefin=pywikibot.page.Claim(site, 'P582', isQualifier=True)
        # addDatefin.setTarget(Datedebutsave)
        #addDatefin.setTarget(pywikibot.WbTime(site=site,year=2018, precision='year'))
        # claim.addQualifier(addDatefin)

        Datedebutbool = 0
        Datefinbool = 0
        if Datedebutbool == 1:
            addDatedebut = pywikibot.page.Claim(site, 'P580', isQualifier=True)
            addDatedebut.setTarget(Datedebutsave)
            claim.addQualifier(addDatedebut)
        if Datefinbool == 1:
            addDatefin = pywikibot.page.Claim(site, 'P582', isQualifier=True)
            addDatefin.setTarget(Datefinsave)
            claim.addQualifier(addDatefin)
