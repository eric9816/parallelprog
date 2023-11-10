import threading
from time import sleep

result = [1]

def task(i=1):
    print(f"-starting task with {threading.current_thread().name}, {threading.active_count()=}")
    global result
    sleep(i)
    result.append(1)
    print(f"---end task with {threading.current_thread().name}")

print(1)
task()
print(2)
thr_1 = threading.Thread(target=task, args=(4,))
print(3)
print(result)
thr_1.start()
print(4)
#thr_1.join()
print(5)

#print(f"{threading.active_count()=}")
print("END MAIN")
sleep(5)
print(result)