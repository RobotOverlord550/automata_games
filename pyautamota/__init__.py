import pygame

display_surface:pygame.Surface
grid_surface:pygame.Surface
clock=pygame.time.Clock()
window_size:int
grid_size:int

def init(window_size:int,grid_size:int):
    pygame.init()
    display_surface=pygame.display.set_mode((window_size, window_size))
    grid_surface=pygame.Surface((grid_size,grid_size))
    clock=pygame.time.Clock()
    running=True