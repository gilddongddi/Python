# 두 정수를 입력 받고, 사칙 연산자 중 하나를 입력 받아 사칙 연산의 결과를 출력한다.

a = int(input('숫자를 입력하세요: '))
b = int(input('숫자를 입력하세요: '))
ao = input('+,-,*,/ 중 하나를 골라 입력하세요: ')
 
if ao == '+':
      print('%d+%d = %d' %(a,b,(a+b)))
elif ao == '-':
      print('%d-%d = %d' %(a,b,(a-b)))
elif ao == '*':
    print('%d*%d = %d' %(a,b,(a*b)))
elif ao == '/':
    print('%d/%d = %d' %(a,b,(a/b)))
else:
    print('END')
    
