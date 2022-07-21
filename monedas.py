import MIAPICTOMA
#from binance_f import RequestClient
from binance.client import Client
from binance.enums import *
from math import log10
from json import dump
import time
client = Client(MIAPICTOMA.API_KEY, MIAPICTOMA.API_SECRET)
#RequestClient(MIAPICTOMA.API_KEY, MIAPICTOMA.API_SECRET)
salida=[]
verme={}
monedas={}
aux={}
info=client.get_exchange_info()['symbols']
exc=[]
listexcl = { 'EURUSDT','SUSDUSDT','USDCUSDT','BUSDUSDT',
'PAXUSDT','TUSDUSDT','DAIUSDT','AUDUSDT','USDPUSDT',
'USDCBUSD','TUSDBSD','EURBUSD','AUDBUSD','TUSDBUSD','USDPBUSD','USTCBUSD'}
for i in range(len(info)):
     verme=info[i]
     if (verme['symbol'].endswith('USDT') or verme['symbol'].endswith('BUSD')) and verme['status']=="TRADING" and verme['symbol'] not in listexcl:
        if (not verme['symbol'].rsplit('USDT')[0].endswith('UP') and not verme['symbol'].rsplit('USDT')[0].endswith('DOWN') and
        not verme['symbol'].rsplit('BUSD')[0].endswith('UP') and not verme['symbol'].rsplit('BUSD')[0].endswith('DOWN')):
            sol=verme['symbol']
            luna=str(int(abs(log10(float(verme['filters'][2]['minQty'])))))
            marte=str(int(abs(log10(float(verme['filters'][0]['minPrice'])))))#minprice
            aux={sol:{'qty':luna,'price':marte}}
            monedas.update(aux)
for e in sorted(monedas.keys(), reverse=True):
    if e.endswith('USDT'):
        simbolo=e.rsplit('USDT')
        for i in sorted(monedas.keys(), reverse=True):
            if i.endswith('BUSD'):
                simbolo1=i.rsplit('BUSD')
                if simbolo==simbolo1:
                    monedas.pop(i)
with open('monedas.json', 'w') as f:
     dump(monedas, f)
x=len(monedas)/4
x=float(x)
aux1={}
for j in range(3):
     txt='mon'+str(j+1)+'.json'
     llaves=list(monedas.keys())
     for i in range(round(x)):
          llave=llaves[i]
          carga=monedas[llave]
          aux1.update({llaves[i]:carga})
          monedas.pop(llaves[i])
     lista = aux1
     with open(txt, 'a') as f:
          dump(aux1, f)
     aux1.clear()

llaves=list(monedas.keys())
for i in range(len(monedas)):
     aux1.update({llaves[i]:monedas[llaves[i]]})
     monedas.pop(llaves[i])
lista = aux1

with open("mon4.json", 'a') as f:
     dump(aux1, f)
print('Finished successfully')