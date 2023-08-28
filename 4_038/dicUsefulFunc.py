'''
in - 키 존재 유무를 판단.
len() - 길이 확인 가능
clear() - 모두 삭제.

'''


memInfo = {'이름':'kim', 
           '메일':'abc@naver.com', 
           '학년':2, 
           '취미':['football', 'basketball']}

print('이름' in memInfo)
print('메일' in memInfo)
print('학년' in memInfo)
print('취미' in memInfo)

print('name' not in memInfo)
print('mail' not in memInfo)
print('grade' not in memInfo)
print('hobby' not in memInfo)
print('-' * 40)

print('홍길동' in memInfo)
print('gildong@gmail.com' in memInfo)
print(3 in memInfo)
#print(['농구', '게임'] in memInfo) # TypeError: unhashable type: 'list'


print('memInfo length : {}'.format(len(memInfo)))

print('memInfo: {}'.format(memInfo))

memInfo.clear()
print('memInfo: {}'.format(memInfo))
