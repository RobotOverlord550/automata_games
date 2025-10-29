class Vector2I():
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    
    def get_x(self)->int:
        return self.x
    
    def set_x(self,x:int):
        self.x=x
    
    def get_y(self)->int:
        return self.y
    
    def set_y(self,y:int):
        self.y=y    
    
    x_pos=property(get_x,set_x)
    y_pos=property(get_y,set_y)    
    
    def __add__(self,other:Vector2I):
        return Vector2I(self.x+other.x,self.y+other.y)
    
    def __eq__(self, value:Vector2I):
        if self.x==value.x and self.y==self.y:
            return True
        else:
            return False

class AbsoluteVector2I(Vector2I):
    def __init__(self,x:int,y:int):
        if x<0:
            raise ValueError(f"Expected a non-negative integer but got {x}")
        if y<0:
            raise ValueError(f"Expected a non-negative integer but got {y}")        
        super().__init__(x,y)
        
    def get_x(self)->int:
        super().get_x()
    
    def set_x(self,x:int):
        if x<0:
            raise ValueError(f"Expected a non=negative integer but got {x}")
        super().set_x(x)
    
    def get_y(self)->int:
        super().get_y()
    
    def set_y(self,y:int):
        if y<0:
            raise ValueError(f"Expected a non=negative integer but got {y}")
        super().set_y(y)