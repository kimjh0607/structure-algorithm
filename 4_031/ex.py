
# 학급별 학생수 max, min 학급 구하기

studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
minClaNo = 0
maxClaNo = 0
minStuCnt = 0
maxStuCnt = 0

n = 0
while n < len(studentCnts):
    if maxStuCnt < studentCnts[n][1]:
        maxClaNo = studentCnts[n][0]
        maxStuCnt = studentCnts[n][1]

    if minStuCnt == 0 or minStuCnt > studentCnts[n][1]:
        minClaNo = studentCnts[n][0]
        minStuCnt = studentCnts[n][1]

    n += 1

print(f'학생 수 가장 많은 반 : {maxClaNo}, 학생 수 : {maxStuCnt}')
print(f'학생 수 가장 적은 반 : {minClaNo}, 학생 수 : {minStuCnt}')
