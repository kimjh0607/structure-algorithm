'''
index - 아이템에 자동으로 부여되는 번호표
0부터 시작한다.
ex) students[0]
'''
students = [10, 'lee', 'jang', 'cho', 'lim']
print(students[0])
print(students[2])
print(students[4])
#print(students[5]) # Error

print(type(students[0]))
print(type(students[2]))

students = ['kim', 'lee', 'jang', 'cho', 'lim']
for index in range(5):
    if index % 2 == 0:
        print(f'인덱스 짝수 학생ㅣstudents[{index}] : {students[index]}')
    else:
        print(f'인덱스 홀수 학생ㅣstudents[{index}] : {students[index]}')
