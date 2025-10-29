# imports
import pygame
import grid
import elements
from input import GameMouse
from vectors import AbsoluteVector2I

# constants
SCREEN_SIZE:float=500
CLOCK_SPEED=20
GRID_SIZE=100

# pygame setup
pygame.init()
display_surface=pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
grid_surface=pygame.Surface((GRID_SIZE,GRID_SIZE))
clock=pygame.time.Clock()
running=True


# grid setup
game_grid=grid.Grid(size=GRID_SIZE,default_cell_color=elements.ColorRef.empty)
def draw_grid()->pygame.Surface:
    pixel_array=pygame.PixelArray(grid_surface)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pixel_array[x][y]=game_grid.grid_list[x][y]
    pixel_array[50][50]=elements.ColorRef.lava
    pixel_array.close()
    return grid_surface

#mouse_pixel_position:AbsoluteVector2I
pixel_input_pos:AbsoluteVector2I=AbsoluteVector2I(round(GRID_SIZE/2),round(GRID_SIZE/2))
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
    if keys[pygame.K_LEFT]:
        pixel_input_pos.x_pos=pixel_input_pos.x_pos-1
    if keys[pygame.K_RIGHT]:
        pixel_input_pos.x_pos=pixel_input_pos.x_pos+1
    
    # input
    game_grid.update_grid(coordinates=pixel_input_pos,color=elements.ColorRef.lava)
            
    # grid
    grid_surface=draw_grid()
    pygame.transform.scale(surface=grid_surface,
                           size=(SCREEN_SIZE,SCREEN_SIZE),
                           dest_surface=display_surface)

    # new frame
    pygame.display.flip()
    clock.tick(CLOCK_SPEED)
    
pygame.quit()