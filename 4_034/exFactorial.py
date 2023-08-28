
# 0부터 10 까지의 각각의 정수에 대한 팩토리얼을 딕셔너리에 추가.

facDic = {}

for index in range(11):
    if index == 0:
        facDic[index] = 1
    else:
        for index2 in range(1, (index+1)):
            facDic[index] = facDic[index-1] * index2

print(f'Factorial : {facDic}')