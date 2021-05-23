# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
#import datetime
#import time

link = 'https://www.cbr.ru/eng/currency_base/daily/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


fullPage = requests.get(link, headers=headers)
soup = BeautifulSoup(fullPage.content, "html.parser")
zero = soup.findAll("td")
print('USD ' + zero[54].text) #USD
print('EUR ' + zero[59].text) #EUR
print('BYN ' + zero[19].text) #BYN
#time = str(datetime.datetime.today())
#string = f"BTC Time: {time[:-7]}\t Cost: {cost}\n"
#print(string)
#/html/body/main/div/div/div/div[3]/div/table/tbody/tr[12]/td[5]