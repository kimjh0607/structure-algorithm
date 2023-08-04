sports = ['농구', '수구', '축구', '마라톤', '테니스']

favoriteSport = input('가장 좋아하는 운동 입력 : ')

for index, value in enumerate(sports):
    if value == favoriteSport:
        print('{}번째에 있습니다.'.format(index+1))
