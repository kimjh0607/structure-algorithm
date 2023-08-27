'''
키값으로 value 조회 가능.
get()함수를 쓸 수도 있음.
'''
students = {'s1':'홍길동', 's2':'박찬호', 's3':'이용규', 's4':['박세리', '골프왕']}

print('students[\'s1\']:{}'.format(students['s1']))
print('students[\'s2\']:{}'.format(students['s2']))
print('students[\'s3\']:{}'.format(students['s3']))
print('students[\'s3\']:{}'.format(students['s4']))
print('students[\'s4\']:{}'.format(students['s4'][0]))
print('students[\'s4\']:{}'.format(students['s4'][1]))

'''
존재하지 않는 키를 이용하여 조회 시 에러 발생.
KeyError: '키값'
'''
# KeyError: 's6'
#print('students[\'s3\']:{}'.format(students['s6']))

print(students.get('s1'))
print(students.get('s2'))
print(students.get('s3'))
print(students.get('s6')) # KeyError 안남. None 반환



memInfo = {'이름':'홍길동', '취미':['농구', '게임', '여행']}
print('memInfo[\'이름\']:{}'.format(memInfo['이름']))
print('memInfo[\'취미\']:{}'.format(memInfo['취미']))
print('memInfo[\'취미[0]\']:{}'.format(memInfo['취미'][0]))
print('memInfo[\'취미[1]\']:{}'.format(memInfo['취미'][1]))
print('memInfo[\'취미[2]\']:{}'.format(memInfo['취미'][2]))

