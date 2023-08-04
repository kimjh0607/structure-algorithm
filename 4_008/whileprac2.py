school = [['1', 18],
          ['2', 19],
          ['3', 23],
          ['4', 21],
          ['5', 20],
          ['6', 22],
          ['7', 17]]

num = 0
mincla = school[0][0]
minstu = school[0][1]
maxcla = school[0][0]
maxstu = school[0][1]

while num < len(school):
    if school[num][1] > maxstu:
        maxcla = school[num][0]
        maxstu = school[num][1]

    if school[num][1] < minstu:
        mincla = school[num][0]
        minstu = school[num][1]

    num += 1

print('학생수 가장 많은 반 : {}반 - {}명'.format(maxcla,maxstu))
print('학생수 가장 적은 반 : {}반 - {}명'.format(mincla,minstu))

