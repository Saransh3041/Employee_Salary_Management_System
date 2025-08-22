# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:26:40 2025

@author: hp
"""
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showpaymentnavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='purple')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='mediumpurple')
    ca2.place(x=50,y=105)
    z=Label(t,text="Payment",font=('arial',25))
    z.place(x=210,y=40)
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    def first():
        global i
        i=0
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        e4.delete(0,1000)
        e5.delete(0,1000)
        e6.delete(0,1000)
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
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        e4.delete(0,1000)
        e5.delete(0,1000)
        e6.delete(0,1000)
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
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select empid,month,deptid,noofleaves,payment,tax,netpay from Payment"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(str(res[1]))
            xc.append(str(res[2]))
            xd.append(str(res[3]))
            xe.append(str(res[4]))
            xf.append(str(res[5]))
            xg.append(str(res[6]))
            
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
    
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=250,y=440)
    bt1=Button(t,text='First',command=first)
    bt1.place(x=200,y=400)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=250,y=400)
    
    bt3=Button(t,text='Last',command=lt)
    bt3.place(x=300,y=400)
    
    bt4=Button(t,text='Previous',command=pt)
    bt4.place(x=350,y=400)
    
    filldata()
    t.mainloop()