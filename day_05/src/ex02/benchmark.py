import sys
import timeit


def duplicate_emails_loop(emails):
    result = []
    for email in emails:
        for _ in range(5):
            result.append(email)
    return result


def duplicate_emails_comprehension(emails):
    return [email for email in emails for _ in range(5)]


def duplicate_emails_map(emails):
    return list(map(lambda email: [email]*5, emails))


def duplicate_emails_filter(emails):
    return list(filter(lambda email: email.endswith("@gmail.com"), emails)) * 5


emails = ['john@gmail.com', 'james@gmail.com',
          'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']


def benchmark(method, num_calls):
    if method == "loop":
        time = timeit.timeit(
            lambda: duplicate_emails_loop(emails), number=num_calls)
    elif method == "list_comprehension":
        time = timeit.timeit(
            lambda: duplicate_emails_comprehension(emails), number=num_calls)
    elif method == "map":
        time = timeit.timeit(
            lambda: duplicate_emails_map(emails), number=num_calls)
    elif method == "filter":
        time = timeit.timeit(
            lambda: duplicate_emails_filter(emails), number=num_calls)
    else:
        print("Invalid method name.")
        return
    print(f"{method} time: {time}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python benchmark.py <method> <num_calls>")
        sys.exit(1)
    method, num_calls = sys.argv[1], int(sys.argv[2])
    benchmark(method, num_calls)
