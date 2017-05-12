from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
edges = []
color = [255, 255, 255]
polygons = []
transform = new_matrix()
ident(transform)

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print


parse_file( 'script', edges, polygons, transform, screen, color)
