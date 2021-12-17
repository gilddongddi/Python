# Q2. 사용자로부터 시작과 끝 값을 입력 받은 후 전체 합계, 짝수의 합계, 홀수의 합계를 출력하는 프로그램


s = int(input('start num: '))
e = int(input('end num: '))
total, even, odd=0,0,0
for i in range(s,e+1):
    total += i
    if i%2 ==0:
        even +=i
    else:
        odd =+i

print('전체합계: ', total)
print('짝수의 합: ',even)
print('홀수의 합: ', odd)
