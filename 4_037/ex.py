
# 딕셔너리에 저장된 점수 중 최저 및 최고 점수를 삭제하는 프로그램 만들기

scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score4':9.8, 'score5':8.8}
minScore = 10
minScoreKey = ''
maxScore = 0 
maxScoreKey = ''

for keyIndex in scores:
    if scores[keyIndex] < minScore:
        minScore = scores[keyIndex]
        minScoreKey = keyIndex

    if scores[keyIndex] > maxScore:
        maxScore = scores[keyIndex]
        maxScoreKey = keyIndex

del scores[maxScoreKey]
del scores[minScoreKey]
print(f'Scores : {scores}')