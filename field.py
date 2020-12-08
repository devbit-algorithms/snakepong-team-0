import numpy as np

class Field:
    def __init__(self, width = 30, height = 30):
        self.width = width
        self.height = height
        self.screen = np.array([[i for i in range(height)] for j in range(width)], dtype=str)

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.screen[i][j] = ' '
    
    def draw_symbol(self, x, y, symbol):
        self.screen[x][y] = symbol
    
    def output_to_terminal(self):
        for j in range(self.width):
            for i in range(self.height):
                print(self.screen[i][j], end=' ')
            print('\n')
        print('\n')       
                


field = Field()
field.clear()
field.output_to_terminal()