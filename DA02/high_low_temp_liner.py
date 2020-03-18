import matplotlib.pyplot as plt
import csv

f = open('../data/seoul.csv', encoding='cp949')
data = csv.reader(f)
next(data)
high = []
low = []
years = []

for row in data:
    date = row[0].split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    if row[-1] != "" and row[-2] != "" and 1993 <= year:
        if month == 1 and day == 23:
            high.append(float(row[-1]))
            low.append(float(row[-2]))
            years.append(year)

plt.figure(figsize = (10, 6))
plt.title('high and low temperature by year')
plt.grid(True, linewidth=0.5, color='#97978F', linestyle='-')
plt.plot(years, high, 'hotpink', label = 'high')
plt.plot(years, low, 'skyblue', label = 'low')
plt.legend()
plt.show()