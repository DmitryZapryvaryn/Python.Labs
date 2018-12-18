import pandas
from pandas import plotting
import matplotlib.pyplot as plt

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

groupby_gender = data.groupby('Gender')

data['Height'].fillna(method='pad', inplace=True)
data['Weight'].fillna(method='pad', inplace=True)
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']],
                        c=(data['Gender'] == 'Female'),
                        alpha=1, cmap='winter')

fig = plt.gcf()
fig.suptitle("blue: male, green: female", size=13)

'''
for gender, value in groupby_gender:
    plotting.scatter_matrix(value[['Weight', 'Height', 'MRI_Count']])
    plt.suptitle(gender)
'''

plt.show()
