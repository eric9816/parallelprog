from threading import Timer
from time import sleep


def worker(task: str):
    sleep(2)
    print(f"{task=} done")

timer = Timer(interval=1, function=worker, args=("print", ))
timer.name = "new_timer"
timer.start()