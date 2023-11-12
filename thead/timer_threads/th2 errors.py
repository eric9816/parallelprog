import threading
from typing import Callable
from time import sleep


def task():
    sleep(2)


def log_task():
    print('Не успешно((')


def thread_log(task: Callable, log_task: Callable, t_check) -> None:
    thread = threading.Thread(target=task, daemon=True)
    timer = threading.Timer(interval=t_check, function=log_task)
    thread.start()
    thread.join(t_check)

    timer.start()
    if thread.is_alive():
        timer.cancel()
    else:
        print('успех')
    timer.join()

thread_log(task, log_task, 1)