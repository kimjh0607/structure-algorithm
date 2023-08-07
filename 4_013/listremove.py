
'''
remove() - 특정 아이템을 삭제할 수 있다.
값이 2개 이상일 경우 가장 앞의 값이 지워진다.
여러개 일 경우 while 문을 쓰면 된다.
'''

students = ['홍길동','박찬호','이용규', '강호동', '박승철','김지은']
print(students)

students.remove('박찬호')
print(students)

