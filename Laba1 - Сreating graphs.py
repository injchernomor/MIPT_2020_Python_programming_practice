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
    pass


def exercise5():
    pass


def exercise6():
    pass


print("Для выхода из программы нажмите цифру ноль")
Flag = True
while Flag:
    exercise_number = int(input("Введите номер упражнения, результат которого хотите уведеть. "))
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
