import threading
import os
import time
import curses
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
        self.pongs = []
        self.balls = []


        self.fps = 15

        self.__create_walls()
        self.__create_pong()
        self.__create_ball()

        self.snake = Snake(40, 15)

        self.__game_loop()

    def __game_loop(self):
        threading.Thread(target=self.__render, daemon=True).start()
        self.__update()

    def __update(self):
        while True:
            # update game logic every x seconds

            # TODO game_over = False

            # TODO process_keyboard_input()

            # TODO check collision_ball()
            # TODO check_collision_snake()
            # TODO check_collision_pong()

            self.__update_ball()
            self.__update_pong()
            self.snake.update()
            
            time.sleep(.150)
        
    def __render(self):
        stdscr = curses.initscr()
        
        curses.start_color()
        curses.use_default_colors()
        try:
            for i in range(0, curses.COLORS): curses.init_pair(i, i, -1)
        except Exception:
            pass
        
        while True:
            stdscr.scrollok(True)
            stdscr.clear()
            self.field.clear()

            for wall in self.walls:
                wall.render(self.field)

            for pong in self.pongs:
                pong.render(self.field)

            for ball in self.balls:
                ball.render(self.field)

            self.snake.render(self.field)

            self.field.render(stdscr)
            stdscr.refresh()

            time.sleep(1/self.fps)

    def __create_walls(self):
        for y in range(self.field.get_height()):
            for x in range(self.field.get_width()):
                if (x == 0 or x == 1 or y == 0 or x > self.field.get_width() - 3 or y > self.field.get_height() - 2):
                    self.walls.append(Wall(x, y))

    def __create_pong(self):
        for y in range(self.field.get_height()):
            for x in range(self.field.get_width()):
                if ((x == 4 or x == 5) and (y >= 13 and y <= 17) ):
                    self.pongs.append(Pong(x, y))

    def __create_ball(self):
            for y in range(self.field.get_height()):
                for x in range(self.field.get_width()):
                    if ((x == 30) and (y == 15)):
                        self.balls.append(Ball(x, y))

    def __update_pong(self):
        up = self.pongs[2].get_y() >= self.balls[0].get_y()
        for pong in self.pongs:
            if up: pong.move_up()
            else: pong.move_down()
    
    def __update_ball(self):
        self.balls[0].move_left()
