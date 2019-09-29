class Player:
    health=10
    default_damage=10
    position=[0,0]
    def was_hit(self):
        self.health-=1
        if self.health>0:
            return True
        else:
            return False