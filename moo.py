#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:57:03 2019

@author: maxime
"""
#operations on names

def concaten(names_table,ii):
    start=names_table[ii]
    for kk in range(ii+1,len(names_table)):
        start=start+" " + names_table[kk]
    return start

class ThisName:
    def __init__(self, name):
        self.name = name
        self.name_cor = name
        self.check_and_revert()
        self.correct_name()
        self.sortkey = self.name_cor
        
    def correct_name(self):
        self.name_cor = self.name_cor.lower()
        self.supprime_accent()

    def supprime_accent(self):
        """ supprime les accents du texte source """
        ligne = self.name_cor
        accents = {'a': ['à', 'ã', 'á', 'â', 'ä'],
                   'e': ['é', 'è', 'ê', 'ë'],
                   'i': ['î', 'ï'],
                   'u': ['ù', 'ü', 'û','ů'],
                   'o': ['ô', 'ö'],
                   's': ['š'],
                   'n': ['ñ'],
                   'ss' : ['ß'],
                   'c' : ['č'],
                   'z' : ['ž']}
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        self.name_cor=ligne 

    def find_start_sortkey(self, start_words):
        for word in start_words:
            if self.name_cor.find(word)!=-1:
                self.sortkey=self.name_cor[len(word):]
                break
        return self.sortkey
    
    def check_and_revert(self):
        names_table = self.name.split(" ")
        
        if names_table[0]==names_table[0].upper():
            last_name=names_table[0]
            end_last_name=0
            for ii in range(1,len(names_table)):
                if names_table[ii]==names_table[ii].upper():
                   last_name=last_name+ " " + names_table[ii]
                else:
                   end_last_name=ii
                   break
            last_name=last_name.lower()
       
            first_name=names_table[end_last_name]
            for ii in range(end_last_name+1,len(names_table)):
                first_name=first_name + " " + names_table[ii]
            
            self.name=first_name + " " + last_name

#A cyclist
class Cyclist(ThisName):
    def __init__(self, id, name, id_item, **kwargs):
        ThisName.__init__(self,name)
        self.key = id
        self.id_item = id_item
        self.dossard = 0
        self.team=''
        nosortkey=kwargs.get('nosortkey',False)
        if nosortkey==False:
            self.sortkey = self.find_sortkey()
        else:
            self.sortkey =''
        self.item=None
        self.nationality=''
        self.rank=0
    
    def find_start_sortkey(self,start_words,names_table,names_cor_table):
        sortkey=''
        for ii in range(1,len(names_cor_table)):
           if names_cor_table[ii] in start_words:
               sortkey=concaten(names_table,ii)
        
        return sortkey
    
    def find_sortkey(self):
        names_cor_table = self.name_cor.split(" ")
        names_table = self.name.split(" ")
        done=False

        family_name_start=[u'van',u'de']
        if len(names_table)==2:
            self.sortkey=names_table[1]
            done=True
        else:
            sortkey=self.find_start_sortkey(family_name_start,names_table,names_cor_table)
            if sortkey!='':
                 self.sortkey=sortkey
            else:
                 print(self.name)
                 ii = input('Index of the family name : ')
                 self.sortkey=concaten(names_table,int(ii))       
         
class Race(ThisName):
    def __init__(self, id, name, id_item, date, **kwargs):
        self.key = id
        ThisName.__init__(self,name)
        self.id_item = id_item
        self.sortkey = self.find_sortkey()
        if date=='':
            site=kwargs.get('site')
            pywikibot=kwargs.get('pywikibot')
            self.date=pywikibot.WbTime(site=site, year=1900, month=1, day=1, precision='day')
        else:
            self.date = date
            
    def find_sortkey(self):
        team_name_start=[u"championnats d'",u"championnats des",u"championnats du",u"championnats de"]
        return ThisName.find_start_sortkey(self, team_name_start)
        
class Team(ThisName):
    def __init__(self, id, name, id_item, date, **kwargs):
        self.key = id
        ThisName.__init__(self,name)
        self.id_item = id_item  
        self.codeUCI = ''
        self.sortkey = self.find_sortkey()
        if date=='':
            site=kwargs.get('site')
            pywikibot=kwargs.get('pywikibot')
            self.date=pywikibot.WbTime(site=site, year=1900, month=1, day=1, precision='day')
        else:
            self.date = date
            
    def find_sortkey(self):
        team_name_start=[u"equipe d'",u"equipe des",u"equipe du",u"equipe de"]
        return ThisName.find_start_sortkey(self,team_name_start)


    