import threading
from time import sleep, perf_counter

result = "*"


def task(time_sleep = 0, s: str = "*"):
    global result
    sleep(time_sleep)
    result += f"--{s}!"


task()
thr_1 = threading.Thread(target=task, args=(1, "1"))
thr_1.start()
thr_2 = threading.Thread(target=task, args=(3, "2"))
thr_2.start()

start_t = perf_counter()
thr_1.join(1.5)
print(f"1 - {perf_counter() - start_t}")

start_t = perf_counter()
thr_2.join(2.2)
print(f"2 - {perf_counter() - start_t}")


print(result)