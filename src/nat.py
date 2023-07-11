#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:37:24 2023

@author: maxime
"""

import pywikibot
from .base import CyclingInitBot, PyItem, create_item, Search
from .data import cc_table
from .func import man_or_women_to_is_women

import sys

class NationalCreator(CyclingInitBot):
    def main(self):
        for year in range(1897,1989):
            mylabel={
                "fr":"championnats nationaux de cyclisme sur route en "+str(year),
                "en":str(year)+ " national road cycling championships"
                }
            self.pyNatChamp=create_item(mylabel)
            self.pyNatChamp.add_value("P31", "Q2306612", u'Nature')
            self.pyNatChamp.add_value("P641","Q3609","add sport")
            date = pywikibot.WbTime(
                site=self.site,
                year=year,
                precision='year')
            self.pyNatChamp.add_value("P585",date, "adding date",date=True)
            pyItemRace=PyItem(id="Q2306612")
            pyItemRace.add_values("P527",self.pyNatChamp.id,'add new year',False)
            self.pyNatChamp.link_year(year,id_master="Q2306612")   

class NationalCreator2(CyclingInitBot):
    def main(self):
        dic={
            "fr":{
                True: {'woman': "Course en ligne féminine",
                      'man': "Course en ligne masculine"
                             },
                False: {'woman': "Contre-la-montre féminin",
                      'man': "Contre-la-montre masculin"
                     }
                },
            "en":{
                True: {'woman': "women RR",
                      'man': "men RR"
                             }  ,
                False: {'woman': "women ITT",
                      'man': "men ITT"
                             } 
                },
            }
        
        master={
            True:{"woman":"Q106858462",
                  "man":"Q106858458"},
            False:{"woman":"Q106858463",
                   "man":"Q106858459",
                }
            }
        
        for year in range(1989,1992):
            for enligne in [True,False]:
                for m_or_w in ["man","woman"]:
                    mylabel={
                        "fr": dic["fr"][enligne][m_or_w]+" aux championnats nationaux de cyclisme sur route " + str(year),
                        "en": str(year)+ " national road cycling championships - "+dic["en"][enligne][m_or_w]
                            }
            
                    self.pyNatChamp=create_item(mylabel)
                    self.pyNatChamp.add_value("P31", master[enligne][m_or_w], u'Nature')
                    self.pyNatChamp.add_value("P641","Q3609","add sport")
                    date = pywikibot.WbTime(
                        site=self.site,
                        year=year,
                        precision='year')
                    self.pyNatChamp.add_value("P585",date, "adding date",date=True)
                    self.pyNatChamp.add_value("P279","Q22231119", "adding class")
                    
                    pyItemRace=PyItem(id=master[enligne][m_or_w])
                    pyItemRace.add_values("P527",self.pyNatChamp.id,'add new year',False)
                    self.pyNatChamp.link_year(year,id_master=master[enligne][m_or_w])   
