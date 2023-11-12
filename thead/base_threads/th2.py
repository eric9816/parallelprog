import threading
from time import sleep

result = "*"


def task(time_sleep = 0):
    global result
    sleep(time_sleep)
    result += "--*!"


task()
thr_1 = threading.Thread(target=task, args=(1, ))
thr_1.start()
thr_2 = threading.Thread(target=task, args=(2, ))
thr_2.start()


print(result)