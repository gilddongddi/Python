# Q2. 사용자로부터 입력 받은 정수가 양수, 음수, 0인지 판별하여 출력하기

num = int(input('정수 입력: '))
if num>0:
    print('%d양수 ' %num)
elif num<0:
    print('%d 음수' %num)
else:
    print('%d 0' %num)
    
