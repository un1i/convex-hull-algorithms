from objects.point import Point
from algorithms.quick_hull import quick_hull
from graphs.conv_graph import print_conv_graph

if __name__ == '__main__':
    points = []
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        for _ in range(n):
            x, y = map(int, file.readline().split())
            points.append(Point(x, y))

    conv = quick_hull(points)

    with open('output.txt', 'w') as file:
        for point in conv:
            file.write(str(point))
            file.write('\n')

    print_conv_graph(conv, points)






