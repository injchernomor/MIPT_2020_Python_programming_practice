import numpy as np
import matplotlib.pyplot as plt


def exercise1():
    x = np.arange(0.1, 30.01, 0.01)
    plt.plot(x, np.log((np.e ** (1 / (np.sin(x) + 1))) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2))
    plt.grid(True)
    plt.show()
    x = 1
    print("Значение в точке x = 1: ",
          np.log((np.e ** (1 / (np.sin(x) + 1))) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2))
    x = 100
    print("Значение в точке x = 100: ",
          np.log((np.e ** (1 / (np.sin(x) + 1))) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2))
    x = 1000
    print("Значение в точке x = 1000: ",
          np.log((np.e ** (1 / (np.sin(x) + 1))) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2))


def exercise2():
    x = np.arange(-10, 10, 1)
    plt.plot(x, x * x - x - 6)
    plt.grid(True)
    plt.show()


def exercise3():
    x = np.arange(4, 10, 0.1)
    plt.plot(x, np.log((x ** 2 + 1) * np.exp(-abs(x) / 10)) / np.log(1 + np.tan(1 / (np.sin(x) ** 2))))
    plt.grid(True)
    plt.show()


def exercise4():
    with plt.xkcd():
        chart_title = str(input("Введите название диаграммы: "))
        print("Введите 4 раза через пробел: Название области - процентное значение области.")
        y1, x1 = map(str, input().split())
        y2, x2 = map(str, input().split())
        y3, x3 = map(str, input().split())
        y4, x4 = map(str, input().split())
        x1 = eval(x1)
        x2 = eval(x2)
        x3 = eval(x3)
        x4 = eval(x4)
        plt.pie([x1, x2, x3, x4], labels=(y1, y2, y3, y4))
        plt.title(chart_title)
        plt.show()


def exercise5():
    print("АААА!!!! Мне не хватает математического аппарата или умений. Разбираться лень."
          "Лаб по физике, как и самой физики - у меня пока еще не было...")


def exercise6():
    x = np.arange(-2, 2, 0.001)
    n = 0
    while True:
        plt.plot(x, 0.5 ** n * np.cos(3 ** n * np.pi * x))
        n += 1
        plt.grid(True)
        plt.show()


print("Для выхода из программы введите цифру ноль.")
Flag = True
while Flag:
    exercise_number = int(input("Введите номер упражнения, результат которого хотите уведеть: "))
    if exercise_number == 1:
        exercise1()
    elif exercise_number == 2:
        exercise2()
    elif exercise_number == 3:
        exercise3()
    elif exercise_number == 4:
        exercise4()
    elif exercise_number == 5:
        exercise5()
    elif exercise_number == 6:
        exercise6()
    elif exercise_number == 0:
        Flag = False
