from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
identity = new_matrix()
ident(identity)

transform = []
transform.append(identity)

parse_file( 'script', edges, polygons, transform, screen, color )
