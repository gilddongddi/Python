# 13강 종합프로잭트 실습1

#함수정의
def add():
    name=input('이름: ')                #이름 등을 입력받아 변수에 저장
    phone=input('전화번호: ')
    email=input('이메일: ')
    return(name,phone,email)

print("메뉴를 선택하세요")
print("1:추가 ")
print("2:종료 ")



datalist = list()                            #여러 사람을 담을 수 있는 리스트 변수 선언  list() <- 빈리스트선언


while True:                                 # T는 대문자
    menu = int(input("메뉴선택? : "))
    
    if menu==1:
        
        datalist.append(add())   # name, phnone, email 변수에 입력된 값을 튜 플로 리스트에 저장
        print(datalist)
        
        
    elif menu==0:
        break
    else:
        print('입력오류')

    
    
