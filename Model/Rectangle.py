import Poligon

class Rectangle (Poligon.Poligon):

    def __init__(self, first, second) -> None:
        super().__init__([first, second])
        self.first = first
        self.second = second
    
    def get_area(self):
        if (self.first < 0 or self.second < 0):
            return Exception ("Сторона  меньше нуля")
        else:
            return self.first*self.second
        
    
    def perimetr (self):
        if (self.first < 0 or self.second < 0):
            return Exception ("Сторона  меньше нуля")
        else:
            return (self.first+ self.second)*2
        
    def get_first(self):
        return self.first
    
    def get_second(self):
        return self.second


