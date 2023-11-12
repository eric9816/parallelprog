import threading
from time import perf_counter as pc


def task():
    print(f"{threading.current_thread().name} started")


t_thr = threading.Timer(2, function=task)

start_time = pc()
t_thr.start()
# запуск потока-таймера не является блокирующим для выполнения других потоков
print(f"{threading.current_thread().name} not blocked")
t_thr.join()
print(f"after {pc() - start_time:.2f} sec.")

# MainThread not blocked
# Thread-1 started
# after 2.01 sec.