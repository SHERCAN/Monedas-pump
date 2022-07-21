# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:40:29 2021

@author: Yesid Farfan
Codigo media movil volumen
macd precio
"""

import numpy, multiprocessing
from requests import post,get
import MIAPI1TOMA, datetime
import MIAPI2TOMA
import MIAPI3TOMA
import MIAPI4TOMA
from binance.client import Client
from talib import EMA

varia=[]
pares = []
mul_vol = 4
base_gap=1627848000000
efi=0.0
# bot = TeleBot('5022330876:AAG6pc1gL4pRgDjluE4pgnf3wvLwMIwhjTg')  # rifa navidad
def send_msg(text):
    token = '5022330876:AAG6pc1gL4pRgDjluE4pgnf3wvLwMIwhjTg'
    chat_id = "-608210583"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    try:
        get(url_req)
    except:
        pass
def compar(x, symbol, klines):
    '''
    total:=(high-low)
    alcista:=(close-low)
    bajista:=(high-close)
    yesfi:=abs(volume*(alcista-bajista)/total)
    '''
    global efi
    try:
        yfi=abs(float(klines[5])*((float(klines[4])-float(klines[3]))-(float(klines[2])-float(klines[4])))/
    (float(klines[2])-float(klines[3])))
    except:
        try:
            yfi=varia[x][-1]
        except:
            yfi=0.0
    varia[x].append(yfi)
    varianp=numpy.array(varia[x])
    varian = EMA(varianp, timeperiod=30)
    try:
        if yfi/6>varian:
            send_msg(symbol)    
    except:
        pass

def toma(a,b,e,active):
    client = Client(a, b)
    tomas = ['noexiste',MIAPI1TOMA.t, MIAPI2TOMA.t, MIAPI3TOMA.t, MIAPI4TOMA.t]
    t = tomas[e]
    llaves=list(t.keys())
    for i in llaves:
        paresupdate=(i)
        pares.append(paresupdate)
        varia.append([] * 1)
    for i in range(len(pares)):
        klines = client.get_klines(symbol=pares[i], interval=Client.KLINE_INTERVAL_1MINUTE, limit = 35)
        for e in range(len(klines)-1):
            compar(i, pares[i], klines[e])
    print('Go '+str(e)) 

    while active.value:
        
        if str(datetime.datetime.now().strftime("%S")) == str("03"):
            for i in range(len(pares)):           
                try:
                    klines = client.get_klines(symbol=pares[i], interval=Client.KLINE_INTERVAL_1MINUTE, limit = 5)
                except Exception as err:
                    print('Error',err)
                    pass
                compar(i, pares[i], klines[-2])
                
    print('No se registran mas entradas ha sido cancelado',active.value)
    raise SystemExit
                  
