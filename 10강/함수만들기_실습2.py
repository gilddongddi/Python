#실습2
#함수정의

def add(n1,n2,n3):
    result =n1+n2+n3
    return result
 
#메인코드
num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num2: '))

#함수호출
result = add(num1,num2, num3)
print(result)
