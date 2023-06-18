import urllib.request
import re
import csv

class Reader: 

    def __init__(self):
        ''' Param:
            subject: the subject inputted by the user
        '''
        self.subject_to_code = {}
        self.list_of_subjects = {"Africana Studies","American Studies","Anthropology", "Applied Mathematics",
                                 "Applied Mathematics-Biology","Applied Mathematics-Computer Science","Applied Mathematics-Economics",
                                 "Archaeology and the Ancient World","Architecture","Astronomy","Behavioral Decision Sciences","Biochemistry & Molecular Biology"
                                 ,"Biology","Biomedical Engineering","Biophysics","Business, Entrepreneurship and Organizations","Chemical Physics","Chemistry",
                                 "Classics","Cognitive Neuroscience","Cognitive Science","Comparative Literature","Computational Biology","Computer Science","Computer Science-Economics",
                                 "Contemplative Studies","Critical Native American and Indigenous Studies","Development Studies","Early Modern World","East Asian Studies","Economics",
                                 "Education Studies","Egyptology and Assyriology","Engineering","Engineering and Physics","English","Environmental Studies","Ethnic Studies","French and Francophone Studies"
                                 ,"Gender and Sexuality Studies","Geological Sciences","Geology-Biology","Geology-Chemistry","Geology-Physics/Mathematics","German Studies","Health & Human Biology",
                                 "Hispanic Literatures and Cultures","History","History of Art and Architecture","Independent Concentration","International and Public Affairs","International Relations",
                                 "Italian Studies","Judaic Studies","Latin American and Caribbean Studies","Linguistics","Literary Arts","Mathematics","Mathematics-Computer Science","Mathematics-Economics",
                                 "Medieval Cultures","Middle East Studies","Modern Culture and Media","Music","Neuroscience","Philosophy","Physics","Physics and Philosophy","Political Science","Portuguese and Brazilian Studies",
                                 "Psychology","Public Health","Public Policy","Religious Studies","Science, Technology, and Society","Slavic Studies","Social Analysis and Research","Sociology","South Asian Studies",
                                 "Statistics","Theatre Arts and Performance Studies","Urban Studies","Visual Art"}
        self.populate_stc_dict()

    def populate_stc_dict(self):
        ''' populates the subject to code dictionary
        '''
        for subject in self.list_of_subjects:
             self.find_code(subject)
        
        # anomaly subjects
        self.subject_to_code["Public Health"] = "php"
        self.subject_to_code["Health & Human Biology"] = "hhbi"
        self.subject_to_code["Mathematics-Computer Science"] = "macs"
        self.subject_to_code["Engineering"] = "engn"
        self.subject_to_code["Physics"] = "phys"
        self.subject_to_code["Biochemistry & Molecular Biology"] = "bchm"
        self.subject_to_code["Biology"] = "biol"
        self.subject_to_code["Neuroscience"] = "neur"
        self.subject_to_code["Mathematics-Economics"] = "mtec"
        self.subject_to_code["Economics"] = "econ"
        self.subject_to_code["Mathematics"] = "math"
        self.subject_to_code["Computer Science"] = "comp"

        with open('subject_to_code_dict.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            for key, value in self.subject_to_code.items():
                writer.writerow([key, value])

        print("successfully saved stc dict as csv")



    def find_code(self, subject):
        ''' takes in a str and returns the str in the page
        '''

        page = urllib.request.urlopen('https://bulletin.brown.edu/the-college/concentrations/')
        #subject =  re.search(subject, str(page.read())).group()
        txt = str(page.read())
        subject_code = txt.split(subject)[0][-7:][0:4]
        subject_code = re.sub(r'[\W_]', "", subject_code)
        self.subject_to_code[subject] = subject_code