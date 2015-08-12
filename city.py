from math import*
from random import*
from Tkinter import*
from tkMessageBox import*
def STP():
        globlist=[]
        def showfig(city_list,x):
                possible=[]
                possible.append(city_list)
                possible=[possible]
                count=0
                possible=genpossible(possible,count,x)
                dist=definedist(city_list)
                least_order=least_dist_as_key(possible,dist)
                key_order=least_order.keys()
                key_order.sort()
                mainroute=least_order[key_order[0]]
                for i in range(len(mainroute)):
                    x,y=city_list[i][0],city_list[i][1]
                    p=c1.create_oval(x,y,x+10,y+10,fill="red")
                    canvas_list.append(p)
                return mainroute
                
        def definedist(city_list):
            dist1={}
            for c in range(0,len(city_list)):
                for c1 in range(0,len(city_list)):
                    dist1[(city_list[c],city_list[c1])]=sqrt(pow(city_list[c1][0]-city_list[c][0],2)+pow(city_list[c1][1]-city_list[c][1],2))
            return dist1
        def least_dist_as_key(possible,dist):
            least_order={}
            for i in possible:
                distance=0
                i1,j=0,1
                while(j<len(i)):
                    distance+=dist[(i[i1],i[j])]
                    i1+=1
                    j+=1
                least_order[distance]=i
            return least_order

        def genpossible(possible,count,x):
            while count<x:
                li1=[]
                for s in possible[-1]:
                    u=s
                    s=s[count:]
                    for i in range(0,len(s)):
                        li1.append(u[0:count]+[s[i]]+s[0:i]+s[i+1:])
                count+=1
                possible=[]
                possible.append(li1)
            possible=possible[0]
            return possible
        colorlist=["orange"]
        def ran():
            lab1=Label(f2,text="Enter the number of cities")
            ent=Entry(f2)
            lab1.grid(row=1,column=0,columnspan=2)
            ent.grid(row=2,column=0,columnspan=2,sticky=W+N+E+S)
            def submit():
                def drawtg():
                        i,j=0,1
                        for l in range(len(route)-1):
                                p=route[l]
                                q=route[l+1]
                                a=c1.create_line(p[0]+5,p[1]+5,q[0]+5,q[1]+5,fill="green",width=2)
                                canvas_list.append(a)
                tg=Button(f2,text="Dtaw for this",command=drawtg)
                tg.grid(row=4,column=0,columnspan=2,sticky=W+N+E+S)
                for c in canvas_list:
                    c1.delete(c)
                x=ent.get()
                x=int(x)
                city_list=[]
                for i in range(x):
                    a=(randint(1,500),randint(1,500))
                    city_list.append(a)
                route=showfig(city_list,x)
                man_route=[]
                def getprint(event):
                        if len(man_route)<=1:
                                p1,p2=event.x,event.y
                                print city_list,p1,p2,len(man_route)
                                for c in city_list:
                                        p3,p4=c[0],c[1]
                                        if not ((p3-10>=p1 or p3+10<=p1)and (p4-10>=p2 or p4+10<=p2)):
                                                   man_route.append(c)
                                print man_route
                        if len(man_route)==2:
                                p1,p2,p3,p4=man_route[0][0],man_route[0][1],man_route[1][0],man_route[1][1]
                                p=c1.create_line(p1+5,p2+5,p3+5,p4+5,fill="green",width=2)
                                canvas_list.append(p)
                                for c in man_route:
                                        man_route.remove(c)
                c1.bind("<Button-1>",getprint)
            sub=Button(f2,text="Submit",command=submit)
            sub.grid(row=3,column=0,columnspan=2,sticky=W+N+E+S)
            

        def manual():
            lab1=Label(f2,text="Enter the cities coordinates HERE")
            ent=Entry(f2)
            lab1.grid(row=1,column=0,columnspan=2)
            ent.grid(row=2,column=0,columnspan=2)
            ent.insert(END,"10,20 50,30")
            def submit():
                def drawtg():
                        i,j=0,1
                        for l in range(len(route)-1):
                                p=route[l]
                                q=route[l+1]
                                a=c1.create_line(p[0]+5,p[1]+5,q[0]+5,q[1]+5,fill="green",width=2)
                                canvas_list.append(a)
                tg=Button(f2,text="Dtaw for this",command=drawtg)
                tg.grid(row=4,column=0,columnspan=2,sticky=W+N+E+S)
                for c in canvas_list:
                    c1.delete(c)
                x1=ent.get()
                x1=x1.split()
                city_list=[]
                for c in x1:
                    bi=(0,0)
                    c=c.split(",")
                    bi=(int(c[0]),int(c[1]))
                    city_list.append(bi)
                x=len(city_list)
                route=showfig(city_list,x)
                print route
            showinfo("hi","keep space between each pair")
            sub=Button(f2,text="Submit",command=submit)
            sub.grid(row=3,column=0,columnspan=2,sticky=W+N+E+S)
        r=Tk()
        r.title("Sales Travelling Person (STP)")
        f=Frame(r,bd=5,bg="black")
        canvas_list=[]
        f.grid(row=0,column=0)
        c1=Canvas(f,width=500,height=500,bg="black")
        c1.grid(row=0,column=0)
        f2=Frame(r,width=500,height=500,bg="purple")
        f2.grid(row=1,column=0,sticky=N+S+W)
        Brandom=Button(f2,text="Randomized cities",bg="red",command=ran)
        Brandom.grid(row=0,column=0,sticky=W+N+E+S)
        Bmanual=Button(f2,text="Set manual cities",bg="red",command=manual)
        Bmanual.grid(row=0,column=1,sticky=W+N+E+S)
        mainloop()
