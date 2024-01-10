# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:28:39 2018

@author: maxime delzenne
"""
import pywikibot
from .base import CyclingInitBot, PyItem, create_item
from .func import man_or_women_to_is_women
import sys
import traceback

class NationalTeamCreator(CyclingInitBot):
    def __init__(
            self,
            man_or_woman: str,
            start_year: int,
            end_year: int,
            country:str=None,
            **kwargs):
        '''
        Create the national teams for all country for one year

        Parameters
        ----------
        man_or_woman : str
            age category and gender of the races to be created
        start_year : int
        end_year : int
        country : str, optional
            UCI code of a country, if false then all countries will be created
        '''
        super().__init__(**kwargs)
        for k in ["man_or_woman","start_year","end_year","country"]:
            setattr(self,k,locals()[k])
        
        d={
            'man':"team man",
            'woman':"team woman",
            'womanU':"team woman U23",
            'manU':"team man U23",
            'womanJ':"team woman U19",
            'manJ':"team man U19"
            }
        self.key = d[man_or_woman]
        self.is_women=man_or_women_to_is_women(man_or_woman)
        
    def main(self):
        '''
        Main function of this script
        '''
        try:
            if self.country is not None:
                if self.country not in self.nation_table:
                    self.log.concat("master of the team not found, contact the Webmaster")
                    return 10, self.log, "Q1"
                
                id_present =self.create_team(self.country,self.nation_table[self.country])
            else:
                for country, e in self.nation_table.items():
                    if e["group"]==1:
                        id_present=self.create_team(country, e)
                    
            return 0, self.log, id_present                   
        except Exception as msg:
            print(traceback.format_exc())
            self.log.concat("General Error in national team creator")
            self.log.concat(traceback.format_exc())
            return 10, self.log, "Q1"
    
    def national_team_label(self,year:int):
        '''
        Create the label of the team
        '''
        if self.man_or_woman == u'man':
            adj = u''
            adjen = u'men'
            adjes = u''
        else:
            adj = u' féminine'
            adjen = u'women'
            adjes = u'femenino'
            
        if "genre es" in self.this_nation:
            genre_es=self.this_nation["genre es"]
        else:
            genre_es=""
        
        return {'fr': "équipe" + " " + self.this_nation["genre"] + \
                 self.this_nation["name fr"] + adj + " de cyclisme sur route " +str(year),
                 'en': self.this_nation["adj en"] + " " +adjen + \
                 u"'s national road cycling team " +  str(year),
                 'es': u"Equipo nacional " + adjes + " de " + genre_es +\
                     self.this_nation["name es"] + " de ciclismo en ruta " + str(year)
                 }
    
    def create_team(self,country: str,e: dict):
        '''
        Create one national team
        
        Parameters
        ----------
        e : dict
            Dictionnary containing the information about the country or the continent
        country : str, optional
            UCI code of a country, if false then all countries will be created
        '''
        try:
            for year in range(self.start_year, self.end_year+1):
                self.this_nation=e
                mylabel = self.national_team_label(year)
                pyItem=create_item(mylabel)
                
                self.log.concat("national team "+ country + " created")
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
                        alias[lang]=[country+ " " + str(year)]
                    pyItem.item.editAliases(aliases=alias,summary=u'Setting Aliases')    
                
                pyItem.add_value("P31", "Q53534649", u'Nature')
                pyItem.add_value("P2094", "Q23726798", u'Category')
                pyItem.add_value("P1998", country, u'CIO code',noId=True)
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
            print(traceback.format_exc())
            self.log.concat("General Error in rider_fast_init")
            self.log.concat(traceback.format_exc())
