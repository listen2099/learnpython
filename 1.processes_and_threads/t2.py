import threading
import logging

FORMAT = '%(asctime)-15s\t [%(threadName)s,%(thread)8d] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker():
    for x in range(100):
        # print("{} is running!\n".format(threading.current_thread().name), end='')  # 线程不安全
        logging.info("{} is running!".format(threading.current_thread().name))  # 线程安全

for i in range(5):
    name = "worker-{}".format(i)
    threading.Thread(target=worker).start()


