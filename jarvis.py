from objects.point import Point
from objects.vector import Vector


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
        deleted_point = cur_point
        cur_vector = Vector(prev, cur_point)
        for point in remaining_points:
            new_vector = Vector(prev, point)
            rotate_val = cur_vector.rotate(new_vector)
            if rotate_val < 0 or (rotate_val == 0 and abs(cur_vector.x) < abs(new_vector.x)):
                cur_point = point
                cur_vector = new_vector

        if cur_point != deleted_point:
            remaining_points.add(deleted_point)
            remaining_points.remove(cur_point)

        if cur_point == conv[0]:
            break
        conv.append(cur_point)
        prev = cur_point
    return conv




