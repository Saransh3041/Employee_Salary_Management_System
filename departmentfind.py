# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:33:20 2025

@author: hp
"""

from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
t=tkinter.Tk()

def showdepartmentfind():
    

    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="Department",font=('arial',25))
    z.place(x=210,y=40)




    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select dname,description where deptid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        
        db.commit()
        db.close()
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select deptid from Department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt    
    
       
    
    a1=Label(t,text='deptid')
    a1.place(x=50,y=120)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=150,y=120)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=180,y=240)
    
    
    
    
    a2=Label(t,text='dname')
    a2.place(x=50,y=160)
    e2=Entry(t,width=30)
    e2.place(x=150,y=160)
    
    a3=Label(t,text='description')
    a3.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=150,y=200)
    
    
    
    
        
    t.mainloop()