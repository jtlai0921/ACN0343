# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:58:46 2019

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
#找到table這個標籤
soup.find('table') #只找到一個
soup.find_all('table') #找到網頁內所有的table
soup.find_all('table', {'border':'2'}) #特別指定'border':'2'
