from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from re import search
import warnings

class scrape_CAB:
    def __init__(self):
        self.driver = None
        self.selenium_setup()
        
    #@ Sets up driver using selenium to be callable by other functions-
    def selenium_setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        # chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("https://cab.brown.edu")
        assert "Brown" in self.driver.title

        #~ Course Term to search 
        term_list = Select(self.driver.find_element(By.ID, "crit-srcdb"))
        for term_option in term_list.options:
            
            #? Looks for the term "Any Term" in term drop down, may be prone to breaking
            any_term = search("Any Term", term_option.text)
            if any_term:
                print("Selected term: " + term_option.text)
                term_list.select_by_visible_text(term_option.text)
                break
            
        if any_term == None:
            warnings.warn("Phrase \"Any Term\" not found in the dropdown. Using default selection. Please open an issue on the github repo")
                
    def search_by_concentration(self, concentration):
        #~ Click on "Courses in Concentration" and extract preqs in list
        conc_button = self.driver.find_element(By.ID, "courses-in-a-conc").click()

        #Waits for new panel to load
        sleep(0.5)
        conc_list_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#programs-select")))
        conc_list = Select(conc_list_element)
        test = conc_list.options
        # for i in test:
        #     print(i.text)
        #~ Select CS-SCB for dev testing
        conc_list.select_by_visible_text(concentration)
        self.driver.find_element(By.ID, "program-search").click()

        #Lets the courses load before trying to select them 
        sleep(2)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".result_link")))
        
        #! need to learn JS to be able to find all matching XPATH entires
        #* also will use same thing to click on the link to scrape the prereq
        courses = self.driver.find_element(By.XPATH, "//a[@class='result__link']//span[@class=\"result__code\"]")
        print(courses.text)

        # for i in Select(courses).options:
        #     print(i.text)

    #*put search by words into own func
    def search_by_course(self, course):
        #~ input a course and will search cab@brown for the specficied course prereqs.
        print("This is just here to prevent indent error")
        # elem = self.driver.find_element(By.ID, "crit-keyword") 




if __name__ == "__main__":
    CAB = scrape_CAB()
    CAB.search_by_concentration("Computer Science - SCB")
    # Prevents Chrome from getting garbage collected
    sleep(10)
    # while True:
    #     pass