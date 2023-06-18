import urllib.request
import re
import csv

class ClassReader:

    def __init__(self) -> None:
        with open('subject_to_code_dict.csv') as csv_file:
            reader = csv.reader(csv_file)
            self.subject_to_code = dict(reader)
            self.class_list = []

    def scrape_html(self, major_code):
        ''' creates list of all courses that count to the concentration
        '''
        page = urllib.request.urlopen('https://bulletin.brown.edu/the-college/concentrations/' + major_code)
        txt = str(page.read())
        
        
        fp = open("webtext.txt", "w+")
        fp.write(txt)
        fp.close()
        
        
    def populate_class_list(self, weblist_link):
        
        try:
            fp = open(weblist_link, "r")
            txt = fp.read()
            fp.close()
        except:
            raise("Website html not found!, Try running scrape_html first")
        
        #~ ampersand capture might be incorrect, kinda scuffed
        class_code = re.findall(r'\b\w[A-Z]{3}\s\w[0-9A-Z]{3,4}\b|\borclass\b|class="blockindent">&amp', txt)
        class_code_clean = [class_code[0]]
        
        
        for i in class_code:
            if class_code_clean[-1] != i:
                class_code_clean.append(i)
                
        self.class_list = class_code_clean
        
        print(self.class_list)
        
if __name__ == "__main__":
    CR = ClassReader()
    CR.scrape_html(CR.subject_to_code["Computer Science"])
    CR.populate_class_list("webtext.txt")
    

