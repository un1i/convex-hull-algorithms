from objects.point import Point
import matplotlib.pyplot as plt
import numpy as np


def print_conv_graph(conv: list[Point], points: list[Point]) -> None:
    fig, ax = plt.subplots()
    conv_x = []
    conv_y = []
    for point in conv:
        conv_x.append(point.x)
        conv_y.append(point.y)
    conv_x.append(conv[0].x)
    conv_y.append(conv[0].y)

    points_x = []
    points_y = []
    for point in points:
        points_x.append(point.x)
        points_y.append(point.y)

    ax.plot(np.array(points_x), np.array(points_y), marker='o', color='b', lw=0)
    ax.plot(np.array(conv_x), np.array(conv_y), marker='o', color='r')
    plt.show()
