# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:26:39 2025

@author: hp
"""
import pymysql
import tkinter
from tkinter import*
def showpaymentfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='purple')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='mediumpurple')
    ca2.place(x=50,y=105)
    z=Label(t,text="Payment",font=('arial',25))
    z.place(x=210,y=40)
    
    
    
    def find():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xd=int(e1.get())
        sql="select month,deptid,Noofleaves,payment,tax,netpay from Payment where Empid=%d "%xd
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,str(data[1]))
        e4.insert(0,str(data[2]))
        e5.insert(0,str(data[3]))
        e6.insert(0,str(data[4]))
        e7.insert(0,str(data[5]))
        db.close()
    def close():
        t.destroy()
    
    a1=Label(t,text='Empid')
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
    
    a5=Label(t,text='Payment',)
    a5.place(x=200,y=270)
    e5=Entry(t,width=30)
    e5.place(x=300,y=270)
    
    a6=Label(t,text='tax')
    a6.place(x=200,y=310)
    e6=Entry(t,width=30)
    e6.place(x=300,y=310)
    
    a7=Button(t,text='Netpay')
    a7.place(x=200,y=350)
    e7=Entry(t,width=30)
    e7.place(x=300,y=350)
    bt1=Button(t,text='Find',command=find)
    bt1.place(x=200,y=390)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=390)
    
    
    t.mainloop()
    
    
    
    
        
    
    
    
    
