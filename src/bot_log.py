# -*- coding: utf-8 -*-

class Log:
    def __init__(self):
        self.txt=""
        
    def concat(self, new):
        print(new) #for local
        self.txt=self.txt+ "\n" + str(new) #write a log that is returned to the site
    
