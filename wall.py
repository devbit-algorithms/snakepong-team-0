from entity import Entity

class Wall(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, field):
        field.draw_symbol(self.getx(). self.gety(), '\u2588')