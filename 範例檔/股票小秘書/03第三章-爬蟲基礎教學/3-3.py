# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:59:12 2019

@author: aaaaa
"""

import requests
from bs4 import BeautifulSoup
import datetime
import json

stock='2002'
#今天的時間
today = datetime.date.today()
#請求的網站
url = 'http://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stock + '&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'
#開始請求
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, "html.parser")
#將扒下來的文字轉成Json
getjson=json.loads(soup.text)
print(getjson)
