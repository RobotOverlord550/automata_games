import json

rules_data:dict
with open('data/data.json','r') as file:
    rules_data=json.load(file)
rules:dict=rules_data.get('rules')
print(rules)