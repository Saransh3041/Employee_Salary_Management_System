from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox


def showhodnavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="HODtable",font=('arial',25))
    z.place(x=210,y=40)

   
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select hodid, hodname, deptid, remarks from hodtable"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
        db.commit()
        db.close()
        
    
    
    a1=Label(t,text='Hod id')
    a1.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=150,y=100)
    
    a2=Label(t,text='Hod Name')
    a2.place(x=50,y=140)
    e2=Entry(t,width=30)
    e2.place(x=150,y=140)
    
    a3=Label(t,text='Dept id')
    a3.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=150,y=180)
    
    a4=Label(t,text='Remarks')
    a4.place(x=50,y=220)
    e4=Entry(t,width=30)
    e4.place(x=150,y=220)
    
    bt1=Button(t,text='First',command=first)
    bt1.place(x=60,y=270)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=160,y=270)
    
    bt3=Button(t,text='Previous',command=pt)
    bt3.place(x=260,y=270)
    
    bt4=Button(t,text='Last',command=lt)
    bt4.place(x=360,y=270)
    
    filldata()
    
    t.mainloop()