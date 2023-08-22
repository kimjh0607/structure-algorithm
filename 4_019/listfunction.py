'''
count() - 함수를 이용하면 특정 아이템의 갯수를 알아낼 수 있다.
del - (함수아니고 명령어) 특정 아이템을 삭제할 수 있다.
'''

students = ['홍길동', '강호동', '박찬호', '이용규', '박승철', '강호동', '김지은']
print('students : {}'.format(students))

# searchCnt = students.count('홍길동')
# print('searchCnt : {}'.format(searchCnt))

# searchCnt = students.count('강호동')
# print('searchCnt : {}'.format(searchCnt))

# searchCnt = students.count('김아무개')
# print('searchCnt : {}'.format(searchCnt))

del students[1]
print('students : {}'.format(students))

del students[2:4]
print('students : {}'.format(students))

del students[1:3]
print('students : {}'.format(students))

