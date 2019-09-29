from random import randint


class Hamster:
    li_positions = [[0, 0]]
    def __init__(self,hid, x_n, y_n):
        self.hid=hid
        self.helth = randint(1, 4)
        self.position = self.get_possition(x_n,y_n)

    def get_possition(self,x,y):
        while True:
            var_new_position=[randint(0, x - 1), randint(0, y - 1)]
            if not var_new_position in self.li_positions:
                self.li_positions.append(var_new_position)
                return var_new_position


    def on_shot(self,hamsters):
        self.helth-=1
        if self.helth==0:
            print(self.hid+1, 'was kiled')
            hamsters.remove(self)
            return True
        else:
            print(self.hid + 1, 'was not kiled')
            return False


