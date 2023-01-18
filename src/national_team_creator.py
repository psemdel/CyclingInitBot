# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: maxime delzenne
"""
import pywikibot
from .base import CyclingInitBot, PyItem, create_item
from .func import man_or_women_to_is_women
import sys

class NationalTeamCreator(CyclingInitBot):
    def __init__(self,man_or_woman,start_year,end_year,**kwargs):
        super().__init__(**kwargs)
        
        self.man_or_woman=man_or_woman
        self.start_year=start_year
        self.end_year=end_year
        self.country=kwargs.get('country')
        
        if man_or_woman == 'man':
            self.key = "team man"
        elif man_or_woman == 'woman':
            self.key = "team woman"
        elif man_or_woman == 'womanU':
            self.key = "team woman U23"
        elif man_or_woman == 'manU':
            self.key = "team man U23"  
        elif man_or_woman == 'womanJ':
            self.key = "team woman U19"
        elif man_or_woman == 'manJ':
            self.key = "team man U19"
        else:
            self.key = "team woman"
        self.is_women=man_or_women_to_is_women(man_or_woman)
        
    def main(self):
        try:
            if self.country:
                if self.country not in self.nation_table:
                    self.log.concat("master of the team not found, contact the Webmaster")
                    return 10, self.log, "Q1"
                
                id_present =self.sub_function(self.country,self.nation_table[self.country])
            else:
                for countryCIO, e in self.nation_table.items():
                    if e["group"]==1:
                        id_present=self.sub_function(countryCIO, e)
                    
            return 0, self.log, id_present                   
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            self.log.concat("General Error in national team creator")
            return 10, self.log, "Q1"
    
    def national_team_label(self,year):
        if self.man_or_woman == u'man':
            adj = u''
            adjen = u'men'
            adjes = u''
        else:
            adj = u' féminine '
            adjen = u'women'
            adjes = u'femenino'
            
        if "genre es" in self.this_nation:
            genre_es=self.this_nation["genre es"]
        else:
            genre_es=""
        
        return {'fr': "équipe" + " " + self.this_nation["genre"] + \
                 self.this_nation["name fr"] + adj + "de cyclisme sur route " +str(year),
                 'en': self.this_nation["adj en"] + " " +adjen + \
                 u"'s national road cycling team " +  str(year),
                 'es': u"Equipo nacional " + adjes + " de " + genre_es +\
                     self.this_nation["name es"] + " de ciclismo en ruta " + str(year)
                 }
    
    def sub_function(self,countryCIO,e):
        try:
            for year in range(self.start_year, self.end_year+1):
                self.this_nation=e
                mylabel = self.national_team_label(year)
                pyItem=create_item(mylabel)
                
                self.log.concat("national team "+ countryCIO + " created")
                self.log.concat("team id: " + pyItem.id)
               
                if pyItem.get_description('fr') == '':
                    description={'fr':"saison " + str(year) + " de l'équipe " + e["genre"] +\
                                 e["name fr"] + " de cyclisme sur route"
                                 }
                    pyItem.item.editDescriptions(description,
                                          summary='Setting/updating descriptions.')
        
                if pyItem.get_alias('fr') == '':
                    alias={}
                    for lang in self.all_langs:
                        alias[lang]=[countryCIO+ " " + str(year)]
                    pyItem.item.editAliases(aliases=alias,summary=u'Setting Aliases')    
                
                pyItem.add_value("P31", "Q53534649", u'Nature')
                pyItem.add_value("P2094", "Q23726798", u'Category')
                pyItem.add_value("P1998", countryCIO, u'CIO code',noId=True)
                pyItem.add_value("P641","Q3609", u'cyclisme sur route')
                pyItem.add_value("P17", e["country"], u'country')
                if self.key in e:
                    pyItem.add_value("P5138", e[self.key], u'part of')
    
                start_date = pywikibot.WbTime(
                    site=self.site,
                    year=year,
                    month=1,
                    day=1,
                    precision='day')
                end_date = pywikibot.WbTime(
                    site=self.site,
                    year=year,
                    month=12,
                    day=31,
                    precision='day')
                
                pyItem.add_value("P580",start_date,'Adding starting date',date=True)
                pyItem.add_value("P582",end_date,'Adding ending date',date=True)
                
                official_name = pywikibot.WbMonolingualText(text=e["name fr"], language='fr')
                pyItem.add_value('P1448',official_name,'Adding official name',noId=True)
                
                if self.is_women:
                    pyItem.add_values('P2094',"Q1451845","women cycling",False)
                
                if self.key in e:
                    pyItem.link_year(year,id_master=e[self.key])
                    pyItem_master=PyItem(id=e[self.key])
                    pyItem_master.add_values("P527",pyItem.id,'new season',False)
    
                return pyItem.id        
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)