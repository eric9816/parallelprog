import threading
import time

# 1. Создайте и запустите поток - таймер с целевой функцией test.
def ttest(timeout: int) -> None:
    print(f"{threading.current_thread().name} started")
    time.sleep(timeout)
    print(f"{threading.current_thread().name} executed")

# tm = threading.Timer(1, function=ttest, args=(3, ))
# tm.start()
# tm.join()

# 2. Создайте поток - таймера демоническим.
# my_timer = threading.Timer(1, function=ttest, args=(3, ))
# my_timer.daemon = True
# my_timer.name = 'my_timer'
# my_timer.start()
# my_timer.join(2)

# 3. Проверьте, что отмена уже запущенного потока (поток, который уже вызвал свою задачу) не выполняется.
my_timer = threading.Timer(1, function=ttest, args=(3, ))
my_timer.name = 'my_timer'
my_timer.start()
my_timer.join(1)
my_timer.cancel()
