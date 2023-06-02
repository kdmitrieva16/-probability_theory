# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9,
# для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен:
# a). первым спортсменом
# б). вторым спортсменом
# в). третьим спортсменом.

p = 1 / 3 * 0.9 + 1 / 3 * 0.8 + 1 / 3 * 0.6
print(f'Вероятность того, что мишень поражена: {round(p, 4)}')

p1 = 1 / 3 * 0.9 / p
print(f'Вероятность того, что 1-й стрелок попал : {round(p1, 4)}')

p2 = 1 / 3 * 0.8 / p
print(f'Вероятность того, что 2-й стрелок попал : {round(p2, 4)}')

p3 = 1 / 3 * 0.6 / p
print(f'Вероятность того, что 3-й стрелок попал : {round(p3, 4)}')