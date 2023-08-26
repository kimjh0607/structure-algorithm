
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
sum = 0
avg = 0

#고전 방법
# for index in range(len(studentCnts)):
#     print(f'{studentCnts[index][0]}반의 학생 수 : {studentCnts[index][1]}')

for innerIndex0, innerIndex1 in studentCnts:
    print(f'{innerIndex0}학급 학생수: {innerIndex1}명')
    sum += innerIndex1

avg = sum / len(studentCnts)
print(f'학생 총합 : {sum}')
print(f'평균 학생수: {avg:.2f}')