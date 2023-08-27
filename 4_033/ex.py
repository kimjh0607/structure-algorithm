myInfo = {'이름':'kim',
          '전공':'data',
          '메일':'abc@naver.com',
          '학년':4,
          '주소':'seoul',
          '취미':['exercise', 'swimming']}

print(myInfo)

print(myInfo['이름'])
print(myInfo['메일'])
print(myInfo['취미'])
#print(myInfo['취미2']) # KeyError: '취미2'

print(myInfo.get('이름'))
print(myInfo.get('학년'))
print(myInfo.get('주소'))
print(myInfo.get('주소2')) # None 반환. KeyError없음.