import CLAVES
from json import load
API_KEY = CLAVES.API4SANDO[0]
API_SECRET = CLAVES.API4SANDO[1]
with open('mon4.json', 'r') as f:
    t=load(f)
