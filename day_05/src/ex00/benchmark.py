import timeit


def duplicate_emails_loop(emails):
    result = []
    for email in emails:
        for _ in range(5):
            result.append(email)
    return result


def duplicate_emails_comprehension(emails):
    return [email for email in emails for _ in range(5)]


emails = ['john@gmail.com', 'james@gmail.com',
          'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']


def main():
    loop_time = timeit.timeit(
        lambda: duplicate_emails_loop(emails), number=90000000)

    comprehension_time = timeit.timeit(
        lambda: duplicate_emails_comprehension(emails), number=90000000)

    if loop_time <= comprehension_time:
        print("It is better to use a loop.")
    else:
        print("It is better to use a list comprehension.")

    print(
        f"Loop time: {loop_time}|List comprehension time: {comprehension_time}")


if __name__ == '__main__':
    main()
