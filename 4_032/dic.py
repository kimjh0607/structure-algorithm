'''
딕셔너리란 
- 키와 값을 이용해서 자료를 관리한다.
- 키는 데이터를 구분하기 위한 유일한 값.
- key, value 에는 숫자, 문자(열), 논리형 뿐만 아니라 컨테이너 자료형도 올 수 있다.
- 그러므로 key는 중복이 안된다 (list,tuple과 다른점) but value는 중복가능
- key 변경불가값(immutable) 변경가능한(mutable)값은 올 수 없다.
- 선언은 중괄호 '{}' 이용. 구분자는 콤마 ','



'''

students = {'s1':'홍길동', 
            's2':'박찬호', 
            's3':'이용규', 
            's4':['박승철', '사장님'], 
            's5':'김지은'}

print('students: {}'.format(students))
print('students type: {}'.format(type(students)))


myInfo = {'이름':'kim',
          '전공':'data',
          '메일':'abc@naver.com',
          '학년':4,
          '주소':'seoul',
          '취미':['cooking', 'traveling']}
print('myInfo: {}'.format(myInfo))