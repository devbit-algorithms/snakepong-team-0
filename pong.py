from entity import Entity, EntitySymbol
from ball import Ball

class Pong(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move_up(self):
        self.y = self.y - 1
    
    def move_down(self):
        self.y = self.y + 1

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u0023", 3))