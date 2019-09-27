from player import Player
from hamsters import Hamster

class Game():
    hamsters_count=4 # Кол. Хомяков в игре
    x_n = 4  # Кол. столбцов в игре
    y_n = 4  # Кол. строк в игре

    def __init__(self):
        self.hamsters=[Hamster(i,self.x_n,self.y_n) for i in range(self.hamsters_count)]
        self.player=Player()

    def add_point(self,position,name,li_map):
        x = position[0]
        y = position[1]
        li_map[y] = li_map[y][:x*3]+ name+'  ' + li_map[y][x*3+3:]
        return li_map


    def render_map(self):
        x_n=self.x_n
        y_n=self.y_n
        li_map = ["*  " * x_n for i in range(y_n)]
        x=self.player.position[0] #Координата героя по х
        y=self.player.position[1] #Координата героя по y
        li_map=self.add_point([x,y],'X',li_map)
        for ham in self.hamsters:
            x=ham.position[0]
            y=ham.position[1]
            li_map=self.add_point([x,y],str(ham.hid+1),li_map)
        print('\n'.join(li_map))

    def move_player(self,destination):
        """destination== a,s,w,d"""
        x_n = self.x_n
        y_n = self.y_n
        x = self.player.position[0]  # Координата героя по х
        y = self.player.position[1]  # Координата героя по y
        if destination=="w" and not y==0:
            self.player.position[1]-=1
        elif destination=='s' and not y==y_n-1:
            self.player.position[1]+=1
        elif destination == 'a' and not x == 0:
            self.player.position[0] -= 1
        elif destination == 'd' and not x == x_n-1:
            self.player.position[0] += 1
        else:
            print('Вы ввели не корректные данные')
            return False
        self.on_move()

    def on_move(self):
        pass

    def start(self):
        self.render_map()
        while True:
            print("a- направо, d налево, w вверх, s вниз, q - выход")
            command=input("Ведите команду: ")
            if command in ['a','d','w','s']:
                self.move_player(command)
                self.render_map()
            elif command=='q':
                print('Game over')
                break
game=Game()
game.start()