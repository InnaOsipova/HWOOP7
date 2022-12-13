import Poligon
import math

class Triangle (Poligon.Poligon):

    def __init__(self, first, second, third) -> None:
        super().__init__([first, second, third])
        self.first = first
        self.second = second
        self.third = third

    def get_area(self):
        if (self.first < 0 or self.second < 0 or self.third < 0):
            return Exception ("Сторона  меньше нуля")
        else:
            p = (self.first + self.second + self.third)/2
            return math.sqrt(p*(p-self.first)*(p-self.second)*(p-self.third))
        
    def get_first(self):
        return self.first
    
    def get_second(self):
        return self.second
    
    def get_third(self):
        return self.third
    
   