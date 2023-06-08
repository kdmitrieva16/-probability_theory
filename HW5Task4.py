# Есть ли статистически значимые различия в среднем росте матерей и
# дочерей?
# двухвыборочный зависимый тест
import pandas as pd
import numpy as np
from scipy import stats

mother = pd.Series(
    [172, 177, 158, 170, 178, 175, 164, 160, 169, 165])

daughter = pd.Series(
    [173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

motherSA = np.mean(mother)
daughterSA = np.mean(daughter)
res = stats.ttest_rel(mother, daughter)
print(res)

# alfa=0.05 < pvalue 0.5228168632983574 статистически значимых различий нет