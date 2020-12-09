from entity import Entity

class Wall(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), "\033[36m\u2588\u2588\033[0m")