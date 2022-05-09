#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:51:33 2022

@author: maxime
"""

import pywikibot
import os
import pandas as pd
import math

from .name import Name
from .base import Search, Cyclist, Team

import sys

####Code without object 
def noQ(item_id):
    return int(item_id[1:])

def is_website():
    if 'bot_requests' in os.listdir():
        return True #site
    return False #bot

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
        return None

def get_single_or_stage(classe):    
    #single=true
    if type(classe)==str:
        if classe[0]=="2":
            return False
    return True

def date_duplicate(date_input):
    #? date_input.copy()
    return pywikibot.WbTime.fromTimestr(date_input.toTimestr(),precision="day")

#function for race
#determine the date of a stage
def date_finder(number,first_stage,last_stage, race_begin,
                race_end):
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if number==last_stage:
         return date_duplicate(race_end)
    elif number<=first_stage:
         return date_duplicate(race_begin)
    elif number!=first_stage:
         output_date=date_duplicate(race_begin)
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

#convert the time in seconds
def time_converter(e, winner_time):
    ecart=False
    
    if not isinstance(e, str):
        if math.isnan(e):
            return -1
    elif e in ['+0', '+00']:
        return winner_time
    else:
        if e.find("+")==0:
            e=e[1:]
            ecart=True
      
        #if h then replace through :, if ' then replace through :
        if isinstance(e, str):
            if e.find("h")!=-1:
                e=e.replace("h",":")
            if e.find("'")!=-1:
                e=e.replace("'",":")   
            if e.find('"')!=-1:
                e=e.replace('"',":")   
            if e.find("::")!=-1:
                e=e.replace("::","")        
            if e.find(".")!=-1:
                e=e.replace(".",":")  
            if e[-1]==":":
                e=e[:-1]
            
            timesplit = e.split(":")
            
            if len(timesplit) == 3:
                t= float_to_int(timesplit[0]) * 3600 + float_to_int(timesplit[1]) * 60 + float_to_int(timesplit[2])
            elif len(timesplit) == 2:
                t= float_to_int(timesplit[0]) * 60 + float_to_int(timesplit[1])
            else:
                t= float_to_int(timesplit[0])
        else:
            return -1
            print("time is not a string")

        if t < 120: #suspicious
            ecart=True
            
        if ecart:
            t+=winner_time
        return t
    
def calc_ecart(e, winner_time):
    if e==-1:
        return e
    else:
        return e-winner_time

def float_to_int(a):
    if a=='':
        return 0
    else:
        if isinstance(a, str):
            a=a.replace(",",".")
        return int(float(a))

def define_article(name):
    if name==None:
        return "", ""
    else:
        this_name=Name(name)
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

def table_reader(filename,**kwargs):  #startline, 
    try:
        verbose=kwargs.get("verbose",False)
        local_saved_list=["champ","champ_clm","champ_man","champ_man_clm"]
        file_csv=True
        filepath=None
        log=''
        all_riders_found=True
        all_teams_found=True
       
        #differentiate local from remote
        if filename[-3:]=='csv': #with the site, the extension is given
            filepath='uploads/'+filename
        elif filename[-4:]=='xlsx':
            filepath='uploads/'+filename
            file_csv=False
        elif filename in local_saved_list:
            if is_website():
                filepath="bot_src/src/input/"+filename+".csv"       
            else:
                filepath="src/input/"+filename+".csv"
        elif not is_website(): #for local use only
            if os.path.isfile('src/input/'+filename+'.csv'):
                filepath='src/input/'+filename+'.csv'
            elif os.path.isfile('src/input/'+filename+'.xlsx'):
                filepath='src/input/'+filename+'.xlsx'
                file_csv=False

        if filepath is None or not os.path.isfile(filepath):
            raise ValueError("import file not found")
        elif verbose:
            print("corrected file path: " + filepath)

        if file_csv:
            df=pd.read_csv(filepath)
        else:
            df=pd.read_excel(filepath)
        
        if len(df.columns)==1:
            raise ValueError("import file uses ; separator, correct to ,")

        #pre-processing
        if 'Result' in df: #no for champ
            if kwargs.get('result_points',False):
                df["Points"]=df["Result"].apply(lambda x:  float_to_int(x)) 
            else:
                winner_time=time_converter(df["Result"].values[0],0)
                df["Time"]=df["Result"].apply(lambda x: time_converter(x, winner_time)) 
                df["Ecart"]=df["Time"].apply(lambda x: calc_ecart(x, winner_time)) 
    
        #search the rider
        if kwargs.get('rider',False):
            name_bool=False
            first_name_bool=False
            last_name_bool=False
            bib_bool=False
            if 'Name' in df.columns:
                name_bool=True
            if 'First Name' in df.columns:
                first_name_bool=True
            if 'Last Name' in df.columns:
                last_name_bool=True
            if 'BIB' in df.columns:
                bib_bool=True
                
            rider_ids=[]
            for ii in range(len(df.index)):
                name=None
                first_name=None
                last_name=None
                bib=None
                
                if name_bool:
                    name=df['Name'].values[ii]
                if first_name_bool:
                    first_name=df['First Name'].values[ii]
                if last_name_bool:
                    last_name=df['Last Name'].values[ii]
                if bib_bool:
                    bib=df['BIB'].values[ii]
                
                s=Search(name) 
                id_rider=s.rider(first_name,last_name)
                
                if kwargs.get("need_complete",False):
                   if id_rider in ['Q0','Q1']:
                       log+="\n" + str(first_name) + " " +  str(last_name) + " "  + str(name) +\
                            " number "+ str(bib)+" not found"
                       all_riders_found=False
                rider_ids.append(id_rider)
            df["ID Rider"]=rider_ids
        if kwargs.get("team",False) or kwargs.get("convert_team_code",False):
            year=kwargs.get("year",None)
            
            if "Team Code" not in df.columns:
                raise ValueError("Team Code not present in import file")
            elif year is None:
                raise ValueError("No year present to create Team Code")
            else:
                df["Team Code"]=df["Team Code"].apply(lambda x: x+" "+str(year))

            if kwargs.get("team",False):
                team_ids=[]
                man_or_woman=kwargs.get('man_or_woman',u'woman') #used only for team
                
                for ii in range(len(df.index)):
                    team_code=df["Team Code"].values[ii]
                    s=Search(team_code)
                    id_team=s.team_by_code(man_or_woman=man_or_woman)
                    
                    if kwargs.get("need_complete",False):
                        if id_team in ['Q0','Q1']:
                            log+="\n" + str(team_code) + " not found"
                            all_teams_found=False
                    team_ids.append(id_team)
                df["ID Team"]=team_ids

        if verbose:
            print('table read')

        return df, all_riders_found, all_teams_found, log
    except Exception as msg:
        _, _, exc_tb = sys.exc_info()
        print("line " + str(exc_tb.tb_lineno))
        print(msg)
        print("table read failure")
        return None, None, None, ''

#transform the df in a list of Cyclist objects
def cyclists_table_reader(df,**kwargs):
    try:
        list_of_cyclists =[]
        list_of_teams=[]
        bib_bool=False
        rank_bool=False
        team_code_bool=False
        id_team_bool=False
        
        #check if all riders are already present
        if "ID Rider" not in df.columns:             
            raise ValueError("ID Rider not present in dataframe")
        if 'BIB' in df.columns:
            bib_bool=True
        if 'Rank' in df.columns:
            rank_bool=True      
        if 'Team Code' in df.columns:
            team_code_bool=True        
        if "ID Team" in df.columns:
            id_team_bool=True
            
        for ii in range(len(df.index)):
            if df["ID Rider"].values[ii] in ['Q0','Q1']:
                this_rider=Cyclist(name='not found')
            else:
                this_rider=Cyclist(id=df["ID Rider"].values[ii])
                if bib_bool:
                    this_rider.dossard=df["BIB"].values[ii]
                if rank_bool:
                    if not math.isnan(df["Rank"].values[ii]):
                        this_rider.rank=df["Rank"].values[ii]
            list_of_cyclists.append(this_rider)

            if id_team_bool:
                if df["ID Team"].values[ii] in ['Q0','Q1']:
                    this_team=Team(name='not found')  #just as filler
                else:
                    this_team=Team(id=df["ID Team"].values[ii])
                    if team_code_bool:
                        this_team.codeUCI=df['Team Code'].values[ii]
                list_of_teams.append(this_team)   

        return list_of_cyclists, list_of_teams
    except Exception as msg:
        print(msg)
        print("cyclists_table_reader read failure")
        return None, None
