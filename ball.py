from entity import Entity, EntitySymbol

class Ball(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, field):
        field.draw_symbol(self.get_x(), self.get_y(), EntitySymbol(self, "\u006f", 3))

    # def move_down(self):
    #     self.y = self.y  + 1

    # def move_up(self):
    #     self.y = self.y - 1
    
    # def move_left(self):
    #     self.x = self.x - 1

    # def move_right(self):
    #     self.x = self.x + 1

    def move_diagonal_left_up(self):
        self.x = self.x - 1
        self.y = self.y - 1

    def move_diagonal_left_down(self):
        self.x = self.x - 1       
        self.y = self.y  + 1

    def move_diagonal_right_up(self):
        self.x = self.x + 1
        self.y = self.y - 1

    def move_diagonal_right_down(self):
        self.x = self.x + 1
        self.y = self.y  + 1