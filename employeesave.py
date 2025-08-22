
from tkinter import ttk

import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showemployeesave():
    t=tkinter.Tk()
    
    t.geometry('500x500')
    Ca1=Canvas(t,height=100,width=500,bg='Blue')
    Ca1.place(x=0,y=0)
    ca2=Canvas(t,height=400,width=500,bg='lightblue')
    ca2.place(x=0,y=100)
    z=Label(t,text="Employee",font=('arial',25))
    z.place(x=210,y=40)

    
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        xg=int(e7.get())
        sql="insert into employee values(%d,'%s','%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Your data is saved.')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
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
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=180,y=380)
    
    t.mainloop()