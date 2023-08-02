'''
- 자료구조란
여러 개의 데이터가 묶여있는 자료형을 컨테이너 자료형이라고 하고,
이러한 컨테이너 자료형의 데이터 구조를 자료구조라고 한다.

    - list - 튜플과 같지만, 데이터를 원하는대로 수정할 수 있다. [] 대괄호
    - tuple - 리스트와 비슷하지만 한번 데이터가 정해지면 바꿀 수 없다. ()소괄호
    - dictionary - 키 - 밸류 짝이 있는 형태 {}중괄호
    - set - 데이터 중복이 안된다. {}중괄호

'''
student1 = 'kim'
student2 = 'lee'
student3 = 'jang'
student4 = 'cho'
student5 = 'lim'
print(type(student1))
print(student1)

students = ['kim', 'lee', 'jang', 'cho', 'lim']
print(students)
print(type(students)) #'list'

for index in students:
    print(index, end=' ')
print()

students = ('kim', 'lee', 'jang', 'cho', 'lim')
print(students)
print(type(students)) #'tuple'

for index in students:
    print(index)

scores = {'kor':85, 'eng':8, 'math':100}
print(scores)
print(type(scores)) #'dict'

for index in scores:
    print(index)

sales = {100, 200, 300, 100} #중복데이터 제외되고 출력
print(sales)
print(type(sales)) #'set'
for index in sales:
    print(index)