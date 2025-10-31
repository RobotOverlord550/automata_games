# main.py
# *file that runs when you start the project
# TODO make file __main__.py
# TODO Clean up imports
# TODO improve comments
# TODO Restructure
# TODO Organize Lose Code into Organized Methods
import pygame
import grid
import elements
from input import GameMouse
from math_functions import clamp
import json
from typing import Tuple
from numpy import ndarray, array

# Constants
# *The constants used in the code
WINDOW_SIZE = 500
GRID_SIZE = 50
FPS = 10

# PyGame Setup
# *Sets up everything related to PyGame
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
grid_surface = pygame.Surface(
    size=([GRID_SIZE]*2))  # TODO move to Grid Class
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
    debug_ref: list = []
    for x in range(GRID_SIZE):
        debug_ref.append([])
        for y in range(GRID_SIZE):
            debug_ref[x]
            pixel_array[x][y] = elements.get_cell_color(
                game_grid.grid_list[x][y])
            debug_ref[x].append(pixel_array[x][y])
        print(f"{x + 1}. " + str(debug_ref[x]))
    pixel_array.close()

    return grid_surface


# Input Setup
# *Sets up input variables
# TODO move to Input class
pixel_input_pos: list = [round(GRID_SIZE/2)]*2

# Loop
# *Primary Program Loop
while running:
    key_up: bool = False

    # Quit Check
    # *Checks to see if the user quit the game by closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input Check
    # * Checks the user input
    # TODO move input check to Input class
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pixel_input_pos[1] -= 1
    if keys[pygame.K_DOWN]:
        pixel_input_pos[1] += 1
    pixel_input_pos[1] = clamp(pixel_input_pos[1], 1, GRID_SIZE-2)
    if keys[pygame.K_LEFT]:
        pixel_input_pos[0] -= 1
    if keys[pygame.K_RIGHT]:
        pixel_input_pos[0] += 1
    pixel_input_pos[0] = clamp(pixel_input_pos[0], 1, GRID_SIZE-2)

    # Add Player
    # *Adds player character to grid based on input
    # TODO Edit Grid class to fix errors
    game_grid.update_grid(coordinates=(
        pixel_input_pos[0], pixel_input_pos[1]-1), element='#')
    game_grid.update_grid(coordinates=(
        pixel_input_pos[0], pixel_input_pos[1]+1), element='#')
    game_grid.update_grid(coordinates=(
        pixel_input_pos[0]+1, pixel_input_pos[1]), element='#')
    game_grid.update_grid(coordinates=(
        pixel_input_pos[0]-1, pixel_input_pos[1]), element='#')

    # Rule Execution
    # *Applies rules to elements on game grid
    game_grid.grid_list = elements.execute_rules(game_grid.grid_list)

    # Window
    # *Setting up what is displayed
    grid_surface = draw_grid()
    pygame.transform.scale(surface=grid_surface,
                           size=(WINDOW_SIZE, WINDOW_SIZE),
                           dest_surface=display_surface)  # TODO Move scaling to Grid Class

    # Frame End
    # *Setup Next Frame
    pygame.display.flip()
    clock.tick(FPS)

# Quit
# *Quit Game
pygame.quit()
