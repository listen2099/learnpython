import threading
import time


def worker():
    counter = 0
    while True:
        print("I am working!")
        counter += 1
        if counter > 10:
            break


t = threading.Thread(target=worker, name='worker_thread')

if __name__ == '__main__':
    print('========== fin ========')
    t.start()
