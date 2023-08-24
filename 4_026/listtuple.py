'''
리스트와 튜플의 차이점
tuple은 list와 달리 아이템 추가, 변경, 삭제가 불가하다.
튜플의 또 다른 선언 방법 - 소괄호 생략가능하다 ((리스트는 불가함))

리스트와 튜플은 자료형 변환이 가능하다.

'''

#튜플 소괄호 생략 선언 방법
students = '홍길동', '박찬호', '이용규', '강호동'
print(students)
print(type(students))

# 튜플 <-> 리스트 자료형 변환
students = ['홍길동', '박찬호', '이용규', '강호동']
print(students)
print(type(students))

students = tuple(students)
print(students)
print(type(students))

students = list(students)
print(students)
print(type(students))
