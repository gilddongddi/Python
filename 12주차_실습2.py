from tkinter import *
from tkinter.messagebox import *

#함수정의
def login():
    if pw.get()=='sejong':
        showinfo('success','로그인성공')
    else:
        showinfo('fail','패스워드오류')
        


w=Tk()

#윈도우 제목
w.title("Welcome to SEJONG!")

#위젯생성
label1 = Label(w, text='패스워드')
pw=Entry(w, show='★')

btn1 = Button(w, text='확인',command=login)
btn2 = Button(w, text='종료', command=quit)

#위젯배치(비로소 창에 표시됨)
label1.pack()
pw.pack()
btn1.pack()
btn2.pack()
w.geometry('300x200')

