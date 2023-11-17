import matplotlib.pyplot as plt
import numpy as np


def print_exec_time_graph(points_number: list[int], time_res: list[tuple[str, list[int]]]):
    fig, ax = plt.subplots()
    for name, time in time_res:
        ax.plot(np.array(points_number), np.array(time), label=name)
    ax.set_xlabel('Количество точек')
    ax.set_ylabel('Время выполнения, мс')
    ax.set_title('Эффективность алгоритмов')
    ax.legend()
    # plt.savefig(f'../images/time_test_max_{points_number[-1]}_points.png')
    plt.show()
