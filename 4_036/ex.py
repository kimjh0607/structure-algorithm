
scores = {'kor':88, 'eng':55, 'mat':85, 'sci':57, 'his':82}
print(f'scores: {scores}')

minScore = 60
fDic = {}
fStr = 'FFFF(재수강!!)'

for key in scores:
    if scores[key] < 60:
        scores[key] = fStr
        fDic[key] = scores[key] ## 여기 못적음

print(f'점수 : {scores}')
print(f'재수강 목록 : {fDic}')