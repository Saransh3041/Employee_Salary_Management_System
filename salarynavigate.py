
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:53:54 2025

@author: hp
"""

from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showsalarynavigate():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="emplsalary",font=('arial',25))
    z.place(x=210,y=40)
    xa=[]
    xb=[]
    xc=[]

    def first():
        global i
        i=0
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def nt():
        global i
        i=i+1
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select Empid,Salary,MonthSalary from EmpSalary"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(str(res[1]))
            xc.append(str(res[2]))
    def close():
        t.destroy()
            
    
    z=Label(t,text="emplsalary",font=('arial',25))
    z.place(x=210,y=40)
    a1=Label(t,text='Empid')
    a1.place(x=200,y=110)
    e1=Entry(t,width=30)
    e1.place(x=300,y=110)
    
    a2=Label(t,text='salary')
    a2.place(x=200,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    
    a3=Label(t,text='Monthsalary')
    a3.place(x=200,y=190)
    e3=Entry(t,width=30)
    e3.place(x=300,y=190)
    
    
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=390)
    bt1=Button(t,text='First',command=first)
    bt1.place(x=300,y=230)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=300,y=270)
    
    bt3=Button(t,text='Last',command=lt)
    bt3.place(x=300,y=310)
    
    bt4=Button(t,text='Previous',command=pt)
    bt4.place(x=300,y=350)
    
    filldata()
    t.mainloop()
