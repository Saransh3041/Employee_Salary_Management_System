# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 16:13:50 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
t=tkinter.Tk()
def showholidayshow():
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='red')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='pink')
    ca2.place(x=50,y=105)
    z=Label(t,text="Holidaymaster",font=('arial',25))
    z.place(x=210,y=40)
    
    
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select * from holidaymaster"
        cur.execute(sql)
        data=cur.fetchall()
        msg=""
        for res in data:
            msg=msg+str(res[0])+"\t"
            msg=msg+str(res[1])+"\t"
            msg=msg+str(res[2])+"\t"
            msg=msg+"\n"
            db.close()
            w.insert(END,msg)
    
            
            
        
    w=Text(t,width=30,height=106)
    w.place(x=50,y=100)
    filldata()
    t.mainloop()
        
