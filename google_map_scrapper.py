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
from geopy.geocoders import Nominatim


Keyword= input("Enter Keyword: ")
city = input('Enter city name: ')
search = (Keyword + ' in ' + city)
pages = 2

header = ['Title', 'Address', 'Latitude','Longitude', 'Short_description', 'Description', 'Website', 'Phone', 'Profiles']
data = []

        
options = webdriver.ChromeOptions()
# options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')

driver.implicitly_wait(2)
driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
more = driver.find_element(By.TAG_NAME,"g-more-link")
more_btn = more.find_element(By.TAG_NAME,"a")
more_btn.click()
time.sleep(10)
def fetch():
    for page in range(2, pages+1):
        elements = driver.find_elements(By.CSS_SELECTOR, 'div#search a[class="vwVdIc wzN8Ac rllt__link a-no-hover-decoration"')
        counter = 1

        for element in elements:
            data_cid = element.get_attribute('data-cid')
            element.click()
            print('item click... 5 seconds...')
            time.sleep(3)

            html = driver.page_source
            soup = bs(html,'html.parser')

            try:
                title = soup.find('div', class_='SPZz6b')
                print('title: ', title.string)
            except Exception as e:
                print(e)

            #address
            try:
                temp_obj = soup.find('span', class_='LrzXr')
                address = temp_obj.string
                try:
                    geolocator = Nominatim(user_agent="google details")
                    location = geolocator.geocode(address)
                    print((location.latitude, location.longitude))
                    latitude = location.latitude
                    longitude = location.longitude
                except Exception:
                    latitude = ''
                    longitude = ''
            except Exception:
                address =""
            print ('address: ',address[0:8],'..')

            #Short description
            try:
                Short_description = soup.find('span', class_="Yy0acb")
                print('Short Description: ',Short_description.text)
                Short_description = Short_description.text
            except Exception:
                Short_description = ''

            #Long description
            try:
                Description = driver.find_element(By.XPATH,"//div[contains(@jscontroller, 'EqEl2e')]")
                Description = Description.get_attribute('data-long-text')
                print('Descriptions: ',Description)
            except Exception:
                Description = ''

            #website
            try:
                temp_obj = soup.find('a', class_='dHS6jb', href=True)
                if len(temp_obj['href']) > 0:
                    website = (temp_obj['href'])
            except Exception:
                website =""

            print('website:', website)

            #phone
            try:
                temp_obj = soup.find('span', class_='zdqRlf')
                print('phone:', temp_obj.string)
                phone = temp_obj.string
            except Exception :
                phone = ""

            # social profiles
            profiles=""
            for s_count in range (1, 6):
                try:
                    temp_obj = driver.find_element(By.CSS_SELECTOR, 'div[data-attrid="kc:/common/topic:social media presence"] div:nth-child(2) > div:nth-child(' + str(s_count) + ') > div > g-link > a')
                    if len(temp_obj.get_attribute('href')) > 0:
                        profiles_str = temp_obj.get_attribute('href')
                except Exception:
                    profiles_str = ""
                    break
                profiles += "<br/>" + profiles_str
            print('profiles: ', profiles)

            try:
                div_element = driver.find_elements(By.CLASS_NAME,"vwrQge")
                try:
                    div_element = div_element[1] 
                except IndexError:
                    div_element = div_element[0]
                # Extract the style attribute value
                style_attr = div_element.get_attribute("style")

                # Extract the image URL from the style attribute value
                image_url = style_attr.split("(")[1].split(")")[0]
                print(image_url)
            except Exception as e:
                image_url = 0


            try:
                logo = driver.find_element(By.ID,'lu-plcst-ml')
                logo = logo.get_attribute('src')
                print('Logo: ',logo)
            except Exception as e:
                logo = ''




            try:
            #print(counter, data_cid, title.text, address, website, phone,rating,reviews,image,category,timing,description,profiles)
                row = [title.string, address, latitude,longitude, Short_description, Description, website, phone,profiles,image_url,logo]
                with open('toronto_restaurants.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file) 
                    writer.writerow(row)
                    
             
            except Exception as e:
                print(e)
                 
            

        try:
            
            page_button = driver.find_element(By.ID,'pnnext')
            #page_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Page ' + str(page) + '"]')
            page_button.click()
            print('page click... 10 seconds...')
            time.sleep(10)
        except Exception:
            break
        fetch()
        
fetch()

