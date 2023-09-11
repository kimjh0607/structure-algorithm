
students = {
    'S21-0001' : {'이름' : '최성훈',
                  '성구분' : 'M',
                  '전공' : '디자인',
                  '연락처' : '010-1234-5678',
                  '메일' : 'hun@gmail.com',
                  '취미' : ['농구', '음악']
                  },
    'S21-0002' : {'이름' : '탁영우',
                  '성구분' : 'M',
                  '전공' : '바리스트',
                  '연락처' : '010-5678-9012',
                  '메일' : 'yeong@gmail.com',
                  '취미' : ['축구']
                  },
    'S21-0003' : {'이름' : '황진영',
                  '성구분' : 'F',
                  '전공' : '음악',
                  '연락처' : '010-9012-3456',
                  '메일' : 'jin@gmail.com',
                  '취미' : ['수영', '코딩']
                  }
}

for stuKey in students.keys():
    print('-' * 40)
    print(f'학생번호 : {stuKey}')
    
    student = students[stuKey]
    for infoKey in student.keys():
        print(f'{infoKey} : {student[infoKey]}')


print('-' * 30)
stuCode = input('조회할 학생번호 입력 : ')
info = students[stuCode]
for key in info.keys():
    print(f'{key} : {info[key]}')