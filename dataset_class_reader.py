import urllib.request
import re
import csv

class ClassReader:

    def __init__(self) -> None:
        with open('subject_to_code_dict.csv') as csv_file:
            reader = csv.reader(csv_file)
            self.subject_to_code = dict(reader)
            self.class_list = []
            self.populate_class_list()

    def populate_class_list(self):
        ''' creates list of all courses that count to the concentration
        '''
        page = urllib.request.urlopen('https://bulletin.brown.edu/the-college/concentrations/comp')
        txt = str(page.read())
        class_code_short = set(re.findall(r'\b\w[A-Z]{3}\s\w[0-9A-Z]{3}\b', txt))
        class_code_long = set(re.findall(r'\b\w[A-Z]{3}\s\w[0-9A-Z]{4}\b', txt))
        self.class_list = class_code_short.union(class_code_long)
    

