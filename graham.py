from objects.point import Point
from objects.vector import Vector


def graham(points: list[Point]) -> list[Point]:
    conv = []
    cur_point = points[0]
    for point in points:
        if point.x < cur_point.x:
            cur_point = point
        elif point.x == cur_point.x and point.y < cur_point.y:
            cur_point = point

    conv.append(cur_point)

    sorted_points = sorted(points, key=lambda x: Vector(cur_point, x))
    conv.append(sorted_points[1])
    for i in range(2, len(sorted_points)):
        while Vector(conv[-2], sorted_points[i]).rotate(Vector(conv[-2], conv[-1])) >= 0:
            conv.pop()
        conv.append(sorted_points[i])

    return conv
