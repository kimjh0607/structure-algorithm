
numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)

print(f'numbers[:4] : {numbers[:4]}')
print(f'numbers[2:5] : {numbers[2:5]}')
print(f'numbers[3:] : {numbers[3:]}')
print(f'numbers[2:-2] : {numbers[2:-2]}')
print(f'numbers[:3] : {numbers[::3]}')

# max(), min() 함수
print(f'최소값 : {min(numbers)}')
print(f'최소값 index : {numbers.index(min(numbers))}')
print(f'최대값 : {max(numbers)}')
print(f'최대값 index : {numbers.index(max(numbers))}')

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))
sciScore = int(input('과학 점수 입력: '))
hisScore = int(input('국사 점수 입력: '))

scores = ({'kor':korScore},
          {'eng':engScore},
          {'mat':matScore},
          {'sci':sciScore},
          {'his':hisScore})

print(f'scores : {scores}')

for item in scores:
    for key in item.keys():
        if item[key] >= 90:
            item[key] = 'A'
        elif item[key] >= 80:
            item[key] = 'B'
        elif item[key] >= 70:
            item[key] = 'C'
        elif item[key] >= 60:
            item[key] = 'D'
        else:
            item[key] = 'F'

print(f'scores : {scores}')