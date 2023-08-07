
students = ['홍길동','박찬호','이용규','박승철','김지은']

print('students: {}'.format(students))
print('students의 길이: {}'.format(len(students)))
print('students의 마지막 인덱스: {}'.format(len(students)-1))

students.append('강호동')
print('students: {}'.format(students))
print('students의 길이: {}'.format(len(students)))
print('students의 마지막 인덱스: {}'.format(len(students)-1))

scores = [['국어', 88], ['영어', 91]]
scores.append(['수학', 96])

print('scores : {}'.format(scores))
for sub, sco in scores:
    print('과목명 : {},  점수 : {}'.format(sub, sco))