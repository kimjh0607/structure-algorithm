
# 튜플을 사용하여 학생 수가 가장 많은 학급 적은 학급 구하기

studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)

maxStuCnts = 0
maxStuClass = 0
minStuCnts = 0
minStuClass = 0

for claNo, stuCnt in studentCnts:
    if maxStuCnts < stuCnt:
        maxStuCnts = stuCnt
        maxStuClass = claNo

print(f'가장 학생 수 많은 반 : {maxStuClass}반 {maxStuCnts}명')

for claNo, stuCnt in studentCnts:
    
    if minStuCnts == 0 or minStuCnts > stuCnt: # minStuCnts == 0 가 뽀인트
        minStuCnts = stuCnt
        minStuClass = claNo

print(f'가장 학생 수 적은 반 : {minStuClass}반 {minStuCnts}명')