import FiguresRepository
import View
import Circle
import Rectangle
import Square
import Triangle


class Controllers ():
    view = View.Print()
    repository = FiguresRepository.FiguresRepository()

    def add_circle (self, radius):
       self.view.print_circle(radius)
       self.repository.add(Circle.Circle(radius))

    def add_rectangle (self, first, second):
       self.view.print_rectangle(first, second)
       self.repository.add(Rectangle.Rectangle(first, second))
    
    def add_square (self, side):
       self.view.print_square(side)
       self.repository.add(Square.Square(side))
    
    def add_triangle (self, first, second, third):
       self.view.print_triangle(first, second, third)
       self.repository.add(Triangle.Triangle(first, second, third))
    
    def print_list_figure (self):
       for figure in self.repository.get_figure_list():
          if  isinstance(figure, Circle.Circle):
             self.view.print_circle(figure.get_radius())
          elif isinstance(figure, Rectangle.Rectangle): 
             self.view.print_rectangle(figure.get_first(), figure.get_second())
          elif isinstance(figure, Square.Square): 
             self.view.print_square(figure.get_side())
          elif isinstance(figure, Triangle.Triangle):
             self.view.print_triangle(figure.get_first(), figure.get_second(), figure.get_third()) 

    def all_area (self):
       m = self.repository.all_area()
       self.view.print_all_area(m)
    
    def all_perimetr (self):
       m = self.repository.all_perimetr()
       self.view.print_all_perimetr(m)


