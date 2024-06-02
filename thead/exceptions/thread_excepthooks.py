import threading


def task():
    raise TypeError("ops, TypeError")


def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    print(f"type: {exc_type}")
    print(f"value: {exc_value}")
    print(f"traceback: {exc_traceback}")
    print(f"thread: {exc_thread}")


threading.excepthook = custom_hook

thread = threading.Thread(target=task)
thread.start()