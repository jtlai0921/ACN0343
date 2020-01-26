# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:48:12 2018

@author: aaaaa
"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import fix_yahoo_finance
import datetime
import talib
import matplotlib
import mpl_finance 
import pylab
import schedule
import time
from bs4 import BeautifulSoup
import requests
import linebot
import urllib.parse
from imgurpython import ImgurClient
from io import StringIO
import json
import flask
import pymongo
import re
