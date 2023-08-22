'''
- 리스트 곱셈 연산 - 리스트의 아이템이 반복된다, 리스트 자체가 두배로 늘어난다(숫자 - 아이템의 속성이 곱하여지는것이 아님.)
- 아이템 위치 찾기 -  index(item) 함수로 item의 인덱스를 알아낼 수 있다.
'''

students = ['홍길동', '박찬호', '이용규']
print('students : {}'.format(students))

studentsMul = students * 2
print('studentsMul : {}'.format(studentsMul))

numbers = [2, 50, 0.12, 1, 9]
print('number : {}'.format(numbers))

numbersMul = numbers * 2
print('numbersMul : {}'.format(numbersMul))
#요소의 값이 두배가 되는 것이 아니다.

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('students: {}'.format(students))

searchIdx = students.index('강호동')
print('searchIdx : {}'.format(searchIdx))

searchIdx = students.index('강호동', 2, 6) #인덱스 2부터 인덱스6앞까지의 범위로 지정.
print('searchIdx : {}'.format(searchIdx))

numbers = [2, 50, 0.12, 1, 9]
searchIdx = numbers.index(0.12)
print('searchIdx : {}'.format(searchIdx))