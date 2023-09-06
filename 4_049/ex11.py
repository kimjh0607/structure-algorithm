subject = ['국어', '영어', '수학', '과학', '국사']
scores = {}

for index in subject:
    score = int(input('점수 입력 :'))
    scores[index] = score

print(f'Scores : {scores}')

