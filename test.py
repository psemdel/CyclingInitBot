#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:45:48 2019

@author: maxime
"""
import csv
import os

if __name__ == '__main__':
    kk=0
    savetable = [[0 for x in range(10)] for y in range(1000)] 
    with open('Champ.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";", quotechar='|')
        for row in spamreader:
            savetable[kk]=row
            kk=kk+1
            if kk==2:
                print(row[1])