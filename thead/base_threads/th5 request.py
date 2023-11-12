import requests
from time import perf_counter
import threading


def target(headers_stor, source):
    headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0

threads = []
for source in sources:
    start_tmp = perf_counter()
    thr = threading.Thread(target=target, args=(headers_stor, source, ))

    # headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta
    thr.start()
    threads.append(thr)

for th in threads:
    th.join()

print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки