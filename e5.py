from random import sample
import time


def countdown():
    a = sample(range(0, 10), 10)
    a.sort()
    a.reverse()
    lst = [str(i) for i in a]
    for i in lst:
        print(i)
        time.sleep(1)
    print("Пуск")
countdown()