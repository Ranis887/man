from time import time, localtime


class Clock:
    @staticmethod
    def say_time():
        res = localtime(time())
        print(f"{res.tm_hour} : {res.tm_min} : {res.tm_sec}")


Clock.say_time()
