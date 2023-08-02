# minScore=60
#
# kor = int(input('국어점수 : '))
# eng = int(input('영어점수 : '))
# mat = int(input('수학점수 : '))
# sci = int(input('과학점수 : '))
# his = int(input('역사점수 : '))
#
# scores = [['국어', kor],
#           ['영어', eng],
#           ['수학', mat],
#           ['과학', sci],
#           ['국사', his]]
#
# for sub, sco in scores:
#     if sco >= minScore: continue
#     print('과목명 : {}, 점수 : {}'.format(sub, sco))


school = [['1', 18],
          ['2', 19],
          ['3', 23],
          ['4', 21],
          ['5', 20],
          ['6', 22],
          ['7', 17]]

standard1 = 0
standard2 = 0

maxcla = school[0][0]
maxstu = school[0][1]
mincla = school[0][0]
minstu = school[0][1]

for cla, stu in school:
    if stu > maxstu:
        maxstu = stu
        maxcla = cla

    if stu < minstu:
        minstu = stu
        mincla = cla

print('학생수가 가장 많은 학급 : {}학급({}명)'.format(maxcla, maxstu))
print('학생수가 가장 적은 학급 : {}학급({}명)'.format(mincla, minstu))

# mincla = school[0][0]
# minstu = school[0][1]

# for cla, stu in school:
#     if stu < minstu:
#         minstu = stu
#         mincla = cla
#
# print('학생수가 가장 적은 학급 : {}학급({}명)'.format(mincla, minstu))
