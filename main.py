# main.py
# *file that runs when you start the project
# TODO make file __main__.py
# TODO Clean up imports
# TODO improve comments
# TODO Restructure
import pygame
import grid
import elements
from input import GameMouse
from math_functions import clamp
import json
from typing import Tuple

# *CONSTANTS
WINDOW_SIZE = 500
GRID_SIZE = 50
FPS = 10

# PyGame Setup
# *Sets up everything related to PyGame
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
grid_surface = pygame.Surface(GRID_SIZE, GRID_SIZE)  # TODO move to Grid Class
clock = pygame.time.Clock()
running = True

# Game Grid Setup
# *Intializes game_grid variable
# TODO move Grid class
game_grid = grid.Grid(size=GRID_SIZE, default_element=' ')


# draw_grid
# *uses CellularAutomata data to modify the pixels on the grid_surface
# TODO move to Grid class
def draw_grid() -> pygame.Surface:
    pixel_array = pygame.PixelArray(grid_surface)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pixel_array[x][y] = elements.get_cell_color(
                game_grid.grid_list[x][y])
    pixel_array.close()
    return grid_surface


# *Input Setup
# TODO setup to Input class
pixel_input_pos: Tuple[int, int] = (round(GRID_SIZE/2), )

# *Primary Program Loop
while running:
    key_up: bool = False

    # *Quit Check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # *Input Check
    # TODO move input check to Input class
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pixel_input_pos.y_pos = pixel_input_pos.y_pos-1
    if keys[pygame.K_DOWN]:
        pixel_input_pos.y_pos = pixel_input_pos.y_pos+1
    pixel_input_pos.y_pos = clamp(pixel_input_pos.y_pos, 1, GRID_SIZE-2)
    if keys[pygame.K_LEFT]:
        pixel_input_pos.x_pos = pixel_input_pos.x_pos-1
    if keys[pygame.K_RIGHT]:
        pixel_input_pos.x_pos = pixel_input_pos.x_pos+1
    pixel_input_pos.x_pos = clamp(pixel_input_pos.x_pos, 1, GRID_SIZE-2)

    # *Applies rules to elements on game grid
    elements.execute_rules(game_grid.grid)

    # *Adds player character to grid based on input
    # TODO Edit Grid class to fix errors
    game_grid.update_grid(coordinates=pixel_input_pos.x, pixel_input_pos.y-1, element='#')
    game_grid.update_grid(coordinates=pixel_input_pos.x, pixel_input_pos.y+1, element='#')
    game_grid.update_grid(coordinates=pixel_input_pos.x-1, pixel_input_pos.y, element='#')
    game_grid.update_grid(coordinates=pixel_input_pos.x+1, pixel_input_pos.y, element='#')

    # *Setting up what is displayed
    grid_surface = draw_grid()
    pygame.transform.scale(surface=grid_surface,
                           size=(WINDOW_SIZE, WINDOW_SIZE),
                           dest_surface=display_surface)  # TODO Move scaling to Grid Class

    # *Setup Next Frame
    pygame.display.flip()
    clock.tick(FPS)

# *Quit Game
pygame.quit()
