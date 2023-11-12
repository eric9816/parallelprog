import threading
from time import sleep, time

def task():
    sleep(2)


def log_task():
    print('Не успешно((')


def thread_log(t_check):
    # дополните код
    thread = threading.Thread(target=task, daemon=True)
    thread.name = 'Thread'
    timer = threading.Timer(interval=t_check, function=log_task)
    timer.name = 'Timer'

    thread.start()
    timer.start()

    thread.join(t_check)
    timer.cancel()
    timer.join()




thread_log(1)

def test_thread_timer(t_check):
    thread = threading.Thread(target=executer, daemon=True, name='Thread') # демон
    timer = threading.Timer(interval=t_check, function=logging) # таймер
    timer.name = 'Timer'
    # запускаем оба
    thread.start() # выполняется в фоне
    timer.start() # выполнится по истечению времени
    #
    thread.join(t_check+0.01) # основной поток будет ожидать чуть больше времени выполнения, чем заложено в таймер на этом этапе
    # если задача выполнится быстрее перейдем на этап отмены;
    timer.cancel() # если таймер истек и запустился, то мы его уже не отменим
    timer.join() # отработает только если таймер не отменился; ожидаем завершения таймера