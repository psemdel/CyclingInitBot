# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:38:42 2018

@author: psemdel
"""

import pywikibot
from pywikibot import pagegenerators as pg
from .data import nation_team_table, language_list, race_list, exception 
from .name import Name, CyclistName, concaten
from datetime import datetime


### All classes in the code ###
class CyclingInitBot():
    def __init__(
            self,
            test:bool=False,
            **kwargs):
        '''
        Master-class for the functions in the bot
        '''
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        self.nation_table= nation_team_table.load()
        self.all_langs=language_list.load()
        self.log=Log()
        self.test=test

def create_item(label:dict, is_women:bool=None):   
    '''
    Create a new item in wikidata
    '''
    search=Search(label['fr'])
    present_id=search.simple()
    site = pywikibot.Site("wikidata", "wikidata")
    repo=site.data_repository()
    create=False
    
    if (present_id == u'Q0'):
        create=True
    elif (present_id == u'Q1'):
        print(label['fr'] + ' already present several times')
        return None
    else:
        item = pywikibot.ItemPage(repo, present_id)
        if is_women is None:
            print(label['fr'] + ' already present')
            return PyItem(id=present_id, item=item)
        else:
            w=False
            
            item.get()
            if (u'P2094' in item.claims):
                P2094=item.claims.get(u'P2094')
                for p2094 in P2094:
                    if p2094.getTarget().getID() in ["Q2466826","Q26849121","Q80425135","Q119942457","Q1451845"]:
                        w=True

            if (u'P31' in item.claims):
                P31=item.claims.get(u'P31')
                for p31 in P31:
                    if p31.getTarget().getID() in ["Q2466826","Q26849121","Q80425135"]:#cats
                        w=True            

            if (is_women and not w) or (not is_women and w): #there is an item but for the other team
                create=True
                
    if create:
        print(label['fr'] + ' created')
        new_item = pywikibot.ItemPage(site)
        new_item.editLabels(labels=label, summary="Setting labels")
    # Add description here or in another function
        pyItem=PyItem(id=new_item.getID(), item=new_item)
        return pyItem

class PyItem():
    def __init__(
            self,
            id:str="Q0",
            item=None,
            **kwargs):
        '''
        Kind of overload of item in pywikibot

        Parameters
        ----------
        id : str, optional
            wikidata id
        item : , optional
            item in wikidata
        '''
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        self.item=item
        self.id=id

        if self.item is None and self.id !="Q0":
            self.item=pywikibot.ItemPage(self.repo, self.id)
            self.item.get()
            
            
        
    def get_country(self)-> str:
        '''
        Return the country id of the item
        '''
        if (u'P17' in self.item.claims):
             P17=self.item.claims.get(u'P17')
             return P17[0].getTarget().getID()
        else:
             return None
            
    def add_value(
            self, 
            prop: str, 
            value, 
            comment:str,
            date:bool=False,
            noId:bool=False,
            ):
        '''
        Add value to the item

        Parameters
        ----------
        prop : str
            Propriety where the value should be added
        value : 
            Value to be added, by default an id is expected
        comment : str
            Comment for wikidata history
        date : bool, optional
            If the value is a date
        noId : bool, optional
            If the value is not an id
        '''
        if ((not isinstance(value,int) or (isinstance(value,int) and value!=0) or date)
           and (not isinstance(value,str) or (isinstance(value,str) and value!="Q0"))): #date is somehow not different from 0
            if prop not in self.item.claims:  # already there do nothing
                claim = pywikibot.Claim(self.repo, prop)
                if date or noId:
                    target=value
                else:
                    target = pywikibot.ItemPage(self.repo, value)
                    
                claim.setTarget(target)
                self.item.addClaim(claim, summary=u'Adding ' + comment)  

    def delete_value(
            self, 
            prop: str, 
            vId: str, 
            comment: str
            ):
        '''
        Delete a value from a property

        Parameters
        ----------
        prop : str
            Propriety where the value should be added
        vId : str
            id to be deleted
        comment : str
            Comment for wikidata history
        '''
        if prop in self.item.claims:
            for ii, e in enumerate(self.item.claims.get(prop)):
                if e.getTarget().getID() == vId:  # Already there
                    claim =  self.item.claims[prop][ii]
                    self.item.removeClaims(claim)

    def delete_property(self, prop:str):
        '''
        Delete all values from a property

        Parameters
        ----------
        prop : str
            Propriety where the value should be added
        '''
        if prop in self.item.claims :
            self.item.removeClaims(self.item.claims[prop])

# Same as add value but for comprend
    def add_values(
            self,
            prop: str,
            value,
            comment: str,
            overpass: bool,
            date:bool=False,
            noId:bool=False,
            ):
        '''
        Add value to the item in a property that has already other items

        Parameters
        ----------
        prop : str
            Propriety where the value should be added
        value : 
            Value to be added, by default an id is expected
        comment : str
            Comment for wikidata history
        overpass : bool
            If true, it will add the value also if it already present. Useful for sorting algorithms.
        date : bool, optional
            If the value is a date
        noId : bool, optional
            If the value is not an id
        '''
        # check if the value is not already 
        Addc = True
        target = None
        claim= None
        
        if not overpass:  # To add a value and then delete it for sorting purpose
            if prop in self.item.claims:  # already there do nothing
                for e in self.item.claims.get(prop) :
                    if date or noId:
                        if e.getTarget() == value:  # Already there
                            claim=e
                            Addc = False
                            print('Item already present')
                            break   
                    elif e.getTarget() is not None and e.getTarget().getID() == value:  # Already there
                            claim=e
                            Addc = False
                            print('Item already present')
                            break
        # add the value
        if Addc:
            claim = pywikibot.Claim(self.repo, prop)
            if date or noId:
                target=value
            elif value!="Q0":
                target = pywikibot.ItemPage(self.repo, value)
            if target is not None:
                claim.setTarget(target)
                self.item.addClaim(claim, summary=u'Adding ' + comment)
        return Addc, claim

    def add_qualifier(
            self,
            claim,
            prop:str,
            target_q,
            update:bool=False):
        '''
        Add a qualifier to a claim

        Parameters
        ----------
        claim : TYPE
            Claim where the qualifier needs to be added
        prop : str
            DESCRIPTION.
        target_q : TYPE
            qualifier to be added
        '''
        Addc = True
        if target_q is not None:
            for qual in claim.qualifiers.get(prop, []): #the get(prop, []) avoids a crash if the qualifier is not present
                if qual.target==target_q:
                    print("qualificatif found")
                    Addc = False
                
            if Addc:
                if update:
                    q=pywikibot.page.Claim(self.site, prop, is_qualifier=True)
                    q.setTarget(qual.target)
                    claim.removeQualifier(q)
                q=pywikibot.page.Claim(self.site, prop, is_qualifier=True)
                q.setTarget(target_q)
                claim.addQualifier(q)
    
    def link_year(
            self, 
            year:int,
            test:bool=False,
            id_master:str=None,
            ):
        '''
        Link an item to the next and previous editions

        Parameters
        ----------
        year : int
        test : bool, optional
            Are we testing the function?
        id_master : str, optional
            Id of the parent of the item
        '''
        year_previous=int(year)-1
        year_next=int(year)+1
        id_previous=None
        id_next=None

        if id_master is None:
            if (u'P5138' in self.item.claims):
                id_master= self.item.claims.get(u'P5138')[0].getTarget().getID()
            elif (u'P361' in self.item.claims):
                id_master= self.item.claims.get(u'P361')[0].getTarget().getID()
            else:
                return #no way to finish
        if id_master:
            id_previous, pyItem_previous=year_child(year_previous, id_master)
            id_next, pyItem_next=year_child(year_next, id_master)
        
            #link the whole
            if test:
                return id_master, id_previous, id_next
            else:
                if id_previous:
                    self.add_value("P155", id_previous, u'link previous')
                    pyItem_previous.add_value("P156", self.id, u'link next')
                if id_next:
                    self.add_value("P156", id_next, u'link next')
                    pyItem_next.add_value("P155", self.id, u'link previous')
        else:
            raise ValueError("id_master not defined in link_year")

    def get_label(self,language:str)-> str:
        '''
        Return a label of an item
        '''
        if language in self.item.labels:
            return self.item.labels[language]
        elif 'en'  in self.item.labels:
            return self.item.labels['en']
        else:
            for lang in self.item.labels:
                   return  self.item.labels[lang]
            return ''
     
    def get_description(self, language:str)-> str:
        '''
        Return a description of an item
        '''
        if language in self.item.descriptions:
            return self.item.descriptions[language]
        else:
            return ''

    def get_alias(self, language:str)-> str:
        '''
        Return the alias of an item
        '''
        if language in self.item.aliases:
            return self.item.aliases[language]
        else:
            return '' 

class Cyclist(PyItem):
    def __init__(
            self,
            name:str=None,
            nosortkey:bool=False,
            **kwargs):
        '''
        Class to handle cyclist

        Parameters
        ----------
        name : str, optional
            Name of the rider
        nosortkey : bool, optional
            Look for the last name in order to define it as sortkey
        '''

        super().__init__(**kwargs)
        
        if name is None and self.item is not None:
            name=self.get_label('fr')
        
        self.nameObj=CyclistName(name)
        self.name =  self.nameObj.name
        self.name_cor =  self.nameObj.name_cor
        
        self.dossard = 0
        self.team=None
        self.sortkey =None
        if nosortkey==False:
            self.find_sortkey()
            
        self.nationality=''
        self.rank=0
        self.national_team=False
    
    def find_start_sortkey(self,start_words:str,names_cor_table:list):
        '''
        Look for the start of last name using Van or De as indicator
        '''
        for ii in range(1,len(names_cor_table)):
           if names_cor_table[ii] in start_words:
               self.sortkey=concaten(names_cor_table,ii)
    
    def find_sortkey(self):
        '''
        Look for the last name
        '''
        names_cor_table = self.nameObj.name_cor.split(" ")
        family_name_start=[u'van',u'de']
        
        if len(names_cor_table)==2:
            self.sortkey=names_cor_table[1]
        elif len(names_cor_table)==1:
            self.sortkey=names_cor_table[0]
        else:
            sortkey=self.find_start_sortkey(family_name_start,names_cor_table) 
            if sortkey is None: 
                 if False:# bot_or_site():
                     ii = input('Index of the family name : ')
                     self.sortkey=concaten(names_cor_table ,int(ii))       
                 else: #site
                     self.sortkey=concaten(names_cor_table ,1) #arbitrary
                     
    def get_present_team(self, time_of_race: pywikibot.WbTime) -> str:
        '''
        Search for the present team of the rider
        '''
        result = 'Q1'
        tt=time_of_race.toTimestamp()
        
        if (u'P54' in self.item.claims):
            allteams = self.item.claims.get(u'P54')
            for this_team in allteams:
                bt=None
                et=None
                if ('P580' in this_team.qualifiers):
                    begin_time = this_team.qualifiers['P580'][0].getTarget()
                    bt=begin_time.toTimestamp()
                if ('P582' in this_team.qualifiers):
                    end_time = this_team.qualifiers['P582'][0].getTarget()
                    if end_time.month == 0:
                        end_time.month = 12
                        end_time.day = 31
                    et=end_time.toTimestamp()
                
                if (bt is None or bt<=tt) and (et is None or et>=tt):
                    result = this_team.getTarget().getID()
                    break
        return result

    def get_nationality(self, time_of_race: pywikibot.WbTime) -> str:
        '''
        return ID of country from nationality
        '''
        try:
            result="Q0"

            for prop in ['P1532' ,'P27']:
                if result=="Q0":
                    if (prop in self.item.claims):
                        nationalities=self.item.claims.get(prop)
                        if len(nationalities)==1:
                           result=nationalities[0].getTarget().getID()
                        else:
                            for nationality in nationalities:
                                if ('P580' in nationality.qualifiers):
                                    begin_time = nationality.qualifiers['P580'][0].getTarget()
                                else:
                                    begin_time = pywikibot.WbTime(
                                    site=self.site, year=1000, month=1, day=1, precision='day')   
                                if ('P582' in nationality.qualifiers):
                                    end_time = nationality.qualifiers['P582'][0].getTarget()
                                    if end_time.month == 0:
                                        end_time.month = 12
                                        end_time.day = 31
                                else:
                                    end_time = pywikibot.WbTime(
                                    site=self.site, year=2100, month=1, day=1, precision='day')
                                
                                bt=begin_time.toTimestamp()
                                tt=time_of_race.toTimestamp()
                                et=end_time.toTimestamp()
                                
                                if bt<=tt and et>=tt:
                                    result = nationality.getTarget().getID()
                                    break

            if  result=="Q15180": #USSR
                print("USSR rider, id: " + str(self.id))
            if result=="Q55": #NED   
                result="Q29999"
            
            return result
        except Exception as msg:
                print(msg)   
         
class Race(PyItem):
    def __init__(
            self,
            name:str=None,
            date:pywikibot.WbTime=None,
            **kwargs):
        '''
        Class to handle races

        Parameters
        ----------
        name : str, optional
            Name of the race
        date : pywikibot.WbTime, optional
            Date of the race
        '''
        super().__init__(**kwargs)
        
        if name is None and self.item is not None:
            name=self.get_label('fr')
            
        self.nameObj=Name(name)
        
        self.date=date
        self.race_begin=None
        self.race_end=None
        
        self.find_sortkey()
        if date is None and self.item is not None:
            self.date=self.get_date()
        else:
            self.date=date

    def find_sortkey(self):
        '''
        Look for a sortkey for the race, here for national championship
        '''
        team_name_start=[u"championnats d'",u"championnats des ",u"championnats du ",u"championnats de "]
        self.nameObj.find_start_sortkey(team_name_start)
        self.sortkey =self.nameObj.sortkey
    
    def get_begin_date(self)-> pywikibot.WbTime:
        if (u'P580' in self.item.claims):
            self.race_begin = self.item.claims.get(u'P580')[0].getTarget()

        return self.race_begin
    
    def get_date(self)->pywikibot.WbTime:
        if (u'P585' in self.item.claims):
             this_claim = self.item.claims.get(u'P585')
             self.date = this_claim[0].getTarget()
        elif (u'P580' in self.item.claims):
            this_claim  = self.item.claims.get(u'P580')
            self.date = this_claim[0].getTarget()
    
        return self.date

    def get_year(self)->int:
        self.get_date()
        if self.date is None:
            print("date not found")
            return datetime.now().year
        else:
            return int(self.date.year)
    
    def get_end_date(self)-> pywikibot.WbTime:
        if (u'P582' in self.item.claims):
            self.race_end = self.item.claims.get(u'P582')[0].getTarget()

        return self.race_end

    def get_class(self)-> str:
        '''
        Return the class id of the race
        '''
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
        
        if (u'P279' in self.item.claims):
            P279=self.item.claims.get(u'P279')
            for p279 in P279:
                tempQ=p279.getTarget().getID()
                if tempQ in class_list:
                    return tempQ
        return None   
    
    def get_is_women(self)-> bool:
        '''
        Check if it a women race
        '''
        if (u'P2094' in self.item.claims):
            P2094=self.item.claims.get(u'P2094')
            for p2094 in P2094:
                if p2094.getTarget().getID()=="Q1451845":
                    return True
        return False
    
    def get_race_name(self)-> str:
         '''
         Return the name of the race, without the year
         '''
         label_raw=self.get_label('fr')
         if label_raw[len(label_raw)-4:].isdigit():
             label=label_raw[:len(label_raw)-5]
         else:
             label=label_raw
         return label
     
    def add_winner(
            self, 
            value: str, 
            order:int, 
            general_or_stage:int,
            stage:bool=False,
            ):
        '''
        Add winners to a race

        Parameters
        ----------
        value : str
            id of the rider
        order : int
            Rank in the race
        general_or_stage : int
            Code to determine which ranking it is
        stage : bool, optional
            Is it a stage?
        '''
        prop = "P1346"
        #general_or_stage to "vainqueur de xy"
        if stage:
            dic_order1={0:'Q20882763',1:'Q20882747',2:'Q20883008',3:'Q20883213',4:'Q20883140',5: "Q20882922", 8:'Q20883329'}
        else:
            dic_order1={0:'Q20882667',2:'Q20883007', 3:'Q20883212', 4:'Q20883139',5: "Q20882921", 8:'Q20883328'}
        Addc = True
        qualifier_nummer = None
    
        if order == 1:
            if general_or_stage in dic_order1:
                qualifier_nummer=dic_order1[general_or_stage]
        elif order == 2 and general_or_stage==0 and not stage:
            qualifier_nummer = 'Q20882668'
        elif order == 3 and general_or_stage==0 and not stage:
            qualifier_nummer = 'Q20882669'
        else:
            Addc = False
            
        if Addc:
            kk=0
            if prop in self.item.claims:
                list_of_winners = self.item.claims.get(prop)
                for winner in list_of_winners:
                    if winner.getTarget().getID() == value:  # Already there
                        Addc = False
                        claim=winner
                        kk+=1

            if Addc: #adding the winner
                claim = pywikibot.Claim(self.repo, prop)
                target = pywikibot.ItemPage(self.repo, value)
                
                claim.setTarget(target)
                self.item.addClaim(claim, summary=u'Adding winner')
                
            #adding the qualifier
            if qualifier_nummer is not None and kk<=1: #if the rider is found several times, it is safer not to introduce anything
                target_q=pywikibot.ItemPage(self.repo, qualifier_nummer)
                self.add_qualifier(claim,'P642',target_q)
                
    def get_is_stage(self)-> bool:
        '''
        Check if the "race" is actually a stage
        '''
        stagesQ=[
        	"Q18131152",
        	"Q20646667", 
        	"Q20646670",
        	"Q20680270",
        	"Q20646668",
        	"Q20679712",
        	"Q2348250",
        	"Q2266066",
        	"Q485321"]
        
        if (u'P31' in self.item.claims):
            P31=self.item.claims.get(u'P31')
            for p31 in P31:
                if p31.getTarget().getID() in stagesQ:
                    return True
        return False
    
    def add_speed(self,time: int):
        '''
        Calculate and add the speed to a race
        '''
        if (u'P3157' in self.item.claims): #distance
            P3157=self.item.claims.get(u'P3157')
            distance=P3157[0].getTarget().amount
            speed=round(distance/time*3600,2)
            itemKmh=pywikibot.ItemPage(self.repo, "Q180154")
            speed_with_unit = pywikibot.WbQuantity(amount=speed, site=self.site, unit=itemKmh)
            self.add_value("P2052", speed_with_unit, u'speed',noId=True)

class Team(PyItem):
    def __init__(
            self,
            name:str=None,
            date:pywikibot.WbTime=None,
            **kwargs):
        '''
        Class to handle teams and team seasons

        Parameters
        ----------
        name : str, optional
            Name of the team
        date : pywikibot.WbTime, optional
            Date of the season
        '''
        super().__init__(**kwargs)
        
        if name is None and self.item is not None:
            name=self.get_label('fr')
            
        self.nameObj=Name(name)
        if date is None and self.item is not None:
            self.get_date()
        else:
            self.date=date
             
        self.codeUCI = ''
        self.find_sortkey()
            
    def find_sortkey(self):
        '''
        Find the sort key, especially for national team
        '''
        team_name_start=[u"equipe d'",u"equipe des ",u"equipe du ",u"equipe de "]
        self.nameObj.find_start_sortkey(team_name_start)
        self.sortkey=self.nameObj.sortkey
    
    def get_date(self) ->pywikibot.WbTime:
        self.date =None
        if (u'P585' in self.item.claims):
            this_claim = self.item.claims.get(u'P585')
            self.date = this_claim[0].getTarget()
        elif (u'P580' in self.item.claims):
            this_claim  = self.item.claims.get(u'P580')
            self.date = this_claim[0].getTarget()

class Search(CyclingInitBot):
    def __init__(self, 
                 search_str:str):
        '''
        Class to search in wikidata for a string        

        Parameters
        ----------
        search_str : str
            String to be searched
        '''
        super().__init__()
        self.search_str=search_str
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        
    def rider(self,
              first_name:str, 
              last_name:str,
              fc_id=None,
              force_disam:bool=False
              ):
        '''
        Function to search for a rider

        Parameters
        ----------
        first_name : str
        last_name : str
        fc_id : TYPE, optional
            Id in firstcycling of the rider
        force_disam : bool, optional
            If the disambiguation function is not returning true, then the result won't be returned            
        '''
        return self.complexe(
            rider_bool=True,
            disam=self.is_it_a_cyclist,
            exception_table=exception.list_of_rider_ex(),
            first_name=first_name, 
            last_name=last_name,
            fc_id=fc_id,
            force_disam=force_disam)
    
    def team_by_code(
            self, 
            man_or_woman:str=None,
            is_women:bool=None,
            ):
        '''
        Search for a team using its UCI code

        Parameters
        ----------
        man_or_woman : str, optional
            age category and gender of the races to be created
        is_women : bool, optional
            Is it a women race/team
        '''
        if man_or_woman=="man" or is_women==False:
            exception_table=exception.list_of_team_code_ex_man()
            dis=self.is_it_a_menteam
        else:
            exception_table=exception.list_of_team_code_ex()
            dis=self.is_it_a_womenteam
   
        return self.complexe(
           disam=dis,
           force_disam=True,
           exception_table=exception_table,
           ) 

    def team_by_name(
            self, 
            man_or_woman:str=None,
            is_women:bool=None,
            ):
        '''
        Search for a team using its name

        Parameters
        ----------
        man_or_woman : str, optional
            age category and gender of the races to be created
        is_women : bool, optional
            Is it a women race/team
        '''        
        if man_or_woman=="man" or is_women==False:
            exception_table=exception.list_of_team_name_ex_man()
            dis=self.is_it_a_menteam
        else:
            exception_table=exception.list_of_team_name_ex()
            dis=self.is_it_a_womenteam
   
        return self.complexe(
           disam=dis,
           force_disam=True,
           exception_table=exception_table,
           fallback=self.team_by_name_fallback
           )      
    
    def team_by_name_fallback(
            self,
            search_name:str=None,
            disam=None, #disambiguation_function
            force_disam:bool=False,
            ):
        '''
        Fallback function for the search of team by name.
        
        to handle case of " - " which could be "-" in wikidata for instance
        
        Parameters
        ----------    
        search_name : str, optional
            String to be search, will override self.search_str
        disam : TYPE, optional
            Function to disambiguate between items. For instance if 2 persons are returned and one is a cyclist, the cyclist will be returned
        force_disam : bool, optional
            If the disambiguation function is not returning true, then the result won't be returned
        '''
        result_id='Q0'
        kk=0
        
        while result_id=='Q0' and kk<3:
            if kk==0:
                search_name=search_name.replace(" -","-")
            elif kk==1:
                search_name=search_name.replace("- ","-")
            elif kk==2:
                search_name=search_name.replace("team","")
            elif kk==3:
                search_name=search_name.replace("cycling","")
                
            while search_name.find("  ")!=-1:    
                search_name=search_name.replace("  "," ") 
            result_id=self.simple(search_name=search_name,disam=disam,force_disam=force_disam)
            kk+=1
        return result_id

    def race(self):
        '''
        Search for a race
        '''
        result = "Q0", ""
        race_table=race_list.load()
        
        thisname=Name(self.search_str)  #delete the accent and so on
        name=thisname.name_cor

        for k, e in race_table.items():
            found=True
            for n in e['names']:
                n_o=Name(n)
                n_cor=n_o.name_cor
                
                if name.find(n_cor) ==-1:
                    found=False

            if found:
                return e['master'], e['genre']
        return result 

    def national_team(self,positive_list:list,negative_list:list):
        '''
        Search for a national team
        '''
        return self.simple(disam=self.is_it_a_nationalteam,
                    positive_list=positive_list,
                    negative_list=negative_list
                    )

    def get_items(self,item_title: str):
        '''
        Search for an item with its title
        '''
        params = {
            'action': 'wbsearchentities',
            'format': 'json',
            'language': 'fr',
            'type': 'item',
            'search': item_title,
            'limit': 10}
        #params.update({'continue': 1})
        rq = pywikibot.data.api.Request(site=self.site, parameters=params)
        res = rq.submit()
        if res['success'] != 1:
            print('WD search failed')
        else:
            return res

    #search_item
    def simple(
            self,
            search_name:str=None,
            disam=None, #disambiguation_function
            fallback=None,
            force_disam:bool=False,
             **kwargs) -> str:
        '''
        Search a string

        Parameters
        ----------
        search_name : str, optional
            String to be search, will override self.search_str
        disam : TYPE, optional
            Function to disambiguate between items. For instance if 2 persons are returned and one is a cyclist, the cyclist will be returned
        fallback : TYPE, optional
            Function to search with another method, if it did not work
        force_disam : bool, optional
            If the disambiguation function is not returning true, then the result won't be returned
        '''
        if search_name==None:
            search_name=self.search_str
        wd_entries=self.get_items(search_name)

        if(wd_entries['search'] == []):
            # no result
            result_id = u'Q0'
            if fallback is not None:
                result_id=fallback(search_name=search_name,disam=disam,force_disam=force_disam, **kwargs)
        elif len(wd_entries['search'])==1:
            temp_id = wd_entries['search'][0]['id']
            
            if force_disam==False:  #disam criteria must be always filed
                result_id=temp_id ##then we don't care, we just return the result
            else:
                if disam(temp_id,**kwargs): #it must be correct, for instance a rider
                    result_id=temp_id 
                else:
                    print(search_name + " found at " + temp_id + " but disambiguation failed")
                    result_id= u'Q0'
        else:
            # several results
            cand=[]
            result_id = u'Q1'
            #for all candidate look if one fulfill the criteria, for instance be a rider
            
            if disam is not None:
                all_res = wd_entries['search']
                for res in all_res:
                    temp_id=res['id']
                    if disam(temp_id,**kwargs): #no force param here, as it must always be checked
                        cand.append(temp_id)
                        result_id=temp_id
                if len(cand)>1:
                    print("2 items found for: " +search_name + " "+ str(cand))
                    result_id = u'Q1'
    
        return result_id

    #search_itemv2
    def complexe(
            self,
            rider_bool:bool=False,
            first_name:str='',
            last_name:str='',
            exception_table:dict={},
            **kwargs) -> str:
        '''
        As simple but additionally look for exception table

        Parameters
        ----------
        rider_bool : bool, optional
            Is it a rider?
        first_name : str, optional
        last_name : str, optional
        exception_table : dict, optional
            List of rider which returns directly an id to avoid issues.
        '''
        if self.search_str not in [None, '', 0]: # to check
            if rider_bool:
                this_name=CyclistName(self.search_str) #reverted
            else:
                this_name=Name(self.search_str)
            search_name=this_name.name_cor
        else:
            name=first_name + " " + last_name
            if name!=" ":
               this_name=CyclistName(name)
               search_name=this_name.name_cor
            else:
               return u'Q1', ''
        #exception management
        for key in exception_table:
            if rider_bool:
                this_exception=CyclistName(key)  
            else:
                this_exception=Name(key)
            exp=this_exception.name_cor 
            if search_name==exp:
                   return exception_table[key]
        
        return self.simple(search_name=search_name,**kwargs)
    
    def is_it_a_cyclist(self,item_id:str,**kwargs)-> bool:
        '''
        Disambiguation method
        Test is the item had cyclist as occupation
        
        Parameters
        ----------
        item_id : str
            id in wikidata of the item
        '''
        item = pywikibot.ItemPage(self.repo, item_id)
        item.get()
        if(u'P106' in item.claims): 
            for occu in item.claims.get(u'P106'):
                if occu.getTarget() is not None and occu.getTarget().getID() in \
                ['Q2309784',  #cyclist
                 'Q15117395', #track cyclist
                 'Q52217314', #road cyclist
                 'Q15117415', #cyclo-cross
                 'Q19799599', #mountain bike
                 'Q15306067', #triathlete
                 'Q53645345', #duathelete
                 'Q13382576', #rowing
                 'Q13382566', #rowing2
                 'Q10866633'  #speed squatting
                 ]: 
                    return True
        if(u'P641' in item.claims): #fallback
            for sport in item.claims.get(u'P641'):
                if sport.getTarget() is not None and sport.getTarget().getID() in \
                    ['Q3609', #road cycling
                     'Q221635', #track cycling
                     'Q2215841', #cycling
                     'Q215184', #BMX
                     'Q672066', #descent
                     'Q1031445', #cross-country
                     'Q1360806', #cross-country marathon
                     'Q111721834', #gravel
                     ]:
                        return True
        return False

    def is_it_a_teamseason(self,item_id: str,**kwargs) -> bool:
        '''
        Disambiguation method
        Test if the item is a team season
        
        Parameters
        ----------
        item_id : str
            id in wikidata of the item
        '''
        item = pywikibot.ItemPage(self.repo, item_id)
        item.get()
        if(u'P31' in item.claims):  
            for nature in item.claims.get(u'P31'):
                if nature.getTarget().getID() == 'Q53534649':  
                    return True
        return False 

    def find_sortkey(self,label: str,words: list)-> bool:
        '''
        Search if one of the words is contained in the label
        '''
        for word in words:
            if label.find(word)!=-1:
                return True
        return False

    def is_it_a_nationalteam(
            self,
            item_id:str,
            positive_list:list=[],
            negative_list:list=[],
            **kwargs)-> bool:
        '''
        Disambiguation method
        Test if the item is a national team

        Parameters
        ----------
        item_id : str
            id in wikidata of the item
        positive_list : list, optional
            List of key words that indicates that it is the case
        negative_list : list, optional
            List of key words that indicates that it is not the case
        '''
        pyItem=PyItem(id=item_id)
        this_label=pyItem.get_label('fr')
        
        if (self.find_sortkey(this_label, positive_list) and 
           not self.find_sortkey(this_label, negative_list)):
            return True
        else:
            return False
        
    def is_it_a_womenteam(self,item_id:str,**kwargs):
        '''
        Disambiguation method
        Test if the item is a women team
        
        Parameters
        ----------
        item_id : str
            id in wikidata of the item
        '''
        if self.is_it_a_teamseason(item_id):
            item = pywikibot.ItemPage(self.repo, item_id)
            item.get()
            
            if (u'P2094' in item.claims):
                P2094=item.claims.get(u'P2094')
                for p2094 in P2094:
                    if p2094.getTarget().getID() in ["Q2466826","Q26849121","Q80425135","Q1451845","Q119942457"]:#, #cats and women cycling, Q1451845 required for national team
                        return True
                    
        return False
            
    def is_it_a_menteam(self,item_id: str,**kwargs):
        '''
        Disambiguation method
        Test if the item is a men team
        
        Parameters
        ----------
        item_id : str
            id in wikidata of the item
        '''
        if self.is_it_a_teamseason(item_id):
            item = pywikibot.ItemPage(self.repo, item_id)
            item.get()
            
            if (u'P2094' in item.claims):
                P2094=item.claims.get(u'P2094')
                for p2094 in P2094:
                    if p2094.getTarget().getID() in ["Q2466826","Q26849121","Q80425135","Q119942457","Q1451845"]:#, "Q1451845" #cats and women cycling 
                        return False
            if (u'P31' in item.claims):
                P31=item.claims.get(u'P31')
                for p31 in P31:
                    if p31.getTarget().getID() in ["Q2466826","Q26849121","Q80425135"]:#cats
                        return False                    
            return True
        return False    
    
    def search_fc_id(self, fc_id:int=None):
        '''
        Search using the firstcycling id
        '''
        query_part1 = """SELECT ?item
        WHERE{
          ?item wdt:P10902 ?fcid .
          FILTER(CONTAINS(?fcid,"""
        query_part2=""")) .
          SERVICE wikibase:label { bd:serviceParam wikibase:language "fr", "en". }
        }"""
        query=query_part1 + str(fc_id) +query_part2
        generator = pg.WikidataSPARQLPageGenerator(query, site=self.site, endpoint='https://query.wikidata.org/sparql')
            
        ii=0
        for item in generator:
            ii+=1 #check that there is only one result
        
        if ii==1:
            generator = pg.WikidataSPARQLPageGenerator(query, site=self.site, endpoint='https://query.wikidata.org/sparql')
            for item in generator:
                return item.getID()
        return u'Q0'

class Log():
    def __init__(self):
        '''
        Save logs
        '''
        self.txt=""
        
    def concat(self, new:str):
        '''
        Add text to the log
        '''
        print(new) #for local
        self.txt+="\n" + str(new) #write a log that is returned to the site
    

def year_child(
        year:int,
        id_master:str,      
        ):
    '''
    Search in a master, the child associated with a year

    Parameters
    ----------
    year : int
    id_master : str
        Id of the parent of the item
    '''
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    
    item_master = pywikibot.ItemPage(repo, id_master)
    item_master.get()
    
    if (u'P527' in item_master.claims):
        for claim in item_master.claims.get(u'P527'):
            v=claim.getTarget().getID()
            pyItem_v=PyItem(item=claim.getTarget(),id=v)
            
            for _, label in pyItem_v.item.labels.items():
                if str(year) in label:
                    return v, pyItem_v
    return None, None



