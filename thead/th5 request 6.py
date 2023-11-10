from time import sleep, perf_counter

headers_stor = {}
sources = ["bing.com",
           "google.ru",
           "yahoo.com",
           "mail.ru",
           "ya.ru"]
start_time = perf_counter()  # запускаем отсчет времени проверки решения

def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"


import threading

# Ваше решение
def task():
    threads = []
    for source in sources:
        thr = threading.Thread(target=get_request_header, args=(source, ), daemon=True)
        thr.start()
        threads.append(thr)

    for th in threads:
        th.join()

thr = threading.Thread(target=task, daemon=True)
thr.start()
thr.join(1.5)

for source in sources:
    if source not in headers_stor.keys():
        headers_stor[source] = "no_response"

assert perf_counter() - start_time <= 2  # проверка того, что решение выполняется не более 2 секунд

print(headers_stor)
print(", ".join(f'{k}-{v}' for k, v in sorted(headers_stor.items())))