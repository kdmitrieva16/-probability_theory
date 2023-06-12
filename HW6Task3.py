# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
#
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

import pandas as pd
import numpy as np
from scipy import stats

mother = pd.Series([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughter = pd.Series([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

nm = len(mother)
nd = len(daughter)

xm = np.mean(mother)
xd = np.mean(daughter)

delta = xm - xd

dm = np.var(mother, ddof=1)
dn = np.var(daughter, ddof=1)
d = (dm + dn) / 2
s = np.sqrt(d / nm + d / nd)

alpha = 0.05
t0 = stats.t.ppf(1 - alpha / 2, df=2 * (nm - 1))
print(t0)
l_border = delta - t0 * s
r_border = delta + t0 * s
print(
    f'95% доверительный интервал для разности среднего роста родителей и детей: [{l_border:.4f}, {r_border:.4f}]')
