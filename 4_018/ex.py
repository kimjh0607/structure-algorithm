import random as rd

sampleList = rd.sample(range(1,11), 10) #1부터10까지 10개

selectIdx = int(input('숫자 7의 위치 입력 : '))
searchIdx = sampleList.index(7)

if searchIdx == selectIdx:
    print('빙고')
else:
    print('실패')

print('sampleList : {}'.format(sampleList))
print('searchIdx : {}'.format(searchIdx))