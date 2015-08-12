from Tkinter import*
from math import*
def calci1():
    root=Tk()
    root.title("Basic Caaluculator")
    fr1=Frame(root,bd=5,bg="green")
    fr1.grid(row=0,column=0)
    tx1=Entry(fr1,width=52)
    tx1.grid(row=0,column=0)
    fr2=Frame(root,bd=5,bg="purple")
    fr2.grid(row=1,column=0)
    def bt0():
        tx1.insert(END,"0")
    def bt1():
        tx1.insert(END,"1")
    def bt2():
        tx1.insert(END,"2")
    def bt3():
        tx1.insert(END,"3")
    def bt4():
        tx1.insert(END,"4")
    def bt5():
        tx1.insert(END,"5")
    def bt6():
        tx1.insert(END,"6")
    def bt7():
        tx1.insert(END,"7")
    def bt8():
        tx1.insert(END,"8")
    def bt9():
        tx1.insert(END,"9")
    def btinto():
        tx1.insert(END,"*")
    def btplus():
        tx1.insert(END,"+")
    def btminus():
        tx1.insert(END,"-")
    def btdot():
        tx1.insert(END,".")
    def btby():
        tx1.insert(END,"/")
    def btequal():
        g=tx1.get()
        tx1.delete(0,END)
        tx1.insert(END,eval(g))




    b1=Button(fr2,text="1",width=10,height=1,bg="grey",command=bt1)
    b1.grid(row=0,column=0)
    b2=Button(fr2,text="2",width=10,height=1,bg="grey",command=bt2)
    b2.grid(row=0,column=1)
    b3=Button(fr2,text="3",width=10,height=1,bg="grey",command=bt3)
    b3.grid(row=0,column=2)
    b4=Button(fr2,text="4",width=10,height=1,bg="grey",command=bt4)
    b4.grid(row=1,column=0)
    b5=Button(fr2,text="5",width=10,height=1,bg="grey",command=bt5)
    b5.grid(row=1,column=1)
    b6=Button(fr2,text="6",width=10,height=1,bg="grey",command=bt6)
    b6.grid(row=1,column=2)
    b7=Button(fr2,text="7",width=10,height=1,bg="grey",command=bt7)
    b7.grid(row=2,column=0)
    b8=Button(fr2,text="8",width=10,height=1,bg="grey",command=bt8)
    b8.grid(row=2,column=1)
    b9=Button(fr2,text="9",width=10,height=1,bg="grey",command=bt9)
    b9.grid(row=2,column=2)
    bi=Button(fr2,text="*",width=10,height=1,bg="grey",command=btinto)
    bi.grid(row=3,column=0)
    b0=Button(fr2,text="0",width=10,height=1,bg="grey",command=bt0)
    b0.grid(row=3,column=1)
    bb=Button(fr2,text="/",width=10,height=1,bg="grey",command=btby)
    bb.grid(row=3,column=2)
    bplus=Button(fr2,text="+",width=10,height=1,bg="grey",command=btplus)
    bplus.grid(row=0,column=3)
    bminus=Button(fr2,text="-",width=10,height=1,bg="grey",command=btminus)
    bminus.grid(row=1,column=3)
    bstring=Button(fr2,text=".",width=10,height=1,bg="grey",command=btdot)
    bstring.grid(row=2,column=3)
    bqul=Button(fr2,text="=",width=10,height=1,bg="grey",command=btequal)
    bqul.grid(row=3,column=3)
    root.mainloop  
