import threading
import time


def worker():
    counter = 0
    while True:
        print("I am working!")
        counter += 1
        if counter > 2:
            break


X = 100


def add(x, y):
    ret = x + y
    print('='*20)
    print(1, ret, threading.current_thread())
    time.sleep(0.1)
    print(2, threading.current_thread())
    getthreadinfo()
    print('~'*20)
    return ret


def getthreadinfo():
    print('***', threading.current_thread(), threading.main_thread())


def show():
    getthreadinfo()


class MyThread(threading.Thread):
    def start(self):
        print('start~~~~~~~~~')
        super().start()

    def run(self):
        print('run~~~~~~~~~')
        super().run()
        #self._target(*self._args)


t = threading.Thread(target=worker, name='worker_thread')
t1 = MyThread(target=show)
t2 = threading.Thread(target=add, args=(4, 5))
t3 = threading.Thread(target=add, args=(3, 4))

if __name__ == '__main__':
    #ts[0].start()
    t1.start()
    t2.start()
    t3.start()

    time.sleep(1)
    print('+'*20)

    if t1.is_alive():
        print('alive')
    else:
        print('daed')
        print(t1)


    print('========== fin ========')


