from Tkinter import*
from tkMessageBox import*
def mat1():
    def start():
        def do():
            temp1=[]
            imp=0
            for i in range(x):
                temp=[]
                for j in range(x):
                    h=lis[imp]
                    imp+=1
                    h1=h.get()
                    if len(h1)==0:
                        showinfo("WRONG","One or more positions are empty;; fill them")
                        return 1
                    else:
                        h1=int(h1)
                        print h1
                    temp.append(h1)
                temp1.append(temp)
            lp=find_det(temp1)
            rg=Label(f1,text=str(lp))
            rg.grid(row=i+2,columnspan=x,sticky=W+N+E+S)
            r.quit()
            showinfo("DET","det is  "+str(lp))
            r.quit()
        f1=Frame(r,width=100,height=100,bd=5,bg="black")
        f1.grid(row=1,column=0,sticky=W+N+E+S)
        x=t.get()
        if len(x)>=1:
            x=int(x)
            lis=[]
            for i in range(x):
                for j in range(x):
                    y=Entry(f1,width=5)
                    y.grid(row=i,column=j)
                    lis.append(y)
            b=Button(f1,text="det",command=do,bg="red")
            b.grid(row=i+1,columnspan=x,sticky=W+N+E+S)
        else:
            showinfo("Alert","Choose a class ex  ::4")
    def find_det(mat):
        def det(mat):
                lk=0
                if len(mat)==2:
                        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
                else:
                        k=len(mat)
                        for i in range(k):
                                key=mat[0][i]
                                if(i%2!=0):
                                        key=-key
                                temp=[]
                                for i1 in range(1,k,1):
                                        temp1=mat[i1][0:i]+mat[i1][i+1:]
                                        temp.append(temp1)
                                lk+=key*det(temp)
                        return lk
                        
        k=det(mat)
        return k
    r=Tk()
    r.title("DET OF A MATRIX")

    f=Frame(r,bd=5,bg="violet")
    f.grid(row=0,column=0,sticky=W+N+E+S)
    menu=Menu(r)
    img=PhotoImage("bg.gif",width=100,height=100)
    l=Label(f,text="Enter the ORDER(EX::4) here")
    l.grid(row=0,column=0)
    t=Entry(f,width=10)
    t.grid(row=0,column=1)
    b1=Button(f,text="go",command=start)
    b1.grid(row=1,columnspan=2,sticky=W+N+E+S)
    menu.add_command(label="start",command=start)
    def help1():
        showinfo("HELP","Here u can find DET of any matric n*n")
    menu.add_command(label="Help",command=help1)
    r.config(menu=menu)
    r.mainloop()
