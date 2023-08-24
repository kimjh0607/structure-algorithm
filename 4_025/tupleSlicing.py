'''
- 리스트와 마찬가지로 [n:m]을 이용하여 원하는 아이템만 뽑아낼 수 있다.
[2:4] - "(2<= item <4)"
- 슬라이싱할 떄 단계를 설정할 수 있다. - numbers[2:-2:2]
- 튜플은 슬라이싱을 이용하여 아이템 변경 불가,
그러나 리스트의 아이템을 튜플 아이템으로 변경하는 것은 가능
'''
students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print('students: {}'.format(students))
print('students: {}'.format(students[2:4]))
print('students: {}'.format(students[:4]))
print('students: {}'.format(students[2:]))
print('students: {}'.format(students[2:-2])) #뒤에서 계산할 떄는 인덱스가 0이 아닌 -1부터 시작
print('students: {}'.format(students[-5:-2]))

numbers = (2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14)
print('numbers: {}'.format(numbers[2:-2]))
print('numbers: {}'.format(numbers[2:-2:2]))
print('numbers: {}'.format(numbers[:-2:2]))
print('numbers: {}'.format(numbers[::2]))

# students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')

# students[1:4] = ('park chanho', 'lee yonggyu', 'gang hodong')
# print('students : {}'.format(students))
#TypeError : 'tuple' object does not support item assignment


students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']

students[1:4] = ('park chanho', 'lee yonggyu', 'gang hodong')
print('students : {}'.format(students))
print(type(students)) #튜플형태의 아이템을 넣어도 타입은 list

#튜플의 slice()
students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print('students: {}'.format(students[slice(2, 4)]))
print('students: {}'.format(students[slice(4)]))
print('students: {}'.format(students[slice(2, len(students))]))
print('students: {}'.format(students[slice(2, len(students)-2)]))
