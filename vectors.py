class AbsoluteVector2I():
    def __init__(self,x:int,y:int):
        if x<0:
            raise ValueError(f"Expected a non-negative integer but got {x}")
        if y<0:
            raise ValueError(f"Expected a non-negative integer but got {y}")        
        self.vector:tuple=(x,y)
        
    def get_x(self) -> int:
        return self.vector[0]
    
    def set_x(self,x:int):
        if x<0:
            raise ValueError(f"Expected a non=negative integer but got {x}")
        self.vector[0]=x
    
    def get_y(self) -> int:
        return self.vector[1]
    
    def set_y(self,y:int):
        if y<0:
            raise ValueError(f"Expected a non=negative integer but got {y}")
        self.vector[1]=y

    x=property(get_x,set_x)
    y=property(get_y,set_y)