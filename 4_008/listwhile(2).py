
minScore = 60
scores = [['국어', 58],
          ['영어', 77],
          ['수학', 89],
          ['과학', 99],
          ['국사', 50]]

num = 0
while num < len(scores):
    if scores[num][1] >= minScore:
        num += 1
        continue

    print('과락과목 : {}, 점수 : {}'.format(scores[num][0], scores[num][1]))
    num += 1


