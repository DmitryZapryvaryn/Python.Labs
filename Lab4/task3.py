import pandas
from pandas import plotting
import matplotlib.pyplot as plt

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

groupby_gender = data.groupby('Gender')

for gender, value in groupby_gender:
    plotting.scatter_matrix(value[['Weight', 'Height', 'MRI_Count']])
    plt.suptitle(gender)

plt.show()
