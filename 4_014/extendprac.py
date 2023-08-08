myFavorNum = [1,3,5,6,7]
friendFavorNum = [2,3,5,8,10]
print(f'myFavorNum : {myFavorNum}')
print(f'friendFavorNum : {friendFavorNum}')

addList = myFavorNum + friendFavorNum
print(f'addList : {addList}')

result = []
for number in addList:
    if number not in result:
        result.append(number)

print(f'result : {result}')
