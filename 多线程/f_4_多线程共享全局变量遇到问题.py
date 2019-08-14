import threading
import time

g_num = 0
mutex = threading.Lock()


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----test1------%s" % str(g_num))


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----test2------%s" % str(g_num))


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()
    time.sleep(4)
    print("------main--------%s" % str(g_num))


if __name__ == "__main__":
    main()
