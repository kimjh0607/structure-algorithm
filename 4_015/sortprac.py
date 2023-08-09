
scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]

scores.sort()
print(f'scores : {scores}')

scores.pop(0)
scores.pop(len(scores)-1)
print(f'scores : {scores}')

sum = 0

for score in scores:
    sum += score

avg = sum / len(scores)
print(f'총합 : %.2f'%sum )
print(f'평균 : %.2f'%avg)