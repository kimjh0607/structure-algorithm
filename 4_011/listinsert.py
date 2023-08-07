

'''
insert() 함수를 이용하면 특정 위치(인덱스)에 아이템을 추가할 수 있다.
그 인덱스에 값이 들어가면 뒤의 값들은 뒤로 한칸씩 밀린다.
'''

students = ['홍길동','박찬호','이용규','박승철','김지은']

print('students: {}'.format(students))
print('students의 길이: {}'.format(len(students)))
print('students의 마지막 인덱스: {}'.format(len(students)-1))

students.insert(3, '강호동')
print('students: {}'.format(students))
print('students의 길이: {}'.format(len(students)))
print('students의 마지막 인덱스: {}'.format(len(students)-1))

words = ['I', 'a', 'boy.']
for word in words:
    print(word, end='')

print()
words.insert(1,'am')
for word in words:
    print('{} '.format(word), end='')