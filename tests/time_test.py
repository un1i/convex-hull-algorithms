import time
from point_generator import generate_points
from algorithms.quick_hull import quick_hull
from algorithms.jarvis import jarvis
from algorithms.graham import graham
from graphs.exec_time_graph import print_exec_time_graph


def time_test(number_points: list[int], funcs: list) -> list[list]:
    result = [[] for _ in range(len(funcs))]
    for number in number_points:
        points = generate_points(number)
        for i in range(len(funcs)):
            start = time.time()
            funcs[i](points)
            finish = time.time()
            exec_time = int((finish - start) * 1000)
            result[i].append(exec_time)
    return result


if __name__ == '__main__':
    tested_number_points = [i for i in range(100, 10000, 100)]
    tested_funcs = [jarvis, graham, quick_hull]
    res = time_test(tested_number_points, tested_funcs)
    time_res = [(tested_funcs[i].__name__, res[i]) for i in range(len(tested_funcs))]
    print_exec_time_graph(tested_number_points, time_res)

