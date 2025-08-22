# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 12:58:05 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*


def showholidaysave():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='red')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='pink')
    ca2.place(x=50,y=105)
    z=Label(t,text="Holidaymaster",font=('arial',25))
    z.place(x=210,y=40)
    
    def save():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=(e2.get())
        xc=int(e3.get())
        sql="insert into Holidaymaster values(%d,'%s',%d)"%(xa,xb,xc)
        
        cur.execute(sql)
        e1.delete(0,1000)
        e2.delete(0,1000)
        e3.delete(0,1000)
        messagebox.showinfo('Message','Data Saved')
        db.commit()
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
    
    bt1=Button(t,text='Save',command=save)
    bt1.place(x=200,y=230)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=230)
        
        
    t.mainloop()    
        

    
#showholidaysave()
    
    