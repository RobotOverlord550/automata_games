import pygame
from vectors import AbsoluteVector2I

class ColorRef():
    empty=(0,0,0)
    lava=(255,0,0)

class Grid():
    def get_grid(self) -> list:
        return self.grid
    def set_grid(self,new_grid:list):
        self.grid=new_grid    
    
    def __init__(self,size:int,default_cell_color:tuple):
        self.grid:list=[]        

        for x in range(size):
            row=[]
            for y in range(size):
               row.append(default_cell_color)
            self.grid.append(row)
            
    grid_list=property(get_grid,set_grid)    