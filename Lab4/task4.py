from scipy import stats
import pandas

data = pandas.read_csv('Lab4/brain_size.csv', sep=';', na_values=".")

print("ttest_1samp(data['VIQ'], 0):\n", stats.ttest_1samp(data['VIQ'], 0))

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']

print(
    'stats.ttest_ind(female_viq, male_viq):\n', stats.ttest_ind(
        female_viq, male_viq))

print(
    "stats.ttest_rel(data['FSIQ'], data['PIQ']):\n", stats.ttest_rel(
        data['FSIQ'], data['PIQ']))

print(
    "stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0):\n", stats.ttest_1samp(
        data['FSIQ'] - data['PIQ'], 0))

print(
    'stats.kruskal(female_viq, male_viq):\n', stats.kruskal(
        female_viq, male_viq))
