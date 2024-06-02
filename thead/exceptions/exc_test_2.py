import threading


def ttest_1():
    raise TypeError("some error")

def ttest_2():
    raise SyntaxError("some error")

def ttest_3():
    raise ZeroDivisionError("some error")

def ttest_4():
    raise SyntaxError("some error")


for function in (ttest_1, ttest_2, ttest_3, ttest_4):
    threading.Thread(target=function).start()

print("А главному потоку все равно")