
'''
딕셔너리는 Index가 없기 때문에, 이 함수들은 유용하게 많이 쓰인다.

**keys() - 전체 키를 조회할 수 있다.**
values() - 전체 밸류를 조회할 수 있다.
items() - 각 키밸류를 tuple로 반환한다.
list()를 써서 list로 변환도 가능하다.

for문을 이용한 조회 - 많~이 쓰인다.
for key in memInfo.keys():
    print(f'{key} : {memInfo[key]}')


'''

memInfo = {'이름':'kim', '메일':'abc@naver.com', '학년':4, '취미':['swim', 'game']}

ks = memInfo.keys()
print(f'ks : {ks}')
print(f'ks type : {type(ks)}')

vs = memInfo.values()
print(f'vs : {vs}')
print(f'vs type : {type(vs)}')

items = memInfo.items()
print(f'items : {items}')
print(f'items type : {type(items)}')

for key in memInfo.keys():
    print(f'{key} : {memInfo[key]}')