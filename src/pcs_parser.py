#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:46:36 2023

@author: maxime
"""
import pandas as pd
import bs4
import requests

def get_pcs(link:str):
    rq = requests.get(link)  
    soup = bs4.BeautifulSoup(rq.text, 'html.parser')
    table=soup.find('table', {'class': 'basic'})
    
    out_df = pd.read_html(str(table), decimal=',')[0]
    trs = table.find_all('tr')[1:]
    headers = [th.text for th in table.thead.find_all('th')]
    soup_df = pd.DataFrame([tr.find_all('td') for tr in trs], columns=headers)
    
    for col, series in soup_df.items():
        if col =="Rider":
            out_df["Inv name"]=out_df["Rider"].str.lower()
            for ii in range(len(series)):
                t=[s for s in series[ii].find_all("a")]
                
                last_name=None
                first_name=None
                
                for l in t:
                    name=False
                    for k in l:
                        if k.find("uppercase")!=-1:
                            last_name=k.text
                            name=True
                        elif name:
                            first_name=k
                
                if last_name is not None and first_name is not None: 
                    out_df["Rider"].values[ii]=first_name+" "+last_name
    out_df.rename(columns={'#':'Rank'},inplace=True)  
    return out_df



