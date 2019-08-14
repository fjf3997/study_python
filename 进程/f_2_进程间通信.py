import time
import multiprocessing


def download_data(q):
    data = [11, 22, 33, 44]
    for d in data:
        q.put(d)



def process_data(q):
    data = list()
    while True:
        d = q.get()
        data.append(d)
        if q.empty():
            break
    print(data)

def main():
    q = multiprocessing.Queue()
    # q.put()
    # q.empty()
    # q.get()
    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p2 = multiprocessing.Process(target=process_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
