from collections.abc import Iterable
from collections.abc import Iterator


class Classmate:
    def __init__(self):
        self.list = list()

    def add(self, content):
        self.list.append(content)

    def __iter__(self):
        return ClassmateIterator()


class ClassmateIterator:
    def __iter__(self):
        pass

    def __next__(self):
        return 11


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
    # for one in classmate:
    #     print(one)


if __name__ == "__main__":
    main()
