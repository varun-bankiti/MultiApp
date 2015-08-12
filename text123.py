from Tkinter import*
from tkMessageBox import*
from tkFileDialog import*
def Text1():
    r=Tk()
    r.title("TextEditor")
    menu=Menu(r)
    def open1():
        x=askopenfilename()
        if len(x)!=0:
            xwr.append(x)
            f=open(x,"r")
            f=f.readlines()
            for c in f:
                text.insert(END,c)
    def new():
        x1=askopenfilename()
        if len(x1)!=0:
            xwr.append(x1)
            f=open(x1,"w")
            t=text.get(1.0,END)
            f.write(t)
    def save1():
        if(len(xwr)==0 or len(xwr[-1])==0):
            showinfo("Bad Option","choose a file                       ")
            return True
        f=open(str(xwr[-1]),"w")
        t=text.get(1.0,END)
        f.write(t)
    xwr=[]
    menu.add_command(label="New",command=new)
    menu.add_command(label="Open",command=open1)
    menu.add_command(label="Save",command=save1)
    r.config(menu=menu)
    f=Frame(r,bg="brown",width=500,height=500,bd=7)
    text=Text(f,width=100,height=30)
    text.pack()
    f.pack();
    r.mainloop()
