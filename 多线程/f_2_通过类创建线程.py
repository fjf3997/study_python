import threading
import time


class Mythread(threading.Thread):
    def run(self) -> None:
        for i in range(5):
            msg = "I'm "+ self.name + "  "+ str(i);
            print(msg)
            time.sleep(1)


if __name__ == "__main__":
    t = Mythread()
    t.start()
