
playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)

playerScore = sorted(playerScore)
print(type(playerScore))
print(playerScore)

playerScore.pop(0) #최저점 삭제
playerScore.pop( len(playerScore)-1 ) #최고점 삭제

sum = 0
avg = 0
for scoIndex in playerScore:
    sum += scoIndex

avg = sum / len(playerScore)

print(f'총합 : {sum:.2f}')
print(f'평균 : {avg:.2f}')