import math
class Point():
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    def get_x(self) -> int:
        return self._x
        
    def set_x(self, new_x: int):
        self._x = new_x

    def get_y(self) -> int:
        return self._y
        
    def set_y(self, new_y: int):
        self._y = new_y

    def compute_distance(self, other_point: "Point") -> float:
        length = math.sqrt(((other_point.get_x() - self.get_x())**2) + ((other_point.get_y() - self.get_y())**2))
        return length


class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    def get_start_point(self) -> Point:
        return self._start_point
        
    def set_start_point(self, new_start: Point):
        self._start_point = new_start

    def get_end_point(self) -> Point:
        return self._end_point
        
    def set_end_point(self, new_end: Point):
        self._end_point = new_end

    def get_length(self) -> float:
        return self._length

class Shape():
    def __init__(self, is_regular: bool, vertices: list[Point], edges: list[Line], inner_angles: list[float]):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def get_is_regular(self) -> bool:
        return self._is_regular
    
    def set_is_regular(self, regular: bool):
        self._is_regular = regular

    def get_vertices(self) -> list[Point]:
        return self._vertices
    
    def set_vertices(self, vertices: list[Point]):
        self._vertices = vertices

    def get_edges(self) -> list[Line]:
        return self._edges
    
    def set_edges(self, edges: list[Line]):
        self._edges = edges

    def get_inner_angles(self) -> list[float]:
        return self._inner_angles
    
    def set_inner_angles(self, angles: list[float]):
        self._inner_angles = angles

    def compute_area(self):
        raise NotImplementedError
    def compute_perimeter(self):
        perimeter = 0
        for line in self._edges:
            perimeter += line.get_length()
        return perimeter
            


class Rectangle(Shape):
    def __init__(self, width: float, height: float, center_point: Point):
        self._width = width
        self._height = height
        self._center_point = center_point

        min_x = self._center_point.get_x() - int(self._width / 2)
        max_x = self._center_point.get_x() + int(self._width / 2)
        min_y = self._center_point.get_y() - int(self._height / 2)
        max_y = self._center_point.get_y() + int(self._height / 2)

        p_bottom_left = Point(min_x, min_y)
        p_bottom_right = Point(max_x, min_y)
        p_top_left = Point(min_x, max_y)
        p_top_right = Point(max_x, max_y)

        self._bottom_line = Line(p_bottom_left, p_bottom_right)
        self._top_line = Line(p_top_left, p_top_right)
        self._left_line = Line(p_bottom_left, p_top_left)
        self._right_line = Line(p_bottom_right, p_top_right)

        self._lines = [self._bottom_line, self._top_line, self._left_line, self._right_line]
        super().__init__(is_regular = False, vertices = 
                         [p_bottom_left, p_bottom_right, p_top_left, p_top_right]
                         , edges = self._lines, inner_angles = [90.0, 90.0, 90.0, 90.0])
    def get_width(self) -> float:
        return self._width
    def set_width(self, width: float):
        self._width = width

    def get_height(self) -> float:
        return self._height
    def set_height(self, height: float):
        self._height = height

    def get_center_point(self) -> Point:
        return self._center_point
    def set_center_point(self, center_point: Point):
        self._center_point = center_point
    def compute_area(self):
        return self._width * self._height



class Square(Rectangle):
    def __init__(self, side_length: float, center_point):
        super().__init__(height = side_length, width = side_length, center_point = center_point)


class Triangle(Shape):
    def __init__(self, base: float, height: float, start_point: Point):
        self._base = base
        self._height = height
        self._start_point = start_point

        p1_vertex = self._start_point
        p2_x = self._start_point.get_x() + int(self._base)
        p2_y = self._start_point.get_y()
        p2_vertex = Point(p2_x, p2_y)
        p3_x = self._start_point.get_x() + int(self._base / 2)
        p3_y = self._start_point.get_y() + int(self._height)
        p3_vertex = Point(p3_x, p3_y)

        self._line1 = Line(p1_vertex, p2_vertex)
        self._line2 = Line(p2_vertex, p3_vertex)
        self._line3 = Line(p3_vertex, p1_vertex)

        self._lines = [self._line1, self._line2, self._line3]

        super().__init__(is_regular = False, vertices = 
                         [p1_vertex, p2_vertex, p3_vertex], edges = self._lines,
                           inner_angles = [60.0, 60.0, 60.0])
        
    def get_base(self) -> float:
        return self._base
    
    def set_base(self, base: float):
        self._base = base

    def get_height(self) -> float:
        return self._height
    
    def set_height(self, height: float):
        self._height = height

    def get_start_point(self) -> Point:
        return self._start_point
    
    def set_start_point(self, start_point: Point):
        self._start_point = start_point

    def compute_area(self):
        return (self._base * self._height)/2

class Isosceles(Triangle):
    pass

class Equilateral(Triangle):
    pass

class Scalene(Triangle):
    pass

class Trirectangle(Triangle):
    pass