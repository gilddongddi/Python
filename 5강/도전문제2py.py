# 아이디와 패스워드를 입력 받아 로그인 인증 결과를 출력한다.
# 아이디('admin'), 패스워드('1234') 둘 다 맞으면 로그인 성공 메시지를 출력하고 둘 중의 하나 이상 틀리면 오류 메시지 출력

sid = input('아이디 입력: ')
spw = input('패스워드 입력: ')

if sid == 'admin' and spw== '1234':
    print('로그인 성공')
else:
    print('로그인 실패')
    
