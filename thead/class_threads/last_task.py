import threading

class NoTargetException(Exception):
    def __init__(self, err):
        super().__init__(err)
        print(f"{err} has no target")

class MyThread(threading.Thread):
    def __init__(self, target = None, result = None):
        super().__init__()
        self.target = target
        self.result = result

    def run(self):
        if not self.target:
            raise NoTargetException(self.name)
        else:
            self.result = self.target()


def custom_hook(arg):
    exc_type, value, trace, thread = arg
    msg = f'{thread.name} (id={thread.ident}) failed'
    print(msg)

threading.excepthook = custom_hook


def target():
    print('112121212')

MyThread().start()

