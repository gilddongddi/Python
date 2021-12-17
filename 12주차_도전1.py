# 도전1 여러가지 도형그리기



from tkinter import *

from turtle import *


w = Tk()
w.title("Python Turtle Graphics")

label1 = Label(w, text='도형그리기')
n=int(textinput('도형그리기', '숫자입력(삼각형:3, 사각형:4, 오각형:5)'))

shape('turtle')


def makepolygon(n):
    for i in range(n):
        forward(300)
        left(360/n)


if n in [3,4,5,6,7,8,9,10]:
    makepolygon(n)

else:
    print('error')
