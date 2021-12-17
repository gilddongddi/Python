#10강 실습1

def grade(s):
    # 점수에 다라 학점을 출력
    if s>=90:
        print('A')
    elif s>=80:
        print('B')
    elif s>=70:
        print('C')
    else:
        print('F')
        

#메인코드

score = int(input('score: '))

#함수는 호출해줘야 의미가 있음
grade(score)
grade()


