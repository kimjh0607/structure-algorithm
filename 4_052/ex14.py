
members = {}

n=1
while n < 6:
    mail = input('메일을 입력하세요 : ')
    pw = input('비밀번호 입력 : ')

    if mail in members:
        print('메일 중복! 다시 입력하세요.')
        continue
    else:
        members[mail] = pw

    n += 1

for key in members.keys():
    print(f'{key} : {members[key]}')


while True:
    delMail = input('삭제 메일 입력 : ')
    if delMail in members:
        delPw = input('비번 입력 : ')
        if delPw == members[delMail]:
            del members[delMail]
            print(f'{delMail}계정 삭제 완료')
            break
        else:
            print('비번 불일치!!')
    else:
        print('계정 불일치!!!')

for key in members.keys():
    print(f'{key} : {members[key]}')