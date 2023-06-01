# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57,
# 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов
# наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

import pandas as pd
import numpy as np

data = pd.Series(
    [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84,
     90, 150])
sa = data.sum() / data.count()
print(sa)
print(np.mean(data))
sd = np.sqrt(((data - sa) ** 2).sum() / data.count())
print(sd)
print(np.std(data))
variance = ((data - sa) ** 2).sum() / data.count()
print(np.var(data))
print(variance)
variance2 = ((data - sa) ** 2).sum() / (data.count() - 1)
print(variance2)
print(np.var(data, ddof=1))
