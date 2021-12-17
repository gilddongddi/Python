# 정수를 입력받아 그 정수가 홀수인지 짝수인지 판단

num = int(input('정수 입력: '))
if (num%2) == 0:
    print('%d 짝수' % num)
else:
    print('%d 홀수' % num)
