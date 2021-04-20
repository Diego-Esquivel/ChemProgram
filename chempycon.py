import json

f = open('chem.json')

w = json.load(f)
#w = json.loads(w)

e = open('Elements.h')

print(w[w["order"][0]]["xpos"])