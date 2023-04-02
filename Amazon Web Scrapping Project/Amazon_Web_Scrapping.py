#import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import smtplib # it allows you to send emails to yourself
##Connect to Website
URL = 'https://www.amazon.com.tr/Asus-VS197DE-Monit%C3%B6r-18-5-1366x768/dp/B00ANCZ3OS/?_encoding=UTF8&pd_rd_w=9r20S&content-id=amzn1.sym.83b0ef12-e9f0-4bb6-999f-ed6f5bc245f7&pf_rd_p=83b0ef12-e9f0-4bb6-999f-ed6f5bc245f7&pf_rd_r=6MV6EBCXZCZ70EB4A32G&pd_rd_wg=mFo5W&pd_rd_r=c9ce2083-fd1e-4696-b1e5-5a00d8b8e47b&ref_=pd_gw_deals_ml'
##headers is user agent. You need to do this for your computer
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
##getting the data starts here
page = requests.get(URL, headers=headers)
##pulling in the content from the page
soup1 = BeautifulSoup(page.content, "html.parser")
##upgrade soup1 and better formatting
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
##we're gonna pull all product title from soup2
title = soup2.find("span", attrs={"id":'productTitle'}).text.strip()
price = soup2.find("span", attrs={"class":'a-price a-text-normal aok-align-center reinventPriceAccordionT2'}).find("span",attrs = {"class":'a-offscreen'}).text.strip()
today = datetime.date.today()
#print(title)
#print(price)
#print(today)
#Additions
"""
#to Clean TL from price
price = price.strip()[:-2] 
today = datetime.date.today()
print(title)
print(price)
print(today)
"""
## w - means write
## newline = when we insert the data it doesn't have a space in between each csv
"""
header = ['Title', 'Price', 'Date']
data = [title, price, today]
with open('AmazonWebScrapperDataset.csv', 'w', newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
"""
## Now we're appending data to csv
## a+ - append the data
"""
with open('AmazonWebScrapperDataset.csv', 'a+', newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
"""
# this functions imports data
def check_price():
    URL = 'https://www.amazon.com.tr/Apple-iPhone-14-Pro-512/dp/B0BDJDCMM8/?_encoding=UTF8&pd_rd_w=JChqW&content-id=amzn1.sym.f52080c4-fe7e-4ff6-b933-259f05962808&pf_rd_p=f52080c4-fe7e-4ff6-b933-259f05962808&pf_rd_r=5F30RARZ578MC89NACNF&pd_rd_wg=OPYN4&pd_rd_r=7e6a1487-ab6b-4747-ba65-4aee9cbeb15c&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser") # print(soup1)
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser") # print(soup2)
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span",attrs = {"class":'a-price-whole'}).get_text()
    title = title.strip()
    price = price.strip()[:-2]
    import datetime
    today = datetime.date.today()
    import csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    with open('AmazonWebScrapperDataset.csv', 'a+', newline = '',encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Checks everyday
while(True):
    check_price()
    time.sleep(86400)

# You will have a timeseries in the end
import pandas as pd
df = pd.read_csv(r'C:\Users\Eser\Desktop\Python\Amazon Web Scrapping\AmazonWebScrapperDataset.csv')
print(df)
