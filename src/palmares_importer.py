#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:51:55 2023

@author: maxime
"""

from .base import CyclingInitBot, PyItem, Search, Race                  
import pywikibot

class PalmaresImporter(CyclingInitBot):
    def __init__(
            self, 
            base_str:str,
            **kwargs):
        
        self.base_str=base_str
        self.inputstr = """
|-
| 1905 || H. P. Hansen || Valdemar Nielsen || Carl Andreasen 
|-
| 1907 || [[Olaf Hansen (cyclisme)|Olaf Hansen]] || K. Lihn || Hans Hansen
|-
| 1908 || Carl Hansen || ||
|-
| 1909 || Hans Olsen || Christian Damm || Fritjof Rosted
|-
| 1910 ||Carl Andreasen || Louis Petersen || Olaf Meyland-Schmidt
|-
| 1913 || [[Olaf Hansen (cyclisme)|Olaf Hansen]] || A. K. Andersen || [[Holger Malmgren]]
|-
| 1915 || [[Holger Malmgren]] || Christian Johansen || [[Olaf Hansen (cyclisme)|Olaf Hansen]]
|-
| 1916 || [[Holger Malmgren]] || [[Carl Mortensen (cyclisme)|Carl Mortensen]] || E. Bilgreen
|-
| 1917 || Christian Frisch || A. K. Andersen || [[Carl Mortensen (cyclisme)|Carl Mortensen]]
|-
| 1918 || [[Carl Mortensen (cyclisme)|Carl Mortensen]] || Willum Nielsen || Henry F. Petersen
|-
| 1919 || [[Carl Mortensen (cyclisme)|Carl Mortensen]] || Marino Nielsen || Christian Frisch
|-
| 1920 || Frederik Ahrensborg Clausen || Christian Johansen ||Willum Nielsen
|-
| 1921 || [[Henry Hansen]] || Frederik Ahrensborg Clausen || Artur Larsen
|-
| 1922 || [[Albert Mansson]] || [[Hans Petersen (cyclisme)|Hans Petersen]] || Johannes Rasmussen
|-
| 1923 || [[Henry Hansen]] || [[Albert Mansson]] || Marino Nielsen
|-
| 1924 || Erik Eloe Andersen || [[Henry Hansen]] || [[Albert Mansson]] 
|-
| 1925 || [[Henry Hansen]] || Eigil Jensen || Edvin Nielsen
|-
| 1926 || Poul Sørensen || Marino Nielsen || [[Orla Jørgensen]]
|-
| 1927 || Poul Sørensen || [[Leo Nielsen]] || Otto Nielsen
|-
| 1929 || [[Finn Nymann]] || Poul Sørensen || [[Oluf Clausen]]
|-
| 1930 || [[Henry Hansen]] || [[Leo Nielsen]] || Erik Eloe Andersen
|-
| 1931 || [[Frode Sørensen (cyclisme)|Frode Sørensen]] || [[Leo Nielsen]] || [[Henry Andersen]]
|-
|1932 || [[Frode Sørensen (cyclisme)|Frode Sørensen]] || [[Leo Nielsen]] || Knud Jacobsen
|-
|1933 || Werner Grundahl || [[Henry Jørgensen]] || Knud Jacobsen
|-
|1934 || [[Leo Nielsen]] || [[Frode Sørensen (cyclisme)|Frode Sørensen]] || Tage Møller
|-
|1935 || [[Frode Sørensen (cyclisme)|Frode Sørensen]] || Werner Grundahl || Knud Jacobsen
|-
|1946 || [[Knud Andersen (cyclisme)|Knud Andersen]] || Rudolf Rasmussen || Børge Saxil Nielsen
|-
|1947 || [[Christian Pedersen]] || Rudolf Rasmussen || [[Jørgen Poulsen]]
|-
|1971 || [[Gunnar Asmussen]] || [[Jørgen Schmidt]] || Benny Pedersen
|-
|1972 || [[Reno Olsen]] || [[Jørn Lund]] || Jørgen Timm
|-
|1973 || [[Reno Olsen]] || Ivar Jakobsen || [[Jørn Lund]]
|-
|1974 || Jørgen Timm || [[Jørgen Marcussen]] || [[Kjell Rodian]]
|-
|1975 || [[Jørgen Marcussen]] || [[Jørgen Schmidt]] || [[Torben Hjort]]
|-
|1976 || Jørgen Timm|| [[Jørn Lund]] || Henning Larsen
|-
|1977 || Per Rydicher || [[Hans-Henrik Ørsted]] || Jørgen Timm
|-
|1978 || [[Hans-Henrik Ørsted]] || [[Jørgen Vagn Pedersen]] || Per Sandahl
|-
|1979 ||Per Sandahl || [[Jørgen Vagn Pedersen]] || Lars Udby
|-
|1980 || [[Hans-Henrik Ørsted]] || [[Per Kjærsgaard]] || [[Michael Marcussen]]
|-
|1981 || [[Michael Marcussen]] || Henning Larsen || [[Jørgen Vagn Pedersen]]
|-
|1982 || Per Sandahl || [[Jesper Worre]] || [[Jørgen Vagn Pedersen]]
|-
|1983 || [[Jørgen Vagn Pedersen]] || [[Michael Marcussen]] || Henning Larsen
|-
|1984 || [[Jørgen Vagn Pedersen]] || [[Michael Marcussen]] || [[Jesper Skibby]]
|-
|1985 || [[Jesper Skibby]] || Tom Dalkvist || [[Alex Pedersen]]
|-
|1986 || [[René W. Andersen]] || Tom Dalkvist || [[Alex Pedersen]]
|-
|1987 || [[Peter Meinert]] || [[Claus Michael Møller]] || Tom Dalkvist
|-
|1988 || [[Peter Meinert]] || Michael Guldhammer || Tommy Nielsen
|-
|1989 || [[Peter Meinert]] || Peter Clausen || Tom Dalkvist
|-
|1990 || [[Brian Holm]] || [[Søren Lilholt]] || [[Alex Pedersen]]
|-
|1991 || [[Claus Michael Møller]] || [[Jan Bo Petersen]] || Michael Guldhammer
|-
|1992 || [[Jørgen Bligaard]] || [[Jørgen Bo Petersen]] || [[Jan Bo Petersen]]
|-
|1993 || [[Claus Michael Møller]] || [[Jens Knudsen]] || [[Alex Pedersen]]
|-
|1994 || [[Jan Bo Petersen]] || [[Henrik Jacobsen]] || Tom Dalkvist
|-
|1995 || [[Jan Bo Petersen]] || [[Michael Steen Nielsen]] || [[Jimmi Madsen]]
|-
|1996 || [[Bjarne Riis]] || [[Jan Bo Petersen]] || [[Michael Blaudzun]]
|-
|1997 || [[Michael Sandstød]] || [[Bjarne Riis]] || [[Peter Meinert Nielsen]]
|-
|1998 || [[Michael Sandstød]] || [[Peter Meinert Nielsen]] || [[Michael Steen Nielsen]]
|-
|1999 || [[Michael Sandstød]] || [[Jesper Skibby]] || [[Michael Steen Nielsen]]
|-
| 2000 || [[Michael Sandstød]] || [[Michael Blaudzun]] || [[Bekim Christensen]] 
|-
| 2001 || [[Michael Blaudzun]] || [[Jørgen Bo Petersen]] || [[Bjarke Nielsen]] 
|-
| 2002 || [[Michael Sandstød]] || [[Lennie Kristensen]] || [[Michael Blaudzun]] 
|-
| 2003 || [[Michael Blaudzun]] ||  [[Jørgen Bo Petersen]] || [[Brian Vandborg]] 
|-
| 2004 || [[Michael Sandstød]] || [[Frank Høj]] || [[Brian Vandborg]] 
|-
| 2005 || [[Michael Blaudzun]] || [[Brian Vandborg]] || [[Lars Bak]] 
|-
| 2006 || [[Brian Vandborg]] || [[Jacob Moe Rasmussen]] || [[Allan Johansen]] 
|-
| 2007 || [[Lars Bak]] || [[Brian Vandborg]] || [[Jacob Kollerup]]
|-
| 2008 || [[Lars Bak]] || [[Frank Høj]] || [[Michael Blaudzun]]
|-
| 2009 || [[Lars Bak]] || [[Alex Rasmussen]] || [[Jakob Fuglsang]]
   
     """
        self.palmaresParsing()


    def palmaresParsing(self):
        # parsing of the raw input
        tableofRow = self.inputstr.split("|-")
        column_of_winner = 1
        table_of_winners = [[0 for x in range(4)] for y in range(len(tableofRow) - 1)]
    
        for ii in range(0, len(tableofRow) - 1):  # range(len(tableofRow))
            tableofCell = {}
            tableofCell = tableofRow[1 + ii].split("||")
            # get the year
            tempforyear = tableofCell[0].split("|")
            table_of_winners[ii][0] = int(tempforyear[1])  # link[0]
            # get first winner
            for jj in range(column_of_winner, column_of_winner + 3):
                linksplit1 = tableofCell[jj].split("[[")
                
                if len(linksplit1)==1:
                    t = linksplit1[0]
                else:
                    link = linksplit1[1].split("]]")
                    t = link[0]

                if len(t.split("|"))==1:
                   t2=t
                else:
                   t2=t.split("|")[1]
                   
                s=Search(t2)
                i=s.rider(None,None)    
                
                if i not in ["Q0","Q1"]:
                    table_of_winners[ii][jj - column_of_winner + 1]=i

        self.table_of_winners= table_of_winners
    
    def main(self):
        for ii in range(len(self.table_of_winners)):  # range(len(table_of_winners))
            year = self.table_of_winners[ii][0]
            s=Search(self.base_str+' ' +  str(year))
            present_id = s.simple()

            if (present_id == u'Q0'):
                print(self.base_str+' ' +  str(year)  + ' not present')
            elif (present_id == u'Q1'):
                print(self.base_str+' ' +  str(year)  + ' present several times')
            else:  # good
                print(present_id)
                race = Race(id=present_id)
                if self.table_of_winners[ii][1]!=0:
                    race.add_winner(self.table_of_winners[ii][1], 1, 0)
                if self.table_of_winners[ii][2]!=0:
                    race.add_winner(self.table_of_winners[ii][2], 2, 0)
                if self.table_of_winners[ii][3]!=0:     
                    race.add_winner(self.table_of_winners[ii][3], 3, 0)

'''                
    def wikidataelementAnalyser(pywikibot, site, repo, table_of_winners):
        # look for riders not created
        counter = 0
        counterrepeat = 0
        table_of_winnersOut = table_of_winners
        exception_table = exception.listOfException()
    
        for ii in range(len(table_of_winners)):
            for jj in range(1, 4):
                Idtemp = search_item(
                    pywikibot, site, table_of_winners[ii][jj])
                if (Idtemp == u'Q0'):  # no previous or several
                    print(table_of_winners[ii][jj] + ' not found')
                    counter = counter + 1
                elif (Idtemp == u'Q1'):
                    # list of exceptions
                    exceptionfound = 0
                    for ll in range(1, len(exception_table)):
                        if table_of_winners[ii][jj] == exception_table[ll][0]:
                            table_of_winnersOut[ii][jj] = exception_table[ll][1]
                            exceptionfound = 1
                    if exceptionfound == 0:
                        print(table_of_winners[ii][jj])
                        print(table_of_winners[ii][jj] + ' found several times')
                        counterrepeat += 1
                else:
                    table_of_winnersOut[ii][jj] = Idtemp

        if counter == 0 and counterrepeat == 0:
            print('All riders found!!')
        elif counterrepeat == 0:
            print(str(counter) + ' riders not found')
        else:
            print(str(counterrepeat) + ' riders found several times')
    
        return counter, counterrepeat, table_of_winnersOut            
                
    # inputstr=input()
    table_of_winners = palmaresParsing(inputstr)
    # print(table_of_winners)
    numberofabsentriders, counterrepeat, table_of_winnersOut = wikidataelementAnalyser(
        pywikibot, site, repo, table_of_winners)

    if numberofabsentriders == 0 and test == 0 and counterrepeat == 0:
        palmaresFilling(
            pywikibot,
            site,
            repo,
            table_of_winnersOut,
            id_championship)
'''     