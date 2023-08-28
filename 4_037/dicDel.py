
'''
딕셔너리 삭제
del, pop()를 이용해서 item을 삭제


'''

memInfo = {'이름':'kim', 
           '메일':'abc@naver.com', 
           '학년':2, 
           '취미':['football', 'basketball']}
print(f'memInfo: {memInfo}')

# # del 사용
# del memInfo['이름'] # '이름'을 키로 가지고 있는 item 삭제
# print(f'memInfo: {memInfo}')

# del memInfo['취미']
# print(f'memInfo: {memInfo}')

# pop() 사용. 삭제된 value값을 반환해줌.
memInfo = {'이름':'kim', 
           '메일':'abc@naver.com', 
           '학년':2, 
           '취미':['football', 'basketball']}

returnValue = memInfo.pop('이름')
print(f'memInfo: {memInfo}')
print(f'returnValue: {returnValue}')
print(f'returnValue type: {type(returnValue)}')

returnValue = memInfo.pop('취미')
print(f'memInfo: {memInfo}')
print(f'returnValue: {returnValue}')
print(f'returnValue type: {type(returnValue)}')