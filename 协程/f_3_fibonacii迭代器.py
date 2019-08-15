class Fibo:
    def __init__(self, num):
        self.num = num
        self.curr = 1
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr < self.num:
            tem = self.a
            self.a, self.b = self.b, self.a+self.b
            self.curr += 1
            return tem

        else:
            raise StopIteration


def main():
    for num in Fibo(10):
        print(num)


if __name__ == "__main__":
    main()
