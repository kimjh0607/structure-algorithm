'''
튜플도 아이템에 자동으로 부여되는 번호표(인덱스)가 있다.
'''

students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
print('students[0] : {}'.format(students[0]))
print('students[1] : {}'.format(students[1]))
print('students[2] : {}'.format(students[2]))
print('students[3] : {}'.format(students[3]))
print('students[4] : {}'.format(students[4])) 

#print('students[5] : {}'.format(students[5])) #범위내에 조회시 out of range 에러 뜸.

numbers = (10, 20, 30, 40, 50)
print('numbers[0] : {}'.format(numbers[0]))
print('numbers[1] : {}'.format(numbers[1]))
print('numbers[2] : {}'.format(numbers[2]))
print('numbers[3] : {}'.format(numbers[3]))
print('numbers[4] : {}'.format(numbers[4]))


friends = ('kim', 'lee', 'jang', 'choi', 'park')

for index in range(len(friends)):
    if index % 2 == 0:
        print(f'짝수 : {index} : {friends[index]}')
    else:
        print(f'홀수 : {index} : {friends[index]}')