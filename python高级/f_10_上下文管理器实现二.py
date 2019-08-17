from contextlib import contextmanager

@contextmanager
def my_open(file, mode):
    f = open(file, mode)
    yield f
    f.close()


if __name__ == '__main__':
    with my_open("context2", "w") as f:
        f.write("hello,fjf\n")