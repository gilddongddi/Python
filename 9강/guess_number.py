import random
com = random.randint(1,20)
print('\n\n♥ ♥ ♥ 이서린, 이서연을 위한!! ♥ ♥ ♥')
print('\n★ 하트뿅뿅♥ 재미있는 컴퓨터 게임♥ ♥ ♥ ★')
print('\n"제1탄"')
print('\n<<컴퓨터가 생각한 1~20까지 숫자 맞추기~~~>>\n')
print('\n[게임방법] 컴퓨터가 1~20까지의 숫자중 한개의 숫자를 생각했어요. 컴퓨터가 생각한 숫자가 무엇인지 맞춰봅시당 ^>^')
print('\n          게임종료는 언제든지 숫자 0 을 눌러주세용~~ ♥ ♥ ♥')

cnt = 0

while True:
    
    player = int(input('\n숫자 입력(종료0): '))
    if player == 0:
        print('종료\n') 
        break
    elif player == com:
       cnt += 1
       print('\n ★정답!\n')
       print('★%d번 만에 맞췄어요! :D' %cnt)
       go=input('\n한판 더 고고?? (y/n) : ')
       if go=='y' :
          cnt = 0
          continue
       else :
          break
    elif player > com:
       cnt += 1
       print( )
       print('*힌트: 더 작은 숫자! 파이팅!!')
       print( )
       
    else :
       cnt += 1
       print( )
       print('*힌트: 더 큰 숫자! 파이팅!!')
       print( )
 
                
