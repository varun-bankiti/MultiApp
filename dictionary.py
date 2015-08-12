from Tkinter import *
from tkMessageBox import*
import urllib2,urllib
def dictionary123():
    def get_mean(i,x,y):
        start=0
        k=""
        for j in range(x+10,y):
            if i[j]=="<":
                start=1
            if i[j]==">":
                start=0
                continue
            if start==0:
                k=k+i[j]
        return i[x+3:x+5]+k+"\n"
    def search():
        word=entry.get()
        print word
        url="http://www.thefreedictionary.com/"+word
        proxy = urllib2.ProxyHandler({'http': 'http://R091057:418S31057VC@10.20.3.2:3128'})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        showinfo("Alert","Make sure that u r connected to INTERNET")
        conn = urllib2.urlopen(url)
    #    try:
    #        conn = urllib2.urlopen(url)
    #    except URLError:
    #        showwarning("Oops you are not connected to Internet")
        return_str = conn.readlines()
        for i in return_str:
            if ('<b>1. </b>' in i)and('<b>3. </b>' in i)and('<b>2. </b>' in i)and('<b>4. </b>' in i):
                x1=i.index('<b>1. </b>')
                y1=i.index('</div><div class="ds-list"><b>2')
                x2=i.index('<b>2. </b>')
                y2=i.index('</div><div class="ds-list"><b>3')
                x3=i.index('<b>3. </b>')
                y3=i.index('</div><div class="ds-list"><b>4')
                x4=i.index('<b>4. </b>')
                y4=i.index('</div></div>')
                a=get_mean(i,x1,y1)
                b=get_mean(i,x2,y2)
                c=get_mean(i,x3,y3)
                d=get_mean(i,x4,y4)
                label1.delete(1.0,END)
                label2.delete(1.0,END)
                label3.delete(1.0,END)
                label4.delete(1.0,END)
                label1.insert(END,a)
                label2.insert(END,b)
                label3.insert(END,c)
                label4.insert(END,d)
            elif ('<b>1. </b>' in i)and('<b>3. </b>' in i)and('<b>2. </b>' in i):
                x1=i.index('<b>1. </b>')
                y1=i.index('</div><div class="ds-list"><b>2')
                x2=i.index('<b>2. </b>')
                y2=i.index('</div><div class="ds-list"><b>3')
                x3=i.index('<b>3. </b>')
                y3=i.index('</div></div>')
                a=get_mean(i,x1,y1)
                b=get_mean(i,x2,y2)
                c=get_mean(i,x3,y3)
                label1.delete(1.0,END)
                label2.delete(1.0,END)
                label3.delete(1.0,END)
                label4.delete(1.0,END)
                label1.insert(END,a)
                label2.insert(END,b)
                label3.insert(END,c)
            elif ('<b>1. </b>' in i)and('<b>2. </b>' in i):
                x1=i.index('<b>1. </b>')
                y1=i.index('</div><div class="ds-list"><b>2')
                x2=i.index('<b>2. </b>')
                y2=i.index('</div></div>')
                a=get_mean(i,x1,y1)
                b=get_mean(i,x2,y2)
                label1.delete(1.0,END)
                label2.delete(1.0,END)
                label3.delete(1.0,END)
                label4.delete(1.0,END)
                label1.insert(END,a)
                label2.insert(END,b)
            elif ('<b>1. </b>' in i):
                x1=i.index('<b>1. </b>')
                y1=i.index('</div></div>')
                a=get_mean(i,x1,y1)
                label1.delete(1.0,END)
                label2.delete(1.0,END)
                label3.delete(1.0,END)
                label4.delete(1.0,END)
                label1.insert(END,a)
            elif 'Word not found in the Dictionary' in i:
                label1.delete(1.0,END)
                label2.delete(1.0,END)
                label3.delete(1.0,END)
                label4.delete(1.0,END)
                label1.insert("The Given Word"+word+"Not found in the Dictionary!!!")

    root=Tk()
    root.title("Dictionary")
    frame=Frame(root,width=500,height=500)
    frame.pack()
    label=Label(frame,text="Enter the word Here:")
    label.grid(row=1,column=1)
    entry=Entry(frame,width=50)
    entry.grid(row=1,column=2)
    button=Button(frame,text="Search",command=search)
    button.grid(row=1,column=3)
    label1=Text(frame,height=4,width=50)
    label1.grid(row=2,column=2)
    label2=Text(frame,height=4,width=50)
    label2.grid(row=3,column=2)
    label3=Text(frame,height=4,width=50)
    label3.grid(row=4,column=2)

    label4=Text(frame,height=4,width=50)
    label4.grid(row=5,column=2)

    mainloop()


