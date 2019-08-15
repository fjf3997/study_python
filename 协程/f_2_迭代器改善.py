from collections.abc import Iterable
from collections.abc import Iterator
import time


class Classmate:
    def __init__(self):
        self.list = list()
        self.curr = 0

    def add(self, content):
        self.list.append(content)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < len(self.list):
            item = self.list[self.curr]
            self.curr += 1
            return item
        else:
            raise StopIteration


def main():
    classmate = Classmate()
    classmate.add(11)
    classmate.add(22)
    classmate.add(33)
    classmate.add(44)
    print("是否是可迭代的:", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)

    print("是否是迭代器:", isinstance(classmate_iterator, Iterator))
    print(next(classmate_iterator))
    for one in classmate:
        time.sleep(1)
        print(one)


if __name__ == "__main__":
    main()
