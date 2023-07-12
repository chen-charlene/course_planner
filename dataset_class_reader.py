import urllib.request
import re
import csv
import os
from pathlib import Path

#! realized issue with not all information about classes being available this way, temporarily shelved

class ClassReader:

    def __init__(self) -> None:
        with open('subject_to_code_dict.csv') as csv_file:
            reader = csv.reader(csv_file)
            self.subject_to_code = dict(reader)
            self.class_list = []
            self.distinct_class_set = []


    def scrape_html(self, major_code):
        ''' creates list of all courses that count to the concentration
        '''
        page = urllib.request.urlopen('https://bulletin.brown.edu/the-college/concentrations/' + major_code)
        txt = str(page.read())
        
        
        fp = open("webtext.txt", "w+")
        fp.write(txt)
        fp.close()

    def scrape_course_html(self):
        ''' read and write all class' html into folder
        '''

        path = "course_html"
        if os.path.exists(path) is False:
            os.makedirs(path)

        for course in self.distinct_class_set:
            split_str = course.split()

            page = urllib.request.urlopen('https://bulletin.brown.edu/search/?P=' + split_str[0] + "%20" + split_str[1])
            txt = str(page.read())
        
            course_file_name = split_str[0] + split_str[1] + ".html"
            with open(os.path.join(path, course_file_name), "w") as courseFile:
                courseFile.write(txt)
                courseFile.close()

    def populate_course_prereq(self):
        ''' loops through the subject htmls and writes down the string after prerequisites
        '''
        course_to_prereq_string = {}
        
        for child in Path('course_html').iterdir():
            if child.is_file():
                fp = open(child, 'r')
                txt = fp.read()
                fp.close()

                prereq_string = re.findall(r'Prerequisites*:([^.]+?)\.', txt)
                child_name = child.parts[1].split('.html')
                course_to_prereq_string[child_name[0]] = prereq_string
        print("hi")
        print(course_to_prereq_string)
        

        
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

        #populate distinct class list
        unWantedWords = ["orclass", 'class="blockindent">&amp']
        self.distinct_class_set = set([x for x in class_code_clean if x not in unWantedWords])
        
        
if __name__ == "__main__":
    CR = ClassReader()
    # subject_code = CR.subject_to_code["Computer Science"]
    # CR.scrape_html(subject_code)
    # CR.populate_class_list("webtext.txt")
    # CR.scrape_course_html()
    CR.populate_course_prereq()

    

