import csv
import matplotlib.pyplot as plt
import math

def appendAllPopulations(populationArr, row):
    for population in row:
        populationArr.append(int(population.replace(",", "")))

def getSize(sizeArr, m, f):
    for index in range(len(m)):
        sizeArr.append(math.sqrt(int(m[index].replace(",", "")) + int(f[index].replace(",", ""))))

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

f = open('../data/gender.csv', encoding='cp949')
data = csv.reader(f)
m = []
f = []
size = []

for row in data :
    if name in row[0] :
        appendAllPopulations(m, row[3:104])
        appendAllPopulations(f, row[106:])
        getSize(size, row[3:104], row[106:])
        break

plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.scatter(m, f, s = size, c= range(101), alpha=0.7, cmap='ocean')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('Male')
plt.ylabel('Female')
plt.show()