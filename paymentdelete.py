# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:26:37 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
def showpaymentdelete():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='purple')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='mediumpurple')
    ca2.place(x=50,y=105)
    z=Label(t,text="Payment",font=('arial',25))
    z.place(x=210,y=40)

    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from Payment where Empid=%d"%xa
        cur.execute(sql)
        
        db.commit()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,100)
        db.close()
               
    def close():
        t.destroy()
               
    
               
    a1=Label(t,text='Empid')
    a1.place(x=200,y=110)
    e1=Entry(t,width=30)
    e1.place(x=300,y=110)
    bt1=Button(t,text='Delete',command=deletedata)
    bt1.place(x=200,y=170)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=170)
    t.mainloop()
