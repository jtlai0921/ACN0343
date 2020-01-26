# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:01 2019

@author: aaaaa
"""

from pymongo import MongoClient
import datetime
import urllib.parse


# Authentication Database認證資料庫
Authdb='資料庫名稱'

    client = MongoClient('你的連接指令')
    db = client[Authdb]
# 切換資料庫
dbname='資料庫名稱'
db = client[dbname]

# 輸入想搜尋的collection
collection_name = 'fountion'
# 注意下方的 coll 只是我自己命名
collect = db[collection_name]

collect.insert({"stock":"2330" ,
                    "data": 'care_stock',
                    "bs": ">",
                    "price": float(10),
                    "date_info": datetime.datetime.utcnow()
                    })
