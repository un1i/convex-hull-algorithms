from objects.point import Point


class Vector:
    def __init__(self, point1: Point, point2: Point):
        self.__coord: Point = Point(point2.x - point1.x, point2.y - point1.y)

    @property
    def x(self) -> int:
        return self.__coord.x

    @property
    def y(self) -> int:
        return self.__coord.y
