# 두 정수를 입력 받고, 사칙 연산자 중 하나를 입력 받아 사칙 연산의 결과를 출력한다.

n1 = int(input('숫자를 입력하세요: '))
n2 = int(input('숫자를 입력하세요: '))
ao = input('+,-,*,/ 중 하나를 골라 입력하세요: ')
 
if ao == '+':
    result=n1+n2
elif ao=='-':
    result=n1-n2
elif ao=='*':
    result=n1*n2
else :
    result=n1/n2


print('%d %s %d=%d' % (n1,ao,n2,result))

