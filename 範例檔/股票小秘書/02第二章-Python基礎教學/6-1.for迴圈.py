# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:34:47 2018

@author: aaaaa
"""
###############################################################################
#                       股票機器人 Python基礎教學 【for迴圈】                      #
###############################################################################

##### 吐出0~4 #####
for i in range(0,5):
    print(i)
    
##### 倒過來吐 #####
for i in range(5,0,-1):
    print(i)
 
##### 計算從1加到10 #####
count=0 #拿來儲存答案
for i in range(1,11):
    count = count + i
print(count)
    
##### 吐出字串 #####
string='2008年金融海嘯'
for i in string:
    print(i)
    
##### 吐出陣列 #####
string=['2008','年','金融','海嘯']
for i in string:
    print(i)
    
##### 巢狀迴圈1 #####
for i in range(0,5): #第一層
    for j in range(0,10): #第二層
        print('現在I是： '+ str(i) + '  J是：　' + str(j))
        
##### 巢狀迴圈2 #####
string=[['2008','年','金融','海嘯'],
        ['導致','許多'],
        ['人','的資產'],
        ['一夕間','歸零']]
for i in string: #第一層
    for j in i: #第二層
        print(j)
    print("-----------第一層結束-----------")