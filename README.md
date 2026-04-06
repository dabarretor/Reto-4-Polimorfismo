# Ejercicio 1
1. Create a superclass called Shape(), which is the base of the classes Reactangle() and Square(), define the methods compute_area and compute_perimeter in Shape() and then using polymorphism redefine the methods properly in Rectangle and in Square.

2. Using the classes Point() and Line() define a new super-class Shape() with the following structure:

```mermaid
classDiagram

class Shape {
    +is_regular : bool
    +vertices: list(Point)
    +edges: list(Line)
    +inner_angles: list(float)
    +compute_area(self)
    +compute_perimeter(self)
    +compute_inner_angles(self)
}

class Point {
    +x : int
    +y : int
    +compute_distance(self, Point)
}

class Line {
    +start_point : Point
    +end_point : Point
    +length : float
}


class Rectangle {
}

class Isosceles {
}

class Equilateral { 
}

class Scalene {   
}

class TriRectangle {
}

class Square {
}

Triangle <|-- TriRectangle
Triangle <|-- Isosceles
Triangle <|-- Equilateral
Triangle <|-- Scalene

Rectangle <|-- Square

Shape <|-- Rectangle
Shape <|-- Triangle
Shape *-- Line
Shape *-- Point
```
Python
```python
```