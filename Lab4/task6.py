import seaborn
import pandas
import matplotlib.pyplot as plt

names = [
    'EDUCATION: Number of years of education',
    'SOUTH: 1=Person lives in South, 0=Person lives elsewhere',
    'SEX: 1=Female, 0=Male',
    'EXPERIENCE: Number of years of work experience',
    'UNION: 1=Union numberm, 0=Not union number',
    'WAGE: Wage (dollar per hour)',
    'AGE: years',
    'RACE: 1=Other, 2=Hispanic, 3=White',
    'OCCUPATION: 1=Management, 2=Sales, 3=Clerical, 4=Service, 5=Professional, 6=Other',
    'SECTOR: 0=Other, 1=Manufacturing, 2=Construction',
    'MARR: 0=Unmarried, 1=Married',
]

short_names = [n.split(':')[0] for n in names]
data = pandas.read_csv('Lab4/data2.txt', sep='	')
data.columns = short_names

seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'], kind='reg')
seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'], kind='reg', hue='SEX')
seaborn.lmplot(y='WAGE', x='EDUCATION', data=data)

plt.show()
