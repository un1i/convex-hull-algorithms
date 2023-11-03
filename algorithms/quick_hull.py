from objects.point import Point
from objects.vector import Vector


def quick_hull_rec(points: list[Point], min_point: Point, max_point: Point, conv: list[Point], is_above: bool):
    if len(points) == 0:
        return

    farthest_point = None
    farthest_vector = None
    farthest_dist = -1

    main_vector = Vector(min_point, max_point)
    for point in points:
        vector = Vector(min_point, point)
        dist = abs(main_vector.rotate(vector))
        if dist > farthest_dist or (dist == farthest_dist and (abs(vector.x) > abs(farthest_vector.x) or
                                                               abs(vector.y) > abs(farthest_vector.y))):
            farthest_dist = dist
            farthest_point = point
            farthest_vector = vector

    below_points1, above_points1 = divide_points(points, min_point, farthest_point)
    below_points2, above_points2 = divide_points(points, farthest_point, max_point)

    if is_above:
        quick_hull_rec(above_points2, farthest_point, max_point, conv, True)
        conv.append(farthest_point)
        quick_hull_rec(above_points1, min_point, farthest_point, conv, True)
    else:
        quick_hull_rec(below_points1, min_point, farthest_point, conv, False)
        conv.append(farthest_point)
        quick_hull_rec(below_points2, farthest_point, max_point, conv, False)


def divide_points(points: list[Point], min_point: Point, max_point: Point) -> tuple[list[Point], list[Point]]:
    above_points = []
    below_points = []
    main_vector = Vector(min_point, max_point)
    for point in points:
        cur_vector = Vector(min_point, point)
        rotate_res = main_vector.rotate(cur_vector)
        if rotate_res > 0:
            above_points.append(point)
        elif rotate_res < 0:
            below_points.append(point)
    return below_points, above_points


def quick_hull(points: list[Point]) -> list[Point]:
    conv = []
    max_point = points[0]
    min_point = points[0]

    for point in points:
        if point.x < min_point.x or (point.x == min_point.x and point.y < min_point.y):
            min_point = point
        if point.x > max_point.x or (point.x == max_point.x and point.y < max_point.y):
            max_point = point

    below_points, above_points = divide_points(points, min_point, max_point)
    conv.append(min_point)
    quick_hull_rec(below_points, min_point, max_point, conv, False)
    conv.append(max_point)
    quick_hull_rec(above_points, min_point, max_point, conv, is_above=True)
    return conv
