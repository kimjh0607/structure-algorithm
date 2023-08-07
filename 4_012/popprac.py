
# scores = [[1, 9.5],
#           [2, 8.9],
#           [3, 9.2],
#           [4, 9.8],
#           [5, 8.8],
#           [6, 9.0]]

playerScore = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
minScoreIdx = 0
minScore = playerScore[0]
maxScoreIdx = 0
maxScore = playerScore[0]

for index, value in enumerate(playerScore):
    if value < minScore:
        minScore = value
        minScoreIdx = index
print('최저 점수 : {}, 인덱스 : {}'.format(minScore, minScoreIdx))
playerScore.pop(minScoreIdx)


for index, value in enumerate(playerScore):
    if value > maxScore:
        maxScore = value
        maxScoreIdx = index
print('최고 점수 : {}, 인덱스 : {}'.format(maxScore, maxScoreIdx))
playerScore.pop(maxScoreIdx)

print('player scores : {}'.format(playerScore))


