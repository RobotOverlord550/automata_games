import grid
import json
from vectors import Vector2I

data_dict:dict
with open('data.json','r') as file:
    data_dict=json.load(file)

colors:dict=data_dict.get('color_ref')
def get_cell_color(element:str)->tuple:
    try:
        return (colors[element][0],colors[element][1],colors[element][2])
    except:
        raise ValueError(f"Excpected an existing element but got {element}")
    
moore_translations=[
    Vector2I(-1,-1),Vector2I(0,-1),Vector2I(1,-1),
    Vector2I(-1,0),Vector2I(0,0),Vector2I(1,0),
    Vector2I(-1,1),Vector2I(0,1),Vector2I(1,1)
]

def execute_rules(grid_list:list):
    def get_neighbors(coordinates:Vector2I)->list:
        neighbors:list=[]
        for translation in moore_translations:
            if not translation==Vector2I(0,0):
                translated=coordinates+translation
                try:
                    result=grid_list[translated.x][translated.y]
                    neighbors.append(result)
                except:
                    neighbors.append(' ')
        return neighbors
    
    for x in range(len(grid_list)):
        for y in range(len(grid_list[x])):
            neighbors=get_neighbors(Vector2I(x,y))
            ocuppied_count=0
            for n in range(len(neighbors)):
                neighbor=neighbors[n]
                if neighbor=="#":
                    ocuppied_count+=1
            if grid_list[x][y]==' ':
                if ocuppied_count==3:
                    grid_list[x][y]='#'
            if grid_list[x][y]=='#':
                if ocuppied_count<2:
                    grid_list[x][y]=' '
                if ocuppied_count>3:
                    grid_list[x][y]=' '