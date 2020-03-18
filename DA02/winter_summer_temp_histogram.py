import csv
import matplotlib.pyplot as plt

f = open('../temp_data/seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
jan = []
aug = []

for row in data:
    month = int(row[0].split('-')[1])
    if row[-1] != '':
        if month == 8:
            aug.append(float(row[-1]))
        elif month == 1:
            jan.append(float(row[-1]))

plt.hist(jan, bins=100, color='b', label='january')
plt.hist(aug, bins=100, color='r', label='august')
plt.legend()
plt.show()