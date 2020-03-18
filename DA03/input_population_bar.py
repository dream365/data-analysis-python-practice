import csv
import matplotlib.pyplot as plt

def appendAllPopulations(populationArr, row):
    for population in row:
        populationArr.append(int(population.replace(",", "")))

f = open('../data/age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
populationArr = []

for row in data:
    if name in row[0]:
        appendAllPopulations(populationArr, row[3:])

plt.style.use('ggplot')
plt.figure(figsize = (10, 6), dpi=300)
plt.title('Korea Population')
plt.bar(range(101), populationArr, color = 'red')
plt.show()


