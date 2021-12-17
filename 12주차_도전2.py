from tkinter import *
from tkinter.messagebox import *

#def login():
#    if id.get()=='sejong' and pw.get()=='1234': 
#        showinfo('success','성공')
#    else:
#        showinfo('fail','아이디나 비밀번호를 확인하세요')
        


def login():
    if id.get()=='sejong':
        if pw.get()=='1234':
            showinfo('success', '로그인성공')
        else:
            showinfo('fail','비밀번호를 확인하세요')
    else:
        showinfo('fail','아이디를 확인하세요')

w=Tk()

w.title("Welcome to SEJONG!")


label1 = Label(w, text= '아이디',fg='red', font = 'Times 15 bold italic')
id=Entry(w)
label2 = Label(w, text='패스워드', font = 'Romans 30 bold')
pw=Entry(w, show='*')

btn1 = Button(w, text='확인', bg='green',command=login)
btn2 = Button(w, text='종료',  command=quit)


label1.grid(row=0, column=0)
id.grid(row=0,column=1)
label2.grid(row=1, column=0)
pw.grid(row=1,column=1)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)


w.geometry('350x200')


