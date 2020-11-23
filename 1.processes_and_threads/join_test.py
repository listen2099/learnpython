import threading
import logging
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s,%(thread)8d] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker():
    for x in range(100):
        time.sleep(0.5)
        # print("{} is running!\n".format(threading.current_thread().name), end='')  # 线程不安全
        logging.info("{} is running!".format(threading.current_thread().name))  # 线程安全


def worker1():
    time.sleep(3)
    logging.info("{} is running!".format(threading.current_thread().name))


t = threading.Thread(target=worker1, name='work-xyz', daemon=True)
t.start()
t.join()  # 在哪个线程里运行，这个线程就等待join前的线程

print(' ======= fin ======= ')
