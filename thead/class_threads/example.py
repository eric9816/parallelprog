import threading


class PrintThread(threading.Thread):  # наследуем оригинальный класс Thread

    def __init__(self, text):  # переопределение инициализатора
        # Инит вызывается главным потоком
        super().__init__()  # инициализация наследуемого класса threading.Thread
        self.text = text  # создание дополнительных атрибутов
        print('init', threading.active_count())

    def run(self):  # переопределение метода run
        # При вызове метода run создается дополнительный поток
        print('run', threading.active_count())
        print(self.text)


my_thread = PrintThread("Очень простой но бесполезный пример работы отдельного потока")
my_thread.start()
thread = threading.Thread()      # Создаем объект потока стандарным конструктором
print(my_thread.__dict__)        # Смотрим доступные методы и атрибуты обоих потоков
print(thread.__dict__)
