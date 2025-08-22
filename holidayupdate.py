# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:13:49 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

def showholidayupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='red')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='pink')
    ca2.place(x=50,y=105)
    z=Label(t,text="Holidaymaster",font=('arial',25))
    z.place(x=210,y=40)
    
    def update():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=(e2.get())
        xc=int(e3.get())
        sql="update holidaymaster set Holidayname='%s',Noofleaves=%d where Empid=%d"%(xb,xc,xa)
        
        cur.execute(sql)
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        messagebox.showinfo('Message','Data Update')
        db.commit()
        db.close()
        
    def find():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select Holidayname,Noofleaves from holidaymaster where Empid=%d"%(xa)
        
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,(data[0]))
        e3.insert(0,str(data[1]))
        
        
        db.close()
    def close():
        t.destroy()
    
    
    a1=Label(t,text='Empid')
    a1.place(x=200,y=110)
    e1=Entry(t,width=30)
    e1.place(x=300,y=110)
    
    a2=Label(t,text='Holidayname')
    a2.place(x=200,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    
    a3=Label(t,text='no of leaves')
    a3.place(x=200,y=190)
    e3=Entry(t,width=30)
    e3.place(x=300,y=190)
    
    bt1=Button(t,text='Update',command=update)
    bt1.place(x=200,y=230)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=230)
    bt3=Button(t,text="Find",command=find)
    bt3.place(x=250,y=270)
    
    
    t.mainloop()