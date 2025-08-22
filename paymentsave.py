# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:18:01 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
def showpaymentsave():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='purple')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='mediumpurple')
    ca2.place(x=50,y=105)
    z=Label(t,text="Payment",font=('arial',25))
    z.place(x=210,y=40)

    
    def save():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=(e2.get())
        xc=int(e3.get())
        xd=int(e4.get())
        xe=int(e5.get())
        xf=int(e6.get())
        xg=float(e7.get())
        sql="insert into Payment values(%d,'%s',%d,%d,%d,%d,%d)"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        
        
    
        messagebox.showinfo('Message','Data Saved')
        db.commit()
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        e4.delete(0,1000)
        e5.delete(0,1000)
        e6.delete(0,1000)
        db.close()
    
    def Payment():
    
        
        m1=int(e5.get())
        m2=int(e6.get())
        c=m1-(m1*m2)/100
        e7.insert(0,str(c))
        e7.delete(0,1000)
        
    def close():
        t.destroy()
    
    a1=Label(t,text='empid')
    a1.place(x=200,y=110)
    e1=Entry(t,width=30)
    e1.place(x=300,y=110)
    
    a2=Label(t,text='month')
    a2.place(x=200,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    
    a3=Label(t,text='deptid')
    a3.place(x=200,y=190)
    e3=Entry(t,width=30)
    e3.place(x=300,y=190)
    
    a4=Label(t,text='HODleaves')
    a4.place(x=200,y=230)
    e4=Entry(t,width=30)
    e4.place(x=300,y=230)
    
    a5=Label(t,text='Payment')
    a5.place(x=200,y=270)
    e5=Entry(t,width=30)
    e5.place(x=300,y=270)
    
    a6=Label(t,text='tax')
    a6.place(x=200,y=310)
    e6=Entry(t,width=30)
    e6.place(x=300,y=310)
    
    a7=Button(t,text='Netpay',command=Payment)
    a7.place(x=200,y=350)
    e7=Entry(t,width=30)
    e7.place(x=300,y=350)
    bt1=Button(t,text='Save',command=save)
    bt1.place(x=200,y=390)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=390)
    
    
    
    
    
    t.mainloop()