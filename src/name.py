import pywikibot

def concaten(names_table,ii):
    '''
    Concatenate first and last name
    '''
    start=names_table[ii]
    for kk in range(ii+1,len(names_table)):
        start=start+" " + names_table[kk]
    return start

class Name():
    def __init__(self, name: str):
        '''
        Name, of team, rider,... corrected
        '''
        self.name = name or ""
        self.name_cor = name or ""
        self.correct_name()
        self.sortkey = self.name_cor
        self.site = pywikibot.Site("wikidata", "wikidata")
        self.repo = self.site.data_repository()
        
    def correct_name(self):
        self.name_cor = self.name_cor.lower()
        self.supprime_accent()

    def supprime_accent(self):
        """ 
        Remove the accents
        """
        ligne = self.name_cor
        accents = {'a': ['à', 'ã', 'á', 'â', 'ä'],
                   'e': ['é', 'è', 'ê', 'ë','ė'],
                   'i': ['î', 'ï'],
                   'u': ['ù', 'ü', 'û','ů'],
                   'o': ['ô', 'ö','ó','ò'],
                   's': ['š'],
                   'n': ['ñ'],
                   'ss' : ['ß'],
                   'c' : ['č','ć'],
                   'z' : ['ž'],
                   ' ': ["\xa0"]}
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        self.name_cor=ligne 

    def find_start_sortkey(self, start_words):
        '''
        Cut beginning of the name
        '''
        for word in start_words:
            if self.name_cor.find(word)!=-1:
                self.sortkey=self.name_cor[len(word):]
                break
        return self.sortkey

class CyclistName(Name):
     def __init__(self, name:str):
        '''
        Name of a cyclist
        '''
        super().__init__(name)
        self.supprime_esset() #keep the upper
        self.check_and_revert()
        self.supprime_accent()
        
     def supprime_esset(self):
        """
        Remove some special character
        """
        accents = {
                   'SS' : ['ß'], #avoid geßner bug
                   }
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                self.name = self.name.replace(accented_char, char)
        
     def check_and_revert(self): 
        '''
        needs upper to distinguish last from first name   
        so no lower before!
        '''
        while self.name.find("  ")!=-1:
            self.name=self.name.replace("  "," ")
            self.name_cor=self.name
            
        names_table = self.name.split(" ")
        if names_table[0]==names_table[0].upper() and not "." in names_table[0]:
            last_name=names_table[0]
            end_last_name=0
            for ii in range(1,len(names_table)):
                if names_table[ii]==names_table[ii].upper() and not "." in names_table[ii]: #avoid Jr. and W.
                   last_name=last_name+ " " + names_table[ii]
                else:
                   end_last_name=ii
                   break
            last_name=last_name.lower()
       
            first_name=names_table[end_last_name]
            first_name=first_name.lower()
            for ii in range(end_last_name+1,len(names_table)):
                first_name=first_name + " " + names_table[ii].lower()
            
            self.name_cor=first_name + " " + last_name
