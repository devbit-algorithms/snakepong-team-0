import threading
import os
import time
import numpy as np
from dllist import DoubleLinkedList

from ball import Ball
from field import Field
from pong import Pong
from snake import Snake
from wall import Wall

class Game:
    def __init__(self):
        self.field = Field()
        self.walls = []

        self.fps = 15

        self.__create_walls()

        self.__game_loop()

    def __game_loop(self):
        threading.Thread(target=self.__render, daemon=True).start()
        self.__update()

    def __update(self):
        while True:
            # update game logic every x seconds

            time.sleep(1)

    def __render(self):
        while True:
            os.system('clear')
            self.field.clear()

            for wall in self.walls:
                wall.render(self.field)

            self.field.output_to_terminal()

            time.sleep(1/self.fps)

    def __create_walls(self):
        for y in range(self.field.get_height()):
            for x in range(self.field.get_width()):
                if (x == 0 or y == 0 or x == self.field.get_width() - 1 or y == self.field.get_height() - 1):
                    self.walls.append(Wall(x, y))