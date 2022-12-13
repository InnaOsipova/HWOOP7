import Circle
import Rectangle
import Square
import Triangle

class Print ():

    def print_circle (self, radius):
        temp = Circle.Circle(radius)
        print(f"Круг - радиус: {radius},  площадь: {temp.get_area()}, окружность: {temp.lengtHable()}") 

    def print_rectangle (self, first, second):
        temp = Rectangle.Rectangle(first, second)
        print(f"Прямоугольник - сторона 1: {first}, сторона 2: {second}, площадь: {temp.get_area()}, периметр: {temp.perimetr()}") 

    def print_square (self, side):
        temp = Square.Square(side)
        print(f"Квадрат - сторона : {side}, площадь: {temp.get_area()}, периметр: {temp.perimetr()}") 
    
    def print_triangle (self, first, second, third):
        temp = Triangle.Triangle(first, second, third)
        print(f"Треугольник - сторона 1: {first}, сторона 2: {second}, сторона 3: {third}, площадь: {temp.get_area()}, периметр: {temp.perimetr()}")

    def print_all_area (self, area):
        print (f"Общая площадь всех фигур = {area}") 
    
    def print_all_perimetr (self, perimetr):
        print (f"Периметр всех фигур = {perimetr}")

