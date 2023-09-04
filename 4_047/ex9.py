
fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits)


curIdx = 0
nextIdx = 1
lastIdx = len(fruits)-1

while True:
    curDic = fruits[curIdx]
    nextDic = fruits[nextIdx]

    curCnt = list(curDic.values())[0]
    nextCnt = list(nextDic.values())[0]

    if nextCnt < curCnt:
        fruits.insert(curIdx, fruits.pop(nextIdx))
        nextIdx = curIdx + 1
        continue

    nextIdx += 1
    if nextIdx > lastIdx:
        curIdx += 1
        nextIdx = curIdx + 1

        if curIdx == 5:
            break

fruits = tuple(fruits)
print(f' FRUITS : {fruits}')
