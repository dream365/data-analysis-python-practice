import csv
import matplotlib.pyplot as plt

f = open('../temp_data/seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
days = []

for i in range(31):
    days.append([])

for row in data:
    date = row[0].split('-')
    month = int(date[1])
    day = int(date[2])

    if row[-1] != '':
        if month == 8:
            days[day - 1].append(float(row[-1]))

plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(days, showfliers=False)
plt.show()