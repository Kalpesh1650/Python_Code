from time import sleep
from threading import *

""" Create thread by extending Thread class """
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


thread1 = Hello()
thread2 = Hi()

thread1.start()
sleep(0.2)
thread2.start()

""" join will wait until current thread finishes execution """
thread1.join()
thread2.join()

print("Bye")