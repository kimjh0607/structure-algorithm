


friends = []
for name in range(5):
    name = input('친구 이름 입력 : ')
    friends.append(name)

sortedList = sorted(friends)
reversedList = sorted(friends, reverse=True)
print(f'친구들 : {friends}')
print(f'오름차순 : {sortedList}')
print(f'내림차순 : {reversedList}')