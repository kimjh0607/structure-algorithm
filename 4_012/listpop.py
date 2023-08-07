

'''
pop() - 마지막 인덱스에 해당하는 아이템을 삭제할 수 있다.
pop(n) - n인덱스에 해당하는 아이템을 삭제할 수 있다.
'''

students = ['홍길동','박찬호','이용규','박승철','김지은','강호동']

students.pop()
print('students : {}'.format(students))
print('students length : {}'.format(len(students)))

students = ['홍길동','박찬호','이용규','박승철','김지은','강호동']

students.pop(3)
print('students : {}'.format(students))
print('students length : {}'.format(len(students)))
