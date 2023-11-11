import threading
from time import sleep

valid_cards = [str(i) for i in range(4007000000028, 4007000000100)]

money = 0


def do_request(card_number: str):
    global money
    sleep(2)
    money += 5


def target():
    threads = []
    for card in valid_cards:
        thr = threading.Thread(target=do_request, args=(card, ), daemon=True)
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()


th = threading.Thread(target=target, daemon=True)
th.start()
th.join(3.9)

print(money)