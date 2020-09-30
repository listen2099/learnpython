import threading


def worker():
    for x in range(100):
        print("{} is running!".format(threading.current_thread().name))


for i in range(5):
    name = "worker-{}".format(i)
    threading.Thread(target=worker).start()
