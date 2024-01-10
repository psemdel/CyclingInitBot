# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:30:20 2018

@author: maxime delzenne
"""
import pywikibot
from .base import CyclingInitBot, PyItem, create_item, Search
from .data import cc_table
from .func import man_or_women_to_is_women

class NationalChampionshipCreator(CyclingInitBot):
    def __init__(
            self,
            man_or_woman:str,
            start_year:int,
            end_year:int,
            CC:bool=False,
            clm: bool=True, 
            road: bool=True,
            country:str=None,
            **kwargs
            ):
        '''
        Create national championships and the corresponding races
        
        Parameters
        ----------
        man_or_woman : str
            age category and gender of the races to be created
        start_year : int
            first year to be created
        end_year : int
            last year to be created
        CC : bool
            Shall continental championships be created
        clm: bool
            Shall the ITT be created
        country : str, optional
            UCI code of a country, if false then all countries will be created
        **kwargs 
            To put test for instance
        '''
        super().__init__(**kwargs)
        
        for k in ["CC","country","start_year","end_year","clm","road"]:
            setattr(self,k,locals()[k])

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
                True:{"man":"Road race man",
                      "woman":"Road race woman"
                      },
                
                False:{"man":"Clm man",
                       "woman":"Clm woman",
                      }
                }
        else:
            self.race_dic={
                True:{"man":"Road race man",
                      "woman":"Road race woman",
                      "manU":"Road race man U23",
                      "womanU":"Road race woman U23",
                      "manJ":"Road race man U19",
                      "womanJ":"Road race woman U19",
                      },
                
                False:{"man":"Clm man",
                       "woman":"Clm woman",
                       "manU":"Clm man U23",
                       "womanU":"Clm woman U23",
                       "manJ":"Clm man U19",
                       "womanJ":"Clm woman U19",
                      }
                 }
 
    def main(self):
        '''
        Main function of this script
        '''
        try:
            if self.CC:
                for _, e in cc_table.load().items():
                    self.sub_function(e)
                #load CC table
            elif self.country is not None:
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
            self.log.concat("General Error in national team creator " + msg)
            return 10, self.log
        
    def national_championship_basic(
            self,
            country_id:str,
            year:int
            ):
        '''
        Fill some information for the main championship

        Parameters
        ----------
        country_id : str
            id in wikidata corresponding to the country
        year : int
        '''
        try:
            self.pyNatChamp.add_value("P31", self.id_NatChampMaster, u'Nature')
            self.pyNatChamp.add_value("P641", "Q3609", u'cyclisme sur route')
            
            pyItem_master=PyItem(id=self.id_NatChampMaster)
            pyItem_master.add_values("P527",self.pyNatChamp.id,'add new year',False)
    
            if not self.CC:        
                s=Search('Championnats nationaux de cyclisme sur route en ' +  str(year))
                id_allchamp = s.simple()
                if id_allchamp in ['Q0',"Q1"]:  
                    raise ValueError(u'Championnats nationaux de cyclisme sur route en ' + str(year)+' not found')
                else:
                    self.pyNatChamp.add_value("P361", id_allchamp, u'part of')
                    pyItem_allchamp=PyItem(id=id_allchamp)
                    pyItem_allchamp.add_values("P527",self.pyNatChamp.id,'add champ',False)
                self.pyNatChamp.add_value("P17", country_id, u'country')
                
            self.pyNatChamp.link_year(year,id_master=self.id_NatChampMaster)            
        except Exception as e:
            self.log.concat(e)
  
    def race_label(
            self, 
            e: dict, 
            year:int,
            man_or_woman: str,
            enligne:bool
            ):
        '''
        Create the label for the RR or ITT

        Parameters
        ----------
        e : dict
            Dictionnary containing the information about the country or the continent
        year : int
        man_or_woman : str
            age category and gender of the races to be created
        enligne : bool
            Is it about the RR (True) or the ITT (False)

        Returns
        -------
        dict
            label of the race
        '''
        dic_adj={
            True: {"man":'masculine',
                              'woman':'féminine',
                              'manU':'masculine espoirs',
                              'womanU':'féminine espoirs',
                              'manJ':'masculine juniors',
                              'womanJ':'féminine juniors'    
                              },
            False:  {"man":'masculin',
                              'woman':'féminin',
                              'manU':'masculin espoirs',
                              'womanU':'féminin espoirs',
                              'manJ':'masculin juniors',
                              'womanJ':'féminin juniors'    
                              }
            }

        if enligne:
            firstword=u"Course en ligne "
        else:
            firstword= u"Contre-la-montre "
       
        return {'fr': firstword + dic_adj[enligne][man_or_woman] + " aux championnats " + e["genre"]+\
               e["name fr"] + " de cyclisme sur route " + str(year)
               }

    def race_basic(
            self,
            pyItem: PyItem,
            id_race: str,
            year: int,
            man_or_woman: str,
            enligne: bool,
            country_id: str
            ): 
        '''
        Fill information for a race

        Parameters
        ----------
        pyItem : PyItem
            DESCRIPTION.
        id_race : str
            Here it for instance course en ligne...without year
        year : int
        man_or_woman : str
            age category and gender of the races to be created
        enligne : bool
            Is it about the RR (True) or the ITT (False)
        country_id : str
            id in wikidata corresponding to the country
        '''
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
            precision='year')
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
        
        dic={
            True:{'woman': "Course en ligne féminine",
                  'man': "Course en ligne masculine"
                 },
            False:{'woman': "Contre-la-montre féminin",
                  'man': "Contre-la-montre masculin"
                 } 
            }

        if not self.CC:
            pyItem.add_value("P17", country_id, u'country')
            
            s=Search(dic[enligne][man_or_woman]+" aux championnats nationaux de cyclisme sur route " + str(year))
            id_allchamp = s.simple()
            pyItem_allchamp=PyItem(id=id_allchamp)
            
            if (id_allchamp == u'Q0')or(id_allchamp == u'Q1'):
                self.log.concat(dic[enligne][man_or_woman]+" aux championnats nationaux de cyclisme sur route " + str(year)+' not found')
                raise ValueError(dic[enligne][man_or_woman]+' not found')
            else:
                pyItem_allchamp=PyItem(id=id_allchamp)
                pyItem_allchamp.add_values("P527",pyItem.id,'add champ',False)
            
    def sub_function(
            self, 
            e: dict
            ):
        '''
        Parameters
        ----------
        e : dict
            Dictionnary containing the information about the country or the continent
        '''
        try:
            if self.CC:
                t=None
            else:
                t=e["country"]
            
            for man_or_woman in self.gender_list:    
                self.is_women=man_or_women_to_is_women(man_or_woman)
                self.log.concat( "championships creation for gender: " + man_or_woman)
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
                        self.national_championship_basic(t,year)
                    
                    l=[]
                    if self.road:
                        l.append(True)
                    if self.clm:
                        l.append(False)

                    for enligne in l:
                        key= self.race_dic[enligne][man_or_woman]

                        if key in e: #if this race is known in the "DB"
                            mylabel_race =self.race_label(e, year,man_or_woman,enligne)
                            pyItemRace=create_item(mylabel_race)
                            
                            if pyItemRace.id!='Q1':
                                self.race_basic(
                                     pyItemRace,
                                     e[key],
                                     year,
                                     man_or_woman,
                                     enligne,
                                     t)
        except Exception as e:
            import sys
            _, e_, exc_tb = sys.exc_info()
            print(e)
            print("line " + str(exc_tb.tb_lineno))
            self.log.concat(e)
