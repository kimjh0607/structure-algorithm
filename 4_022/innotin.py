'''
- in / not in 키워드를 이용하면 아이템의 존재 유/무를 알 수 있다.
- 튜플 등 문자열에서도 사용 가능하다.
'''
studentsTuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

# searchName = input('학생 이름 입력: ')
# if searchName in studentsTuple:
#     print('{} 학생은 우리반 학생입니다.'.format(searchName))
# else:
#     print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))

# searchName = input('학생 이름 입력: ')
# if searchName not in studentsTuple:
#     print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))
# else:
#     print('{} 학생은 우리반 학생입니다.'.format(searchName))


# studentsList = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

# searchName = input('학생 이름 입력: ')
# if searchName in studentsList:
#     print('{} 학생은 우리반 학생입니다.'.format(searchName))
# else:
#     print('{} 학생은 우리반 학생이 아닙니다.'.format(searchName))

    
    
    
pythonStr = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
            '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
            '파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'
    
print(f'\'Python\' in String? : {"Python" in pythonStr}')
print(f'\'python\' in String? : {"python" in pythonStr}')