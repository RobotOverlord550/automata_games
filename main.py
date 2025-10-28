import pygame
import updates
import grid
from vectors import AbsoluteVector2I

SCREEN_SIZE:float=500
CLOCK_SPEED=60
GRID_SIZE=100

pygame.init()
display_surface=pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
grid_surface=pygame.Surface((GRID_SIZE,GRID_SIZE))
clock=pygame.time.Clock()
running=True

game_grid=grid.Grid(size=GRID_SIZE,default_cell_color=grid.ColorRef.empty)

def draw_grid()->pygame.Surface:
    pixel_array=pygame.PixelArray(grid_surface)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pixel_array[x][y]=game_grid.grid_list[x][y]
    pixel_array.close()
    return grid_surface

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    grid_surface=draw_grid()
    pygame.transform.scale(surface=grid_surface,
                           size=(SCREEN_SIZE,SCREEN_SIZE),
                           dest_surface=display_surface)
    pygame.display.flip()
    clock.tick(CLOCK_SPEED)
    
pygame.quit()