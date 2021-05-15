# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 05:20:15 2018

@author: Neil
"""
import bravado
from shutil import copyfile
from FonctionsNico import *
from FonctionsAlgo import *
import bitmex
import pandas as pd
import numpy as np
import time
import matplotlib
import os
import pandas as pd
import time


idd="h21fGYIqg1PoTHXH9Q6tSKh6"
keyd="729O0LE0aPLiMolkEgcg_7qwI3fsIOruhGwcC3PIJdxsC6Tk"
client=bitmex.bitmex(test=False, api_key=idd, api_secret=keyd)
balance_btc=client.User.User_getMargin().result()[0]["marginBalance"]/100000000#-self.cran
ob=client.OrderBook.OrderBook_getL2(symbol="XBTUSD", depth=1).result()
ob_eth=client.OrderBook.OrderBook_getL2(symbol="ETHUSD", depth=1).result()
BTC_price=(ob[0][0]["price"]+ob[0][1]["price"])/2
ETH_price=(ob_eth[0][0]["price"]+ob_eth[0][1]["price"])/2
#Balance_in_BTC for the Fixed Rate 25/06 by FTR
print("balance in btc")
print(balance_btc)
print("Balance in USD")
print(int(balance_btc*BTC_price))

