
aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'

splitList = aboutPython.split()
print(splitList)

dict = {}

for idx, value in enumerate(splitList):
    dict[idx] = value

print(dict)