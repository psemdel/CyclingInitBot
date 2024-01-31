"""
Created on Thu Jan  4 15:28:39 2018

@author: psemdel
"""
import pywikibot
import traceback
from .base import CyclingInitBot, PyItem, create_item

class TeamCreator(CyclingInitBot):
    def __init__(
            self,
            name: str,
            id_master: str,
            country: str,
            UCIcode: str,
            year: int,
            category_id:str=None,
            **kwargs):
        '''
        Createa season for a team

        Parameters
        ----------
        name : str
            Name of the race in the current year
        id_master : str
            wikidata id of the race, idenpendent from the year
        country : str
            code of the country, for instance "FRA"
        UCIcode : str
            UCI code of the team in the current year
        year : int
        category_id : str, optional
            Category of the team in the current year
        '''
        super().__init__(**kwargs)
        for k in ["name","id_master","country","UCIcode","year","category_id"]:
            setattr(self,k,locals()[k])

        self.label={}
        self.alias={}
        
        for lang in self.all_langs:
            self.label[lang] = self.name + " " + str(self.year)
            if self.UCIcode and self.UCIcode!="":
                self.alias[lang]=[self.UCIcode + " "   + str(self.year)]
                
        self.is_women=False
        if self.category_id in ["Q2466826","Q26849121","Q80425135","Q119942457"]:
            self.is_women=True
    
    def main(self):
        '''
        Main function of this script
        '''
        try:
            pyItem=create_item(self.label, is_women=self.is_women)
            if pyItem is not None:
                self.log.concat("team id: "+ pyItem.id)
                description={'fr':'Saison ' + str(self.year) +" de l'équipe cycliste " + self.name}
                pyItem.item.editDescriptions(description,
                                      summary='Setting/updating descriptions.')
                
                if pyItem.get_alias('fr')=='':
                    pyItem.item.editAliases(aliases=self.alias, summary='Setting Aliases')                
                
                if self.UCIcode and self.UCIcode!="":
                    pyItem.add_value( "P1998", self.UCIcode, 'UCI code',noId=True)
                
                if self.category_id:
                    pyItem.add_values("P2094", self.category_id, 'Category', False)
                pyItem.add_values("P31", "Q53534649", 'Season', False)
                pyItem.add_value("P641", "Q3609", 'cyclisme sur route')
                pyItem.add_value("P17", self.nation_table[self.country]["country"], 'country')
                pyItem.add_value("P5138", self.id_master, 'part of')
                pyItem_master=PyItem(id=self.id_master)
                pyItem_master.add_values("P527",pyItem.id,'new season',False)
                start_date = pywikibot.WbTime(
                    site=self.site,
                    year=self.year,
                    month=1,
                    day=1,
                    precision='day')
                end_date = pywikibot.WbTime(
                    site=self.site,
                    year=self.year,
                    month=12,
                    day=31,
                    precision='day')
                
                pyItem.add_value("P580",start_date,'Adding starting date',date=True)
                pyItem.add_value("P582",end_date,'Adding ending date',date=True)
                
                official_name = pywikibot.WbMonolingualText(text=self.name, language='fr')
                pyItem.add_value('P1448',official_name,'Adding official name',noId=True)
                pyItem.link_year(self.year,id_master=self.id_master)
                
                if self.category_id and self.category_id in ['Q80425135','Q2466826','Q26849121']:
                    pyItem.add_values('P2094',"Q1451845","women cycling",False)

            return 0, self.log, pyItem.id
        except:
            self.log.concat("General Error in team creator")
            self.log.concat(traceback.format_exc())
            return 10, self.log, "Q1"

    

    


