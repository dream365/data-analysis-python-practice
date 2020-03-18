import csv
import matplotlib.pyplot as plt

def appendAllPopulations(populationArr, row):
    for population in row:
        populationArr.append(int(population.replace(",", "")))

f = open('../data/age.csv', encoding='cp949')
data = csv.reader(f)
next(data)

sinlim_population = []
yeongdeungpo_population = []
sangbong_population = []
yeongtong_population = []
jeonmin_population = []
ages = []

for year in range(101):
    ages.append(year)

for row in data:
    if "영등포구 영등포본동" in row[0]:
        appendAllPopulations(yeongdeungpo_population, row[3:])
    elif "관악구 신림동" in row[0]:
        appendAllPopulations(sinlim_population, row[3:])
    elif "중랑구 상봉제1동" in row[0]:
        appendAllPopulations(sangbong_population, row[3:])
    elif "영통구 영통1동" in row[0]:
        appendAllPopulations(yeongtong_population, row[3:])
    elif "유성구 전민동" in row[0]:
        appendAllPopulations(jeonmin_population, row[3:])

plt.style.use('ggplot')
plt.figure(figsize = (10, 6), dpi=300)
plt.title('Korea Population')
plt.plot(ages, yeongdeungpo_population, 'hotpink', label="Yeongdeungpo")
plt.plot(ages, sinlim_population, 'blue', label="Sinlim")
plt.plot(ages, sangbong_population, 'green', label="Sangbong")
plt.plot(ages, yeongtong_population, 'gold', label="Yeongtong")
plt.plot(ages, jeonmin_population, 'red', label="Jeonmin")
plt.legend()
plt.show()


