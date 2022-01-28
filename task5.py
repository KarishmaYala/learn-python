import json

f = open('Nested-JSON-1.json')

data = json.load(f)

topping = input('Enter topping: ')

for rec in data:
    if rec['type'] == 'donut':
        for top in rec['topping']:
            if top['type'] == topping:
                print(rec['name'])
            else:
                print('No Matches Found')