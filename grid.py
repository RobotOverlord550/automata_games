# grid.py
# *Controls the game grid
# TODO Make Comments
# TODO Clean up imports
import pygame
from typing import Tuple


class Grid():
    def _get_grid(self) -> list:
        return self.grid

    def _set_grid(self, new_grid: list):
        self.grid = new_grid

    def update_grid(self, coordinates: Tuple[int, int], element: str):
        self.grid[coordinates[0]][coordinates[1]] = element

    def __init__(self, size: int, default_element: str):
        self.grid: list = []
        for x in range(size):
            row = []
            for y in range(size):
                row.append(default_element)
            self.grid.append(row)

    grid_list = property(_get_grid, _set_grid)
