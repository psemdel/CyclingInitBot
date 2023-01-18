# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:30:20 2018

@author: maxime delzenne
"""
import pywikibot
from .base import CyclingInitBot, PyItem, create_item, Search
from .data import cc_table
from .func import man_or_women_to_is_women

import sys

class NationalChampionshipCreator(CyclingInitBot):
    def __init__(self,man_or_woman,option, start_year,end_year,CC,**kwargs):
        super().__init__(**kwargs)
        
        self.CC=CC
        self.country=kwargs.get('country',False)
        self.start_year=start_year
        self.end_year=end_year
        
        if option == 'clmoff':
            self.clm = False
        else:
            self.clm = True

        if man_or_woman in ["woman","man","womanU","manU","womanJ","manJ"]:
            self.gender_list=[man_or_woman]
        elif man_or_woman == u"both":   
            self.gender_list=["woman","man"]    
        elif man_or_woman == u"all": 
            self.gender_list=["woman","man","womanU","manU","womanJ","manJ"]    
        else:
            self.gender_list=["woman"]   

        if CC:
            self.race_dic={
            "man":{"road race":"Road race man",
                   "clm":"Clm man"                     
                   },
            "woman":{"road race":"Road race woman",
                   "clm":"Clm woman"                       
                   }
            }
        else:
            self.race_dic={
            "man":{"road race":"Road race man",
                   "clm":"Clm man"                     
                   },
            "woman":{"road race":"Road race woman",
                   "clm":"Clm woman"                       
                   },
            "manU":{"road race":"Road race man U23",
                   "clm":"Clm man U23"                     
                   },
            "womanU":{"road race":"Road race woman U23",
                   "clm":"Clm woman U23"                       
                   },               
            "manJ":{"road race":"Road race man U19",
                   "clm":"Clm man U19"                     
                   },
            "womanJ":{"road race":"Road race woman U19",
                   "clm":"Clm woman U19"                       
                   },
            }
 
    def main(self):
        try:
            if self.CC:
                for _, e in cc_table.load().items():
                    self.sub_function(e)
                #load CC table
            elif self.country:
                if self.country not in self.nation_table:
                    self.log.concat("master of the team not found, contact the Webmaster")
                    return 10, self.log
            
                self.sub_function(self.nation_table[self.country])
            else:
                for _, e in self.nation_table.items():
                    if e["group"] in [1,2]:
                        self.sub_function(e)
                    
            return 0, self.log
        except Exception as msg:
            print(msg)
            self.log.concat("General Error in national team creator")
            return 10, self.log
        except:
            self.log.concat("General Error in national team creator")
            return 10, self.log  
        
    def national_championship_basic(self,country_id,year):
        self.pyNatChamp.add_value("P31", self.id_NatChampMaster, u'Nature')
        self.pyNatChamp.add_value("P641", "Q3609", u'cyclisme sur route')
        
        pyItem_master=PyItem(id=self.id_NatChampMaster)
        pyItem_master.add_value("P527",self.pyNatChamp.id,'add new year')

        if not self.CC:        
            s=Search('Championnats nationaux de cyclisme sur route en ' +  str(year))
            id_allchamp = s.simple()
            if (id_allchamp == u'Q0') or (id_allchamp == u'Q1'):  
                self.log.concat(u'Championnats nationaux de cyclisme sur route en ' + str(year)+' not found')
                print(u'Championnats nationaux de cyclisme sur route en ' + str(year)+' not found')
                return 1
            else:
                self.pyNatChamp.add_value("P361", id_allchamp, u'part of')
                pyItem_allchamp=PyItem(id=id_allchamp)
                pyItem_allchamp.add_values("P527",self.pyNatChamp.id,'add champ',False)
            self.pyNatChamp.add_value("P17", country_id, u'country')
            
        self.pyNatChamp.link_year(year,id_master=self.id_NatChampMaster)            
        return 0
    
    def national_championship_race_label(self, e, year,m_or_w,enligne):
       dic_adj_enligne = {"man":'masculine',
                          'woman':'féminine',
                          'manU':'masculine espoirs',
                          'womanU':'féminine espoirs',
                          'manJ':'masculine juniors',
                          'womanJ':'féminine juniors'    
                          }
       dic_adj_clm=      {"man":'masculin',
                          'woman':'féminin',
                          'manU':'masculin espoirs',
                          'womanU':'féminin espoirs',
                          'manJ':'masculin juniors',
                          'womanJ':'féminin juniors'    
                          }
       
       if enligne:
           firstword=u"Course en ligne "
           adj=dic_adj_enligne[m_or_w]
       else:
           firstword= u"Contre-la-montre "
           adj=dic_adj_clm[m_or_w]
           
       return {'fr': firstword + adj + " aux championnats " + e["genre"]+\
               e["name fr"] + " de cyclisme sur route " + str(year)
              }

    def national_championship_race_basic(self,pyItem,id_race,year,m_or_w,enligne,country_id): #id_race is for instance course en ligne...without year
            pyItem.add_value("P31", id_race, 'Nature')
            pyItem.add_value("P641", "Q3609", 'cyclisme sur route')
            self.pyNatChamp.add_values("P527",pyItem.id,'adding to master',False)
            pyItem_race=PyItem(id=id_race)
            pyItem_race.add_values("P527",pyItem.id,'adding to master',False)
            
            pyItem.add_value("P361", self.pyNatChamp.id, u'part of')
            
            pyItemRace=PyItem(id=id_race)
            pyItemRace.add_value("P527",pyItem.id,'add new year')

            date = pywikibot.WbTime(
                site=self.site,
                year=year,
                month=1,
                day=1,
                precision='day')
            pyItem.add_value('P585',date,'Adding date',date=True)
            pyItem.link_year(year,id_master=id_race)   
            
            if self.CC:
                if self.pyNatChamp.id in ["Q934877","Q2630733"]:
                    item_to_add = 'Q23015458'  # CDM
                else:
                    item_to_add = 'Q22231118'  # CC
            else:
                item_to_add = 'Q22231119' # CN

            pyItem.add_value("P279",item_to_add,'Adding CN')
            
            if self.is_women:
                pyItem.add_value('P2094',"Q1451845","women cycling")
            
            if enligne:
                dic ={'woman': "Course en ligne féminine",
                      'man': "Course en ligne masculine"
                             }     
            else:
                dic ={'woman': "Contre-la-montre féminin",
                      'man': "Contre-la-montre masculin"
                     }  

            if not self.CC:
                pyItem.add_value("P17", country_id, u'country')
                
                s=Search(dic[m_or_w]+" aux championnats nationaux de cyclisme sur route " + str(year))
                id_allchamp = s.simple()
                pyItem_allchamp=PyItem(id=id_allchamp)
                
                if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):
                    self.log.concat(dic[m_or_w]+" aux championnats nationaux de cyclisme sur route " + str(year)+' not found')
                    print(dic[m_or_w]+' not found')
                    return 1
                else:
                    pyItem_allchamp=PyItem(id=id_allchamp)
                    pyItem_allchamp.add_values("P527",pyItem.id,'add champ',False)
            return 0
            
    def sub_function(self, e):
        try:
            if self.CC:
                t=None
            else:
                t=e["country"]
            
            for m_or_w in self.gender_list:    
                self.is_women=man_or_women_to_is_women(m_or_w)
                self.log.concat( "championships creation for gender: " + m_or_w)
                self.id_NatChampMaster=e["National championship master"]
                
                for year in range(self.start_year, self.end_year+1):
                    self.log.concat( "championships creation for year: " + str(year))
                    mylabel={"fr": "Championnats " + e["genre"] + e["name fr"] + \
                            " de cyclisme sur route " + str(year)
                    }
                    if not self.CC: #no english for CC
                        mylabel[u'en'] = str(year) + " " + e["adj en"] + " National Road Race Championships"
                    self.pyNatChamp=create_item(mylabel)
                    
                    ##create championship
                    if self.pyNatChamp.id!='Q1': 
                        r=self.national_championship_basic(t,year)
                        if r==1:
                            self.log.concat(u'Code interrupted')
                            return 10, self.log
                    
                    for k in ["road race","clm"]:
                        key= self.race_dic[m_or_w][k]
                        if key in e:
                            mylabel_race =self.national_championship_race_label(e, year,m_or_w,k=="road race")
                            pyItemRace=create_item(mylabel_race)
                            
                            if pyItemRace.id!='Q1':
                                r=self.national_championship_race_basic(
                                     pyItemRace,
                                     e[key],
                                     year,
                                     m_or_w,
                                     k=="road race",
                                     t)
                                if r==1:
                                    self.log.concat(u'Code interrupted')
                                    return 10, self.log
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            raise RuntimeError("error sub_function")
