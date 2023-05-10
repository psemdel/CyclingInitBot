#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:51:33 2022

@author: maxime
"""

import pywikibot
import os
import pandas as pd
import numpy as np
import math
from datetime import datetime

from .name import Name
from .base import Search, Cyclist, Team
from .first_cycling_api import RaceEdition

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

def man_or_women_to_is_women(man_or_woman):
    print("man_or_woman")
    print( man_or_woman)
    print(man_or_woman in ["woman","womanJ","womanU"])
    
    if man_or_woman in ["woman","womanJ","womanU"]:
        return True
    else:
        return False

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
    elif e in ['+','+0', '+00']:
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

def to_float(a):
    try:
        if a=='':
            return 0
        else:
            if isinstance(a, str):
                a=a.replace(",",".")
            t=float(a)
            if t==int(t):
                return int(a)
            else:
                return t
    except Exception as msg:
        print("exception in to_float")
        print(msg)
        print("faulty string: " +a)

def float_to_int(a):
    return int(to_float(a))

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

general_or_stage_to_fc={
    0:'gc', #general
    1:'sta',#stage
    2:'point',#points
    3:'mountain',#mountains
    4:'youth',#youth 
    5:'team',#teamtime
    8:'sprint'#sprint 
    }
general_or_stage_to_fc_inv = {v: k for k, v in general_or_stage_to_fc.items()}

def get_fc_dic(fc,**kwargs):
    stage_num=kwargs.get("stage_num")
    year=kwargs.get("year",datetime.now().year)
    if stage_num==0:
        stage_num=None
    race_edition = RaceEdition(race_id=fc, year=year)
    race_edition.ext_results(stage_num=stage_num)
    
    general_or_stages=[]
    
    for k in race_edition.standings:
        general_or_stages.append(general_or_stage_to_fc_inv[k])

    return general_or_stages

def table_reader(filename,fc,**kwargs):  #startline, 
    try:
        verbose=kwargs.get("verbose",False)
        local_saved_list=["champ","champ_clm","champ_man","champ_man_clm"]
        file_csv=True
        filepath=None
        log=''
        all_riders_found=True
        all_teams_found=True
        year=kwargs.get("year",datetime.now().year)

        #differentiate local from remote
        if fc is not None:
            stage_num=kwargs.get("stage_num")
            if stage_num==0:
                stage_num=None
            race_edition = RaceEdition(race_id=fc, year=year)
            ext_res=race_edition.ext_results(stage_num=stage_num)
            
            if kwargs.get("general_or_stage") is not None and len(race_edition.standings)!=1: #single day race
                df=race_edition.standings[general_or_stage_to_fc[kwargs.get("general_or_stage")]]
            else:
                df=ext_res.results_table
            
        else: #real file
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
        if fc is not None: 
            point_column_name="Points"
            time_column_name="Time"
        else:
            if 'Result' in df.columns:
                point_column_name="Result"
            elif 'Points' in df.columns:
                point_column_name="Points"
            time_column_name="Result"
            
        if kwargs.get('result_points',False):
            if point_column_name in df.columns:
                df["Points"]=df[point_column_name].apply(lambda x: to_float(x)) 
        else:
            if time_column_name in df.columns:
                winner_time=time_converter(df[time_column_name].values[0],0)
                df["Time"]=df[time_column_name].apply(lambda x: time_converter(x, winner_time)) 
                df["Ecart"]=df["Time"].apply(lambda x: calc_ecart(x, winner_time)) 

        if fc is not None:
            for i in df.index:
                try:
                    df.loc[i,"Rank"]=int(df.loc[i,"Pos"])
                except:
                    df.loc[i,"Rank"]=df.loc[i,"Pos"] #DNF, DNS
            
        #search the rider
        if kwargs.get('rider',False):
                
            rider_ids=[]
            for ii in range(len(df.index)):
                name=None
                first_name=None
                last_name=None
                bib=None
                fc_id=None
                
                if 'Name' in df.columns:
                    name=df['Name'].values[ii]
                if 'Rider' in df.columns:
                    name=df['Rider'].values[ii]
                if 'First Name' in df.columns:
                    first_name=df['First Name'].values[ii]
                if 'Last Name' in df.columns:
                    last_name=df['Last Name'].values[ii]
                if 'BIB' in df.columns:
                    bib=df['BIB'].values[ii]
                if 'Rider_ID' in df.columns:
                    fc_id=df['Rider_ID'].values[ii]

                if type(name)!=str: #nan
                    rider_ids.append("QO")
                else:
                    s=Search(name) 
                    id_rider=s.rider(first_name,last_name,fc_id=fc_id)
                    if id_rider in ['Q0','Q1']:
                        if first_name is not None:
                            log+="\n" + str(first_name) + " " +  str(last_name) +" number "
                        else:
                            log+="\n" + str(name) +" number "
                        if bib is not None:
                            log+=str(bib)
                        log+=" not found"
                        if kwargs.get("need_complete",False):
                            all_riders_found=False
                    rider_ids.append(id_rider)
            df["ID Rider"]=rider_ids
        team=kwargs.get("team",False)
        if team or kwargs.get("convert_team_code",False):
            try_with_team_name=False
            
            if "Team Code" not in df.columns:
                print("Team Code not present in import file")

                if "Team" not in df.columns:
                    print("Team not present in import file")
                    team=False
                else:
                    try_with_team_name=True
                    df["Team"]=df["Team"].apply(lambda x: str(x)+" "+str(year) if str(x)!="nan" and str(x)!="NaN" else str(x))
            else:
                 df["Team Code"]=df["Team Code"].apply(lambda x: str(x)+" "+str(year) if str(x)!="nan" and str(x)!="NaN" else str(x))

            if team:
                team_ids=[]
                code_to_id={"nan":"Q0"}
                man_or_woman=kwargs.get('man_or_woman',u'woman') #used only for team
            
                if try_with_team_name:
                    df2=pd.unique(df["Team"].values)
                else:
                    df2=pd.unique(df["Team Code"].values)
               
                for ii in range(len(df2)):
                    team_str=df2[ii]
                    if team_str not in ["nan","NaN"]:
                        s=Search(team_str)
                        if try_with_team_name:
                            id_team=s.team_by_name(man_or_woman=man_or_woman)
                        else:
                            id_team=s.team_by_code(man_or_woman=man_or_woman)
                        if id_team in ['Q0','Q1']:
                            log+="\n team: " + str(team_str) + " not found"
                            if kwargs.get("need_complete",False):
                                all_teams_found=False
                        code_to_id[team_str]=id_team
                    
                for ii in range(len(df.index)):
                    if try_with_team_name:
                        id_team=code_to_id[df["Team"].values[ii]]
                    else:
                        id_team=code_to_id[df["Team Code"].values[ii]]
                    team_ids.append(id_team)   #in the end has the same length as     rider_ids         
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
       
        #check if all riders are already present
        if "ID Rider" not in df.columns:             
            raise ValueError("ID Rider not present in dataframe")
        
        for ii in range(len(df.index)):
            if df["ID Rider"].values[ii] in ['Q0','Q1']:
                this_rider=Cyclist(name='not found')
            else:
                this_rider=Cyclist(id=df["ID Rider"].values[ii])
                if 'BIB' in df.columns:
                    if not math.isnan(df["BIB"].values[ii]):
                        this_rider.dossard=int(df["BIB"].values[ii])
                if 'Rank' in df.columns:
                    if type(df["Rank"].values[ii])==str:
                        this_rider.rank=str(df["Rank"].values[ii]) 
                    elif (type(df["Rank"].values[ii])==float or 
                       type(df["Rank"].values[ii])==int) and not math.isnan(df["Rank"].values[ii]):
                        this_rider.rank=str(int(df["Rank"].values[ii]))
                        
            list_of_cyclists.append(this_rider)

            if "ID Team" in df.columns:
                if df["ID Team"].values[ii] in ['Q0','Q1']:
                    this_team=Team(name='not found')  #just as filler
                else:
                    this_team=Team(id=df["ID Team"].values[ii])
                    if 'Team Code' in df.columns:
                        this_team.codeUCI=df['Team Code'].values[ii]
                list_of_teams.append(this_team)   

        return list_of_cyclists, list_of_teams
    except Exception as msg:
        _, _, exc_tb = sys.exc_info()
        print("line " + str(exc_tb.tb_lineno))
        print(msg)
        print("cyclists_table_reader read failure")
        return None, None
    
