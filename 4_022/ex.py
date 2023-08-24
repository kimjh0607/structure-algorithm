
# 난수 생성 후 사용자가 입력한 숫자가 있는지 또는 없는지를 출력하는 프로그램
import random as rd

rNumbers = rd.sample(range(1, 11), 5)

uNumber = int(input('1~10 정수 입력 : '))

if uNumber in rNumbers:
    print('숫자 있음!!!!!')
    print(f'입력숫자 : {uNumber} , com숫자 : {rNumbers}')
else:
    print('숫자 없음ㅠㅠ')
    print(f'입력숫자 : {uNumber} , com숫자 : {rNumbers}')

#문장에서 비속어가 있는지 알아내는 프로그램
wrongWord = ['쩔었다', '짭새', '꼽사리', '먹튀', '지린', '쪼개다', '뒷담 까다']
sentence = '짭새 등장에 강도들은 모두 쩔었다. 그리고 강도 들은 지린 듯 도망갔다.'

for word in wrongWord:
    if word in sentence:
        print(f'비속어 : {word}')