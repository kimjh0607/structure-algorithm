
str = input('문장 입력 : ')

cnt = 0
for index, value in enumerate(str):
    if value == ' ':
        cnt += 1

print('총 공백의 갯수는 : {}'.format(cnt))