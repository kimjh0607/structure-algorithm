
words = {
    '꺼지다' : '가다',
    '쩔다' : '엄청나다',
    '짭새' : '경찰관',
    '꼽사리' : '중간에 낀 사람',
    '먹튀' : '먹고 도망',
    '지린다' : '겁을 먹다',
    '쪼개다' :  '웃다',
    '뒷담 까다' : '험담하다'
}

txt = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'
keys = list(words.keys())

for key in keys:
    if key in txt:
        # print(f'key : {key}')
        # print(f'수정 : {words[key]}')
        txt = txt.replace(key, words[key]) # txt 변수에 다시 할당하지 않으면 치환이 적용되지 않은 원래의 txt 문자열이 그대로 유지

print(txt)