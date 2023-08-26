
# 과락과목 출력하기 3가지 방법
minScore = 60
korScore = int(input('국어 점수: '))
engScore = int(input('영어 점수: '))
matScore = int(input('수학 점수: '))
sciScore = int(input('과학 점수: '))
hisScore = int(input('국사 점수: '))

scores = (
    ('국어', korScore),
    ('영어', engScore),
    ('수학', matScore),
    ('과학', sciScore),
    ('국사', hisScore))

# index활용 - 고전
for item in scores:
    if item[1] < minScore:
        print('과락 과목: {}, 점수: {}'.format(item[0], item[1]))

# iterable 객체 활용
for subject, score in scores:
    if score < minScore:
        print('과락 과목: {}, 점수: {}'.format(subject, score))

#continue 활용
for subject, score in scores:
    if score >= minScore: continue
    print('과락 과목: {}, 점수: {}'.format(subject, score))