from classes_.Point import Point
from classes_.Line import Line
from classes_.Shapes.Shape import Shape
#type: ignore

my_shape = Shape(
    [Point(0, 0),
     Point(0, 2),
     Point(1, 1),
     Point(2, 2),
     Point(2, 0)])

print(my_shape.compute_inner_angles())
