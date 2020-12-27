from entity import Entity, EntitySymbol

class Snake(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move_down(self):
        self.y = y  + 1

    def move_up(self):
        self.y = y - 1
    
    def move_left(self):
        self.x = x + 1

    def move_right(self):
        self.x = x - 1

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u2715", 3))