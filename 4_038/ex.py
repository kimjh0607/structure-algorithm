myInfo = {'이름':'kim',
          '나이':'32',
          '연락처': '010-3333-9999',
          '주민등록번호':'010101-1234567',
          '주소':'seoul'}
print(myInfo)

deleteItems = ['연락처', '주민등록번호']

for item in deleteItems:
    if item in myInfo:
        del myInfo[item]

print(myInfo)