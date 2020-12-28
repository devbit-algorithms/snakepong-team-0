from entity import Entity, EntitySymbol
from ball import Ball

class Pong(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update_pong(self, ball):
        if ball.get_y() > self.get_y():
            self.move_down()
        if ball.get_y() < self.get_y():
            self.move_up()

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u0023", 1))