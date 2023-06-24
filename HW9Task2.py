# Задача 2 Посчитать коэффициент линейной регрессии при заработной плате (zp), используя
# градиентный спуск (без intercept).


import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


def mse(b1, x, y):
    return np.sum((b1 * x - y) ** 2) / len(x)


def mse_p(b1, x, y):
    return (2 / len(x)) * np.sum((b1 * x - y) * x)


alpha = 1e-6
b1 = 0.1
mse_min = mse(b1, zp, ks)
i_min = 1
b_min = b1
iteration = 10000
for i in range(iteration):
    b1 -= alpha * mse_p(b1, zp, ks)
    if i % 100 == 0:
        print(f'>>> Итерация #{i}, b1={b1}, mse={mse(b1, zp, ks)}')
    if mse(b1, zp, ks) > mse_min:
        print(
            f'>>> Итерация #{i_min}, b1={b_min}, mse={mse_min},\n>>> Достигнут минимум\n>>> Получили {b_min} ') #5.889820285147628 
        break
    else:
        mse_min = mse(b1, zp, ks)
        i_min = i
        b_min = b1
