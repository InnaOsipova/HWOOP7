import Figure
import ILengthable

class Circle (ILengthable.ILengthable, Figure.Figure):
    
    def __init__(self, radius, pi = 3.14) :
        super().__init__()
        self.radius = radius
        self.pi = pi

    def get_area (self):
        if (self.radius < 0):
            return Exception ("Радиус меньше нуля")
        else:
            return self.pi*self.radius*self.radius

    def lengtHable (self):
        if (self.radius < 0):
            return Exception ("Радиус меньше нуля")
        else:
            return 2*self.pi*self.radius
    
    def get_radius(self):
        return self.radius
