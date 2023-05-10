# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:38:42 2018

@author: psemdel
"""

import pywikibot
from pywikibot import pagegenerators as pg
from .data import nation_team_table, language_list, race_list, exception 
from .name import Name, CyclistName, concaten

### All classes in the code ###

#Master-class for the functions in the bot
class CyclingInitBot():
    def __init__(self,**kwargs):
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        self.nation_table= nation_team_table.load()
        self.all_langs=language_list.load()
        self.log=Log()
        self.test=kwargs.get("test",False)

    def get_items(self,item_title):
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

def create_item(label):   
    search=Search(label['fr'])
    present_id=search.simple()
    site = pywikibot.Site("wikidata", "wikidata")
    repo=site.data_repository()
    
    if (present_id == u'Q0'):
        print(label['fr'] + ' created')
        return create_item_sub(label)
    elif (present_id == u'Q1'):
        print(label['fr'] + ' already present several times')
        return None
    else:
        print(label['fr'] + ' already present')
        item = pywikibot.ItemPage(repo, present_id)
        return PyItem(id=present_id, item=item)

def create_item_sub(label):
    try:
        pywikibot.exception(tb=True)
        site=pywikibot.Site("wikidata", "wikidata")
        new_item = pywikibot.ItemPage(site)
        new_item.editLabels(labels=label, summary="Setting labels")
    # Add description here or in another function
        pyItem=PyItem(id=new_item.getID(), item=new_item)
        return pyItem
    except Exception as msg:
        print("create_item crash")
        print(msg)
        #pywikibot.exception(msg)

#kind of overload of item in pywikibot
class PyItem():
    def __init__(self, **kwargs):
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        self.id=kwargs.get("id","Q0")
        self.item=kwargs.get("item")
        
        if self.item is None and self.id !="Q0":
            self.item=pywikibot.ItemPage(self.repo, self.id)
            self.item.get()
        
    def get_country(self):
        if (u'P17' in self.item.claims):
             P17=self.item.claims.get(u'P17')
             return P17[0].getTarget().getID()
        else:
             return None
            
    def add_value(self, prop, value, comment,**kwargs):
        if value!=0 or kwargs.get("date",False): #date is somehow not different from 0
            if prop not in self.item.claims:  # already there do nothing
                claim = pywikibot.Claim(self.repo, prop)
                if kwargs.get("date",False) or kwargs.get("noId",False):
                    target=value
                else:
                    target = pywikibot.ItemPage(self.repo, value)
                    
                claim.setTarget(target)
                self.item.addClaim(claim, summary=u'Adding ' + comment)  

    def delete_value(self, prop, vId, comment):
        if prop in self.item.claims:
            for ii, e in enumerate(self.item.claims.get(prop)):
                if e.getTarget().getID() == vId:  # Already there
                    claim =  self.item.claims[prop][ii]
                    self.item.removeClaims(claim)

    def delete_property(self, prop):
        if prop in self.item.claims :
            self.item.removeClaims(self.item.claims[prop])

# Same as add value but for comprend
    def add_values(self,prop,vId,comment,overpass):
        # check if the value is not already 
        Addc = True
        
        if not overpass:  # To add a value and then delete it for sorting purpose
            if prop in self.item.claims:  # already there do nothing
                for e in self.item.claims.get(prop) :
                    if e.getTarget().getID() == vId:  # Already there
                        claim=e
                        Addc = False
                        print('Item already present')
                        break
        # add the value
        if Addc:
            claim = pywikibot.Claim(self.repo, prop)
            target = pywikibot.ItemPage(self.repo, vId)
            claim.setTarget(target)
            self.item.addClaim(claim, summary=u'Adding ' + comment)
        return Addc, claim

    #note: as claim is defined, the pyItem calling does not matter
    def add_qualifier(self,claim,prop,target_q):
        Addc = True
        for qual in claim.qualifiers.get(prop, []):
            Addc = False
        if Addc:
            q=pywikibot.page.Claim(self.site, prop, is_qualifier=True)
            q.setTarget(target_q)
            claim.addQualifier(q)

    def link_year(self, year,**kwargs):
        year_previous=int(year)-1
        year_next=int(year)+1
        id_master=kwargs.get("id_master")
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
            item_master = pywikibot.ItemPage(self.repo, id_master)
            item_master.get()
            
            #look for next and previous
            if (u'P527' in item_master.claims):
                for claim in item_master.claims.get(u'P527'):
                    v=claim.getTarget().getID()
                    pyItem_v=PyItem(item=claim.getTarget(),id=v)
                    label=pyItem_v.get_label('fr')
                    
                    if str(year_previous) in label:
                        id_previous=v
                        pyItem_previous=pyItem_v
                    elif str(year_next) in label:
                        id_next=v
                        pyItem_next=pyItem_v
        
            #link the whole
            if kwargs.get("test",False):
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

    def get_label(self,language):
        if language in self.item.labels:
            return self.item.labels[language]
        elif 'en'  in self.item.labels:
            return self.item.labels['en']
        else:
            for lang in self.item.labels:
                   return  self.item.labels[lang]
            return ''
     
    def get_description(self, language):
        if language in self.item.descriptions:
            return self.item.descriptions[language]
        else:
            return ''

    def get_alias(self, language):
        if language in self.item.aliases:
            return self.item.aliases[language]
        else:
            return '' 

class Cyclist(PyItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        name=kwargs.get("name")
        if name is None and self.item is not None:
            name=self.get_label('fr')
        
        self.nameObj=CyclistName(name)
        self.name =  self.nameObj.name
        self.name_cor =  self.nameObj.name_cor
        
        self.dossard = 0
        self.team=None
        
        nosortkey=kwargs.get('nosortkey',False)
        self.sortkey =None
        if nosortkey==False:
            self.find_sortkey()
            
        self.nationality=''
        self.rank=0
        self.national_team=False
    
    def find_start_sortkey(self,start_words,names_cor_table):
        for ii in range(1,len(names_cor_table)):
           if names_cor_table[ii] in start_words:
               self.sortkey=concaten(names_cor_table,ii)
    
    def find_sortkey(self):
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
                     print(self.nameObj.name)
                     ii = input('Index of the family name : ')
                     self.sortkey=concaten(names_cor_table ,int(ii))       
                 else: #site
                     self.sortkey=concaten(names_cor_table ,1) #arbitrary
                     
    def get_present_team(self, time_of_race):
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
    
    #return ID of country from nationality
    def get_nationality(self, time_of_race):
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
                print("USSR rider")
                print(self.id)
            if result=="Q55": #NED   
                result="Q29999"
            
            return result
        except Exception as msg:
                print(msg)   
         
class Race(PyItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        name=kwargs.get("name")
        date=kwargs.get("date") 
        
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
        #if still none
        #if self.date is None:
        #    self.date=pywikibot.WbTime(site=self.site, year=1900, month=1, day=1, precision='day')

    def find_sortkey(self):
        team_name_start=[u"championnats d'",u"championnats des ",u"championnats du ",u"championnats de "]
        self.nameObj.find_start_sortkey(team_name_start)
        self.sortkey =self.nameObj.sortkey
    
    def get_begin_date(self):
        if (u'P580' in self.item.claims):
            self.race_begin = self.item.claims.get(u'P580')[0].getTarget()

        return self.race_begin
    
    def get_date(self):
        if (u'P585' in self.item.claims):
             this_claim = self.item.claims.get(u'P585')
             self.date = this_claim[0].getTarget()
        elif (u'P580' in self.item.claims):
            this_claim  = self.item.claims.get(u'P580')
            self.date = this_claim[0].getTarget()
    
        return self.date

    def get_year(self):
        self.get_date()
        if self.date is None:
            print("date not found")
            return 0
        else:
            return int(self.date.year)
    
    def get_end_date(self):
        if (u'P582' in self.item.claims):
            self.race_end = self.item.claims.get(u'P582')[0].getTarget()

        return self.race_end

    def get_class(self):
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
    
    def get_is_women(self):
        if (u'P2094' in self.item.claims):
            P2094=self.item.claims.get(u'P2094')
            for p2094 in P2094:
                if p2094.getTarget().getID()=="Q1451845":
                    return True
        return False
    
    def get_race_name(self):
         label_raw=self.get_label('fr')
         if label_raw[len(label_raw)-4:].isdigit():
             label=label_raw[:len(label_raw)-5]
         else:
             label=label_raw
         return label
     
    def add_winner(self, value, order, general_or_stage):
        print("add winner")
        prop = "P1346"
        #general_or_stage to "vainqueur de xy"
        dic_order1={0:'Q20882667',2:'Q20883007', 3:'Q20883212', 4:'Q20883139',8:'Q20883328',100:'Q20882747',101:'Q20882763'}
        Addc = True
    
        if order == 1:
            if general_or_stage in dic_order1:
                qualifier_nummer=dic_order1[general_or_stage]
            else:
                qualifier_nummer = 'Q20882667'
        elif order == 2 and general_or_stage==0:
            qualifier_nummer = 'Q20882668'
        elif order == 3 and general_or_stage==0:
            qualifier_nummer = 'Q20882669'
        else:
            Addc = False
    
        if Addc:
            if prop in self.item.claims:
                list_of_winners = self.item.claims.get(prop)
                for winner in list_of_winners:
                    if winner.getTarget().getID() == value:  # Already there
                        Addc = False
                        claim=winner
                        print("claim found")
    
            if Addc: #adding the winner
                claim = pywikibot.Claim(self.repo, prop)
                target = pywikibot.ItemPage(self.repo, value)
                
                claim.setTarget(target)
                self.item.addClaim(claim, summary=u'Adding winner')
                
            #adding the qualifier
            print(qualifier_nummer)
            target_q=pywikibot.ItemPage(self.repo, qualifier_nummer)
            self.add_qualifier(claim,'P642',target_q)
                
    def get_is_stage(self):
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
    
class Team(PyItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        name=kwargs.get("name")
        
        if name is None and self.item is not None:
            name=self.get_label('fr')
            
        self.nameObj=Name(name)
        date=kwargs.get("date")
        if date is None and self.item is not None:
            self.get_date()
        else:
            self.date=date
             
        self.codeUCI = ''
        self.find_sortkey()
       
            
    def find_sortkey(self):
        team_name_start=[u"equipe d'",u"equipe des ",u"equipe du ",u"equipe de "]
        self.nameObj.find_start_sortkey(team_name_start)
        self.sortkey=self.nameObj.sortkey
    
    def get_date(self):
        self.date =None
        if (u'P585' in self.item.claims):
            this_claim = self.item.claims.get(u'P585')
            self.date = this_claim[0].getTarget()
        elif (u'P580' in self.item.claims):
            this_claim  = self.item.claims.get(u'P580')
            self.date = this_claim[0].getTarget()

class Search(CyclingInitBot):
    def __init__(self, search_str):
        super().__init__()
        self.search_str=search_str
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        
    def rider(self, first_name, last_name, **kwargs):
        return self.complexe(
            rider_bool=True,
            disam=self.is_it_a_cyclist,
            exception_table=exception.list_of_rider_ex(),
            first_name=first_name, 
            last_name=last_name,
            fc_id=kwargs.get("fc_id"))
    
    def team_by_code(self, **kwargs):
        if kwargs.get("man_or_woman","woman")=="man" or kwargs.get("is_women",True)==False:
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

    def team_by_name(self, **kwargs):
        if kwargs.get("man_or_woman","woman")=="man" or kwargs.get("is_women",True)==False:
            exception_table=exception.list_of_team_name_ex_man()
            dis=self.is_it_a_menteam
        else:
            exception_table=exception.list_of_team_name_ex()
            dis=self.is_it_a_womenteam
   
        return self.complexe(
           disam=dis,
           force_disam=True,
           exception_table=exception_table,
           )        
            
    def race(self):
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

    def national_team(self,positive_list,negative_list):
        return self.simple(disam=self.is_it_a_nationalteam,
                    positive_list=positive_list,
                    negative_list=negative_list
                    )

    #search_item
    def simple(self,**kwargs):
        search_name=kwargs.get("search_name",self.search_str)
        disam=kwargs.get('disam') #disambiguation_function
        wd_entries=self.get_items(search_name)
        
        if(wd_entries['search'] == []):
            # no result
            result_id = u'Q0'
            fallback=kwargs.get("fallback")
            if fallback is not None:
                result_id=fallback(**kwargs)
        elif len(wd_entries['search'])==1:
            temp_id = wd_entries['search'][0]['id']
            
            if kwargs.get('force_disam',False)==False:  #disam criteria must be always filed
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
    def complexe(self,**kwargs):
        rider_bool=kwargs.get("rider_bool",False)
        
        if self.search_str not in [None, '', 0]: # to check
            if rider_bool:
                this_name=CyclistName(self.search_str) #reverted
            else:
                this_name=Name(self.search_str)
            search_name=this_name.name_cor
        else:
            first_name=kwargs.get('first_name','')
            last_name=kwargs.get('last_name','')
            name=first_name + " " + last_name
            if name!=" ":
               this_name=CyclistName(name)
               search_name=this_name.name_cor
            else:
               return u'Q1', ''
        #exception management
        exception_table=kwargs.get('exception_table',{})

        for key in exception_table:
            if rider_bool:
                this_exception=CyclistName(key)  
            else:
                this_exception=Name(key)
            exp=this_exception.name_cor 
            if search_name==exp:
                   return exception_table[key]
        
        return self.simple(search_name=search_name,**kwargs)
    
    def is_it_a_cyclist(self,item_id,**kwargs):
        item = pywikibot.ItemPage(self.repo, item_id)
        item.get()
        if(u'P106' in item.claims): 
            for occu in item.claims.get(u'P106'):
                try:
                    if occu.getTarget().getID() == 'Q2309784': 
                        return True
                except Exception as msg:
                    print(msg)
                    return False
        return False

    def is_it_a_teamseason(self,item_id,**kwargs):
        item = pywikibot.ItemPage(self.repo, item_id)
        item.get()
        if(u'P31' in item.claims):  
            for nature in item.claims.get(u'P31'):
                if nature.getTarget().getID() == 'Q53534649':  
                    return True
        return False 

    def find_sortkey(self,label,words):
        for word in words:
            if label.find(word)!=-1:
                return True
        return False

    def is_it_a_nationalteam(self,item_id,**kwargs):
        positive_list=kwargs.get('positive_list',[])
        negative_list=kwargs.get('negative_list',[])
        
        pyItem=PyItem(id=item_id)
        this_label=pyItem.get_label('fr')
        
        if (self.find_sortkey(this_label, positive_list) and 
           not self.find_sortkey(this_label, negative_list)):
            return True
        else:
            return False
        
    def is_it_a_womenteam(self,item_id,**kwargs):
        if self.is_it_a_teamseason(item_id):
            item = pywikibot.ItemPage(self.repo, item_id)
            item.get()
            
            if (u'P2094' in item.claims):
                P2094=item.claims.get(u'P2094')
                for p2094 in P2094:
                    if p2094.getTarget().getID() in ["Q2466826","Q26849121","Q80425135","Q1451845"]:#, #cats and women cycling, Q1451845 required for national team
                        return True
            #if (u'P31' in item.claims):
            #    P31=item.claims.get(u'P31')
            #    for p31 in P31:
            #        if p31.getTarget().getID() in ["Q2466826","Q26849121","Q80425135"]:#cats
            #            return True                    
                    
        return False
            
    def is_it_a_menteam(self,item_id,**kwargs):
        if self.is_it_a_teamseason(item_id):
            item = pywikibot.ItemPage(self.repo, item_id)
            item.get()
            
            if (u'P2094' in item.claims):
                P2094=item.claims.get(u'P2094')
                for p2094 in P2094:
                    if p2094.getTarget().getID() in ["Q2466826","Q26849121","Q80425135"]:#, "Q1451845" #cats and women cycling 
                        return False
            if (u'P31' in item.claims):
                P31=item.claims.get(u'P31')
                for p31 in P31:
                    if p31.getTarget().getID() in ["Q2466826","Q26849121","Q80425135"]:#cats
                        return False                    
            return True
        return False    
    
    def search_fc_id(self, **kwargs):
        fc_id=kwargs.get("fc_id")
        
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
        self.txt=""
        
    def concat(self, new):
        print(new) #for local
        self.txt+="\n" + str(new) #write a log that is returned to the site
    





