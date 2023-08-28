
import random

babyCnt = 0 #(0-7)
babyFee = 0
kidCnt = 0 #(8-13)
kidFee = 0
studentCnt = 0 #(14-19)
studentFee = 0
adultCnt = 0 #(20-64)
adultFee = 0
grandCnt = 0 #(65-)
grandFee = 0
totalFee = 0

peopleList = random.sample(range(1, 101), 100)
print(peopleList)

for person in peopleList:
    if person >= 0 and person <= 7:
        babyCnt += 1
    elif person >= 8 and person <= 13:
        kidCnt += 1
        kidFee += 200
    elif person >= 14 and person <= 19:
        studentCnt += 1
        studentFee += 300
    elif person >= 20 and person <= 64:
        adultCnt += 1
        adultFee += 500
    else:
        grandCnt += 1

totalFee = kidFee + studentFee + adultFee
print('-' * 30)
print(f'영유아 : {babyCnt}명 : {babyFee}원')
print(f'어린이 : {kidCnt}명 : {kidFee}원')
print(f'청소년 : {studentCnt}명 : {studentFee}원')
print(f'성인 : {adultCnt}명 : {adultFee}원')
print(f'어르신 : {grandCnt}명 : {grandFee}원')
print('-' * 30)
print(f'1일 요금 총합계 : {totalFee}원')
print('-' * 30)