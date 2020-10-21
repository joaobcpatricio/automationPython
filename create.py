import sys
import os
from selenium import webdriver

path = "/home/coolnoname2/Programming/5Projects/AutomationPython/"
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

#print("Hello");

if __name__ == "__main__":
    create()