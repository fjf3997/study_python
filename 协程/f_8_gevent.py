import gevent
import time
from gevent import monkey

monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)
        time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    gevent.joinall([
        gevent.spawn(f, 5),
        gevent.spawn(f, 5),
        gevent.spawn(f, 5)
    ])
    end_time = time.time()


    # g1.join()
    # end_time = time.time()
    # g2.join()
    #
    # g3.join()

    print(end_time-start_time)
