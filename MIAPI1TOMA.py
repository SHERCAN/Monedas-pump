import CLAVES
from json import load
API_KEY = CLAVES.CWICR[0]
API_SECRET = CLAVES.CWICR[1]
with open('mon1.json', 'r') as f:
    t=load(f)

