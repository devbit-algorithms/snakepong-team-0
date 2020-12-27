from ball import Ball
from dllist import DoubleLinkedList
from entity import Entity
from field import Field
from game import Game
from pong import Pong
from snake import Snake
from wall import Wall

def test_move_snake_down():
    snake = Snake(2,2)
    snakedown = Snake(2,3)
    snake.move_down()
    assert snake == snakedown

def test_move_snake_up():
    snake = Snake(2,2)
    snakeup = Snake(2,1)
    snake.move_up()
    assert snake == snakeup

def test_move_snake_left():
    snake = Snake(2,2)
    snakeleft = Snake(1,2)
    snake.move_left()
    assert snake == snakeleft

def test_move_snake_right():
    snake = Snake(2,2)
    snakeright = Snake(3,2)
    snake.move_down()
    assert snake == snakeright