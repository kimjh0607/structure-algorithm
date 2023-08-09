
'''
sort() : 아이템을 정렬할 수 있다.
sort(reverse=True) : 내림차순
'''

stu = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print(f'students : {stu}')

stu.sort() #오름차순
print(f'students : {stu}')

stu.sort(reverse=True) #내림차순
print(f'students : {stu}')

numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print(f'numbers : {numbers}')

numbers.sort(reverse=True)
print(f'numbers : {numbers}')
