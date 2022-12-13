import Rectangle

class Square (Rectangle.Rectangle):

    def __init__(self, side) -> None:
        super().__init__(side, side)
        self.side = side
    
    def get_sum(self):
        if (self.side < 0):
            return Exception ("Сторона  меньше нуля")
        else:
            return self.side*self.side
   
    def perimetr (self):
        if (self.side < 0 ):
            return Exception ("Сторона  меньше нуля")
        else:
            return self.side*4
    
    def get_side(self):
        return self.side
    
    