

pws = ('password1234', 'abc123', 'qwerty', 'letmein', 'welcome00')
print(f'passwords : {pws}')

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))
total = 0

for sco1, sco2 in scores:
    yearScore = sco1 + sco2
    total += yearScore

print(f'3학년 동안의 총학점 : {total}')
print(f'3학년 동안의 평균학점 : {total / len(scores) / 2}')
print('-' * 40)

score4 = round(((4.0 * 8) - total), 1)
print(f'4학년 목표 총 학점 : {score4}')
print(f'4학년 한학기 최소 학점 : {score4 / 2}')
print('-' * 40)

scores = list(scores)
scores.append((score4, (score4/2)))

scores = tuple(scores)
print(scores)
print(type(scores))