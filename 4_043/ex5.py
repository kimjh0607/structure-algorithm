numbers = [4, 6, 7, 9]
result = []

for num1 in numbers:
    for num2 in numbers:
        if num1 == num2:
            continue

        result.append([num1, num2])

print(f'경우의 가짓 수 : {len(result)}')
print(f'result : {result}')

# n! / (n-r)!
import math
pernutation = math.factorial(len(numbers)) / math.factorial(len(numbers)-2)
print(f'경우의 가짓 수 : {pernutation}')