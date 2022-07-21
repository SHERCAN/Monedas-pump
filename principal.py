"""
Created on Sun Feb 28 18:26:43 2021

@author: Yesid Farfan

Crear instancias de toma
"""
from multiprocessing import Process,Value
import MIAPI1TOMA,MIAPICTOMA
import MIAPI2TOMA
import MIAPI3TOMA
import MIAPI4TOMA
import TOMA1p

if __name__== '__main__':
    
    stringc=[MIAPICTOMA.API_KEY,MIAPICTOMA.API_SECRET]
    string=[['sol','luna'],[MIAPI1TOMA.API_KEY,MIAPI1TOMA.API_SECRET],[MIAPI2TOMA.API_KEY,MIAPI2TOMA.API_SECRET]
           ,[MIAPI3TOMA.API_KEY,MIAPI3TOMA.API_SECRET],[MIAPI4TOMA.API_KEY,MIAPI4TOMA.API_SECRET]]
    act = Value("b",False, lock=False)
    act.value= True
    for i in range(1,5):#len(string)):
        print("Entro",i)
        gata = Process(target = TOMA1p.toma, args =(string[i][0],string[i][1],i,act,))
        gata.start()
    while True:
      acti=input('Ingresa "stop" para cancelar')
      if acti.upper() == 'STOP':
        act.value = False
        print('Se cancelo')
        break