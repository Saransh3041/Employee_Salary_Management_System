from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showcompanynavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    h1=Label(t,text='Company Master',font=('arial',30))
    h1.place(x=100,y=20)


   
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
    
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select compid, compname, address, phone, email,city from companymaster"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])  
            xf.append(res[5])
        db.commit()
        db.close()
        
    
   
    
    a1=Label(t,text='Comp id')
    a1.place(x=50,y=120)
    e1=Entry(t,width=30)
    e1.place(x=150,y=120)
    
    a2=Label(t,text='Comp Name')
    a2.place(x=50,y=160)
    e2=Entry(t,width=30)
    e2.place(x=150,y=160)
    
    a3=Label(t,text='Address')
    a3.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=150,y=200)
    
    a4=Label(t,text='Phone')
    a4.place(x=50,y=240)
    e4=Entry(t,width=30)
    e4.place(x=150,y=240)
    
    a5=Label(t,text='Email')
    a5.place(x=50,y=280)
    e5=Entry(t,width=30)
    e5.place(x=150,y=280)
    
    a6=Label(t,text='city')
    a6.place(x=50,y=320)
    e6=Entry(t,width=30)
    e6.place(x=150,y=320)
    
    bt1=Button(t,text='First',command=first)
    bt1.place(x=60,y=360)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=160,y=360)
    
    bt3=Button(t,text='Previous',command=pt)
    bt3.place(x=260,y=360)
    
    bt4=Button(t,text='Last',command=lt)
    bt4.place(x=360,y=360)
    
    filldata()
    
    t.mainloop()