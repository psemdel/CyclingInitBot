#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:34:29 2019

@author: maxime
"""



def startlist_importer (pywikibot,site,repo, prologueorfinal, id_race, separator,timeOfRace,chrono,test,teamTable):
    #For Europa
    resulttable = [[0 for x in range(10)] for y in range(200)] 
    kk=0
    rankrow=-1
    lastnamerow=-1
    firstnamerow=-1
    namerow=-1
    resultrow=-1
    pointsrow=-1
    teamcoderow=-1
    reversename=0
        
    with open('Results.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in spamreader:
            if kk==0:
                print(row)
                for jj in range(len(row)):
                    if row[jj]=='Rank':
                        rankrow=jj
                    elif row[jj]=='Last name' or row[jj]=='Last Name':
                        lastnamerow=jj
                    elif row[jj]=='First name' or row[jj]=='First Name':
                        firstnamerow=jj
                    elif row[jj]=='Name':
                        namerow=jj
                    elif row[jj]=='Results' or row[jj]=='Result': 
                        resultrow=jj
                    elif row[jj]=='Points':  
                        pointsrow=jj
                    elif row[jj]=='Team Code':  
                        teamcoderow=jj 
                    elif row[jj]=='BIB':  
                        dossardrow=jj     
                    
                if firstnamerow==-1 and namerow!=-1:
                    reversename=1
                if rankrow==-1:
                    print('no rank column')
                    return 0
            elif kk!=0 and row[dossardrow]!='':
                if rankrow!=-1:
                    resulttable[kk-1][0]=row[rankrow]
                if namerow!=-1:
                    resulttable[kk-1][1]=row[namerow]
                if firstnamerow!=-1:
                    resulttable[kk-1][2]=row[firstnamerow]
                if lastnamerow!=-1:
                    resulttable[kk-1][3]=row[lastnamerow]
                if dossardrow!=-1:
                    resulttable[kk-1][4]=row[dossardrow]
            kk=kk+1
    item =pywikibot.ItemPage(repo, id_race)
    item.get()    

    #delete the zeros
    resulttable2 = [[0 for x in range(10)] for y in range(kk-1)] 
    for ii in range(0,kk-1):
        resulttable2[ii]=resulttable[ii]

    #Sort by dossard
    resulttable2=sorted(resulttable2, key=lambda tup: int(tup[4]))
    resulttable=resulttable2
    
    print('table read and sorted')
    #check if all riders are already present
    if test==1:
        for kk in range(len(resulttable)):
            RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)

    alreadylist=0
    Year=timeOfRace.year
    if test==0:
        if(u'P'+str('710') in item.claims) and prologueorfinal==0:  #already there do nothing
            print(u'List of starters already there')
        else:   
            #check national team
            nationalteamdetected=0
            allsameteam=1
            for kk in range(len(resulttable)):
                if int(resulttable[kk][4])%10==1:
                    #insert last team
                    if nationalteamdetected==1 and allsameteam<0:
                        print(u'national team detected '+IDtoCIOsearch(teamTable, noQ(nationalteamnation)))
                        for jj in range(nationalteambegin,kk):
                            resulttable[jj][5]=IDtoCIOsearch(teamTable, noQ(nationalteamnation)) + " " + str(Year)
                    nationalteamdetected=1
                    nationalteambegin=kk
                    nationalteamnation=u'reset'
                    proteam=u'reset'
                    allsameteam=1
                if nationalteamdetected!=0 and prologueorfinal!=1:    
                    RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)
                    itemRider =pywikibot.ItemPage(repo, RiderID)
                    itemRider.get()
                    if (u'P27' in itemRider.claims):
                        nationality=itemRider.claims.get(u'P27')
                        if nationalteamnation==u'reset':
                            nationalteamnation=nationality[0].getTarget().getID()
                        else:
                            if nationalteamnation!=nationality[0].getTarget().getID():
                                nationalteamdetected=0
                    team=getPresentTeam(pywikibot,site,repo,RiderID,timeOfRace)
                    if proteam==u'reset':
                        proteam=team
                    else:
                        if team!=0 and proteam!=team: 
                            allsameteam=allsameteam-1
            claim=pywikibot.Claim(repo, u'P'+str('710')) 
            if (u'P'+str('710') in item.claims):
                alreadylist=1
            list_of_comprend=item.claims.get(u'P'+str(710))
            if prologueorfinal==1:
                list_of_comprendbool=[0 for x in range(len(list_of_comprend))] 
            qualifierDNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
            qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
            qualifierDossard=pywikibot.page.Claim(site, 'P1618', is_qualifier=True)
            for kk in range(len(resulttable)):
                RiderID=searchRider(pywikibot,site,repo,resulttable,kk,reversename)
                if RiderID!='0':
                    target = pywikibot.ItemPage(repo, RiderID)
                    print('target')
                    print(target)
                    #look for it
                    Addc=-1
                    if alreadylist==1:
                        for ii in range(len(list_of_comprend)):
                           if list_of_comprend[ii].getTarget()==target: #Already there
                                Addc=ii
                                if prologueorfinal==1:
                                    list_of_comprendbool[ii]=1
                    if Addc==-1:  ##create the rider
                        if prologueorfinal==1:
                            print('rider not found'+str(RiderID))
                        claim=pywikibot.Claim(repo, u'P'+str('710'))  #reinit everytime
                        claim.setTarget(target)
                        item.addClaim(claim, summary=u'Adding starterlist')
                        #qualifierDossard=pywikibot.page.Claim(site, 'P1618', is_qualifier=True)
                        target_qualifier =resulttable[kk][4]  #pywikibot.WbQuantity(amount=resulttable[kk][4], site=repo)
                        qualifierDossard.setTarget(target_qualifier)
                        claim.addQualifier(qualifierDossard)
                        if resulttable[kk][5]!=0: #national team
                            Idnationalteam=searchItem(pywikibot,site,resulttable[kk][5])
                            if Idnationalteam!=u'Q0' and Idnationalteam!=u'Q1':
                               #print(Idnationalteam)
                               qualifierTeam=pywikibot.page.Claim(site, 'P54', is_qualifier=True)
                               target_qualifier = pywikibot.ItemPage(repo, Idnationalteam)
                               qualifierTeam.setTarget(target_qualifier)
                               claim.addQualifier(qualifierTeam)
                        if prologueorfinal==1 or prologueorfinal==2:
                           if resulttable[kk][0]=='': #no ranking
                               qualifierDNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                               target_qualifier = pywikibot.ItemPage(repo, u'Q1210380')
                               qualifierDNF.setTarget(target_qualifier)
                               claim.addQualifier(qualifierDNF)
                           else:
                               qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                               target_qualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                               qualifier_rank.setTarget(target_qualifier)
                               claim.addQualifier(qualifier_rank)
                        riderTricot(pywikibot,site,repo,RiderID,timeOfRace,claim,chrono)  
                    else: ##rider already there
                        print(Addc)
                        if prologueorfinal==1 or prologueorfinal==2:
                           if resulttable[kk][0]=='': #no ranking
                               qualnotfound=1
                               for qual in list_of_comprend[Addc].qualifiers.get('P1534', []):
                                   qualnotfound=0
                               if qualnotfound==1:
                                   #qualifierDNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                                   target_qualifier = pywikibot.ItemPage(repo, u'Q1210380')
                                   qualifierDNF.setTarget(target_qualifier)
                                   list_of_comprend[Addc].setTarget(target) 
                                   list_of_comprend[Addc].addQualifier(qualifierDNF)
                           else:
                               qualnotfound=1
                               for qual in list_of_comprend[Addc].qualifiers.get('P1352', []):
                                   qualnotfound=0
                               if qualnotfound==1:
                                   #qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                                   target_qualifier =  pywikibot.WbQuantity(amount=int(resulttable[kk][0]), site=repo)
                                   qualifier_rank.setTarget(target_qualifier)
                                   list_of_comprend[Addc].setTarget(target) 
                                   list_of_comprend[Addc].addQualifier(qualifier_rank)
            #all riders are classified, assumption the other are DNF
            if prologueorfinal==1:
                for kk in range(len(list_of_comprend)):
                    if list_of_comprendbool[kk]==0: ##rider not found in this result sheet
                         list_of_comprend[kk].setTarget(target) 
                         qualifierDNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                         qualnotfound=1
                         for qual in list_of_comprend[kk].qualifiers.get('P1534', []):
                             qualnotfound=0
                         if qualnotfound==1:
                             target_qualifier = pywikibot.ItemPage(repo, u'Q1210380')
                             qualifierDNF.setTarget(target_qualifier)
                             list_of_comprend[kk].addQualifier(qualifierDNF)