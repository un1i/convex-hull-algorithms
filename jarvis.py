from objects.point import Point
from objects.vector import Vector


def det(vector1: Vector, vector2: Vector) -> int:
    return vector1.x * vector2.y - vector1.y * vector2.x


def jarvis(points: list[Point]) -> list[Point]:
    remaining_points = set(points)
    conv = list()
    cur_point: Point = points[0]

    for point in points:
        if point.x < cur_point.x:
            cur_point = point
        elif point.x == cur_point.x and point.y < cur_point.y:
            cur_point = point

    conv.append(cur_point)
    # remaining_points.remove(cur_point)

    prev: Point = cur_point

    while True:
        cur_point = remaining_points.pop()
        cur_vector = Vector(prev, cur_point)
        for point in remaining_points:
            new_vector = Vector(prev, point)
            determinant = det(cur_vector, new_vector)
            if determinant < 0 or (determinant == 0 and abs(cur_vector.x) < abs(new_vector.x)):
                remaining_points.add(cur_point)
                cur_point = point
                cur_vector = new_vector
                remaining_points.remove(point)

        if cur_point == conv[0]:
            break
        conv.append(cur_point)
        prev = cur_point
    return conv




