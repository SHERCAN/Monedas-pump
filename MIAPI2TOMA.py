import CLAVES
from json import load
API_KEY = CLAVES.CSENA[0]
API_SECRET = CLAVES.CSENA[1]
with open('mon2.json', 'r') as f:
    t=load(f)
