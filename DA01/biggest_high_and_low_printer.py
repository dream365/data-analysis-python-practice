import csv
import numpy as np

high_low_dict = {}
biggest_high_and_low_month = 0
biggest_high_and_low = 0

f = open('temp_data/seoul.csv', encoding='cp949')
data = csv.reader(f)
header = next(data)

for month in range(1, 13):
    high_low_dict[month] = []

for row in data:
    if row[-1] == "":
        row[-1] = -999
    if row[-2] == "":
        row[-2] = -999
    row[-1] = float(row[-1])
    row[-2] = float(row[-2])

    month = int(row[0][5:7])
    high_low_dict[month].append(row[-1] - row[-2] if not(row[-1] == -999 or row[-2] == -999) else 0)

for month in range(1, 13):
    mean = np.mean(np.array(high_low_dict[month]))
    if biggest_high_and_low < mean:
        biggest_high_and_low = mean
        biggest_high_and_low_month = month

print('평균적으로 일교차가 가장 큰 달은', biggest_high_and_low_month,'월로,', biggest_high_and_low, '도 였습니다.')
f.close()