# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:59:59 2019

@author: aaaaa
"""

import pandas as pd
stock='2002'
 # 要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock 
getdata=pd.read_html(url,encoding='big5',header=0)
