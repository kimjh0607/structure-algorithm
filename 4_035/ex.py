
# 학생의 시험 점수가 60점 미만이면 F로 값을 변경

# scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
# print(f'scores : {scores}')

# minScore = 60
# fStr = 'FFF(재수강 요망!)'

# if scores['kor'] < minScore : scores['kor'] = fStr
# if scores['eng'] < minScore : scores['eng'] = fStr
# if scores['mat'] < minScore : scores['mat'] = fStr
# if scores['sci'] < minScore : scores['sci'] = fStr
# if scores['his'] < minScore : scores['his'] = fStr
# print(f'scores : {scores}')


#실습
myBodyInfo = {'이름':'hong', '몸무게':83.0, '신장':1.8}
myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)
print(f'myBodyInfo: {myBodyInfo}')
print(f'myBMI: {myBMI:.2f}')

date = 0
while True:
    date += 1
    
    myBodyInfo['몸무게'] = round((myBodyInfo['몸무게'] - 0.3), 2)
    print(f'몸무게 : {myBodyInfo["몸무게"]}')

    myBodyInfo['신장'] = round((myBodyInfo['신장'] + 0.001), 3)
    print(f'신장 : {myBodyInfo["신장"]}')

    myBMI = myBodyInfo['몸무게'] / (myBodyInfo['신장'] ** 2)

    if date == 30:
        break

print(f'myBodyInfo : {myBodyInfo}')
print(f'myBMI : {round(myBMI, 2)}')