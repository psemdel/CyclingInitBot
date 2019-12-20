# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
from cycling_init_bot_low import * 
from calendar_list import *

def race_creator(pywikibot,site,repo,time,team_table_femmes,race_name,race_genre,
                 id_race_master,year,UCI,WWT,race_begin,countryCIO,classe,
                     single_race,**kwargs):
    #optional: end_date, only_stages, create_stages, first_stage,  last_stage, stage_race_id
    
    def race_basic(pywikibot,repo,item,site,country_code,master,start_date, UCI, WWT, year,
               single_race, **kwargs):
    #No need for the table here
        addValue(pywikibot,repo,item,31,master,u'Nature')
        addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
        if country_code!=0:
            addValue(pywikibot,repo,item,17,country_code,u'country')
    
        if single_race:
            addDate(pywikibot, repo, item, 585, start_date, u' date')
        else:
            addDate(pywikibot,repo,item,580,start_date,u'starting date')
            end_date=kwargs.get('end_date')
            print(end_date)
            addDate(pywikibot,repo,item,582,end_date,u'ending date')
    
        if UCI:
            calendar_id=calendaruciID(str(year))
        elif WWT:
            calendar_id=calendarWWTID(str(year))
        if UCI or WWT:
            addValue(pywikibot,repo,item,361,noQ(calendar_id),u'part of') #
    
    def stage_basic(pywikibot,repo,item,site,number,country_code,master,input_date):
    
        if Number==0:
            addValue(pywikibot,repo,item,31,485321,u'Nature')  #prologue
        else:
            addValue(pywikibot,repo,item,31,18131152,u'Nature')  #étape
    
        addValue(pywikibot,repo,item,361,master,u'part of')
        addValue(pywikibot,repo,item,641,3609,u'cyclisme sur route')
        addValue(pywikibot,repo,item,17,country_code,u'country')
        addValue(pywikibot,repo,item,1545,str(number),u'order')
        #race_begin later
    
    def date_finder(pywikibot,repo,site,number,first_stage,last_stage, race_begin,
                    race_end):
        
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        output_date=race_begin
        if number==last_stage:
             output_date=race_end
        elif number!=first_stage:
             output_date=race_begin
             day_begin=race_begin.day
             month_begin=race_begin.month
             year_begin=race_begin.year
    
             day_temp=day_begin+(number-first_stage)
             if day_temp>days_in_month[month_begin]:
                 day_temp=day_temp-days_in_month[month_begin]
                 month_temp=month_begin+1
                 if month_temp>12:
                     output_date.year=year_begin+1
                     output_date.month=month_temp-12
                 else:
                     output_date.month=month_temp
             output_date.day=day_temp
    
        return output_date
    
    
    def stage_label(number, genre,race_name, year):
        mylabel={}
    
        if number==0:
            label_part1_fr = u"Prologue"
        elif number==1:
            label_part1_fr = u"1re étape"
        else:
            label_part1_fr = str(number)+u"e étape"
    
        mylabel[u'fr']= label_part1_fr+" " + genre + race_name + " "+ str(year)
        return mylabel
 
    ##main starts here##
    mydescription={}
    create_main=True
    
    if single_race:
        only_stages=False
        create_stages=False
        end_date=None
    else:
        only_stages=kwargs.get('only_stages')
        end_date=kwargs.get('end_date')
        print(end_date)
        create_stages=kwargs.get('create_stages')
        first_stage=kwargs.get('first_stage')
        last_stage=kwargs.get('last_stage')
        if only_stages:
            stage_race_id=kwargs.get('stage_race_id')
            create_main=False
            id_present=u'Q'+ str(stage_race_id)
            item =pywikibot.ItemPage(repo, id_present)
            item.get()  
   
    if create_main:
        mylabel={}
        mylabel[u'fr']=race_name + " " + str(year)
        id_present, item=create_present(pywikibot, site,repo,time,mylabel)
        
        if id_present!=u'Q1':
            if get_description('fr',item)=='':
                mydescription[u'fr']=u'édition ' + str(year) +" "+ race_genre + race_name
                item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')

            race_basic(pywikibot,repo,item,site,CIOtoIDsearch(team_table_femmes, countryCIO),
                       id_race_master,race_begin, UCI, WWT, year,single_race,end_date=end_date)
        
            if UCI:
                 calendar_id=calendaruciID(str(year))
            elif WWT:
                 calendar_id=calendarWWTID(str(year))
            if UCI or WWT:
                item_calendar =pywikibot.ItemPage(repo, calendar_id)
                item_calendar.get()
                addMultipleValue(pywikibot,repo,item_calendar,527,noQ(id_present),u'in',0)
            
            class_id=get_class_id(classe)
            if class_id:
                addMultipleValue(pywikibot,repo,item,31, class_id,u'Class',0)
            #link previous and next
            link_year(pywikibot, site,repo,id_present,year,race_name)
            #link to master
            item_master= pywikibot.ItemPage(repo, u'Q'+ str(id_race_master))
            item_master.get()
            addMultipleValue(pywikibot,repo,item_master,527,noQ(id_present),u'link year '+ str(year),0) 
    
    #Create the stages
    if create_stages or only_stages:   
        print("stage creation")
        stageLabel={}  
        for ii in range(first_stage,last_stage+1):
            stage_label=stage_label(ii, race_genre, race_name, year)
            id_stage_present, item=create_present(pywikibot, site,repo, stage_label)
            print(id_stage_present)
            
            if id_stage_present!='Q1':
                if get_description('fr',id_stage_present)=='':
                    mydescription[u'fr']=u'étape'+" " + race_genre + race_name + " "+ str(year)
                    itemStagePresent.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
                
                race_basic(pywikibot,repo,id_stage_present,site,ii,CIOtoIDsearch(team_table_femmes, countryCIO),noQ(id_present),race_begin,True)
                stage_date=date_finder(pywikibot,repo,site,ii,first_stage,last_stage, race_begin,race_end)
                addDate(pywikibot,repo,id_stage_present,585,stage_date,u'date')
                
                #Link to the master for this year, so item
                addMultipleValue(pywikibot,repo,item,527,noQ(id_stage_present),u'link stage '+str(ii),0) 
                #Link to previous
                if ii==0:
                    lookforprevious=0
                else:   
                    if ii==1:
                        if first_stage==0:
                            lookforprevious=1
                        else:
                            lookforprevious=0
                    else:
                        lookforprevious=1
            
                    if lookforprevious==1:
                        stageLabelprevious=stage_label(ii-1, race_genre, race_name, year)
                        id_stage_previous=searchItem(pywikibot,site,stageLabelprevious['fr'])
                        if (id_stage_previous!=u'Q0')and(id_stage_previous!=u'Q1'):  #no previous or several
                            addValue(pywikibot,repo,itemStagePresent,155,noQ(id_stage_previous),u'link previous') 
                                #Link to the previous
                            item_stage_previous=pywikibot.ItemPage(repo, id_stage_previous)
                            item_stage_previous.get()
                            addValue(pywikibot,repo,item_stage_previous,156,noQ(id_stage_present),u'link next')
                    
            #Link to next
            #Not required 
