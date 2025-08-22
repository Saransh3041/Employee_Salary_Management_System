# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:33:21 2025

@author: hp
"""

from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showdepartmentnavigate():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="Department",font=('arial',25))
    z.place(x=210,y=40)



    
    
    xa=[]
    xb=[]
    xc=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
       
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
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
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select deptid,dname,description from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])  
            xf.append(res[5])
        db.commit()
        db.close()
        
    
    
    
    a1=Label(t,text=' deptid')
    a1.place(x=50,y=120)
    e1=Entry(t,width=30)
    e1.place(x=150,y=120)
    
    a2=Label(t,text='dname')
    a2.place(x=50,y=160)
    e2=Entry(t,width=30)
    e2.place(x=150,y=160)
    
    a3=Label(t,text='description')
    a3.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=150,y=200)
    
   
    
    bt1=Button(t,text='First',command=first)
    bt1.place(x=60,y=360)
    
    bt2=Button(t,text='Next',command=nt)
    bt2.place(x=160,y=360)
    
    bt3=Button(t,text='Previous',command=pt)
    bt3.place(x=260,y=360)
    
    bt4=Button(t,text='Last',command=lt)
    bt4.place(x=360,y=360)
    
    filldata()
    
    t.mainloop()