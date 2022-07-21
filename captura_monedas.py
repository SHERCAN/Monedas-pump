# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:46:51 2021

@author: Yesid Farfan
"""
from llaves import *
from binance.spot import Spot as ClienteSpot
from gate_api import ApiClient, Configuration, SpotApi
#gate
key=api_gate['key']
api_secret=api_gate['api_secret']
host_used=api_gate['host']
configu = Configuration(key=key, secret=api_secret, host=host_used)
spot_api = SpotApi(ApiClient(configu))
api_response = spot_api.list_currencies()
#binance spot
cliente = ClienteSpot(api_binance['key'],api_binance['secret'])
respuesta=cliente.coin_info()
lista=list()
for i in api_response:
    for e in respuesta:
        if i.currency==e['coin']:
            break
        if e == respuesta[-1] and not i.currency.find('_')>-1 and not i.currency:
            lista.append(i.currency)
    
'''
#binance
cliente = Client(config.api_binance['key'],config.api_binance['secret'])
info = client.get_symbol_info('BNBBTC')
'''


