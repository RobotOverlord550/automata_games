# elements.py
# *handles elements and their rules
# TODO Rename to rules.py
# TODO Make a non static class Rules to encompase these methods to allow for multiple rule definitions
# TODO Change to focus on using bools instead of ints and characters

import json
from typing import Tuple

MOORE_TRANSLATIONS: Tuple[
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
] = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

data_dict: dict
with open('data.json', 'r') as file:
    data_dict = json.load(file)

colors: dict = data_dict.get('color_ref')


def get_cell_color(element: str) -> tuple:
    try:
        return (colors[element][0], colors[element][1], colors[element][2])
    except:
        raise ValueError(f"Excpected an existing element but got {element}")


MOORE_TRANSLATIONS: Tuple[
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
    Tuple[int, int],
] = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def execute_rules(grid_list: list) -> list:
    def get_neighbors(coordinates: Tuple[int, int]) -> list:
        neighbors: list = []
        for translation in MOORE_TRANSLATIONS:
            translated: list = list(coordinates)+list(translation)
            result = grid_list[translated[0]][translated[1]]
            neighbors.append(result)
        return neighbors

    for x in range(len(grid_list)):
        for y in range(len(grid_list[x])):
            neighbors = get_neighbors(coordinates=(x, y))
            ocuppied_count = 0
            for n in range(len(neighbors)):
                neighbor = neighbors[n]
                if neighbor == "#":
                    ocuppied_count += 1
            if grid_list[x][y] == ' ':
                if ocuppied_count == 3:
                    grid_list[x][y] = '#'
            if grid_list[x][y] == '#':
                if ocuppied_count < 2:
                    grid_list[x][y] = ' '
                if ocuppied_count > 3:
                    grid_list[x][y] = ' '
    return grid_list
