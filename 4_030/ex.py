
studentCnts = (1, 18), (2, 19), (3, 23), (4, 21), (5, 20), (6, 22), (7, 17)
sum = 0
avg = 0


n = 0
while n < len(studentCnts):
    print(f'{studentCnts[n][0]}반 학생 수 : {studentCnts[n][1]}')

    sum += studentCnts[n][1]
    n += 1

avg = sum / len(studentCnts)
print(f'총 학생 수 : {sum:.2f}')
print(f'평군 학생 수 : {avg:.2f}')
print(f'평군 학생 수 : {(sum / len(studentCnts)):.2f}')