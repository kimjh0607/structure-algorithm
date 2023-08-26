
'''
tuple , for문 사용하기 - 튜플은 이터러블한 객체.

'''


cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

# 인덱스활용 고전방식
# for index in range(len(cars)):
#     print(cars[index])

# iterable사용 - 튜플은 이터러블 객체로 사용가능 / int는 사용 불가
for car in cars:
    print(car)


studentCnts = (1, 19), (2, 20), (3, 22), (4, 18), (5, 21)

# 인덱스활용 고전방식
# for index in range(len(studentCnts)):
#     print(f'{studentCnts[index][0]}학급 학생수: {studentCnts[index][1]}')

for innerIndex1, innerIndex2 in studentCnts:
    print(f'{innerIndex1}학급 학생수: {innerIndex2}')