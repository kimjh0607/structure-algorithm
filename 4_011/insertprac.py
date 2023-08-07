
numbers = [1,3,6,11,45,54,62,74,85]
inputNum = int(input('숫자입력 : '))
insertIdx = 0

for idx, num in enumerate(numbers):
    if insertIdx == 0 and inputNum < num:
        insertIdx = idx

numbers.insert(insertIdx, inputNum)
print(numbers)