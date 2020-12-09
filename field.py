import numpy as np

from wall import Wall

class Field:
    def __init__(self, width = 30, height = 30):
        self.width = width
        self.height = height
        self.screen = [[i for i in range(height)] for j in range(width)]
        self.clear()

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.screen[x][y] = '  '
    
    def draw_symbol(self, x, y, symbol):
        self.screen[x][y] = symbol
    
    def output_to_terminal(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.screen[x][y], end='')
            print('')
        print('')