import IRepository
import Poligon
import Circle
import Rectangle
import Square
import Triangle



class FiguresRepository (IRepository.IRepository):
    figure_list = []

    def add (self, some_class):
        self.figure_list.append(some_class)
    
    def get_figure_list (self):
        return self.figure_list
    
    def all_perimetr (self):
        allper = 0.0
        for figure in self.figure_list:
            if isinstance(figure, Rectangle.Rectangle): 
             allper += figure.perimetr()
            elif isinstance(figure, Square.Square): 
             allper += figure.perimetr()
            elif isinstance(figure, Triangle.Triangle):
             allper += figure.perimetr()
        return allper

    def all_area (self):
        allar = 0.0
        for figure in self.figure_list:
            if  isinstance(figure, Circle.Circle):
             allar += figure.get_area()
            elif isinstance(figure, Rectangle.Rectangle): 
             allar += figure.get_area()
            elif isinstance(figure, Square.Square): 
             allar += figure.get_area()
            elif isinstance(figure, Triangle.Triangle):
             allar += figure.get_area()
        return allar 
            