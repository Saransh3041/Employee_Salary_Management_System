# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:13:50 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import*
def showholidaydelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='red')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='pink')
    ca2.place(x=50,y=105)
    z=Label(t,text="Holidaymaster",font=('arial',25))
    z.place(x=210,y=40)
    
    def delete():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from holidaymaster where Empid=%d"%xa
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Data Deleted')
        db.close()
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select Empid from holidaymaster"%xa
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
    bt1=Button(t,text='Delete',command=delete)
    bt1.place(x=200,y=160)
    bt2=Button(t,text='Close',command=close)
    bt2.place(x=300,y=160)
    t.mainloop()