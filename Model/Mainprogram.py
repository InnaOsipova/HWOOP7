# import sys
# sys.path.append('path/to/HWOOP7/ForWork')
# import sys
# sys.path.append('../')
import FigureController

class Main_figures ():

    def run (self):
     controller = FigureController.Controllers()

     controller.add_circle(3)
     controller.add_rectangle(3,4)
     controller.add_square(6)
     controller.add_triangle(3,5,4)
     print()
     controller.all_area()
     print()
     controller.all_perimetr()
     print()
     controller.print_list_figure()

m = Main_figures()
m.run()
