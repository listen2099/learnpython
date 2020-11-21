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
    time.sleep(5)
    logging.info("{} is running!".format(threading.current_thread().name))


for i in range(1, 6):
    name = "worker-{}".format(i)
    if i < 5:
        threading.Thread(target=worker, name=name, daemon=True).start()  # 如果一个线程是daemon，主线程不等他结束，主线程运行到自己结束就全结束
    if i == 5:
        threading.Thread(target=worker1, name=name, daemon=False).start()

print(' ======= fin ======= ')
