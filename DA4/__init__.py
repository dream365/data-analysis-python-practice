import csv

f = open('../data/subwayfee.csv', encoding='cp949')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
mx_station = ''

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if (row[4] + row[6]) > 100000:
        rate = row[4] / (row[4] + row[6])
        if rate > mx:
            mx = rate
            mx_station = row[3] + ' ' + row[1]

print(mx_station, round(mx * 100, 2))

