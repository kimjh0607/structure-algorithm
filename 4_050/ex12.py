

# n각형의 내각의 합 : 180 * (n-2)

nDic = {}

for n in range(3,11):
    angSum = 180 * (n-2)
    eachAng = angSum / n
    nDic[n] = [angSum, eachAng]

print(nDic)
print('-' * 40)

#1부터 10까지 각각의 정수에 대한 약수를 저장하는 딕셔너리를 만들고 출력하는 프로그램


dict = {}

for n1 in range(1,11):
    divisiors = []
    for n2 in range(1, n1+1):
        if n1 % n2 == 0:
            divisiors.append(n2)
    dict[n1] = divisiors

print(dict)