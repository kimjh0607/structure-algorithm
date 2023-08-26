
cars = ('그랜저', '소나타', '말리부', '카니발', '쏘렌토')

n = 0
while n < len(cars):
    print(cars[n])
    n += 1


n = 0
flag = True #플래그 변수 사용
while flag:
    print(cars[n])
    n += 1

    if n == len(cars):
        flag = False


n = 0
while True:
    print(cars[n])
    n += 1

    if n == len(cars):
        break #break로 빠져나오기


studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

n = 0
while n < len(studentCnts):
    print('{}학급 학생수: {} '.format(studentCnts[n][0], studentCnts[n][1]))
    n += 1