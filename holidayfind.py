# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:13:48 2025

@author: hp
"""
from tkinter import ttk
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

def showholidayfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='red')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='pink')
    ca2.place(x=50,y=105)
    z=Label(t,text="Holidaymaster",font=('arial',25))
    z.place(x=210,y=40)
    
        
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
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select Empid from holidaymaster"
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
    
    a2=Label(t,text='Holidayname')
    a2.place(x=200,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    
    a3=Label(t,text='no of leaves')
    a3.place(x=200,y=190)
    e3=Entry(t,width=30)
    e3.place(x=300,y=190)
    
    bt1=Button(t,text='Find',command=find)
    bt1.place(x=200,y=230)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=230)
    
    
    t.mainloop()