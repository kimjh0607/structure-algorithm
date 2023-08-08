'''
extend() : 리스트에 또 다른 리스트를 연결(확장)할 수 있다.
덧셈 연산자를 이용해서 리스트르 연결할 수도 있다.
'''

group1 = ['홍길동', '박찬호', '이용규']
group2 = ['강호동', '박승철', '김지은']
print('group1 : {}'.format(group1))
print('group2 : {}'.format(group2))

# group1.extend(group2)
# print('group1 : {}'.format(group1))
# print('group2 : {}'.format(group2))

result = group1 + group2

print('group1 : {}'.format(group1))
print('group2 : {}'.format(group2))
print('result : {}'.format(result))
