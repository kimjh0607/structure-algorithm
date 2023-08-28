
'''
딕셔너리추가
"딕셔너리[키] = 값" 형태로 아이템 추가

'''

myInfo = {}

myInfo['이름'] = 'kim'
myInfo['전공'] = 'data'
myInfo['메일'] = 'abc@naver.com'
myInfo['학년'] = 4
myInfo['주소'] = 'seoul'
myInfo['취미'] = ['exercise', 'swimming']

print(f'myInfo : {myInfo}')
print(f'myInfo : {len(myInfo)}')



myInfo['메일'] = 'aaaaaaaaaaa@naver.com' #키는 중복될 수 없다. 새로 추가되는것이 아닌 변경됨
print(f'myInfo : {myInfo}')

studentInfo = {}

studentInfo['name'] = input('이름 입력: ')
studentInfo['grade'] = input('학년 입력: ')
studentInfo['mail'] = input('메일 입력: ')
studentInfo['addr'] = input('주소 입력: ')

print(f'studentInfo : {studentInfo}')