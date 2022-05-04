# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:48:04 2018

@author: psemdel
"""
import pywikibot
import sys
from .base import CyclingInitBot, Race, PyItem, Team, Cyclist
#sort the victories by date

class DateSorter(CyclingInitBot):
    def __init__(self,team_id, prop,**kwargs):
        super().__init__(**kwargs)
        self.team=PyItem(id=team_id)
        self.prop=prop
    
    def main(self):
        try:
            self.listo = []

            if(self.prop in self.team.item.claims):
                list_of_comprend = self.team.item.claims.get(self.prop)
            else:
                print("property for date sorting not found")
            
            for e in list_of_comprend: #ii needed below
                race=Race(None,None,id=e.getTarget().getID())
                if race.date is None:
                    self.log.concat(race.get_labels('fr') + ' has no date')
                self.listo.append(race)

            self.new_order = [ii for ii in range(len(list_of_comprend))]
            old_order = self.new_order.copy()
        
            self.date_sort()
            order_ok=True
            
            if not self.test:
                for ii, e in enumerate(self.new_order):
                    if e != old_order[ii]: #change only from the moment it differs, afterwards everything must be ordered
                        order_ok=False
                    if not order_ok:
                        key = e
                        
                self.team.delete_value(self.prop,self.listo[key].id,'race for sorting')
                self.team.add_values(self.prop,self.listo[key].id,'race for sorting',True)

            return 0, self.log     
        except:
            self.log.concat("General Error in date sorter")
            return 10, self.log            
        
    def date_sort(self):
        iimax = len(self.new_order) - 1
        for ii in range(iimax - 1):
            jjmax = iimax - ii
            table_sorted = True
            for jj in range(jjmax):
                victoire1 = self.listo[self.new_order[jj]]
                victoire2 = self.listo[self.new_order[jj + 1]]
                date1 = victoire1.date
                date2 = victoire2.date
                if date1.toTimestamp() > date2.toTimestamp():  # bad order
                    temp = self.new_order[jj]
                    self.new_order[jj] = self.new_order[jj + 1]
                    self.new_order[jj + 1] = temp
                    table_sorted = False
            if table_sorted:
                break
        self.log.concat(self.new_order)

#sort the family name of cyclists
class NameSorter(CyclingInitBot):
    def __init__(self,team_id, prop,**kwargs):
        super().__init__(**kwargs)
        self.team=PyItem(id=team_id)
        self.prop=prop     
        
    def check_if_team(self):
        list_of_team_cat = [
        "Q6154783", "Q20638319", "Q382927", "Q1756006", 
        "Q23726798", "Q20738667", "Q28492441", "Q20639848", 
        "Q20639847", "Q20652655", "Q20653563", "Q20653564",
        "Q20653566", "Q2466826", "Q26849121", "Q78464255", 
        "Q80425135", "Q53534649", "Q2466826"
        ]
        
        team=False
        if u'P31' in self.team.item.claims:
            list_of_comprend = self.team.item.claims.get(u'P31')
            for e in list_of_comprend:
                if e.getTarget().getID() in list_of_team_cat:
                    team=True
        return team
        
    def main(self):
        try:
            if(self.prop in self.team.item.claims):
                list_of_comprend = self.team.item.claims.get(self.prop)
            else:
                print("property for name sorting not found")
                self.log.concat("property for name sorting not found")
                return 10, self.log   
            dic = {}
            #list_of_names = [['' for x in range(2)] for y in list_of_comprend]
            list_of_names=[]
            
            for e in list_of_comprend:
                if self.prop =="P1923":
                    o=Team(id=e.getTarget().getID())
                elif self.check_if_team():
                    o=Cyclist(id=e.getTarget().getID())
                else:
                    o=Race(id=e.getTarget().getID())
    
                dic[o.sortkey]=o
              #  list_of_objects.append(o)
                list_of_names.append(o.sortkey) #sortkey is generate automatically
                
            sorted_names = sorted(list_of_names, key=lambda tup: tup[0])    
            self.log.concat('sorted list :')
            self.log.concat(sorted_names)
            order_ok=True

            if not self.test:
                for ii, name in enumerate(sorted_names):
                    if name != list_of_names[ii]: #change only from the moment it differs, afterwards everything must be ordered
                        order_ok=False
                    if not order_ok:
                        claim = self.team.item.claims[self.prop][0]
                
                        # Save the qualifiers
                        saved_qualifiers={}
                        for qual in claim.qualifiers:
                            saved_qualifiers[qual]=claim.qualifiers[qual][0].getTarget()
                        
                        self.team.delete_value(self.prop,dic[name].id,'rider for sorting')
                        self.team.add_values(self.prop,dic[name].id,'rider for sorting',True)

                        for qual in saved_qualifiers:
                            this_qual = pywikibot.page.Claim(self.site, qual, isQualifier=True)
                            this_qual.setTarget(saved_qualifiers[qual])
                            claim.addQualifier(this_qual) 
            
            return 0, self.log     
        except Exception as msg:
            _, _, exc_tb = sys.exc_info()
            print("line " + str(exc_tb.tb_lineno))
            print(msg)
            self.log.concat("General Error in name sorter")
            return 10, self.log   
        except:     
            self.log.concat("General Error in name sorter")
            return 10, self.log   

