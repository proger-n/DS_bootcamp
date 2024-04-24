import sys
import timeit
import random
from collections import Counter


def create_dict_custom(lst):
    return {num: lst.count(num) for num in set(lst)}


def create_dict_counter(lst):
    return dict(Counter(lst))


def top_10_custom(lst):
    counts = create_dict_custom(lst)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]


def top_10_counter(lst):
    return Counter(lst).most_common(10)


def benchmark():
    lst = [random.randint(0, 100) for _ in range(1000000)]
    time = timeit.timeit(lambda: create_dict_custom(lst), number=1)
    print(f"my function time: {time}")
    time = timeit.timeit(lambda: top_10_custom(lst), number=1)
    print(f"my top 10 time: {time}")
    lst = [random.randint(0, 100) for _ in range(1000000)]
    time = timeit.timeit(lambda: create_dict_counter(lst), number=1)
    print(f"Counter function time: {time}")
    time = timeit.timeit(lambda: top_10_counter(lst), number=1)
    print(f"Counter top 10 time: {time}")
    return


if __name__ == "__main__":
    benchmark()
