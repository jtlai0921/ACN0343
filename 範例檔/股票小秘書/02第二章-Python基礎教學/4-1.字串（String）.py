# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:34:47 2018

@author: aaaaa
"""

###############################################################################
#                       股票機器人 Python基礎教學 【字串】                      #
###############################################################################

##### 字串設定 #####
anyname = "這個是字串It's str."
anyname

##### 字串加總 #####
word1='中華'
word2='鋼鐵'
word3=word1+word2
word3

interger=2002
word4=word3+interger
word4=word3+str(interger)

##### 字串長度計算 #####
count='我想要買中鋼，在23元的時候'
len(count)

##### 取字串 #####
word5='我覺得現在中鋼好像很便宜，可以下手'
word5[1:3]
word5[1:]
word5[:3]
word5[:-3]

###### 刪除前後空白 ######
word7 = ' hello apple '
word7.strip()

###### 刪除所有空白 ######
word6 = ' hello apple '
word6.replace(" ","")
