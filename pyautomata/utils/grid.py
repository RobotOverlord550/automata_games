from typing import Tuple

import cellpylib as cpl
import pygame

from point import Point

class Grid:
    def __init__(self, size: Point, empty_color: Tuple[int, int, int] = (0, 0, 0),
                 occupied_color: Tuple[int, int, int] = (255, 255, 255)):
        self.rows, self.cols = size
        self.empty_color = empty_color
        self.occupied_color = occupied_color
        self.surface = pygame.Surface((self.cols, self.rows))

        self.automaton = cpl.init_simple2d(self.rows, self.cols)

    def update(self, timesteps: int = 1) -> None:
        self.automaton = cpl.evolve2d(self.automaton,
                                      timesteps=timesteps,
                                      neighbourhood='moore',
                                      apply_rule=cpl.game_of_life_rule)[-1]

    def set_cell(self, row: int, col: int, state: int) -> None:
        self.automaton[row, col] = state

    def get_cell(self, row: int, col: int) -> int:
        pixel_array = pygame.PixelArray(self.surface)

        for x in range(self.cols):
            for y in range(self.rows):
                pixel_array[x, y] = (
                    self.occupied_color if self.automaton[y, x]
                    else self.empty_color
                )

        pixel_array.close()
        return self.surface
