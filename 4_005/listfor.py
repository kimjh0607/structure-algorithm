cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

for index in range(len(cars)):
    print(cars[index])

for car in cars:
    print(car)

studentCnts = [[1, 19], [2, 20], [3,22], [4, 18], [5,21]]

#방법1
for index in range(len(studentCnts)):
    print('{}학급 {}명의 학생 수'.format(studentCnts[index][0], studentCnts[index][1]))

#방법2
for classNo, cnt in studentCnts: # iterrable 객체에 변수를 두개 줄 수도 있다.
    print('{}학급 {}명의 학생 수'.format(classNo, cnt))

#실습
studentCnts = [[1, 18], [2, 19], [3,23], [4, 21], [5,20], [6,22], [7,17]]
sum = 0
avg = 0
for classNo, cnt in studentCnts:
    print('{}학급의 학생 수는 {}명'.format(classNo, cnt))
    sum += cnt # here

print('전체 학생수는 {}명'.format(sum))
avg = sum / len(studentCnts)
print('평균 학생수는 {}명'.format(avg))