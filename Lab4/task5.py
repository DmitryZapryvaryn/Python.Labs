import pandas
import numpy as np
from statsmodels.formula.api import ols
from scipy import stats

x = np.linspace(-5, 5, 20)
np.random.seed(1)

y = -5 + 3*x + 4 * np.random.normal(size=x.shape)

data = pandas.DataFrame({'x': x, 'y': y})

model = ols("y ~ x", data).fit()
print(model.summary())

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")
model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())

data_fsiq = pandas.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pandas.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pandas.concat((data_fsiq, data_piq))
print(data_long)
model = ols("iq ~ type", data_long).fit()
print(model.summary())

print('t-test(independent):\n', stats.ttest_ind(data['FSIQ'], data['PIQ']))
print('t-test(related):\n', stats.ttest_rel(data['FSIQ'], data['PIQ']))