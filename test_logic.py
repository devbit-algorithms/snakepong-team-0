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
    assert snake.get_x() == snakedown.get_x()
    assert snake.get_y() == snakedown.get_y()

def test_move_snake_up():
    snake = Snake(2,2)
    snakeup = Snake(2,1)
    snake.move_up()
    assert snake.get_x() == snakeup.get_x()
    assert snake.get_y() == snakeup.get_y()

def test_move_snake_left():
    snake = Snake(2,2)
    snakeleft = Snake(1,2)
    snake.move_left()
    assert snake.get_x() == snakeleft.get_x()
    assert snake.get_y() == snakeleft.get_y()

def test_move_snake_right():
    snake = Snake(2,2)
    snakeright = Snake(3,2)
    snake.move_right()
    assert snake.get_x() == snakeright.get_x()
    assert snake.get_y() == snakeright.get_y()

def test_move_down_pong():
    pong = Pong(0,2)
    pongdown = Pong(0,3)
    pong.move_down()
    assert pong.get_x() == pongdown.get_x()
    assert pong.get_y() == pongdown.get_y()

def test_move_up_pong():
    pong = Pong(0,2)
    pongup = Pong(0,1)
    pong.move_up()
    assert pong.get_x() == pongup.get_x()
    assert pong.get_y() == pongup.get_y()

def test_update_pong():
    ball = Ball(5,3)
    pong = Pong(0,6)
    pong.update_pong(ball)
    assert pong.get_y() == 5