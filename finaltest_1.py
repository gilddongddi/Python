from tkinter import *


import random


root = Tk()
root.title("파이썬 기말과제 가위바위보 게임")

root.geometry("1500x1000")


frame = Frame(root)
frame.pack()





#프레임 생성

l_frame = Frame(frame, width=500, height=400, bg='white')
l_frame.grid(row=2, column=0)

c_frame = Frame(frame, width=200, height=400, padx=40, background='sky blue')
c_frame.grid(row=2, column=1)

r_frame = Frame(frame, width=500, height=400,background="light blue")
r_frame.grid(row=2, column=2)

bottom_frame = Frame(frame,width=1200, pady=30, height=200, bg="light green")
bottom_frame.grid(row=3, column=0, columnspan=3, sticky=E+W+S+N)



#캔바스 삽입

canvas1 = Canvas(l_frame, width=500, height=400, bg='blue')
canvas1.grid(row=2, column=0)

canvas2 = Canvas(r_frame, width=500, height=400, bg='blue')
canvas2.grid(row=2, column=2)



#레이블 생성

label = Label(frame, text="가위!바위!보!", width=50, pady=30,font=('나눔고딕코딩', 20, 'bold'))
label.grid(row=0, column=0, columnspan=3)

label1 = Label(frame, text="플레이어", width=50, font=('나눔고딕코딩',20, 'bold'))
label1.grid(row=1, column=0)

label2 = Label(frame, text="컴퓨터", width=50, font=('나눔고딕코딩', 20, 'bold'))
label2.grid(row=1, column=2)

vs = Label(c_frame, text="VS", font=("Romans", 35, "bold"))
vs.grid(row=2, column=1)


com_list = ['가위', '바위', '보']

player = ['가위', '바위', '보']



#게임 함수 생성

def com_choice():
    rand_choice = random.randint(0,2)
    if com_list[rand_choice] == '가위':
        canvas2.create_image(250,200, image=kawi)
    elif com_list[rand_choice] == '바위':
        canvas2.create_image(250,200, image=bawi)
    else:
        canvas2.create_image(250,200, image=po)
    
    return com_list[rand_choice]
    


def play(a):

    canvas1.delete("all")
    canvas2.delete("all")
    
    com_choice()

    if a == "가위":
        canvas1.create_image(250,200, image=kawi)
        


    elif a == "바위":
        canvas1.create_image(250,200, image=bawi)

        

    else:
        canvas1.create_image(250,200, image=po)
        
        
        
    

    

  
    
    if a == "가위":
        canvas1.create_image (200, 200, image=tk_k1)

        if computer == 1:

            l2= Label(w, width=10, text='무승부!!',fg="purple", font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)

        elif computer == 2:

            l2 = Label(w,text='컴퓨터 승!!',fg="purple", font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)
            canvas2.create_image(250,380, image=winner)
            computer1 += 1

        elif computer == 3:

            l2= Label(w, text='플레이어승!!',fg="purple",font=("둥근모꼴",30,"bold"))
            l2.grid (row=1, column=1)
            canvas1.create_image(250,380, image=winner)
            player1 += 1
            
    elif a == "바위":
        canvas1.create_image (200, 200, image=tk_b1)

        if computer == 1:

            l2 = Label(w, text='플레이어승!!',fg="purple", font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)
            canvas1.create_image(250,380, image=winner)
            player1 += 1
            
        elif computer == 2:

            l2 = Label(w, width=10,text='무승부!!' ,fg="purple",font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)

        elif computer == 3:

            l2 = Label(w, text='컴퓨터 승!!',fg="purple", font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)
            canvas2.create_image(250,380, image=winner)
            computer1 += 1
            
    elif a == "보":
        canvas1.create_image (250, 200, image=tk_p1)
        
        if computer == 1:

            l2 = Label(w, text='컴퓨터 승!!', fg="purple",font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)
            canvas2.create_image(250,380, image=winner)
            computer += 1
            
        elif computer == 2:

            l2 = Label(w, text='플레이어승!!',fg="purple", font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)
            canvas1.create_image(250,380, image=winner)
            player1 += 1
            
        elif computer == 3:

            l2 = Label(w,width=10, text='무승부!!', fg="purple",font = ("둥근모꼴",30, "bold"))
            l2.grid (row=1, column=1)



#버튼 생성

btn1 = Button(bottom_frame, text='가위', width=10, font=('Gothic', 20, 'bold'), command=lambda:play("가위"))
btn2 = Button(bottom_frame, text='바위',width=10,  font=('나눔고딕코딩', 20, 'bold'), command=lambda:play("바위"))
btn3 = Button(bottom_frame, text='보', width=10,  font=('명조', 20, 'bold'), command=lambda:play("보"))

btn1.grid(row=3, column=0, padx=50)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)


#이미지 삽입
kawi=PhotoImage(file="kawi3.png")
bawi=PhotoImage(file="bawi.png")
po=PhotoImage(file="po5.png")
winner = PhotoImage(file='winner.png')







    
#승


#패

#무승부






























root.mainloop()
