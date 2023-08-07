
myList = ['마케팅 회의', '회의록 정리', '점심 약속', '월간 업무 보고', '치과 방문', '마트 장보기']
print('일정 : {}'.format(myList))

# removeItem = input('지울 계획 입력 : ')
myList.remove(input('지울 계획 입력 : '))
print('일정 : {}'.format(myList))

mySubject = ['국어', '영어', '수학', '과학', '국사']
print(mySubject)

# mySubject.remove(input('지워버리고 싶은 과목 입력 : '))
# print(mySubject)

removeSubject = input('지우고 싶은 과목 입력 : ')
while removeSubject in mySubject:
    mySubject.remove(removeSubject)

print(mySubject)