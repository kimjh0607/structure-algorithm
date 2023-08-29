

numbers = [4, 6, 7, 9]
result = []

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 == num2 or num2 == num3 or num1 == num3:
                continue

            result.append([num1, num2, num3])

print(f'경우의 가짓 수 : {len(result)}')
print(f'result : {result}')