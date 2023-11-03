from objects.point import Point


class Vector:
    def __init__(self, point1: Point, point2: Point):
        self.__coord: Point = Point(point2.x - point1.x, point2.y - point1.y)

    def rotate(self, other) -> int:
        return self.x * other.y - self.y * other.x

    def __lt__(self, other):
        rotate_val = self.rotate(other)
        if rotate_val > 0 or (rotate_val == 0 and (self.x < other.x or (self.x == other.x and abs(self.y) < abs(other.y)))):
            return True
        return False

    @property
    def x(self) -> int:
        return self.__coord.x

    @property
    def y(self) -> int:
        return self.__coord.y
