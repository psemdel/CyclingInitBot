# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:38:42 2018

@author: psemdel
"""
 
#from moo import *
#import exception


from .moo import ThisName, Cyclist, Team
from . import exception 

import csv 
import xlrd
import os.path

### Functions that are used from several other functions ###

# ==Low level function ==
def checkprop(property_nummer):
    if type(property_nummer)==str and property_nummer[0]=="P":
        prop=property_nummer
    else:
        prop=u'P' + str(property_nummer)
    return prop

def checkid(this_id): #avoid need for noQ and such parasit things
    if type(this_id)==str and this_id[0]==u'Q':
        result_id=this_id
    else:
        result_id=u'Q' + str(this_id)
    return result_id

def add_value(pywikibot, repo, item, property_nummer, value, comment):  # Add a value to a property
    prop=checkprop(property_nummer)
        
    if value!=0:
        if prop not in item.claims:  # already there do nothing
            claim = pywikibot.Claim(repo, prop)
            if isinstance(value, str):
                target = value
            else:
                target = pywikibot.ItemPage(repo, checkid(value))
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Adding ' + comment)

def add_Qvalue(pywikibot, repo, item, prop, value, comment):
 
    if value!=0:
        if prop not in item.claims:  # already there do nothing
            claim = pywikibot.Claim(repo, prop)
            target = pywikibot.ItemPage(repo, checkid(value))
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Adding ' + comment)  

def add_date(pywikibot, repo, item, property_nummer, input_date, comment):
    prop=checkprop(property_nummer)
    
    if prop not in item.claims:  # already there do nothing
        claim = pywikibot.Claim(repo, prop)
        claim.setTarget(input_date)
        item.addClaim(claim, summary=u'Adding ' + comment)

def delete_value(pywikibot, repo, item, property_nummer, value, comment):
    prop=checkprop(property_nummer)
    
    item_found = False
    item_position = 0
    if prop in item.claims:
        list_of_comprend = item.claims.get(prop)
        item_to_delete = pywikibot.ItemPage(repo, checkid(value))
        for ii in range(len(list_of_comprend )):
            if list_of_comprend [ii].getTarget() == item_to_delete:  # Already there
                item_found = True
                item_position = ii
    if item_found:
        allclaims = item.claims[prop]
        claim = allclaims[item_position]
        item.removeClaims(claim)

def delete_property(pywikibot, repo, item_id, property_nummer):
    prop=checkprop(property_nummer)
    
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if prop in item.claims :
        item.removeClaims(item.claims[prop])

# Same as add value but for comprend
def add_multiple_value(
        pywikibot,
        repo,
        item,
        property_nummer,
        value,
        comment,
        overpass):
    
    prop=checkprop(property_nummer)
    
    if value!=0:
        # check if the value is not already present
        if overpass:  # To add a value and then delete it for sorting purpose
            Addc = True
        else:
            Addc = True
            if prop in item.claims:  # already there do nothing
                list_of_comprend = item.claims.get(prop)
                item_to_add = pywikibot.ItemPage(repo, checkid(value))
                for comprend in list_of_comprend :
                    if comprend.getTarget() == item_to_add:  # Already there
                        Addc = False
                        print('Item already in the Master list')
        # add the value
        if Addc:
            claim = pywikibot.Claim(repo, prop)
            target = pywikibot.ItemPage(repo, checkid(value))
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Adding ' + comment)
        return Addc

def add_to_master(pywikibot,site,repo,present_id,id_master):
    item_master = pywikibot.ItemPage(repo,  checkid(id_master))
    item_master.get()
    add_multiple_value(
        pywikibot,
        repo,
        item_master,
        "P527",
        present_id,
        u'link year',
        0)

def add_winner(pywikibot, site, repo, item, value, order, general_or_stage):
    prop = "P1346"
    dic_order1={0:'Q20882667',2:'Q20883007', 3:'Q20883212', 4:'Q20883139'}
    Addc = True

    if order == 1:
        if general_or_stage in dic_order1:
            qualifier_nummer=dic_order1[general_or_stage]
        else:
            qualifier_nummer = 'Q20882667'
    elif order == 2 and general_or_stage==0:
        qualifier_nummer = 'Q20882668'
    elif order == 3 and general_or_stage==0:
        qualifier_nummer = 'Q20882669'
    else:
        Addc = False

    if Addc:
        if prop in item.claims:
            list_of_winners = item.claims.get(prop)
            item_to_add = pywikibot.ItemPage(repo, value)
            # look if already there as a rider can't be first, second and third
            # at the same time
            for winner in list_of_winners:
                if winner.getTarget() == item_to_add:  # Already there
                    Addc = False
                    print('winner already in the list')

        if Addc:
            claim = pywikibot.Claim(repo, prop)
            target = pywikibot.ItemPage(repo, value)
            claim.setTarget(target)
            item.addClaim(claim, summary=u'Adding winner')
            qualifierDe = pywikibot.page.Claim(site, 'P642', isQualifier=True)
            targetQualifier = pywikibot.ItemPage(repo, qualifier_nummer)
            qualifierDe.setTarget(targetQualifier)
            claim.addQualifier(qualifierDe)

def noQ(item_id):
    itemResult = item_id[1:]
    return int(itemResult)

# ==date==
def compare_dates(date1, date2):
    # equal to 1 if date 1 is higher than 2, otherwise 2, and 0 if equal
    year1 = int(date1.year)
    year2 = int(date2.year)
    if year1 > year2:
        output = 1
    elif year1 < year2:
        output = 2
    else:
        month1 = int(date1.month)
        month2 = int(date2.month)
        if month1 > month2:
            output = 1
        elif month1 < month2:
            output = 2
        else:
            day1 = int(date1.day)
            day2 = int(date2.day)
            if day1 > day2:
                output = 1
            elif day1 < day2:
                output = 2
            else:
                output = 0  # equal date
    return output

def link_year(pywikibot, site,repo, present_id,arg1,arg2):
    #arg1 = year or nameprev
    #arg2 = name or namenext

    if isinstance(arg1, str):
        year_bool=False
        nameprev=arg1
        namenext=arg2        
    elif isinstance(arg1, dict):
        year_bool=False
        nameprev=arg1['fr']
        namenext=arg2['fr']
    else:
        year_bool=True
        year=arg1
        if isinstance(arg2, dict): #should be the case
            name=arg2['fr']
        else:
            name=arg2
    #previous or next
    kk=-1
    
    while kk<2:
        mylabel_other={}
        if year_bool:
            mylabel_other['fr'] = name + " " + str(year + kk)
        else:
            if kk==-1:
                mylabel_other['fr'] = nameprev
            else:
                mylabel_other['fr'] = namenext
        id_other = search_item(pywikibot, site, mylabel_other['fr'])
        if (id_other != u'Q0') and (id_other != u'Q1'):  # no previous or several
            if kk==-1:
                p1="P155"
                suffix1='previous'
                p2="P156"
                suffix2='next'
            else:
                p2="P155"
                suffix2='previous'
                p1="P156"
                suffix1='next'
            item = pywikibot.ItemPage(repo, present_id)
            item.get()
            add_Qvalue(pywikibot, repo, item, p1, id_other, u'link '+suffix1)
            item_other = pywikibot.ItemPage(repo, id_other)
            item_other.get()
            add_Qvalue(pywikibot, repo, item_other, p2, present_id, u'link '+suffix2)
        kk=kk+2

def create_present(pywikibot, site,repo,time, label):   
   present_id = search_item(pywikibot, site, label['fr'])
   
   if (present_id == u'Q0'):
       print(label['fr'] + ' created')
       # Type code
       present_id = create_item(pywikibot, site, label)
       time.sleep(1.0)
   elif (present_id == u'Q1'):
       print(label['fr'] + ' already present several times')
   else:
       print(label['fr'] + ' already present')
   if present_id!=u'Q1':
       item = pywikibot.ItemPage(repo, present_id)
       item.get()
   return present_id, item

def get_year(pywikibot, repo, present_id):
    item = pywikibot.ItemPage(repo, present_id)
    item.get()
    if (u'P585' in item.claims):
         this_claim = item.claims.get(u'P585')
         this_date = this_claim[0].getTarget()
    elif (u'P580' in item.claims):
        this_claim  = item.claims.get(u'P580')
        this_date = this_claim[0].getTarget()
    else:
        return 0

    return int(this_date.year)

def get_date(pywikibot, repo, present_id):
    item = pywikibot.ItemPage(repo, present_id)
    item.get()
    if (u'P585' in item.claims):
         this_claim = item.claims.get(u'P585')
         this_date = this_claim[0].getTarget()
    elif (u'P580' in item.claims):
        this_claim  = item.claims.get(u'P580')
        this_date = this_claim[0].getTarget()
    else:
        return 0

    return this_date

def date_duplicate(pywikibot, date_input):
    return pywikibot.WbTime.fromTimestr(date_input.toTimestr(),precision="day")
    
#function for race
#determine the date of a stage
def date_finder(pywikibot, number,first_stage,last_stage, race_begin,
                race_end):
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if number==last_stage:
         return date_duplicate(pywikibot,race_end)
    elif number<=first_stage:
         return date_duplicate(pywikibot, race_begin)
    elif number!=first_stage:
         output_date=date_duplicate(pywikibot, race_begin)
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

# ==Table reader ==

def float_to_int(a):
    if isinstance(a, str):
        a=a.replace(",",".")
       # a=a.replace(".0","")
    return int(float(a))

def clean_txt(a):
    return a

#convert the time in seconds
def time_converter(this_input):
    ecart=False
    if this_input == '' or this_input == 0 or this_input == '0':
        return 0, ecart
    elif this_input == '+0' or this_input == '+00':
        return 0, True
    else:
        if this_input.find("+")==0:
            this_input=this_input[1:]
            ecart=True
      
        timesplit = this_input.split(":")
        
        if len(timesplit) == 3:
            thistime= float_to_int(timesplit[0]) * 3600 + float_to_int(timesplit[1]) * 60 + float_to_int(timesplit[2])
        elif len(timesplit) == 2:
            thistime= float_to_int(timesplit[0]) * 60 + float_to_int(timesplit[1])
        else:
            thistime= float_to_int(timesplit[0])

        if thistime < 120: #suspicious
            ecart=True
        return thistime, ecart


def bot_or_site():
    if 'bot_requests' in os.listdir():
        return False #site
    else:
        return True #bot

def excel_to_csv(filepath, destination):
    wb = xlrd.open_workbook(filepath)
    list_of_sheets=wb.sheet_names()
    sheet_nm=['Results','Invidual','Team']
    if list_of_sheets is None:
        print("empty excel file")
        return None

    sh=wb.sheet_by_name(list_of_sheets[0])
    for sheet in list_of_sheets:
        if sheet in sheet_nm:
            sh = wb.sheet_by_name(sheet)
            break
        
    destination_file = open(destination, 'w')
    wr = csv.writer(destination_file, delimiter=";", quoting=csv.QUOTE_NONE)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    destination_file.close()
    return destination
        
def table_reader(filename,result_dic, startline, verbose):
    default_separator=';'
    bot=bot_or_site() 
    filepathxlsx=None
    local_saved_list=["champ","champ_clm","champ_man","champ_man_clm"]
    
    clean_txt_bool=False
    #differentiate local from remote
    if filename[(len(filename)-3):]=='csv' or filename[(len(filename)-4):]=='xlsx':
        if filename[(len(filename)-3):]=='csv':
            filepathcsv='uploads/'+filename
        else:
            filepathcsv=None
            filepathxlsx='uploads/'+filename
 
    elif filename in local_saved_list:
        if bot:
            filepathcsv="src/input/"+filename+".csv"
        else:
            filepathcsv="bot_src/src/input/"+filename+".csv"
        if os.path.isfile(filepathcsv)==False:
            print("champ file detection failed!")
    elif bot: #by site not allowed other type
        filepathcsv='src/input/'+filename+'.csv'
        filepathxlsx='src/input/'+filename+'.xlsx'    
    
    if (filepathcsv is not None) and os.path.isfile(filepathcsv):
        filepath=filepathcsv
    elif (filepathxlsx is not None) and os.path.isfile(filepathxlsx):
        filename=filename[:(len(filename)-5)] #excel
        if bot:
            destination='src/input/'+filename+'.csv'
        else:
            destination='uploads/'+filename+'.csv'
        filepath=excel_to_csv(filepathxlsx,destination)
        clean_txt_bool=True
    else:
        print(filename + ': no file found')
        return None, 0, None
    
    if verbose:
        print("corrected file path: " + filepath)
    
    with open(filepath, newline='') as csvfile:
        file_object = csv.reader(csvfile, delimiter=default_separator, quotechar='|')
        
        for row in file_object: 
            if len(row)==1:  #wrong separator, try coma
                separator=','
            else:
                separator=default_separator
            break #always break
    if verbose: 
        print(u'separator :' + separator)
    #count the number of rows not empty 
    kk=0       
    with open(filepath, newline='') as csvfile:
        file_object = csv.reader(csvfile, delimiter=separator, quotechar='|')
        for row in file_object:
            is_empty=True
            for ii in range(len(row)):
                if row[ii]!='':
                    is_empty=False
            if is_empty:
                break
            else:
                kk=kk+1
                
        row_count =kk-1
    if verbose:
        print(str(row_count) + " lines in the file")
    
    result_table = [[0 for x in range(len(result_dic))] for y in range(row_count)]
    kk = 0
    ecart_global=False
    
    with open(filepath, newline='') as csvfile:
        file_object = csv.reader(csvfile, delimiter=separator, quotechar='|')

        for row in file_object:
            if kk == startline:
                if verbose:
                    print(row)  #allow to see if there is no problem with the separator
                for jj in range(len(row)):
                    if clean_txt_bool:
                        row[jj]=clean_txt(row[jj])
                    column=row[jj].lower()
                    if column in result_dic:
                        result_dic[column][0]=jj
            elif kk>startline and kk<=row_count:
                for dic_key in result_dic:
                    dic_content=result_dic[dic_key]
                    if dic_content[0]!=-1:
                        if dic_key=='rank' or dic_key=='bib':
                            if row[dic_content[0]]=='':
                                result_table[kk-1][dic_content[1]]=0
                            else:
                                result_table[kk-1][dic_content[1]]=float_to_int(row[dic_content[0]])
                        else:
                            if dic_content[2]=='time':
                                result_table[kk-1][dic_content[1]], ecart=time_converter(row[dic_content[0]])
                                if kk==startline+2:
                                    ecart_global=ecart
                            elif  dic_content[2]=='points':
                                result_table[kk-1][dic_content[1]]=float_to_int(row[dic_content[0]])
                            else:
                                if clean_txt_bool:
                                    result_table[kk-1][dic_content[1]]=clean_txt(row[dic_content[0]])
                                else:
                                    result_table[kk-1][dic_content[1]]=row[dic_content[0]]
            kk = kk + 1
    if verbose:
        print('table read')
    return result_table, row_count, ecart_global

#create a list of cyclist objects from result_table
#check that all items are there before modifying the database
def cyclists_table_reader(pywikibot, site, repo, result_table,result_dic, **kwargs):
    list_of_cyclists = []
    list_of_teams=[]
    all_riders_found=True
    all_teams_found=True
    log=''
    search_team=kwargs.get('search_team',False)
    man_or_woman=kwargs.get('man_or_woman',u'woman') #used only for team
    #check if all riders are already present
    for ii in range(len(result_table)):
        if (result_table[ii][result_dic['name'][1]]!=0 or result_table[ii][result_dic['first name'][1]]!=0):
           id_rider=search_rider(pywikibot, site, repo,result_table[ii][result_dic['name'][1]],
                                    result_table[ii][result_dic['first name'][1]],result_table[ii][result_dic['last name'][1]] )
   
           if id_rider!='Q0' and id_rider!='Q1':
               item_rider = pywikibot.ItemPage(repo, id_rider)
               item_rider.get()
               
               nosortkey=kwargs.get('nosortkey',False)

               this_label=get_label('fr', item_rider)
               this_rider=Cyclist(ii, this_label, id_rider, nosortkey=nosortkey)
               this_rider.item=item_rider
               this_rider.dossard=result_table[ii][result_dic['bib'][1]]
               this_rider.rank=result_table[ii][result_dic['rank'][1]]
           else:
               all_riders_found=False
               error_msg=str(result_table[ii][result_dic['name'][1]]) 
               error_msg = error_msg + " " +  str(result_table[ii][result_dic['last name'][1]]) + " "  
               error_msg = error_msg + str(result_table[ii][result_dic['bib'][1]]) + " not found"
               log=log + '\n' + error_msg
               print(error_msg)
               
               this_rider=Cyclist(ii, 'not found', id_rider)
           list_of_cyclists.append(this_rider)
        if search_team:
            if result_table[ii][result_dic['team code'][1]]!=0 and result_table[ii][result_dic['team code'][1]]!="":
                if man_or_woman=="woman":
                    id_team=search_team_by_code(pywikibot, site,  repo, result_table[ii][result_dic['team code'][1]])
                else:
                    id_team=search_team_by_code_man(pywikibot, site, repo,  result_table[ii][result_dic['team code'][1]])
                
                if id_team!='Q0' and id_team!='Q1':
                    this_team=Team(ii, 
                                   result_table[ii][result_dic['team code'][1]],
                                   id_team,
                                   '',site=site,pywikibot=pywikibot)
                else:
                    this_team=Team(ii,'not found', "Q0", '',site=site,pywikibot=pywikibot) 
                    error_msg=str(result_table[ii][result_dic['team code'][1]])+ " not found"
                    print(error_msg)
                    log = log + '\n' + error_msg
                    all_teams_found=False
            else:
                this_team=Team(ii,'no team', "Q0", '',site=site,pywikibot=pywikibot) 
            list_of_teams.append(this_team)        

    if all_teams_found: 
        log = log+' list of teams created'
        print('list of teams created')
    else:
        log= log+' reading of list of teams: failure not all teams found'
        print('reading of list of teams: failure not all teams found')
    
    if all_riders_found: 
        log = log+' list of cyclists created'
        print('list of cyclists created')
    else:
        log= log+' reading of list of cyclists: failure not all riders found'
        print('reading of list of cyclists: failure not all riders found')
    return list_of_cyclists, all_riders_found, log, list_of_teams, all_teams_found

# ==Search ==
def search_race(name, race_table,race_dic):
    result = 0, 0
    
    thisname=ThisName(name)  #delete the accent and so on
    name=thisname.name_cor
    
    for ii in range(len(race_table)):
        if race_table[ii][race_dic['name1']] != 0 and race_table[ii][race_dic['name2']] != 0:
            thisname2=ThisName(race_table[ii][race_dic['name1']])
            key1=thisname2.name_cor
            
            thisname3=ThisName(race_table[ii][race_dic['name2']])
            key2=thisname3.name_cor  
            
            if name.find(key1) != -1:
                if name.find(key2) != -1:
                    return race_table[ii][race_dic['master']], race_table[ii][race_dic['genre']]

    return result 

def is_it_a_cyclist(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if(u'P106' in item.claims): 
        list_of_occupation = item.claims.get(u'P106')
        cyclist_occupation = pywikibot.ItemPage(repo, u'Q2309784')
        for occu in list_of_occupation:
            if occu.getTarget() == cyclist_occupation:  # Already there
                return True
    return False

def is_it_a_teamseason(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if(u'P31' in item.claims):  
        list_of_natures = item.claims.get(u'P31')
        team_season = pywikibot.ItemPage(repo, u'Q53534649')
        for nature in list_of_natures:
            if nature.getTarget() == team_season:  # Already there
                return True
    return False


def search_item(pywikibot, site, search_string):
    from pywikibot.data import api
    wikidata_entries = get_items(api, site, search_string)
        
    if(wikidata_entries['search'] == []):
        # no result
        result_id = u'Q0'
    elif len(wikidata_entries['search'])==1:
        wikidataSearchresult = wikidata_entries['search']
        wikidataSearchresult1 = wikidataSearchresult[0]
        result_id = wikidataSearchresult1['id']
    else:
        # several results
        result_id = u'Q1'

    return result_id

def search_itemv2(pywikibot, site,  repo, search_string, rider_bool,code_bool, **kwargs): #For Team and rider
    from pywikibot.data import api
    
    if search_string!=0:
        this_name=ThisName(search_string)
        if rider_bool:
            ref_name=this_name.name_cor
        else:
            ref_name=this_name.name #no need to revert
    else:
        first_name=kwargs.get('first_name','')
        last_name=kwargs.get('last_name','')
        name=first_name + " " + last_name
        if name!=" ":
           this_name=ThisName(name)
           ref_name=this_name.name_cor
        else:
           return u'Q1', ''
    
    #exception management
    exception_table=kwargs.get('exception_table',[])
    for ii in range(len(exception_table)):
        this_exception=ThisName(exception_table[ii][0])  
        if code_bool:
            exp=this_exception.name
        else:
            exp=this_exception.name_cor
       
        if ref_name==exp:
               return exception_table[ii][1]
      

    wikidata_entries = get_items(api, site, ref_name)
    disam=kwargs.get('disam',None) #disambiguation_function
    force_disam=kwargs.get('force_disam',False) #disam criteria must be always filed
    
    if(wikidata_entries['search'] == []):
        # no result
        result_id = u'Q0'
    elif len(wikidata_entries['search'])==1:
        wikidataSearchresult = wikidata_entries['search']
        wikidataSearchresult1 = wikidataSearchresult[0]
        temp_id  = wikidataSearchresult1['id'] 
        if force_disam==False:
            result_id=temp_id
        else:
            if disam(pywikibot, repo, temp_id):
                result_id=temp_id
    else:
        candidate=0
        result_id = u'Q1'
        if disam!=None:
            all_results = wikidata_entries['search']
            for result in all_results:
                temp_id=result['id']
                if disam(pywikibot, repo, temp_id):
                    if force_disam==False:
                        result_id=temp_id
                        break
                    else:
                        candidate=candidate+1
            if candidate==1:
                result_id=temp_id
            elif candidate>1:
                print("2 teams found for: " +ref_name)
        
    return result_id

def search_rider(pywikibot, site, repo,search_string, first_name, last_name):
    exception_table=exception.list_of_rider_exception()
    return search_itemv2(pywikibot, site, repo, search_string, True, False, disam=is_it_a_cyclist, 
                        exception_table=exception_table, first_name=first_name, last_name=last_name)

def search_team_by_name(pywikibot, site,  repo, search_string):
    exception_table=exception.list_of_team_name_exception()
    return search_itemv2(pywikibot, site,  repo, search_string, False, False, exception_table=exception_table)

def search_team_by_code(pywikibot, site, repo,  search_string):
    exception_table=exception.list_of_team_code_exception()
    return search_itemv2(pywikibot, site,  repo, search_string, False, True,
                         exception_table=exception_table,
                         disam=is_it_a_teamseason,
                         force_disam=True)

def search_team_by_code_man(pywikibot, site,  repo, search_string):
    exception_table=exception.list_of_team_code_exception_man()
    return search_itemv2(pywikibot, site, repo,  search_string, 
                         False, 
                         True, 
                         exception_table=exception_table, 
                         disam=is_it_a_teamseason,
                         force_disam=True)

## other ##
def get_class_id(classe_text):
    dic_class={
      "1.1":"Q22231110",
      "2.1":"Q22231112",
      "1.2":"Q22231111",
      "2.2":"Q22231113",
      "1.WWT":"Q23005601",
      "2.WWT":"Q23005603",
      "1.Pro":"Q74275170",
      "2.Pro":"Q74275176",
      "1.5":"Q98686837",
      "1.UWT":"Q22231106",
      "2.UWT":"Q22231107",
       } 
    
    if classe_text in dic_class:
        return dic_class[classe_text]
    else:
        return 0
    
def get_class_WWT(classe):    
    UCI=True
    
    dic_WWT={
      "1.1":False,
      "2.1":False,
      "1.2":False,
      "2.2":False,
      "1.5":False,
      "1.WWT":True,
      "2.WWT":True,
      "1.Pro":False,
      "2.Pro":False,
      "1.UWT":False,
      "2.UWT":False,
         } 
    
    dic_UWT={
      "1.1":False,
      "2.1":False,
      "1.2":False,
      "2.2":False,
      "1.5":False,
      "1.WWT":False,
      "2.WWT":False,
      "1.Pro":False,
      "2.Pro":False,
      "1.UWT":True,
      "2.UWT":True,
         }  
    
    if classe in dic_WWT:
        return UCI, dic_WWT[classe], dic_UWT[classe]
    else:
        return UCI, 0, 0    

def get_single_or_stage(classe):    
    #single=true
    if type(classe)==str:
        if classe[0]=="2":
            return False
    return True

def get_country(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if (u'P17' in item.claims):
         P17=item.claims.get(u'P17')
         return P17[0].getTarget().getID()
    else:
        return "Q0"
    
#return ID of country from nationality
def get_nationality(pywikibot, repo, site, item_id, time_of_race):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    result="Q0"
    if (u'P1532' in item.claims):
        nationalities=item.claims.get(u'P1532')
        if len(nationalities)==1:
           result=nationalities[0].getTarget().getID()
        else:
            for nationality in nationalities:
                if ('P580' in nationality.qualifiers):
                    begin_time = nationality.qualifiers['P580'][0].getTarget()
                else:
                    begin_time = pywikibot.WbTime(
                    site=site, year=1000, month=1, day=1, precision='day')   
                    
                if ('P582' in nationality.qualifiers):
                    end_time = nationality.qualifiers['P582'][0].getTarget()
                    if end_time.month == 0:
                        end_time.month = 12
                        end_time.day = 31
                else:
                    end_time = pywikibot.WbTime(
                    site=site, year=2100, month=1, day=1, precision='day')
            
                if (compare_dates(begin_time,time_of_race) == 2 or compare_dates(begin_time,time_of_race) == 0) and (compare_dates(end_time,time_of_race) == 1 or compare_dates(end_time,time_of_race) == 0):
                    result = nationality.getTarget().getID()
                    break
        
    if result=="Q0":
        if (u'P27' in item.claims):
            nationalities=item.claims.get(u'P27')
            if len(nationalities)==1:
               result=nationalities[0].getTarget().getID()
            else:
                for nationality in nationalities:
                    if ('P580' in nationality.qualifiers):
                        begin_time = nationality.qualifiers['P580'][0].getTarget()
                    else:
                        begin_time = pywikibot.WbTime(
                        site=site, year=1000, month=1, day=1, precision='day')   
                    if ('P582' in nationality.qualifiers):
                        end_time = nationality.qualifiers['P582'][0].getTarget()
                        if end_time.month == 0:
                            end_time.month = 12
                            end_time.day = 31
                    else:
                        end_time = pywikibot.WbTime(
                        site=site, year=2100, month=1, day=1, precision='day')
                
                    if (compare_dates(begin_time,time_of_race) == 2 or compare_dates(begin_time,time_of_race) == 0) and (compare_dates(end_time,time_of_race) == 1 or compare_dates(end_time,time_of_race) == 0):
                        result = nationality.getTarget().getID()
                        break
    if  result=="Q15180": #USSR
        print("USSR rider")
        print(item_id)
    return result
    
 
def get_race_begin(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if (u'P580' in item.claims):
        this_date = item.claims.get(u'P580')[0].getTarget()
    else:
        return 0
    
    return this_date

def get_end_date(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    if (u'P582' in item.claims):
        this_date = item.claims.get(u'P582')[0].getTarget()
    else:
        return 0
    return this_date    

    
def get_class(pywikibot, repo, item_id):
    item = pywikibot.ItemPage(repo, item_id)
    item.get()
    
    class_list=[
        "Q22231106",
        "Q22231107",
        "Q22231108",
        "Q22231109",
        "Q22231110",
        "Q22231111",
        "Q22231112",
        "Q2231113",
        "Q22231114",
        "Q22231115",
        "Q22231116",
        "Q22231117",
        "Q22231118",
        "Q22231119",
        "Q23015458",
        "Q23005601",
        "Q23005603",
        "Q74275170",
        "Q74275176" 
     ]
    
    if (u'P31' in item.claims):
        P31=item.claims.get(u'P31')
        for p31 in P31:
            tempQ=p31.getTarget().getID()
            if tempQ in class_list:
                return tempQ
    return ""
 
def define_article(name):
    this_name=ThisName(name)
    race_name=name
    
    correspondance_start={
        "le " : "du ",
        "la " : "de la ",
        "les " : "des "        
        }
    
    correspondance={
		"trois":"des ",
		"quatre":"des ",
		"boucles":"des ",
		"triptyque":"du ",
		"tour":"du ",
		"grand prix":"du ",
		"circuit":"du ",
		"memorial":"du ",
		"trophee":"du ",
		"ronde":"de la ",
		"semaine":"de la ",
		"classica":"de la ",
		"fleche":"de la ",
		"course":"de la ",
		"classique":"de la ",
		"race":"de la ",
		"etoile":"de l'",
        "championnats": "des ",
        "championnat": "du ",
        "chrono": "du ",
        "contre-la-montre": "du ",
        "criterium": "du ",
		}
    
    vocal=['a','e','i','o','u']
    
    for key in correspondance_start:
        if this_name.name_cor.find(key)==0:
            race_name=name[len(key):]
            
            return correspondance_start[key], race_name
   
    if this_name.name_cor[0] in vocal:
        return "de l'" , race_name
    
    for key in correspondance:
        if this_name.name_cor.find(key)!=-1:
            return correspondance[key], race_name

    return "du ", race_name #default

def get_items(api, site, itemtitle):
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'fr',
        'type': 'item',
        'search': itemtitle,
        'limit': 10}
    #params.update({'continue': 1})
    request = api.Request(site=site, parameters=params)
    search_results = request.submit()
    if search_results['success'] != 1:
        print('WD search failed')
    else:
        return search_results

def get_present_team(pywikibot, site, repo, id_rider, time_of_race):
    result = 'Q1'
    item = pywikibot.ItemPage(repo, id_rider)
    item.get()
    if (u'P54' in item.claims):
        allteams = item.claims.get(u'P54')
        for this_team in allteams:
            if ('P580' in this_team.qualifiers):
                begin_time = this_team.qualifiers['P580'][0].getTarget()
            if ('P582' in this_team.qualifiers):
                end_time = this_team.qualifiers['P582'][0].getTarget()
                if end_time.month == 0:
                    end_time.month = 12
                    end_time.day = 31
            else:
                end_time = pywikibot.WbTime(
                    site=site, year=2100, month=1, day=1, precision='day')
            
            if (compare_dates(begin_time,time_of_race) == 2 or compare_dates(begin_time,time_of_race) == 0) and (compare_dates(end_time,time_of_race) == 1 or compare_dates(end_time,time_of_race) == 0):
                result = this_team.getTarget().getID()
                break
    return result

def teamCIOsearch(team_table, CIOcode):
    result = 0

    for ii in range(len(team_table)):
        if team_table[ii][7] == CIOcode:
            result = ii
            break

    return result


def CIOtoIDsearch(team_table, CIOcode):
    result = 0

    for ii in range(len(team_table)):
        if team_table[ii][7] == CIOcode:
            result = team_table[ii][3]
            break
    return result


def IDtoCIOsearch(team_table, ID):
    #exception
    if ID==55:
        return 'NED'
    
    result = "no code"
    for ii in range(len(team_table)):
        if team_table[ii][3] == ID:
            result = team_table[ii][7]
            break
    if result=="no code":
        print("country ID not found: " + str(ID))
    return result

# ==Create==
def create_item(pywikibot, site, label_dict):
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
    elif 'en'  in wikidataitem.labels:
        return wikidataitem.labels['en']
    else:
        for lang in wikidataitem.labels:
               return  wikidataitem.labels[lang]
        return ''

def get_alias(language, wikidataitem):
    if language in wikidataitem.aliases:
        return wikidataitem.aliases[language]
    else:
        return('')



