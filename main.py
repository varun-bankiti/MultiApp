from Tkinter import*
from tkMessageBox import*
from text123 import*
from caluculator import*
from sudoku import*
from city import*
from det import*
from dictionary import*
r=Tk()
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
b1=Button(f,text="caluculator",width=25,height=10,command=calci)
b1.grid(row=0,column=0,sticky=W+N+E+S)
b2=Button(f,text="DET",width=25,height=10,command=DET)
b2.grid(row=0,column=1,sticky=W+N+E+S)
b2=Button(f,text="Text Editor",width=25,height=10,command=text)
b2.grid(row=0,column=2,sticky=W+N+E+S)
b2=Button(f,text="STP problem",width=25,height=10,command=stp)
b2.grid(row=0,column=3,sticky=W+N+E+S)
b2=Button(f,text="SUDOKU",width=25,height=10,command=sudoku)
b2.grid(row=1,column=0,sticky=W+N+E+S)
b2=Button(f,text="DICTIONARY",width=25,height=10,command=dis)
b2.grid(row=1,column=1,sticky=W+N+E+S)
b2=Button(f,text="Will fill this very soon",width=25,height=10,command=dis1)
b2.grid(row=1,column=2,columnspan=2,sticky=W+N+E+S)
r.mainloop()
