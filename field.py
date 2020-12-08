import numpy as np

class Field:
    def __init__(self, width = 30, height = 30):
        self.width = width
        self.height = height
        self.screen = np.array([[i for i in range(height)] for j in range(width)])

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.screen[i][j] = 0
    


field = Field()
field.clear()
print(field.screen)
