
#최고 최저 점수 삭제한 후 총점과 평균구하기
playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)

playerScore = list(playerScore) #리스트로 변환
print(type(playerScore))

playerScore.sort() # 소팅
print(playerScore)

playerScore.pop(0)
playerScore.pop( len(playerScore)-1 )
print(playerScore)

playerScore = tuple(playerScore) # 튜플로 다시 변환
print(playerScore)
print(type(playerScore))

sum = 0
avg = 0

for scoreIndex in playerScore:
    sum += scoreIndex
    
avg = sum / len(playerScore)
print(f'총합 : {sum:.2f}')
print(f'평균 : {avg:.2f}')