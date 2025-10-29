import json

class ColorRef():
    empty=(0,0,0)
    water=(86,86,235)
    lava=(255,155,46)

rules_data:dict
with open('data.json','r') as file:
    rules_data=json.load(file)
rules:dict=rules_data.get('rules')
print(rules)