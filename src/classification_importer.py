# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:08 2018

@author: maxime delzenne
"""

from .cycling_init_bot_low import (get_year, table_reader, search_team_by_code, 
search_team_by_code_man, search_rider, add_winner)
from .bot_log import Log

def copy_team(pywikibot, site, startlist, claim, target,**kwargs):
    this_starter=None
    this_starter_id=None
    team=None
    test=kwargs.get('test',False)
     
    for starter in startlist:
        if starter.getTarget()==target: #Already there
            this_starter=starter
            this_starter_id=this_starter.getTarget().getID()
            break
    if this_starter!=None:
        for qual in this_starter.qualifiers.get('P54', []):
            team=qual.getTarget().getID()
            qualifier_team=pywikibot.page.Claim(site, 'P54', is_qualifier=True)
            qualifier_team.setTarget(qual.getTarget())
            if not test:
                claim.addQualifier(qualifier_team)
    if test:
        return this_starter_id, team

def put_dnf_in_startlist(pywikibot, site, repo, item, startlist, row_count, 
                         result_table, result_dic,**kwargs):
    
    test=kwargs.get('test',False)
    
    stage_nummer=-1
    if(u'P1545' in item.claims):  
        list_of_order=item.claims.get(u'P1545')
        stage_nummer=str(list_of_order[0].getTarget())
    for ii in range(row_count):
        if result_table[ii][result_dic['rank'][1]]==0: #dnf
            this_id=search_rider(pywikibot, site, repo,result_table[ii][result_dic['name'][1]],
                                result_table[ii][result_dic['first name'][1]],result_table[ii][result_dic['last name'][1]] )
            if this_id!=u'Q1' and this_id!=u'Q0':
                target = pywikibot.ItemPage(repo, this_id)
                this_starter=None
                for starter in startlist:
                   if starter.getTarget()==target: #Already there
                        this_starter=starter
                        break
                if this_starter!=None:
                     qualnotfound=True
                     for qual in this_starter.qualifiers.get('P1534', []):
                         qualnotfound=False
                     if qualnotfound:
                         target_qualifier = pywikibot.ItemPage(repo, u'Q1210380')
                         qualifier_DNF=pywikibot.page.Claim(site, 'P1534', is_qualifier=True)
                         qualifier_DNF.setTarget(target_qualifier)
                         if not test:
                             this_starter.addQualifier(qualifier_DNF)
                     qualnotfound=True
                     for qual in this_starter.qualifiers.get('P1545', []):
                         qualnotfound=False 
                     if qualnotfound and stage_nummer!=-1:   
                         qualifier_stage_number=pywikibot.page.Claim(site, 'P1545', is_qualifier=True)
                         qualifier_stage_number.setTarget(stage_nummer)
                         if not test:
                             this_starter.addQualifier(qualifier_stage_number)
                     if test and stage_nummer!=-1: 
                         return this_starter, stage_nummer #return first dnf rider
    return None, stage_nummer                          

def is_there_a_startlist(item, general_or_stage, general_or_stage_team, startliston):
    there_is_a_startlist=False #only useful for stage race
    in_parent=False
    startlist=None
    item_with_startlist=None
    
    if (general_or_stage not in general_or_stage_team) and  startliston:
        if(u'P710' in item.claims): 
            item_with_startlist=item
        elif (u'P361' in item.claims):
            list_of_comprend=item.claims.get(u'P361')
            parent=list_of_comprend[0].getTarget()
            parent.get()
            if(u'P710' in parent.claims): 
                item_with_startlist=parent
                in_parent=True
       
        if item_with_startlist is not None:
            startlist=item_with_startlist.claims.get(u'P710')
            there_is_a_startlist=True

    return there_is_a_startlist, startlist, in_parent
                    
def f(pywikibot,site,repo,general_or_stage, id_race,
                           final, maxkk,test,**kwargs):
     
    try:
        general_or_stage_points=[2,3,6,7,8]
        general_or_stage_team=[5,6]
        general_or_stage_addwinner=[0, 2, 3,4]
        general_or_stage_prop={
               0:'2321', #general
               1: '2417',#stage
               2:'3494',#points
               3:'4320',#mountains
               4:'4323',#youth 
               5:'3497',#teamtime
               6:'3496',#team points   
               7:'4323',#youth points
               8:'4322'#sprint 
                }
        
        verbose=False
        log=Log()
        year=kwargs.get('year',0)
        if year==0:
            year=get_year(pywikibot, repo, id_race)
        if year==0:
            print(u'no year found')
            return
        
        man_or_woman=kwargs.get('man_or_woman',u'woman')
        
        startliston=kwargs.get('startliston',True)
        file=kwargs.get('file','Results')
        
        if general_or_stage in general_or_stage_prop:
            property_nummer=general_or_stage_prop[general_or_stage]
        if general_or_stage in general_or_stage_points:
            result='points'
        else:
            result='time'
        
        result_dic={
            'rank':[-1, 0, ''],
            'last name':[-1, 1,''],
            'first name':[-1, 2,''],
            'name':[-1, 3,''],
            'result':[-1, 4,result],
            'points':[-1, 5, 'points'],
            'team code':[-1, 7, ''],
            'ecart':[1,6,''],  #always created, not set on time otherwise makes strange things
            'bib':[-1,8,''] #dossard
            }
    
        result_table, row_count, ecart=table_reader(file,result_dic,0,True) #'input/Results.csv'
        
        #post-processing
        maxkk=min(row_count,maxkk)
        for ii in range(maxkk):
            if  result_table[ii][result_dic['team code'][1]]!=0:
                result_table[ii][result_dic['team code'][1]]=result_table[ii][result_dic['team code'][1]]+" "+str(year)  
            if result=='time':
                if ii==0:
                    result_table[ii][result_dic['ecart'][1]]=0
                else:
                    if ecart:
                        result_table[ii][result_dic['ecart'][1]]=result_table[ii][result_dic['result'][1]]
                    else:
                        result_table[ii][result_dic['ecart'][1]]=result_table[ii][result_dic['result'][1]]-result_table[0][result_dic['result'][1]]
            else:
                if result_table[ii][result_dic['points'][1]]==0:
                    result_table[ii][result_dic['points'][1]]=result_table[ii][result_dic['result'][1]]
        
        
        log.concat('result_table created')
        if verbose:
            print(result_table[0:maxkk])
        item =pywikibot.ItemPage(repo, id_race)
        item.get()
        
        there_is_a_startlist, startlist, in_parent=is_there_a_startlist(item, general_or_stage, general_or_stage_team, startliston)
        if there_is_a_startlist:
            log.concat('startlist found')
        
        if not test:
            if(u'P'+str(property_nummer) in item.claims):  #already there do nothing
                log.concat(u'Classification already there')
            else: 
                claim=pywikibot.Claim(repo, u'P'+str(property_nummer))  
                for ii in range(maxkk):
                    if general_or_stage in general_or_stage_team: #team
                        if verbose:
                            log.concat("this a " + man_or_woman + " team")
                        if man_or_woman=="woman":
                            this_id=search_team_by_code(pywikibot, site, repo,  result_table[ii][result_dic['team code'][1]])
                        else:
                            this_id=search_team_by_code_man(pywikibot, site,  repo, result_table[ii][result_dic['team code'][1]])
                    else:
                        this_id=search_rider(pywikibot, site, repo,result_table[ii][result_dic['name'][1]],
                                            result_table[ii][result_dic['first name'][1]],result_table[ii][result_dic['last name'][1]] )
                    if this_id!=u'Q1' and this_id!=u'Q0':
                       claim=pywikibot.Claim(repo, u'P'+str(property_nummer))  
                       target = pywikibot.ItemPage(repo, this_id)
                       claim.setTarget(target)
                       item.addClaim(claim, summary=u'Adding classification')
                       qualifier_rank=pywikibot.page.Claim(site, 'P1352', is_qualifier=True)
                       target_qualifier =  pywikibot.WbQuantity(amount=result_table[ii][result_dic['rank'][1]], site=repo)
                       qualifier_rank.setTarget(target_qualifier)
                       claim.addQualifier(qualifier_rank)
                       itemSeconds=pywikibot.ItemPage(repo, "Q11574")
                       if general_or_stage in general_or_stage_points:
                           qualifier_points=pywikibot.page.Claim(site, 'P1358', is_qualifier=True)
                           target_qualifier = pywikibot.WbQuantity(amount=result_table[ii][result_dic['points'][1]], site=repo)
                           qualifier_points.setTarget(target_qualifier)
                           claim.addQualifier(qualifier_points)
                       elif result_table[ii][result_dic['rank'][1]]==1:
                           qualifier_time=pywikibot.page.Claim(site, 'P2781', is_qualifier=True)
                           target_qualifier = pywikibot.WbQuantity(amount=result_table[ii][result_dic['result'][1]], site=repo, unit=itemSeconds)
                           qualifier_time.setTarget(target_qualifier)
                           claim.addQualifier(qualifier_time)
                       else:
                           qualifier_ecart=pywikibot.page.Claim(site, 'P2911', is_qualifier=True)
                           target_qualifier = pywikibot.WbQuantity(amount=result_table[ii][result_dic['ecart'][1]], site=repo, unit=itemSeconds)
                           qualifier_ecart.setTarget(target_qualifier)
                           claim.addQualifier(qualifier_ecart)
                       #look for team in startlist
                       if there_is_a_startlist:
                           copy_team(pywikibot, site, startlist, claim, target)
    
                       if (general_or_stage in general_or_stage_addwinner) and final:
                           add_winner(pywikibot, site,repo,item,this_id,result_table[ii][result_dic['rank'][1]],general_or_stage) 
                           
                    else:
                       log.concat(str(result_table[ii][result_dic['name'][1]]) + ', ' +str(result_table[ii][result_dic['last name'][1]]))
                       log.concat(u'item not found, interrupted at row ' + str(ii))
                       return 0
            log.concat('result inserted')
            #fill startlist with DNF, HD and so on
            if there_is_a_startlist and general_or_stage==1:
                log.concat('completion of startlist with DNF')
                put_dnf_in_startlist(pywikibot, site, repo, item, startlist, row_count, 
                             result_table, result_dic)
                log.concat('completion of startlist with DNF finished')
            return 0, log                          
    except Exception as msg:
            print(msg)
            log.concat("General Error in classification_importer")
            return 10, log  
