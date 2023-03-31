# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib # it allows you to send emails to yourself

# Connect to Website

URL = 'https://www.amazon.com.tr/Asus-VS197DE-Monit%C3%B6r-18-5-1366x768/dp/B00ANCZ3OS/?_encoding=UTF8&pd_rd_w=9r20S&content-id=amzn1.sym.83b0ef12-e9f0-4bb6-999f-ed6f5bc245f7&pf_rd_p=83b0ef12-e9f0-4bb6-999f-ed6f5bc245f7&pf_rd_r=6MV6EBCXZCZ70EB4A32G&pd_rd_wg=mFo5W&pd_rd_r=c9ce2083-fd1e-4696-b1e5-5a00d8b8e47b&ref_=pd_gw_deals_ml'
# headers is user agent. You need to do this for your computer

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

# getting the data starts here

page = requests.get(URL, headers=headers)

# pulling in the content from the page

soup1 = BeautifulSoup(page.content, "html.parser") # print(soup1)

# upgrade soup1 and better formatting

soup2 = BeautifulSoup(soup1.prettify(), "html.parser") # print(soup2)

# we're gonna pull all product title from soup2

title = soup2.find("span", attrs={"id":'productTitle'}).text.strip()

price = soup2.find("span", attrs={"class":'a-price a-text-normal aok-align-center reinventPriceAccordionT2'}).find("span",attrs = {"class":'a-offscreen'}).text.strip()

print(title)
print(price)

