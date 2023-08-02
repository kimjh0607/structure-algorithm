students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

print(students)

#print(len(students))
#len함수가 반환하는 것은 int형

sLength = len(students)
print(sLength)

for index in range(sLength): # or len(students)
    print(students[index])

num = 0
while num < sLength:
    print('n : {}'.format(num))
    num += 1

str = 'Hello Python!!'
print('문자의 길이는? {}'.format(len(str)))

myFavoriteSports = ['수영', '배구', '야구', '조깅']

for index in range(len(myFavoriteSports)):
    print(myFavoriteSports[index])

num = 0
while num < len(myFavoriteSports):
    print(myFavoriteSports[num])
    num += 1