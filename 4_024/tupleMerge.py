
'''
두개의 튜플을 결합할 수 있다.
리스트에서 사용하던 extend()함수는 튜플에서 사용할 수 없다.
# 튜플로 만들어주기 ()소괄호에 ,콤마 찍기 - myNums = myNums + (numIndex, ) 
'''
tuple1 = ('홍길동', '박찬호', '이용규')
tuple2 = ('박승철', '김지은', '강호동')

tuple3 = tuple1 + tuple2 #결합
print('studentTuple3: {}'.format(tuple3))

studentList1 = ['홍길동', '박찬호', '이용규']
studentList2 = ['박승철', '김지은', '강호동']

studentList1.extend(studentList2)
print('studentList1: {}'.format(studentList1)) #리스트는 가능하다



#튜플에서는 길이가 늘어날 수 없으므로 extend 사용 불가
# AttributeError : 'tuple' object has no attribute 'extend'
studentTuple1 = ('홍길동', '박찬호', '이용규')
studentTuple2 = ('박승철', '김지은', '강호동')

studentTuple1.extend(studentTuple2)
print('studentTuple1: {}'.format(studentTuple1)) 
