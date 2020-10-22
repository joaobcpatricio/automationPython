import sys
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
path = os.getenv("FILEPATH")
#username = os.getenv("USERNAME")
#password = os.getenv("PASSWORD")

#path = "/home/coolnoname2/Programming/5Projects/AutomationPython/"
browser = webdriver.Firefox()
browser.get('http://github.com/login')

def create():
    folderName = str(sys.argv[1])
    os.mkdir(path + str(sys.argv[1]))
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]   
    #from browser copy XPath 
    python_button.send_keys('botParrot')
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]    
    python_button.send_keys('Pomares18')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]")[0]   
    python_button.click()
    browser.get('http://github.com/new')
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]    
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_css_selector('button.first-in-line')   
    python_button.submit()
    #browser.quit()

#print("Hello");

if __name__ == "__main__":
    create()