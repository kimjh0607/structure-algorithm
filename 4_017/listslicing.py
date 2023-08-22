'''
[n:m]을 이용하면('n이상 m미만') 리스트에서 원하는 아이템만 뽑아낼 수 있다.
[n:m:o] 'o'는 범위내에서 슬라이싱할 칸수를 의미한다.
slice(n,m)
'''

students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']

print('students : {}'.format(students))
print('students : {}'.format(students[2:4]))
print('students : {}'.format(students[:4])) #앞이나 뒤 생략가능
print('students : {}'.format(students[2:]))
print('students : {}'.format(students[2:-2]))

numbers = [1,2,3,4,5,6,7,8,9,10]
print('numbers : {}'.format(numbers))
print('numbers : {}'.format(numbers[2:4]))
print('numbers : {}'.format(numbers[:4]))
print('numbers : {}'.format(numbers[2:]))
print('numbers : {}'.format(numbers[2:-2]))
print('numbers : {}'.format(numbers[-5:-2]))

numbers2 = [2, 50, 0.12, 1, 9, 7, 17 ,35, 100, 3.14]
print('numbers2 : {}'.format(numbers2[2:-2]))
print('numbers2 : {}'.format(numbers2[2:-2:2]))
print('numbers2 : {}'.format(numbers2[:-2:2]))
print('numbers2 : {}'.format(numbers2[::2]))

#슬라이싱을 통해 아이템을 변경 - but 슬라이싱의 개수가 맞지 않으면 할당해주는 값으로만 채워진다.
students[1:4] = ['park', 'lee', 'kang']
print('students : {}'.format(students))

students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
students[1:4] = ['park', 'lee','kang', 'kim']
print('students : {}'.format(students))

students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
students[1:4] = ['park', 'lee']
print('students : {}'.format(students))

students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print('students : {}'.format(students))
print('students : {}'.format(students[slice(2, 4)]))
print('students : {}'.format(students[slice(4)]))
print('students : {}'.format(students[slice(2, len(students))]))
print('students : {}'.format(students[slice(2, len(students)-2)]))
print('students : {}'.format(students[slice(len(students)-5, len(students)-2)]))