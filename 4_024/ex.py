
#실습
myNums = (1, 3, 5, 6, 7)
friNums = (2, 3, 5, 8, 10)

print(f'myNums : {myNums}')
print(f'friNums : {friNums}')

result = myNums + friNums
print(f'result : {result}')

for numIndex in friNums:
    if numIndex not in myNums:
        myNums = myNums + (numIndex, ) # 튜플로 만들어주기 ()소괄호에 ,콤마 찍기

print(f'myLastNumbers : {myNums}')