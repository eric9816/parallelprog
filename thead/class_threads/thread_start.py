import threading


class PrintThread(threading.Thread):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def start(self):
        print(self.text)


print_thread = PrintThread("Очень простой но бесполезный пример работы отдельного потока")
print_thread.start()