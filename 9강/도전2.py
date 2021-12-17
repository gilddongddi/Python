# 도전2: 스마트폰 주소록 프로그램
# 1) 친구등록 2) 검색 3) 종료:

addr={} # 빈 딕셔너리 생성

while True:
    s = int(input('\n1) 친구 등록 2) 검색 3) 종료 :'))
    if s == 1:
        name=input('name: ')
        phone = input('phone: ')
        addr[name]=phone
    elif s==2:
        name=input('name: ')
        print(addr.get(name, 'not found'))
    elif s==3:
        print('프로그램이 종료됩니다')
        break
    else:
        print('menu error')
