from objects.point import Point
import random


def generate_points(number: int, min_coord: int = -2000, max_coord: int = 2000) -> list[Point]:
    points = set()
    while len(points) != number:
        x = random.randrange(min_coord, max_coord)
        y = random.randrange(min_coord, max_coord)
        points.add(Point(x, y))
    return list(points)

