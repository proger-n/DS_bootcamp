def data_types():
    print(f"""[{', '.join([type(e).__name__ for e in [
          1, '1', 1.0, True, [], {}, (), set()]])}]""")


if __name__ == '__main__':
    data_types()
