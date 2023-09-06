members = {'alkjh':'1723803',
           'ajhbs':'1827632',
           'cvgbf':'3819573',
           'svfdd':'5621522',
           'kjiok':'5215632',
           'vbhgv':'2122112',
           'bnjhg':'7951126',
           'vbgfc':'8965456',
           'cvbhg':'2145212',
           'jnbhn':'2141115'}

memID = input('ID 입력: ')
memPW = input('PW 입력: ')

if memID in members:
    if memPW == members[memID]:
        print('로그인 성공~')
    else:
        print('비밀번호 틀림!')
else:
    print('아이디가 없습니다!')
