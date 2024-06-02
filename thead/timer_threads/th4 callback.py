from threading import Timer, Thread
from typing import Callable

def callback_handler(task: Callable = None, args=(), callback_task: Callable = None) -> None:
    global result
    # дополните код