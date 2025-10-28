class AbsoluteVector2I():
    def __init__(self,x:int,y:int):
        if x<0:
            raise ValueError(f"Expected a non-negative integer but got {x}")
        if y<0:
            raise ValueError(f"Expected a non-negative integer but got {y}")        
        self.x:int=x
        self.y:int=y
        
    def get_x(self) -> int:
        return self.x
    
    def set_x(self,x:int):
        if x<0:
            raise ValueError(f"Expected a non=negative integer but got {x}")
        self.x=x
    
    def get_y(self) -> int:
        return self.y
    
    def set_y(self,y:int):
        if y<0:
            raise ValueError(f"Expected a non=negative integer but got {y}")
        self.y=y

    x_pos=property(get_x,set_x)
    y_pos=property(get_y,set_y)