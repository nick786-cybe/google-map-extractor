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

header = [ "Name","Profile", "Website", "Location","Stipend","About","Work"]
data = []
with open('internshala.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(header)
        
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
firstpage = driver.get('https://internshala.com/internships/')

print('hello')
driver.implicitly_wait(5)
links = []


close = driver.find_element(By.ID,"no_thanks").click()
def fetch_links():
    
    total_pages = driver.find_element(By.ID,"total_pages")
    print(total_pages.text)
    totalpage = int(total_pages.text)
    for i in range(200,totalpage):
        print(i)
        link = f'page-{i}/'
        print(link)
        driver.get('https://internshala.com/internships/'+link)

        details = driver.find_elements(By.LINK_TEXT, 'View details')
       
        for i in details:
            links.append(i.get_attribute('href'))
            print(i.get_attribute('href'))

    


def find_elements():
    fetch_links()

    for i in links:
            driver.get(i)
            

            try:
                profile = driver.find_element(By.CLASS_NAME,"profile")
                print("Profile: ",)
                profile = profile.text
            except Exception:
                 profile = ''
            try:
                company = driver.find_element(By.CLASS_NAME,"company_name")
                print("Company: ",company.text)
                company = company.text
            except Exception:
                 company = ''
            try:
                location = driver.find_element(By.ID,"location_names")
                print('Loacation: ', location.text)
                location = location.text
            except Exception:
                 location = ""
            try:
                stipend = driver.find_element(By.CLASS_NAME, "stipend")
                print('Stipend :', stipend.text)
                stipend = stipend.text
            except Exception:
                 stipend = ""
            try:
                Website = driver.find_element(By.LINK_TEXT,"Website")
                print('Website: ',Website.get_attribute('href'))
                website = Website.get_attribute('href')
            except Exception as e:
                 website = ''
            try:
                work = driver.find_elements(By.CLASS_NAME, "text-container")
                
                print('work: ',work[2].text)

            except Exception  as e:
                print(e)
                work = ''
            try:
                about = driver.find_element(By.CLASS_NAME, "about_company_text_container")
                print('about :', about.text)
            except Exception as e:
                 about = ''
            try:
                row = [company, profile, website, location, stipend, about.text,work[2].text]
                with open('internshala.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(row)
            except Exception as e:
                 pass
   
   
    
find_elements()
