import csv
import matplotlib.pyplot as plt

def getSumAllPopulations(row):
    sum = 0
    for population in row:
        sum +=int(population.replace(",", ""))
    return sum

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

f = open('../data/gender.csv', encoding='cp949')
data = csv.reader(f)

size = []

for row in data :
    if name in row[0] :
        m = getSumAllPopulations(row[3:104])
        f = getSumAllPopulations(row[106:])
        break

size.append(m)
size.append(f)

color = ['crimson', 'darkcyan']
plt.axis('equal')
plt.pie(size, labels=['Male', 'Female'], autopct='%.1f%%', colors=color, startangle=90)
plt.title('Jeju Gender Ratio')
plt.show()