class Player:
    health=10
    max_health=10
    default_damage=1
    position=[0,0]
    def was_hit(self):
        self.health-=1
        if self.health>0:
            return True
        else:
            return False
    def wait(self):
        if self.health<self.max_health:
            self.health+=1
            print('Здоровье игрока -',self.health)
