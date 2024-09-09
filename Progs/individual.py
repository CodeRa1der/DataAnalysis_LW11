#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs, factorial, pow, e, sin, isclose
from multiprocessing import Process, Queue

E = 10e-7

# Вариант 9
def var_1(x, queue):
    mnum = x
    S, k = mnum, 2

    while fabs(mnum) > E:
        kf = (2 * k) + 1
        mnum = (pow(-1, k) * pow(x, kf)) / kf
        S += mnum
        k += 1

    queue.put(S)


# Вариант 10
def var_2(x, queue):
    mnum = x
    S, k = mnum, 2

    while fabs(mnum) > E:
        kf = 2 * k
        mnum = pow(x, kf) / factorial(kf)
        S += mnum
        k += 1

    queue.put(S)


def main():
    queue = Queue()

    x1 = 1.0
    x2 = 1.0

    proc1 = Process(target=var_1, args=(x1, queue))
    proc2 = Process(target=var_2, args=(x2, queue))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    result1 = queue.get()
    result2 = queue.get()

    control1 = sin(x1)
    control2 = pow(e, x2)

    print(f"x1 = {x1}")
    print(f"Сумма ряда 1: {round(result1, 4)}")
    print(f"Контрольное значение ряда 1: {round(control1, 4)}")
    print(f"Проверка 1: {isclose(result1, control1, rel_tol=1e-4)}")

    print(f"x2 = {x2}")
    print(f"Сумма ряда 2: {round(result2, 4)}")
    print(f"Контрольное значение ряда 2: {round(control2, 4)}")
    print(f"Проверка 2: {isclose(result2, control2, rel_tol=1e-4)}")


if __name__ == "__main__":
    main()