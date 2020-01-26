# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:57:17 2019

@author: aaaaa
"""
import requests
from bs4 import BeautifulSoup

stock='2002'
 # 要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock 
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
#找到b這個標籤
getstock= soup.find('b').text #只抓到第一個<b>
print(getstock)

getstock= soup.findAll('b')[1].text #抓到收盤價格
print(getstock)
