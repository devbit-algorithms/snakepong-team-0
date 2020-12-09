from entity import Entity, EntitySymbol

class Snake(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    # def update(self):
def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u2715", 3))