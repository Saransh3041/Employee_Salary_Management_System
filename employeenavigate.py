from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox

def showemployeenavigate():
    t=tkinter.Tk()
    t.geometry('500x500')
    Ca1=Canvas(t,height=100,width=500,bg='Blue')
    Ca1.place(x=0,y=0)
    ca2=Canvas(t,height=400,width=500,bg='lightblue')
    ca2.place(x=0,y=100)
    z=Label(t,text="Employee",font=('arial',25))
    z.place(x=210,y=40)


    

    
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
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
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select empid,name,city,address,email,phone,deptid from employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])  
            xf.append(res[5])
            xg.append(res[6])
        db.commit()
        db.close()
        
    
    
    
    a1=Label(t,text='Emp ID')
    a1.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=150,y=100)
    
    a2=Label(t,text='Name')
    a2.place(x=50,y=140)
    e2=Entry(t,width=30)
    e2.place(x=150,y=140)
    
    a3=Label(t,text='City')
    a3.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=150,y=180)
    
    a4=Label(t,text='Address')
    a4.place(x=50,y=220)
    e4=Entry(t,width=30)
    e4.place(x=150,y=220)
    
    a5=Label(t,text='Email')
    a5.place(x=50,y=260)
    e5=Entry(t,width=30)
    e5.place(x=150,y=260)
    
    a6=Label(t,text='Phone')
    a6.place(x=50,y=300)
    e6=Entry(t,width=30)
    e6.place(x=150,y=300)
    
    a7=Label(t,text='Dept ID')
    a7.place(x=50,y=340)
    e7=Entry(t,width=30)
    e7.place(x=150,y=340)
    
    bt1=Button(t,text='First',command=first)
    bt1.place(x=60,y=400)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=160,y=400)
    
    bt3=Button(t,text='Previous',command=pt)
    bt3.place(x=260,y=400)
    
    bt4=Button(t,text='Last',command=lt)
    bt4.place(x=360,y=400)
    
    filldata()
    
    t.mainloop()