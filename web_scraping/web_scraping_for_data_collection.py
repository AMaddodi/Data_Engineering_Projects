# Import
import time
import datetime
import requests
import smtplib
import datetime
import csv

from bs4 import BeautifulSoup

def check_price():
    url = 'https://www.amazon.co.uk/Apple-AirPods-Pro-2nd-generation/dp/B0BDJ37NF5?ref_=Oct_DLandingS_D_ceaf11f2_0'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    
    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()
    
    title = title.strip()
    price = price.strip()
    price = price.replace('\n','')[31:37]
    
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title,price,today]
    
    with open('AmazonWebDataSet.csv', 'a+', newline='', encoding ='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return

# Connect to website
url = 'https://www.amazon.co.uk/Apple-AirPods-Pro-2nd-generation/dp/B0BDJ37NF5?ref_=Oct_DLandingS_D_ceaf11f2_0'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()

title = title.strip()
title = title.rstrip()
price = price.strip()
price = price.replace('\n','')[31:37]

today = datetime.date.today()

header = ['Title', 'Price', 'Date']
data = [title,price,today]

with open('AmazonWebDataSet.csv', 'w', newline='', encoding ='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

while(True):
    check_price()
    time.sleep(5)

