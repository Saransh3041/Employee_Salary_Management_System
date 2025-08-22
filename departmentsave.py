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
def showdepartmentsave():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="Department",font=('arial',25))
    z.place(x=210,y=40)




   
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        
        sql="insert into Department values(%d,'%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Your %s company is recorded.'%(xb))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        db.close()
    
    
    
    a1=Label(t,text='deptid')
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
    
    
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=180,y=360)
    
    t.mainloop()