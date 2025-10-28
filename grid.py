import pygame
from vectors import AbsoluteVector2I

class GridCellType():
    def get_name(self) -> str:
        return self.name
    
    def set_name(self,name:str):
        self.name=name
    
    def get_color(self) -> tuple:
        return self.color
    
    def __init__(self,name:str,color:tuple):
            self.name=property(self.get_name)
            self.color=property(self.get_color)  
            self.name=name
            self.color=color
        

class GridCell():
    def __init__(self,type:GridCellType):
        self.type=type

class Grid():
    def __init__(self,size:int,default_cell_type:GridCellType):
        self._game_grid=[]
        for x in range(size):
            row=[]
            for y in range(size):
               cell=GridCell(default_cell_type)
               row.append(cell)
            self._game_grid.append(row)
    
    def get_cell(self,coordinates:AbsoluteVector2I) -> GridCell:
        return self._game_grid[coordinates.x][coordinates.y]
    
    def get_cell_type(self,coordinates:AbsoluteVector2I) -> GridCellType:
        return self.get_cell(coordinates=coordinates).type
    
    def get_cell_color(self,coordinates:AbsoluteVector2I) -> tuple:
        return self.get_cell_type(coordinates=coordinates).color
        
        