"""Перехват ошибок"""
# import threading
# from time import sleep
#
#
# def task():
#     sleep(0.5)
#     raise Exception("!!! exception in task !!!")
#
#
# thread_1 = threading.Thread(target=task)
# thread_1.start()

import threading
import traceback
from time import sleep

# Функция перехвата
def custom_hook(arg):
    # print(arg) # Тут будет храниться вся инфа об ошибке
    # print(f"{threading.current_thread().name=} failed")
    exc_type, exc_value, exc_traceback, exc_thread = arg
    print(f"Тип исключения: {exc_type.__name__}")
    print(f"Сообщение исключения: {exc_value}")
    print(f"Номер потока: {exc_thread.ident}")
    print(f"Имя потока: {exc_thread.name}")
    print(f"Путь исключения:")
    traceback.print_tb(exc_traceback)

def task():
    sleep(0.5)
    raise Exception("!!! exception in task !!!")

# перехват exceptions
threading.excepthook = custom_hook

thread_1 = threading.Thread(target=task)
thread_1.start()