import random as rd

types = ['A', 'B', 'O', 'AB']
todayData = []
typeCnt = []

for index in range(100):
    type = types[rd.randrange(len(types))]
    todayData.append(type)

print('todayData : {}'.format(todayData))
print('todayData length : {}'.format(len(todayData)))

for index in types:
    print('{} 갯수 : {}'.format(index, todayData.count(index)))

