import sys
import timeit
from functools import reduce


def sum_of_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total


def sum_of_squares_reduce(n):
    return reduce(lambda x, y: x + y ** 2, [i for i in range(1, n + 1)])


def benchmark(method, num_calls, n):
    if method == "loop":
        time = timeit.timeit(lambda: sum_of_squares_loop(n), number=num_calls)
    elif method == "reduce":
        time = timeit.timeit(
            lambda: sum_of_squares_reduce(n), number=num_calls)
    else:
        print("Invalid method name.")
        return
    print(f"{method} time: {time}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python benchmark.py <method> <num_calls> <n>")
        sys.exit(1)
    method, num_calls, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    benchmark(method, num_calls, n)
