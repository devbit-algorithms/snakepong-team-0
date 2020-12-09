from entity import Entity
from ball import Ball

class Pong(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)


    def move_up(self):
        self.y = self.y - 1
    
    def move_down(self):
        self.y = self.y + 1

    def update_pong(self, ball):
        if ball.get_y() > self.get_y():
            self.move_down()
        if ball.get_y() < self.get_y():
            self.move_up()
