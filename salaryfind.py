# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:53:52 2025

@author: hp
"""
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox

def showsalaryfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="emplsalary",font=('arial',25))
    z.place(x=210,y=40)
    
    def find():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select Empid,Salary,MonthlySalary from EmpSalary where Empid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,str(data[0]))
        e3.insert(0,str(data[1]))
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select Empid from EmpSalary"%xa
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1['values']=lt
    
    def close():
         t.destroy()   
    
        
    
    a1=Label(t,text='Empid')
    a1.place(x=200,y=110)
    e1=ttk.Combobox(t)
    filldata
    e1.place(x=300,y=110)
    
    a2=Label(t,text='salary')
    a2.place(x=200,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    
    a3=Label(t,text='Monthsalary')
    a3.place(x=200,y=190)
    e3=Entry(t,width=30)
    e3.place(x=300,y=190)
    
    bt1=Button(t,text='Find',command=find)
    bt1.place(x=200,y=230)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=230)
    t.mainloop()