from entity import Entity, EntitySymbol

class Snake(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.direction = "up"

    def update(self):
        if self.direction == "up": self.move_up()

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u2715", 3))
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u2715", 3))