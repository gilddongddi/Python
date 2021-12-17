from tkinter import *
import random
import pygame

pygame.init()



    
w = Tk()
w.title("파이썬 기말과제  가위바위보")


player1=0
computer1=0


def count():
    global player1
    count_player = str(player1)
    global computer1
    count_computer = str(computer1)

def play(a):

    canvas1.delete("all")
    canvas2.delete("all")
    
    count()

    global player1
    global computer1
    
    global computer
    computer = random.randint(1, 3)

    
    if computer == 1: #가위
        canvas2.create_image (250, 200, image=tk_k1)
    elif computer == 2: #바위
        canvas2.create_image (250, 200, image=tk_b1)
    elif computer == 3: #보
        canvas2.create_image (250, 200, image=tk_p1)


    if a == "가위":
        canvas1.create_image (200, 200, image=tk_k1)
        kawi_sound = pygame.mixer.Sound('sound1.mp3')
        kawi_sound.play()

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
        bawi_sound = pygame.mixer.Sound('sound2.mp3')
        bawi_sound.play()

        
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
        po_sound = pygame.mixer.Sound('sound3.mp3')
        po_sound.play()
        

        
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


    










playerLabel = Label(w, text="플레이어", font=("Gothic",20, "bold"))
playerLabel.grid(row=0, column=0)

comLabel = Label(w, text="컴퓨터", font=("Gothic",20, "bold"))
comLabel.grid(row=0,column=2)


vs = Label(w, text='VS', font =("Romans", 30, "bold"))
vs.grid(row=2,column=1)



canvas1 = Canvas(w, width=500, height=400)
canvas1.grid(row=1, column=0)

canvas2 = Canvas(w, width=500, height=400)
canvas2.grid (row=1, column=2)

'''
pointbox = Label(w, text=computer1)
pointbox.grid(row=2,column=2)

pointbox2 = Label(w, text=player1)
pointbox2.grid(row=2, column=0)

'''

canvas3 = Canvas(w, width=500, height=100)
canvas3.grid(row=2, column=0)

canvas4 = Canvas(w, width=500, height=100)
canvas4.grid(row=2, column=2)


canvas3.create_rectangle((200, 30, 300, 70), fill="yellow")
canvas3.create_text((250,50), text=player1 )

canvas4.create_rectangle((200, 30, 300, 70), fill="yellow")
canvas4.create_text((250, 50), text=computer1)



'''
label_user.create_test(text=computer1)

label_user = Label(w, textvariable = player1, font = ("Romans", 35, "bold"), fg="red")
label_user.grid(row=2, column=0)

label_com = Label(w, textvariable = computer1, font =( "Romans", 35, "bold"), fg="blue")
label_com.grid(row=2, column=2)
'''



'''
k1=Image.open("kawi.png")
b1=Image.open("bawi.png")
p1=Image.open("po2.png")
'''
tk_k1=PhotoImage(file="kawi3.png")
tk_b1=PhotoImage(file="bawi.png")
tk_p1=PhotoImage(file="po5.png")
winner = PhotoImage(file='winner.png')

canvas1.create_text(225,200, text="가위 바위 보를 선택하세요!!", font=("나눔고딕코딩",20, 'bold'),fill="darkgreen")

'''
num = 0
kbp = ["바위","보","가위"]
for loop in kbp:
    def clickKBP(j=loop):
        onClick(j)
    button=Button(w, text=loop,  font=("둥근모꼴",12,"bold"), width = 25, command=clickKBP)
    button.grid (row=3, column=num)
    num=num+1

'''

btn1=Button(w, text="가위", font=("둥근모꼴",12,"bold"),width=25, command=lambda:play("가위"))
btn1.grid(row=3, column=0)

btn2=Button(w, text="바위", font=("둥근모꼴",12,"bold"),width=25, command=lambda:play("바위"))
btn2.grid(row=3, column=1)

btn3=Button(w, text="보", font=("둥근모꼴",12,"bold"),width=25, command=lambda:play("보"))
btn3.grid(row=3, column=2)




    
w.mainloop()
