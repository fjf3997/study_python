class File:
    def __init__(self, filename, mode):
        self.filenaem = filename
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.f = open(self.filenaem,self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.f.close()


if __name__ == '__main__':
    with File("context", "a") as f:
        f.write("hello,it' me\n")
