from pygame import PixelArray, Surface
import cellpylib
import numpy as np
from typing import Tuple, Union
from array import array
from typing_extensions import Self


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def create_color(r: int, g: int, b: int) -> Tuple[int, int, int]:
        if r in range(256) and g in range(256) and b in range(256):
            return (r, g, b)


class Point():
    def __init__(self, x: int, y: int):
        self._data = array('i', [0, 0])
        self._data[0] = x
        self._data[1] = y


    def get_x(self) -> int:
        return self._data[0]
    

    def get_y(self) -> int:
        return self._data[1]
    

    def set_y(self, value: int) -> Self:
        self._data[1] = value
        return self
    

    def set_x(self, value: int) -> Self:
        self._data[0] = value
        return self

        
    x = property(get_x, set_x)
    y = property(get_y, set_y)


    def move_point(self, modifier_point: Self) -> Self:
        self._data[0] += modifier_point.x
        self._data[1] += modifier_point.y
        return self


    def abs_point(self) -> Self:
        self._data[0] = abs(self._data[0])
        self._data[1] = abs(self._data[1])
        return self
    

    def clamp_point(self, min_point: Self, max_point: Self) -> None:
        self._data[0] = max(min_point.x, min(self._data[0], max_point.x))
        self._data[1] = max(min_point.y, min(self._data[1], max_point.y))


class Grid:
    def __init__(
                    self, 
                    size: Point, 
                    empty_color: Color = Color.BLACK,
                    occupied_color: Color = Color.WHITE
                ):
        self.size = size.abs_point()
        self.empty_color = empty_color
        self.occupied_color = occupied_color
        self.surface = Surface(size=(self.size.x, self.size.y))

        self.automaton = cellpylib.init_simple2d(rows=self.size.y, cols=self.size.x, dtype=np.bool)


    def update(self, timesteps: int = 1) -> None:
        self.automaton = cellpylib.evolve2d(self.automaton,
                                      timesteps=timesteps,
                                      neighbourhood='moore',
                                      apply_rule=cellpylib.game_of_life_rule)
    
    
    def get_cell(self, point: 'GridPoint') -> bool:
        return self.automaton[-1, point[0], point[1]]


    def set_cell(self, point: 'GridPoint', state: bool) -> None:
        point.abs_point().clamp_point(Point(0, 0), Point(self.size.x-1, self.size.y-1))
        self.automaton[-1, point.y, point.x] = state
        
        
    def draw(self, target_surface: Surface) -> Surface:
        self.update()
        pixel_array = PixelArray(self.surface)

        for x in range(self.size.x):
            for y in range(self.size.y):
                if self.automaton[-1, y, x]==np.bool(True):
                    pixel_array[x, y] = self.occupied_color
                else:
                    pixel_array[x, y] = self.empty_color

        pixel_array.close()
        return target_surface
    

class GridPoint(Point):
    def __init__(self, grid:Grid, x: int, y: int) -> Self:
        if x < 0 or y < 0:
            raise ValueError("GridPoint coordinates must be non-negative integers.")
        if x >= grid.size.x or y >= grid.size.y:
            raise ValueError("GridPoint coordinates must be within the grid bounds.")
        super().__init__(self, x, y)