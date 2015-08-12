from Tkinter import *
from random import *
import tkFileDialog
import tkMessageBox
def sdk():
    root=Tk()
    root.title("SUDOKU")
    menu=Menu(root)
    frame=Frame(root,bg="orange",bd=5,width="252",height="172")
    frame.pack(expand=-1)
    entry_list=[]
    list1=[]
    def new_game_hard():
        new_game(3)
    def new_game_normal():
        new_game(2)
    def new_game_easy():
        new_game(1)


    def load_game():
        a=tkFileDialog.askopenfilename(filetypes=[("sudoku", ".v")])
        f=open(a)
        lines=f.readlines()
        for i in range(9):
            temp=[]
            for j in range(9):
                if (lines[i][j]=="0"):
                    entry=Entry(frame,width=4)
                    entry.grid(row=i,column=j)
                else:
                    entry=Entry(frame,width=4)
                    entry.grid(row=i,column=j)
                    entry.insert(END,lines[i][j])
                    entry.config(state=DISABLED)
                temp.append(entry)
            entry_list.append(temp)

    def save_game():
        b=tkFileDialog.asksaveasfilename(filetypes=[("sudoku", ".v")])
        print b
        f=open(b,"w")
        for i in entry_list:
            for j in i:
                x=j.get()
                if x=="":
                    f.write("0")
                else:
                    f.write(x)
            f.write("\n")
    def check():
        count =0
        for i in range(0,9):
            for j in range(0,9):
                if entry_list[i][j].get()==str(list1[i][j]):
                    count=count+1
        if count==81:
            tkMessageBox.showinfo(title="Correct", message="Good Job")
        else:
            tkMessageBox.showwarning(title="Wrong", message="It Looks you had mistaken Try Again")
    def howto_paly():
        print "Instructions"
    def about():
        print "Hi!!!!"
    def sudoku(l1):
        temp=[]
        for k in range(9):
            j=1;
            while j: 
                i=randint(1,9)
                if i not in temp:
                    temp.append(i)
                    j=0
        for j in range(3):
            for i in range(3):
                l1.append(temp[(j+(3*i)):]+temp[:(j+(i*3))])
        
    def new_game(i):
        sudoku(list1)
        temp_list=list1
        if (i==3):
            for j in range(0,9):
                a=randint(4,8)
                for i in range(a):
                    b=randint(0,8)
                    temp_list[j][b]=0
        elif(i==2):
            for j in range(0,9):
                a=randint(3,6)
                for i in range(a):
                    b=randint(0,8)
                    temp_list[j][b]=0
        else:
            for j in range(0,9):
                a=randint(2,5)
                for i in range(a):
                    b=randint(0,8)
                    temp_list[j][b]=0
        for i in range(9):
            temp=[]
            for j in range(9):
                if (temp_list[i][j]==0):
                    entry=Entry(frame,width=4)
                    entry.grid(row=i,column=j)
                else:
                    entry=Entry(frame,width=4)
                    entry.grid(row=i,column=j)
                    entry.insert(END,temp_list[i][j])
                    entry.config(state=DISABLED)
                temp.append(entry)
            entry_list.append(temp)
        button=Button(frame,text="Check",command=check)
        button.grid(row=10,column=0,columnspan=9,sticky=W+N+E+S)
    root.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    newgame=Menu(menu)
    filemenu.add_cascade(label="New Game",menu=newgame)
    newgame.add_cascade(label="Hard",command=new_game_hard)
    newgame.add_cascade(label="Normal",command=new_game_normal)
    newgame.add_cascade(label="Easy",command=new_game_easy)

    filemenu.add_cascade(label="Load Game",command=load_game)
    filemenu.add_separator()
    filemenu.add_cascade(label="Save Game",command=save_game)
    helpmenu=Menu(menu)
    menu.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_cascade(label="How to Play",command=howto_paly)
    helpmenu.add_cascade(label="About",command=about)
    mainloop()
