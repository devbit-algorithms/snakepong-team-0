from entity import Entity, EntitySymbol

class Wall(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u2588", 3))