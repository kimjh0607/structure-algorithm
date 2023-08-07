
students = ['홍길동','박찬호','이용규','강호동','박승철','김지은','강호동']
print(students)

#students.remove('강호동')
#print(students)

while ('강호동' in students): #강호동이 students에 있으면 True, 없을 때 Flase.
    students.remove('강호동')

print(students)