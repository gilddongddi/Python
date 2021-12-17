# Q. 사각형 그리기

#import turtle

#turtle.shape('turtle')
#turtle.forward(100)


from turtle import *

shape('turtle')
color('red')

backward(100)
left(90)


for i in range(4):
    forward(500)
    left(90)

