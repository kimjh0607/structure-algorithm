
minScore = 60
kor = int(input('국어점수 : '))
eng = int(input('영어점수 : '))
mat = int(input('수학점수 : '))
sci = int(input('과학점수 : '))
his = int(input('역사점수 : '))

scores = [['국어', kor],
          ['영어', eng],
          ['수학', mat],
          ['과학', sci],
          ['국사', his]]

num = 0
while num < len(scores):
    if scores[num][1] < minScore:
        print('과락과목명 : {}, 점수 : {}'.format(scores[num][0],scores[num][1]))

    num += 1
