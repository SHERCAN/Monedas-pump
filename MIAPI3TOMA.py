import CLAVES
from json import load
API_KEY = CLAVES.CYUBI[0]
API_SECRET = CLAVES.CYUBI[1]
with open('mon3.json', 'r') as f:
    t=load(f)
