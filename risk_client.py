# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 05:20:15 2018

@author: Neil
"""
import bravado
from shutil import copyfile
import bitmex


def updatePositions(client, btc_today_price,balance_btc):
    rr = client.Position.Position_get().result()
    balance = balance_btc

    real_position = [["XBTUSD", int(balance * btc_today_price), abs(int(balance * btc_today_price)), balance],
                     ["ETHUSD", 0, 0, 0]
                     ]

    print(real_position)
    symbols = ["XBTUSD", "ETHUSD"]
    for p in rr[0]:
        if p["symbol"] == "XBTUSD":

            real_position[0][1] = real_position[0][1] - p["foreignNotional"]
            real_position[0][2] = real_position[0][2] + p["currentQty"]
            real_position[0][3] = real_position[0][3] + p["homeNotional"]
        elif p["symbol"] == "ETHUSD":
            real_position[1][1] = real_position[1][1] - p["foreignNotional"]
            real_position[1][2] = real_position[1][2] + p["currentQty"]
            real_position[1][3] = real_position[1][3] + p["homeNotional"]
        else:
            symbols.append(p["symbol"])
            real_position.append([p["symbol"], -p["foreignNotional"], p["currentQty"],
                                  p["homeNotional"]])
    return real_position, symbols



idd="h21fGYIqg1PoTHXH9Q6tSKh6"
keyd="729O0LE0aPLiMolkEgcg_7qwI3fsIOruhGwcC3PIJdxsC6Tk"
client=bitmex.bitmex(test=False, api_key=idd, api_secret=keyd)




balance_btc=client.User.User_getMargin().result()[0]["marginBalance"]/100000000#-self.cran
ob=client.OrderBook.OrderBook_getL2(symbol="XBTUSD", depth=1).result()
ob_eth=client.OrderBook.OrderBook_getL2(symbol="ETHUSD", depth=1).result()
BTC_price=(ob[0][0]["price"]+ob[0][1]["price"])/2
all_positions,symbols=updatePositions(client,BTC_price,balance_btc)
ETH_price=(ob_eth[0][0]["price"]+ob_eth[0][1]["price"])/2
position_future_eth=all_positions[symbols.index("ETHM21")][2]*ETH_price
#Balance_in_BTC for the Fixed Rate 25/06 by FTR
print("Balance in btc")
print(balance_btc)
print("Balance in USD")
print(int(balance_btc*BTC_price))
print("Collateralization %")
print(int((balance_btc*BTC_price)/position_future_eth*100)/100)

