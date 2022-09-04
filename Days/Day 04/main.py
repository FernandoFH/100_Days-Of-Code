import requests
import json 

## Requesting data from the API
#url = 'https://rickandmortyapi.com/api/character/100'
#r = requests.get(url)
#j = r.json()

# print(j)
#status = j['status']
#print(status)

"""
i = 1

while i < 10:
    url = 'https://rickandmortyapi.com/api/character/' + str(i)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status = j['status']
    print('El personaje {} tiene status {}'.format(name, status))
    i += 1
"""

# Request al primer episodio
url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()

personajes = j['characters']
list_name = list()

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    list_name.append(name)

print (list_name)

