from random import *
from turtle import *

shape("turtle")
width(5)


def ex1():
    for i in range(50):
        step = randint(20, 100)
        angle_turn = randint(1, 360)
        right(angle_turn)
        forward(step)


ex1()