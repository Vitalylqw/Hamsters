from random import randint


class Hamster:

    def __init__(self,hid, x_n, y_n):
        self.hid=hid
        self.helth = 1 #randint(1, 4)
        self.position = [randint(0, x_n-1), randint(0, y_n-1)]

    def on_shot(self,hamsters):
        self.helth-=1
        print(self.hid, 'was kiled')
        hamsters.remove(self)


