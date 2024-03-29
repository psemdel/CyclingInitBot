#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:05:33 2019

@author: maxime
"""
from .base import CyclingInitBot, create_item
import traceback

class RiderFastInit(CyclingInitBot):
    def __init__(
            self,
            name, 
            country, 
            man_or_woman, 
            **kwargs):
        '''
        Create an item corresponding to a rider

        Parameters
        ----------
        name : TYPE
            Name of the rider
        country : TYPE
            code of the country, for instance "FRA"
        man_or_woman : TYPE
            age category and gender of the races to be created
        '''
        super().__init__(**kwargs)
        self.country=country
        self.man_or_woman=man_or_woman
        self.label = {}

        #same name for all latin languages
        for lang in self.all_langs:
            self.label[lang] = name
        
    def create_fr_description(self):
        '''
        Generate the description for the rider
        '''
        if self.man_or_woman==u'man':
            mydescription={'fr': 'coureur cycliste '+\
                                        self.nation_table[self.country]['adj fr man'] or ''}
        else:
            mydescription={'fr': 'coureuse cycliste '+\
                                        self.nation_table[self.country]['adj fr woman'] or ''}
        self.pyItem.item.editDescriptions(mydescription,
                              summary=u'Setting/updating descriptions.')

    def main(self):
        '''
        Main function of this script
        '''
        try:
            print("rider_fast_init")
        
            self.pyItem=create_item(self.label)
            if self.pyItem is not None:
                self.log.concat("rider id: "+ self.pyItem.id)
                self.create_fr_description()
                
                self.pyItem.add_value("P31", "Q5", u'nature')
                
                if self.man_or_woman==u'man':
                    genre="Q6581097"
                else:
                    genre="Q6581072"
                self.pyItem.add_value("P21", genre, u'genre')
                self.pyItem.add_value("P27",
                                       self.nation_table[self.country]["country"], 
                                       u'nationality')
                self.pyItem.add_value("P106", "Q2309784", u'cyclist')
            else:
                self.log.concat("AlreadyThere several instance of this item")
                return 1, self.log, "Q1"
            return 0, self.log, self.pyItem.id
        
        except Exception as msg:
            print(traceback.format_exc())
            self.log.concat("General Error in rider_fast_init")
            self.log.concat(traceback.format_exc())
            return 10, self.log, "Q1"
