import random

lotto=[]
print('로또 프로그램 시작')

while True:
    num=random.randint(1,45)
    if lotto.count(num)==0:
        lotto.append(num)

    if len(lotto)==6:
        break

print('추첨된 번호')
#print(lotto)
lotto.sort()
#print(lotto)

for i in range(6):
   print('{}'.format(lotto[i]),end=' ')
