# Задача 3 (Дополнительно) Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что
# изменение коэффициентов должно производиться
# на каждом шаге одновременно (то есть изменение одного коэффициента не должно
# влиять на изменение другого во время одной итерации).


import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


def mse_b0b1(b0, b1, x, y):
    return np.sum(((b0 + b1 * x) - y) ** 2) / len(x)


def mse_pb0(b0, b1, x, y):
    return 2 * np.sum((b0 + b1 * x) - y) / len(x)


def mse_pb1(b0, b1, x, y):
    return 2 * np.sum(((b0 + b1 * x) - y) * x) / len(x)


alpha = 1e-5
b0 = 0.1
b1 = 0.1
mseb0b1_min = mse_b0b1(b0, b1, zp, ks)
i_min = 1
b0_min = b0
b1_min = b1
iteration = 1000000
for i in range(iteration):
    b0 -= alpha * mse_pb0(b0, b1, zp, ks)
    b1 -= alpha * mse_pb1(b0, b1, zp, ks)
    if i % 50000 == 0:
        print(f'>>> Итерация #{i}, b0={b0}, b1={b1}, mse={mse_b0b1(b0, b1, zp, ks)}')
    if mse_b0b1(b0, b1, zp, ks) > mseb0b1_min:
        print(
            f'>>> Итерация #{i_min}, b0={b0_min}, b1={b1_min}, mse={mseb0b1_min},\n Достигнут минимум.')
        break
    else:
        mseb0b1 = mse_b0b1(b0, b1, zp, ks)
        i_min = i
        b1_min = b1
        b0_min = b0
print(f'>>> b0 = {b0_min}\n>>> b1 = {b1_min}')


# >>> b0 = 441.3964121468653
# >>> b1 = 2.641007764600045 mse=6473.672292822534