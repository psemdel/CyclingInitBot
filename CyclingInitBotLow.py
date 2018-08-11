# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:38:42 2018

@author: psemdel
"""

#==Low level function ==
def addValue(pywikibot,repo,item,propertyNummer,value,comment): #Add a value to a property
    if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
        a=1
    else:
       claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
       if isinstance(value, str):
           target=value
       else:
           target = pywikibot.ItemPage(repo, u'Q'+str(value))
       claim.setTarget(target)
       item.addClaim(claim, summary=u'Adding '+comment) 

def addDate(pywikibot,repo,item,propertyNummer,inputDate,comment):
    if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
        a=1
    else:
       claim=pywikibot.Claim(repo, u'P'+str(propertyNummer))  
       claim.setTarget(inputDate)
       item.addClaim(claim, summary=u'Adding '+comment) 

def deleteValue(pywikibot,repo,item,propertyNummer,value,comment): 
    itemfound=0
    itemposition=0
    if(u'P'+str(propertyNummer) in item.claims):
         listOfcomprend=item.claims.get(u'P'+str(propertyNummer))
         itemToDelete=pywikibot.ItemPage(repo,u'Q'+str(value))
         for ii in range(len(listOfcomprend)):
             if listOfcomprend[ii].getTarget()==itemToDelete: #Already there
                 itemfound=1 
                 itemposition=ii
    if itemfound==1:
        allclaims=item.claims[u'P'+str(propertyNummer)] 
        claim=allclaims[itemposition]
        item.removeClaims(claim)
   
    
def addMultipleValue(pywikibot,repo,item,propertyNummer,value,comment,overpass): #Same as add value but for comprend
    #check if the value is not already present
    if overpass==1:  #To add a value and then delete it for sorting purpose
        Addc=1
    else:
        Addc=1
        if(u'P'+str(propertyNummer) in item.claims):  #already there do nothing
           listOfcomprend=item.claims.get(u'P'+str(propertyNummer))
           itemToAdd=pywikibot.ItemPage(repo,u'Q'+str(value))
           for ii in range(len(listOfcomprend)):
               if listOfcomprend[ii].getTarget()==itemToAdd: #Already there
                    Addc=0
                    print('Item already in the Master list')
    #add the value    
    if Addc==1:  
       claim=pywikibot.Claim(repo, u'P'+str(propertyNummer)) 
       target = pywikibot.ItemPage(repo, u'Q'+str(value))
       claim.setTarget(target)
       item.addClaim(claim, summary=u'Adding '+comment) 
    return Addc
    
def addWinner(pywikibot,site,repo,item,value,order):
    propertyNummer=1346
    Addc=1
    if order==1:
        qualifierNummer='Q20882667'
    elif order==2:
        qualifierNummer='Q20882668'
    elif order==3:  
        qualifierNummer='Q20882669'
    else:
        Addc=0  
    
    if(u'P'+str(propertyNummer) in item.claims):
        listOfWinner=item.claims.get(u'P'+str(propertyNummer))
        itemToAdd=pywikibot.ItemPage(repo,value)
        #look if already there as a rider can't be first, second and third at the same time
        for ii in range(len(listOfWinner)):
           if listOfWinner[ii].getTarget()==itemToAdd: #Already there
                Addc=0
                print('winner already in the list')
        
    if Addc==1:   
        claim=pywikibot.Claim(repo, u'P'+str(propertyNummer)) 

        target = pywikibot.ItemPage(repo, value)
        claim.setTarget(target)
        item.addClaim(claim, summary=u'Adding winner')
        qualifierDe=pywikibot.page.Claim(site, 'P642', isQualifier=True)
        targetQualifier = pywikibot.ItemPage(repo, qualifierNummer)
        qualifierDe.setTarget(targetQualifier)
        claim.addQualifier(qualifierDe)

      
def noQ(itemID):
    itemResult=itemID[1:len(itemID)]
    return int(itemResult)

#==date==
def compareDates(date1,date2):
    #equal to 1 if date 1 is higher than 2, otherwise 2, and 0 if equal
    year1=date1.year
    year2=date2.year
    if year1>year2:
        output=1
    elif year1<year2:
        output=2
    else:
        month1=date1.month
        month2=date2.month
        if month1>month2:
            output=1
        elif month1<month2:
            output=2
        else:
             day1=date1.day
             day2=date2.day
             if day1>day2:
                 output=1
             elif day1<day2:
                 output=2
             else:
                 output=0 #equal date
    return output      


#==Search ==
def searchItem(pywikibot,site,search_string):
    from pywikibot.data import api
    wikidataEntries =getItems(api, site, search_string)
    if(u'search-continue' in wikidataEntries):
        #several results
        resultId=u'Q1'
    elif(wikidataEntries['search']==[]):
        #no result
        resultId=u'Q0'
    else:
        wikidataSearchresult= wikidataEntries['search']
        wikidataSearchresult1=wikidataSearchresult[0]
        resultId=wikidataSearchresult1['id']
    return resultId

def getItems(api,site, itemtitle):
     params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'fr', 'type' : 'item', 'search': itemtitle, 'limit': 2}
     #params.update({'continue': 1})
     request = api.Request(site=site,parameters=params)
     search_results=request.submit()
     if search_results['success'] != 1:
         print('WD search failed')
     else:
         return search_results

#==Select
def teamCIOsearch(teamTable, CIOcode):
    result=0
    print( teamTable[35][7]==CIOcode)
    
    for ii in range(len(teamTable)):
        if teamTable[ii][7]==CIOcode:
            result=ii
            break
    
    return result

def CIOtoIDsearch(teamTable, CIOcode):
    result=0
    
    for ii in range(len(teamTable)):
        if teamTable[ii][7]==CIOcode:
            result=teamTable[ii][3]
            break
    return result


#==Create==
def create_item(pywikibot,site, label_dict):
    new_item = pywikibot.ItemPage(site)
    new_item.editLabels(labels=label_dict, summary="Setting labels")
    # Add description here or in another function
    return new_item.getID()   
        
def get_description(language, wikidataitem):
  if language in wikidataitem.descriptions:
    return wikidataitem.descriptions[language]
  else:
    return('') 
    
def get_label(language, wikidataitem):
  if language in wikidataitem.labels:
    return wikidataitem.labels[language]
  else:
    return('') 

def get_alias(language, wikidataitem):
  if language in wikidataitem.aliases:
      return wikidataitem.aliases[language]
  else:
      return('') 