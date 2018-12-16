import pandas
import numpy as np

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")
print(data)

t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

data1 = pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
print(data1)
print(type(data1))
