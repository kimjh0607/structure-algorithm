'''
튜플의 길이 - 리스트와 마찬가지로 len()함수를 쓸 수 있다.

'''

students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
# sLength = len(students)
# print('length of students : {}'.format(sLength))

# for index in range(len(students)):
#     print(f'index : {index}')
#     print(f'students[{index}] : {students[index]}')

# n = 0
# while n < len(students):
#     print(f'index : {n}')
#     print(f'students[{n}] : {students[n]}')
#     n += 1


#iterable 활용
for stuIndex in students:
    print(f'student : {stuIndex}')