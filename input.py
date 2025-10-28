from vectors import AbsoluteVector2I

class GameMouse:
    def get_mouse_pixel_position(pos:tuple,screen_size:int,grid_size:int)->AbsoluteVector2I:
        factor=round(grid_size/screen_size)
        mouse_pos_int:tuple=round(pos[0]),round(pos[1])
        return AbsoluteVector2I(x=mouse_pos_int[0]*factor,y=mouse_pos_int[1]*factor)