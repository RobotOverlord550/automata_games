# imports
import pygame
import grid
import elements
from input import GameMouse
from vectors import AbsoluteVector2I
from math_functions import clamp
import json

# constants
data_dict:dict
with open('data.json','r') as file:
    data_dict=json.load(file)
c:dict=data_dict.get('constants')
window_size:int=c.get('screen_size')
clock_speed:float=c.get('clock_speed')
grid_size:int=c.get('grid_size')

# pygame setup
pygame.init()
display_surface=pygame.display.set_mode((window_size, window_size))
grid_surface=pygame.Surface((grid_size,grid_size))
clock=pygame.time.Clock()
running=True


# grid setup
game_grid=grid.Grid(size=grid_size,default_element=' ')
def draw_grid()->pygame.Surface:
    pixel_array=pygame.PixelArray(grid_surface)
    for x in range(grid_size):
        for y in range(grid_size):
            pixel_array[x][y]=elements.get_cell_color(game_grid.grid_list[x][y])
    pixel_array.close()
    return grid_surface

#mouse_pixel_position:AbsoluteVector2I
pixel_input_pos:AbsoluteVector2I=AbsoluteVector2I(round(grid_size/2),round(grid_size/2))
while running:
    key_up:bool=False
    
    # events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pixel_input_pos.y_pos=pixel_input_pos.y_pos-1
    if keys[pygame.K_DOWN]:
        pixel_input_pos.y_pos=pixel_input_pos.y_pos+1
    pixel_input_pos.y_pos=clamp(pixel_input_pos.y_pos,1,grid_size-2)
    if keys[pygame.K_LEFT]:
        pixel_input_pos.x_pos=pixel_input_pos.x_pos-1
    if keys[pygame.K_RIGHT]:
        pixel_input_pos.x_pos=pixel_input_pos.x_pos+1
    pixel_input_pos.x_pos=clamp(pixel_input_pos.x_pos,1,grid_size-2)
    
    
    # input
    elements.execute_rules(game_grid.grid)    
    game_grid.update_grid(coordinates=AbsoluteVector2I(pixel_input_pos.x, pixel_input_pos.y-1),element='#')
    game_grid.update_grid(coordinates=AbsoluteVector2I(pixel_input_pos.x, pixel_input_pos.y+1),element='#')
    game_grid.update_grid(coordinates=AbsoluteVector2I(pixel_input_pos.x-1, pixel_input_pos.y),element='#')
    game_grid.update_grid(coordinates=AbsoluteVector2I(pixel_input_pos.x+1, pixel_input_pos.y),element='#')
            
    # grid
    grid_surface=draw_grid()
    pygame.transform.scale(surface=grid_surface,
                           size=(window_size,window_size),
                           dest_surface=display_surface)

    # new frame
    pygame.display.flip()
    clock.tick(clock_speed)
    
pygame.quit()