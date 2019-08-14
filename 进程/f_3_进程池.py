from multiprocessing import Pool
import os
import time
import random


def worker(i):
    start_time = time.time()
    print("%s进程开始工作,进程号为%s" % (i, os.getpid()))
    time.sleep(random.random()*2)
    end_time = time.time()
    print("%s进程工作结束,执行时间为%s" % (i, (end_time-start_time)))


def main():
    po = Pool(3)
    for i in range(1, 10):
        po.apply_async(worker, (i,))
    print("---start-----")
    po.close()
    po.join()
    print("----end------")


if __name__ == "__main__":
    main()
