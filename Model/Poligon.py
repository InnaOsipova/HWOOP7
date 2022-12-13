import Figure
import Iperimeterable

class Poligon(Figure.Figure, Iperimeterable.Iperimeterable):
    

    def __init__ (self, first = 0, second = 0, third = 0):
        super().__init__()
        self.first = first
        self.second = second
        self.third = third

    
    def perimetr (self):
        if self.first < 0 or self.second < 0 or self.third < 0:
            return Exception("Сторона меньше нуля")
        return self.first + self.second + self.third

   