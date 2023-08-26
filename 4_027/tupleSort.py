'''
- 튜플의 정렬 - 튜플은 수정이 불가, 리스트로 변환 후 정렬하자.
list() -> sort() / sort(reverse=True) -> tuple()
- sorted() 함수를 이용하면 튜플도 정렬할 수 있다. but sorted()는 '"리스트"' 자료형으로 반환한다
list로 변환 하지 않고 정렬. 그러나 반환타입은 list
'''

students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print('students type: {}'.format(type(students)))
print('students: {}'.format(students))

students = list(students)
students.sort()
print('students type: {}'.format(type(students)))
print('students: {}'.format(students))

students = tuple(students)
print('students type: {}'.format(type(students)))
print('students: {}'.format(students))


'''
sorted() 함수 - 튜플을 정렬하는데, 반환이 ''리스트형''이다
'''
# students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
# sortedStudents = sorted(students)

# print('sortedStudents type: {}'.format(type(sortedStudents)))
# print('sortedStudents: {}'.format(sortedStudents))

# print('students type: {}'.format(type(students)))
# print('students: {}'.format(students))

# sortedStudents = sorted(students, reverse=True)
# print('sortedStudents type: {}'.format(type(sortedStudents)))
# print('sortedStudents: {}'.format(sortedStudents))