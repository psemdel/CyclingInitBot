# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:29:49 2018

@author: maxime delzenne
"""
from .cycling_init_bot_low import (add_Qvalue, add_date, add_value, CIOtoIDsearch,
 get_country, get_class_WWT, define_article, create_present, link_year, 
 add_multiple_value, get_description, get_class_id, get_race_begin, get_end_date,
 get_class, get_year
 )
                                   
from .calendar_list import calendaruciID, calendarWWTID, calendarUWTID
from .bot_log import Log

def f(pywikibot,site,repo,time,team_table_femmes,race_name,
                 year,single_race,man_or_woman,**kwargs):
    #optional: end_date, only_stages, create_stages, first_stage,  last_stage, stage_race_id
    
    def UCI_to_calendar_id(UCI, WWT, UWT, man_or_woman):
        if UCI and man_or_woman==u"woman":
             calendar_id=calendaruciID(str(year))
        elif WWT:
             calendar_id=calendarWWTID(str(year))
        elif UWT:
             calendar_id=calendarUWTID(str(year))
        else:
            calendar_id=None
        return calendar_id
    
    def race_basic(pywikibot,repo,item,site,country_code,master,start_date, UCI, WWT, year,
               single_race, man_or_woman, **kwargs):
    #No need for the table here
        add_Qvalue(pywikibot,repo,item,"P31",master,u'Nature')
        add_Qvalue(pywikibot,repo,item,"P641","Q3609",u'cyclisme sur route')
        if country_code!=0:
            add_Qvalue(pywikibot,repo,item,"P17",country_code,u'country')
    
        if single_race:
            add_date(pywikibot, repo, item, "P585", start_date, u' date')
        else:
            add_date(pywikibot,repo,item,"P580",start_date,u'starting date')
            end_date=kwargs.get('end_date')
            print(end_date)
            add_date(pywikibot,repo,item,"P582",end_date,u'ending date')
    
        #insert the 
        calendar_id=UCI_to_calendar_id(UCI, WWT, UWT, man_or_woman)
        if calendar_id is not None:
            add_Qvalue(pywikibot,repo,item,"P361",calendar_id,u'part of') #
    
    def stage_basic(pywikibot,repo,item,site,number,country_code,master):
    
        if number==0:
            add_Qvalue(pywikibot,repo,item,"P31","Q485321",u'Nature')  #prologue
        else:
            add_Qvalue(pywikibot,repo,item,"P31","Q18131152",u'Nature')  #étape
    
        add_Qvalue(pywikibot,repo,item,"P361",master,u'part of')
        add_Qvalue(pywikibot,repo,item,"P641","Q3609",u'cyclisme sur route')
        add_Qvalue(pywikibot,repo,item,"P17",country_code,u'country')
        add_value(pywikibot,repo,item,"P1545",str(number),u'order')
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
    
             print(race_begin.day)
             print(number)
             print(first_stage)
             day_temp=day_begin+(number-first_stage)
             print(day_temp)

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
    race_begin=kwargs.get('race_begin')
    end_date=kwargs.get('end_date')
    classe=kwargs.get('classe')
    countryCIO=kwargs.get('countryCIO')
    id_race_master=kwargs.get('id_race_master')
    edition_nr=kwargs.get('edition_nr')
    year=kwargs.get('year')
    log=Log()

    if single_race:
        only_stages=False
        create_stages=False
        end_date=None
    else:
        only_stages=kwargs.get('only_stages')
        first_stage=kwargs.get('first_stage')
        last_stage=kwargs.get('last_stage')
        if only_stages:
            stage_race_id=kwargs.get('stage_race_id')
            create_stages=True
            create_main=False
            present_id=stage_race_id
            item =pywikibot.ItemPage(repo, present_id)
            item.get() 
            if countryCIO is None:
                countryCIO=get_country(pywikibot, repo, present_id)
            if race_begin is None:
                race_begin=get_race_begin(pywikibot, repo, present_id)
            if end_date is None:
                end_date=get_end_date(pywikibot, repo, present_id)
            if classe is None:
                classe=get_class(pywikibot, repo, present_id)
            if year is None:
                year=get_year(pywikibot, repo, present_id)
        else:
            create_stages=kwargs.get('create_stages')
            create_main=True
            if year is None and race_begin is not None: 
                year=race_begin.year
            
    if isinstance(countryCIO, str):
        country_id=CIOtoIDsearch(team_table_femmes, countryCIO)
    else:
        country_id=countryCIO
    
    race_genre, race_name=define_article(race_name)
    UCI, WWT, UWT=get_class_WWT(classe)
    
    if create_main:
        mylabel={}
        mylabel[u'fr']=race_name + " " + str(year)
        present_id, item=create_present(pywikibot, site,repo,time,mylabel)
        
        if present_id!=u'Q1':
            if get_description('fr',item)=='':
                mydescription[u'fr']=u'édition ' + str(year) +" "+ race_genre + race_name
                item.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')

            race_basic(pywikibot,repo,item,site,country_id,
                       id_race_master,race_begin, UCI, WWT, year,single_race,man_or_woman,end_date=end_date)
            if edition_nr!='':
                 add_value(pywikibot,repo,item,382,int(edition_nr),u'edition nr')
            
            #insert the race in the main calendar
            calendar_id=UCI_to_calendar_id(UCI, WWT, UWT, man_or_woman)
                
            if calendar_id is not None:
                item_calendar =pywikibot.ItemPage(repo, calendar_id)
                item_calendar.get()
                add_multiple_value(pywikibot,repo,item_calendar,"P527",present_id,u'in',0)
            
            class_id=get_class_id(classe)
            if class_id:
                add_multiple_value(pywikibot,repo,item,"P31", class_id,u'Class',0)
            #link previous and next
            link_year(pywikibot, site,repo,present_id,year,race_name)
            #link to master
            item_master= pywikibot.ItemPage(repo, id_race_master)
            item_master.get()
            add_multiple_value(pywikibot,repo,item_master,"P527",present_id,u'link year '+ str(year),0) 
    
    #Create the stages
    if create_stages:   
        log.concat("stage creation")
        stage_label_present={}  
        
        for ii in range(first_stage,last_stage+1):
            stage_label_present=stage_label(ii, race_genre, race_name, year)
            id_stage_present, item_stage=create_present(pywikibot, site,repo,time, stage_label_present)
            log.concat("id stage present "+id_stage_present)
            
            if id_stage_present!='Q1':
                if get_description('fr',item_stage)=='':
                    mydescription[u'fr']=u'étape'+" " + race_genre + race_name + " "+ str(year)
                    item_stage.editDescriptions(mydescription, summary=u'Setting/updating descriptions.')
                
                stage_basic(pywikibot,repo,item_stage,site,ii,country_id,present_id)
                log.concat("race begin " + str(race_begin))
                stage_date=date_finder(pywikibot,repo,site,ii,first_stage,last_stage, race_begin,end_date)
                add_date(pywikibot,repo,item_stage,"P585",stage_date,u'date')
                
                #Link to the master for this year, so item
                add_multiple_value(pywikibot,repo,item,"P527",id_stage_present,u'link stage '+str(ii),0) 
                #Link to previous
                id_stage_previous="Q0"
                
                if ii==0:
                    lookforprevious=False
                else:   
                    if ii==1:
                        if first_stage==0:
                            lookforprevious=True
                        else:
                            lookforprevious=False
                    else:
                        lookforprevious=True
            
                    if lookforprevious:
                        #stage_label_previous=stage_label(ii-1, race_genre, race_name, year)
                        #id_stage_previous=search_item(pywikibot,site,stage_label_previous['fr'])
                        #if (id_stage_previous!=u'Q0')and(id_stage_previous!=u'Q1'):  #no previous or several
                        add_Qvalue(pywikibot,repo,item_stage,"P155",id_stage_previous,u'link previous') 
                            #Link to the previous
                        item_stage_previous=pywikibot.ItemPage(repo, id_stage_previous)
                        item_stage_previous.get()
                        add_Qvalue(pywikibot,repo,item_stage_previous,"P156",id_stage_present,u'link next')
                        id_stage_previous=id_stage_present     
                    
            #Link to next
            #Not required 
    return 0, log   