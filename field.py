import numpy as np
import curses

from entity import EntitySymbol
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
                self.screen[x][y] = EntitySymbol(None, '  ')
    
    def draw_symbol(self, x, y, symbol):
        self.screen[x][y] = symbol

    def render(self, window):
        try:
            for y in range(self.height):
                for x in range(self.width):
                    window.addstr(y, x * 2, str(self.screen[x][y]), curses.color_pair(self.screen[x][y].get_color()))
        except Exception:
            pass

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height