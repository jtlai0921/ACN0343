# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:34:47 2018

@author: aaaaa
"""
import datetime 
import time
###############################################################################
#                       股票機器人 Python基礎教學 【時間】                      #
###############################################################################

##### datetime #####
now = datetime.datetime.now() #現在時間（到毫秒）
now #展示目前時間
type(now) #顯示資料格式

##### 現在時間 #####
datetime.datetime.now().date() #現在時間（到天）
datetime.date.today() #現在時間（到天）

##### 明天 #####
datetime.date.today() + datetime.timedelta(days=1)

##### 時間差 #####
(datetime.datetime.now() - datetime.datetime(2015,1,13,12,0,0)).total_seconds() #2015年到現在過了幾秒

#####  TimeStamp #####
time.time() #timestamp
time.localtime() #time tuple

##### 轉換 #####

#datetime轉字串
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#字串轉datetime
datetime.datetime.strptime("2018-11-07 13:11:43", "%Y-%m-%d %H:%M:%S")

#datetime轉TimeStamp
datetime.datetime.now().timetuple()

#TimeStamp轉datetime
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())
