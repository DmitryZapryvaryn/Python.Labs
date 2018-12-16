import pandas
import numpy as np
import matplotlib.pyplot as plt

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")
print(data.shape)
print(data.columns)
print(data['Gender'])
print(data[data['Gender'] == 'Female']['VIQ'].mean())

groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))
    
print('\nGender count:\n',groupby_gender.size())

print('\nGender means:\n', groupby_gender.mean())

print('\nGender MRI mean:\n', groupby_gender['MRI_Count'].mean())

print('\nData VIQ mean:\n', data['VIQ'].mean())

groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])

plt.show()
