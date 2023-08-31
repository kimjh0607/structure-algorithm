tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

tuple1 = list(tuple1)
tuple2 = list(tuple2)

listH = []
listG = []
for num1 in tuple1:
    listH.append(num1)
for num2 in tuple2:
    if num2 not in tuple1:
        listH.append(num2)
    
    
for num1 in tuple1:
    for num2 in tuple2:
        if num1 == num2:
            listG.append(num2)

listH = sorted(listH)
listG = sorted(listG)

listH = tuple(listH)
listG = tuple(listG)

print(f'합집합 : {listH}')
print(f'교집합 : {listG}')
