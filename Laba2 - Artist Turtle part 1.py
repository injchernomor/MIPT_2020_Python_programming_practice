from turtle import *
import numpy

width(5)
shape('turtle')


def exercise2():
    shape('turtle')
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)

def exercise3():
    for i in range(4):
        forward(100)
        right(90)


def exercise4():
    for i in range(180):
        forward(5)
        right(2)


def exercise5():
    step = 0
    y = 0
    x = 0
    for i in range(10):
        step += 50
        y += 25
        x -= 25
        pendown()
        for j in range(4):
            forward(step)
            right(90)
        penup()
        goto(x, y)


def exercise6():
    # n = int(input("Введите n: "))
    n = 12
    for i in range(n):
        angle_step = 360 / n
        forward(100)
        stamp()
        right(180)
        forward(100)
        right(angle_step)


def exercise7():
    length = 0.01
    for i in range(900):
        forward(length)
        right(2 / 2 * numpy.pi)
        length += 0.01


def exercise8():
    length = 10
    for i in range(30):
        forward(length)
        right(90)
        length += 10


def exercise9():
    n = 3
    x = 0
    y = 0
    step = 50
    for i in range(10):
        for j in range(n):
            forward(step)
            right(360 / n)
        n += 1
        step += 20
        penup()
        x -= 10
        y += 20
        goto(x, y)
        pendown()


def exercise10():
    speed(1000)
    for i in range(6):
        exercise4()
        right(60)


def exercise11():
    speed(1000)
    x = 36  # 36 раз по 10 шагов отрезков
    y = 10
    R = 50  # радиус

    right(270)  # разварот как на гифке

    for j in range(10):
        L = 2 * 3.14 * R  # длина окружности
        for i in range(x):
            forward(L / x)
            right(y)

        for i in range(x):
            forward(L / x)
            left(y)

        R += 10


def exercise12():  # does not work
    speed(100000)
    x = 0
    y = 0
    right(270)  # разварот как на гифке

    def duga1():
        for i in range(100):
            forward(2)
            right(2)

    def duga2():
        for i in range(20):
            forward(2)
            right(2)

    for i in range(5):
        duga1()
        right(90)
        duga2()


def exercise13():
    pass


def exercise14():
    pass


print("Для выхода из программы введите цифру ноль.")
Flag = True
while Flag:
    exercise_number = int(input("Введите номер упражнения, результат которого хотите уведеть: "))
    if exercise_number == 2:
        exercise2()
        reset()
    elif exercise_number == 3:
        exercise3()
        reset()
    elif exercise_number == 4:
        exercise4()
        reset()
    elif exercise_number == 5:
        exercise5()
        reset()
    elif exercise_number == 6:
        exercise6()
        reset()
    elif exercise_number == 7:
        exercise7()
        reset()
    elif exercise_number == 8:
        exercise8()
        reset()
    elif exercise_number == 9:
        exercise9()
        reset()
    elif exercise_number == 10:
        exercise10()
        reset()
    elif exercise_number == 11:
        exercise11()
        reset()
    elif exercise_number == 12:
        exercise12()
        reset()
    elif exercise_number == 13:
        exercise13()
        reset()
    elif exercise_number == 14:
        exercise14()
        reset()
    elif exercise_number == 0:
        Flag = False

exercise12()
