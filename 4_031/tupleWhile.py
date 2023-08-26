
'''
for문이 좋지만,
while문을 써야할 떄

'''

minScore = 60

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
mat = int(input('수학 점수 입력 : '))
sci = int(input('과학 점수 입력 : '))
his = int(input('역사 점수 입력 : '))

scores = (
    ('국어', kor),
    ('영어', eng),
    ('수학', mat),
    ('과학', sci),
    ('역사', his))

n = 0
while n < len(scores):
    if scores[n][1] < minScore:
        print(f'과락 과목 : {scores[n][0]}, 점수 : {scores[n][1]}')

    n += 1

# continue 사용
n = 0
while n < len(scores):
    if scores[n][1] >= minScore: 
        n += 1
        continue
        
    print(f'과락 과목 : {scores[n][0]}, 점수 : {scores[n][1]}')
    n += 1