import threading
import time

mutex1 = threading.Lock()
mutex2 = threading.Lock()


class Mythread1(threading.Thread):
    def run(self) -> None:
        mutex1.acquire()
        print("--------1------up-----")
        time.sleep(1)
        mutex2.acquire()
        print("--------2-------down---")
        mutex2.release()
        mutex1.release()


class Mythread2(threading.Thread):
    def run(self) -> None:
        mutex2.acquire()
        print("--------2------up-----")
        time.sleep(1)
        mutex1.acquire()
        print("--------2-------down---")
        mutex1.release()
        mutex2.release()


def main():
    t1 = Mythread1()
    t2 = Mythread2()
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
