
studentCnt = ({'cls01':18},
              {'cls02':21},
              {'cls03':20},
              {'cls04':19},
              {'cls05':22},
              {'cls06':20},
              {'cls07':23},
              {'cls08':17})
totalCnt = 0
minStuCnt = 0
minClass = ''
maxStuCnt = 0
maxClass = ''
dev = []

for index, dic in enumerate(studentCnt):
    for key, val in dic.items():
        totalCnt += val

        if maxStuCnt < val:
            maxStuCnt = val
            maxClass = key

        if minStuCnt > val or minStuCnt == 0:
            minStuCnt = val
            minClass = key

avgCnt = totalCnt/len(studentCnt)

print(f'전체 학생 수: {totalCnt}명')
print(f'평균 학생 수: {totalCnt/len(studentCnt)}명')
print(f'학생 수가 가장 적은 학급: {minClass}({minStuCnt}명)')
print(f'학생 수가 가장 많은 학급: {maxClass}({maxStuCnt}명)')

for index, dict in enumerate(studentCnt):
    for key, value in dict.items(): #
        dev.append({key : value-avgCnt})

print(f'반별 편차 : {dev}')
