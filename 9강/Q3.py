# Q3. 레벨 판별 프로그램

score = [ 85,95,70,50,100]
n=0
print('코딩 시험 결과')
print('-'*30)
for s in score:
    n += 1

    if s>=90:
        result='LEVEL1'
    elif s>=80:
        result='LEVEL2'
    elif s>=70:
        result='LEVEL3'
    else:
        result='FAIL'

    print('{}번 학생의 점수는 {}입니다.'.format(n,s))
    print('결과는 {}입니다.' .format(result))
    print()
