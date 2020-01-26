# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:01:40 2019

@author: aaaaa
"""


import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


### 先與網站請求抓到法人資料 ###
url = 'http://www.twse.com.tw/fund/BFI82U'
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, "html.parser")
getjson=json.loads(soup.text)

iilist=[]
### 判斷請求是否成功 ###
if getjson['stat'] != '很抱歉，沒有符合條件的資料!': #如果抓不到資料會顯示這個
    iilist=getjson['data'][4][1:] #直接取到三大法人最後加總的資料
 
### 判斷是否為空值 ###
if len(iilist) != 0: 
    ### 顯示結果 ###
    print('日期 ＝ ' + getjson['title'])
    print('三大法人合計買進 ＝ ' + str(iilist[0]))
    print('三大法人合計賣出 ＝ ' + str(iilist[1]))
    print('三大法人合計相差 ＝ ' + str(iilist[2]))
else:
    print('請求失敗，請檢查您的股票代號')
