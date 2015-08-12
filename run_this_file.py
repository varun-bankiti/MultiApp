from Tkinter import*
from tkMessageBox import*
from text123 import*
from caluculator import*
from sudoku import*
from city import*
from det import*
from dictionary import*
r=Tk()
img1=PhotoImage(file="m.gif")
img2=PhotoImage(file="Calculator.gif")
img3=PhotoImage(file="Dic.gif")
img4=PhotoImage(file="notepad-icon-128.gif")
img5=PhotoImage(file="sudoku.gif")
img6=PhotoImage(file="V.gif")
r.title("RGUKT")
def text():
    Text1()
def calci():
    calci1()
def DET():
    mat1()
def stp():
    STP()
def sudoku():
    sdk()
def dis():
    dictionary123()
def dis1():
    showinfo("Hi......","This Under Construction")
menu=Menu(r)
f=Frame(r,width=700,height=300,bd=10,bg="orange")
f.pack(fill=BOTH)
b1=Button(f,image=img2,width=200,height=10,command=calci)
b1.grid(row=0,column=0,sticky=W+N+E+S)
b2=Button(f,image=img1,width=200,height=10,command=DET)
b2.grid(row=0,column=1,sticky=W+N+E+S)
b2=Button(f,image=img4,width=200,height=10,command=text)
b2.grid(row=0,column=2,sticky=W+N+E+S)
b2=Button(f,text="STP problem",width=25,height=10,command=stp)
b2.grid(row=0,column=3,sticky=W+N+E+S)
b2=Button(f,image=img5,width=200,height=10,command=sudoku)
b2.grid(row=1,column=0,sticky=W+N+E+S)
b2=Button(f,image=img3,width=200,height=10,command=dis)
b2.grid(row=1,column=1,sticky=W+N+E+S)
b2=Button(f,image=img6,width=25,height=200,command=dis1)
b2.grid(row=1,column=2,columnspan=2,sticky=W+N+E+S)
r.mainloop()
