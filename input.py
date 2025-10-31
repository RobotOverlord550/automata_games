from typing import Tuple


class GameMouse:
    def get_mouse_pixel_position(pos: tuple, screen_size: int, grid_size: int) -> Tuple[int, int]:
        factor = round(grid_size/screen_size)
        mouse_pos_int: tuple = round(pos[0]), round(pos[1])
        return mouse_pos_int[0]*factor, mouse_pos_int[1]*factor
