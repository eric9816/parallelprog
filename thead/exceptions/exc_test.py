import threading
import sys


def task():
    raise TypeError("ops, TypeError")


def sys_custom_hook(*args):
    print(*args, sep="\n")
    print(f"{threading.current_thread().name=} failed")


sys.excepthook = sys_custom_hook

task()