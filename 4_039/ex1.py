
# 1부터 사용자가 입력한 숫자까지의 약수와 소수를 리스트를 각각 저장, 출력
inputNum = int(input('1보다 큰 정수 입력: '))
listA = []
listB = []

#약수 구하기
for index in range(1, inputNum):
    if index == 1:
        listA.append(index)
    else:
        if inputNum % index == 0:
            listA.append(index)

#소수 구하기
for index in range(2, inputNum+1):
    flag = True
    for index2 in range(2, index):
        if index % index2 == 0:
            flag = False
            break

    if flag:
        listB.append(index)

print(f'{inputNum}의 약수: {listA}')
print(f'{inputNum}까지의 소수: {listB}')