# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:36:32 2019

@author: aaaaa
"""

###############################################################################
#                       股票機器人 Python基礎教學 【判斷式】                      #
###############################################################################

stock_price=100
if not(stock_price > 90):
    print('這支股票漲超過90元了')
else:
    print('這支股票再90元以下')


string='我要發大財'
if '發大' in string :
    print('有')
else:
    print('沒')
    

string=['我','要','發','大財']
if '發' in string :
    print('有')
else:
    print('沒')


ID = 'TMRjhkjk998567'
if ID == 'TMR998660':
    print('登入！')
elif 'TMR' in ID:
    print('TMR會員，但 ID 錯誤！')
else:
    print('會員登入失敗！')
