
numbers = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'numbers : {numbers}')

n = 0
while True:
    if n == len(numbers):
        break

    if numbers.count(numbers[n]) > 1:
        numbers.remove(numbers[n])
        continue

    n += 1

print(f'numbers : {numbers}')