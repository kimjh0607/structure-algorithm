
'''
딕셔너리 수정. 키를 이용하여 밸류를 수정.
"딕셔너리[키] = 값" 형태로 아이템을 수정.


'''

myInfo = {}

myInfo['이름'] = 'kim'
myInfo['전공'] = 'data'
myInfo['메일'] = 'abc@naver.com'
myInfo['학년'] = 1
myInfo['주소'] = 'seoul'
myInfo['취미'] = ['swim', 'football']
print(f'myInfo : {myInfo}')

myInfo['전공'] = 'sports'
myInfo['학년'] = '4'
print(f'myInfo : {myInfo}')

