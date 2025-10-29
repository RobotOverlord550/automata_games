import grid
import json

rules_data:dict
with open('data.json','r') as file:
    rules_data=json.load(file)
rules:list=rules_data.get('rules')

colors:dict=rules_data.get('color_ref')
def get_cell_color(element:str)->tuple:
    try:
        return (colors[element][0],colors[element][1],colors[element][2])
    except:
        raise ValueError(f"Excpected an existing element but got {element}")
    
def execute_rules(grid_list:grid.Grid):
    for rule in rules:
        pass