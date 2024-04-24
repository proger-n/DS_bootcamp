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


def main():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    loop_time = timeit.timeit(
        lambda: duplicate_emails_loop(emails), number=90000000)

    comprehension_time = timeit.timeit(
        lambda: duplicate_emails_comprehension(emails), number=90000000)

    map_time = timeit.timeit(
        lambda: duplicate_emails_map(emails), number=90000000)

    times = [(loop_time, "loop"), (comprehension_time,
                                   "list comprehension"), (map_time, "map")]

    times.sort()

    if times[0][1] == "map":
        print("It is better to use a map.")
    elif times[0][1] == "list comprehension":
        print("It is better to use a list comprehension.")
    else:
        print("It is better to use a loop.")

    for time, method in times:
        print(f"{method} time: {time}|", end=" ")


if __name__ == '__main__':
    main()
