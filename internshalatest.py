'''
Google Map Scraper Using Selenium
Code By Nikhil Rathour
17 July, 2022
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import csv
import time
from bs4 import BeautifulSoup as bs



pages = 2

header = ["title", "address", "website", "phone","profiles"]
data = []

        
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://internshala.com/internship/detail/python-development-internship-in-hyderabad-at-zestiot-technologies-private-limited1674450367')

driver.implicitly_wait(5)



close = driver.find_element(By.ID,"no_thanks").click()
# details = driver.find_elements(By.LINK_TEXT, 'View details')

driver.implicitly_wait(5)


def find_elements():
  
       
            driver.implicitly_wait(10)

            try:
                profile = driver.find_element(By.CLASS_NAME,"profile")
                print("Profile: ",profile.text)
                company = driver.find_element(By.CLASS_NAME,"company_name")
                print("company: ",company.text)
                location = driver.find_element(By.ID,"location_names")
                print('Loacation: ', location.text)
                stipend = driver.find_element(By.CLASS_NAME, "stipend")
                print('stipend :', stipend.text)
                website = driver.find_element(By.LINK_TEXT,"Website")
                print('Website: ',website.get_attribute('href'))
   
            # try:
            #     stipend = soup.find('i', class_='')
            #     print('stipend: ',stipend.string)
            # except Exception as e:
            #     print(e)
            # try:
            #     website = soup.find('div', class_='')
            #     print('website: ', website)
            except Exception as e:
                 print(e)
            
        
    
find_elements()