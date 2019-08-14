import threading
import time

g_nums = [11, 22]


def test1(nums):
    nums.append(33)
    print("-----test1------%s" % str(nums))


def test2(nums):
    print("-----test2------%s" % str(nums))

def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("------main--------%s" % str(g_nums))


if __name__ == "__main__":
    main()
