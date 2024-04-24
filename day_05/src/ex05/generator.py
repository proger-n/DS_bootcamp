# https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset

import sys
import resource


def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    lines_gen = read_file_generator(file_path)
    for line in lines_gen:
        pass
    peak_memory = resource.getrusage(
        resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
    user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    sys_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime
    total_time = user_time + sys_time
    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.2f}s")
