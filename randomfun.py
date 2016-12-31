import requests

from bmp import BitMap, Color
from itertools import product
from random import choice


colors = []
store = []

url = "https://www.random.org/integers"
try:
    req = requests.get(url, params={'num':'256','min':'0','max':'255','col':'3','base':'10','format':'plain','rnd':'new'})
    for r in req.content:
        if r.isdigit():
            store.append(r)
except requests.exceptions.RequestException as e:
    print e


for i in xrange(0, 254*3, 3):
    colors.append(Color(store[i],store[i+1],store[i+2]))

bmp = BitMap(128,128)
for x,y in product(xrange(128),xrange(128)):
    bmp.setPenColor(choice(colors))
    bmp.plotPoint(x,y)

bmp.saveFile("128x128.bmp", compress=False)
