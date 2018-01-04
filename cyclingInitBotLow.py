# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:35:56 2018

@author: maxime delzenne
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
 
def addComprend(pywikibot,repo,item,value,comment): #Same as add value but for comprend
    Addc=1
    
    if(u'P'+str(527) in item.claims):  #already there do nothing
       listOfcomprend=item.claims.get(u'P527')
       itemToAdd=pywikibot.ItemPage(repo,u'Q'+str(value))
       for ii in range(len(listOfcomprend)):
           if listOfcomprend[ii].getTarget()==itemToAdd: #Already there
                Addc=0
                print('Item already in the Master list')
        
    if Addc==1:  
       claim=pywikibot.Claim(repo, u'P527') 
       target = pywikibot.ItemPage(repo, u'Q'+str(value))
       claim.setTarget(target)
       item.addClaim(claim, summary=u'Adding '+comment) 

      
def noQ(itemID):
    itemResult=itemID[1:len(itemID)]
    return int(itemResult)

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
    
    for ii in range(len(teamTable)):
        if teamTable[ii][7]==CIOcode:
            result=ii
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