import csv
import matplotlib.pyplot as plt

def appendAllPopulations(populationArr, row):
    for population in row:
        populationArr.append(int(population.replace(",", "")))

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

f = open('../data/gender.csv', encoding='cp949')
data = csv.reader(f)
m = []
f = []

for row in data :
    if name in row[0] :
        appendAllPopulations(m, row[3:104])
        appendAllPopulations(f, row[106:])

plt.style.use('ggplot')
plt.figure(figsize = (10, 6), dpi=300)
plt.title('Population by gender')
plt.barh(range(101), [-1 * population for population in m], color = 'skyblue', label = "Male")
plt.barh(range(101), f, color = 'hotpink', label = "Female")
plt.legend()
plt.show()