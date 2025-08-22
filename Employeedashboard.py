
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:17:22 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from employeesave import *
from employeefind import *
from employeedelete import *
from employeeupdate import *
from employeeshow import*
from employeenavigate import *

def employeedashboard():
    t=tkinter.Tk()
    t.geometry('500x500')
    
    a=Label(t,text='EmployeeDashboard',fg='red',font=('arial',30))
    a.place(x=300,y=20)
    bt1=Button(t,text='Save',command=showemployeesave)
    bt1.place(x=100,y=100)
    bt2=Button(t,text='Find',command=showemployeefind)
    bt2.place(x=100,y=140)
    bt3=Button(t,text='Deleted',command=showemployeedelete)
    bt3.place(x=100,y=180)
    bt4=Button(t,text='Update',command=showemployeeupdate)
    bt4.place(x=100,y=220)
    bt5=Button(t,text='Show',command=showemployeeshow)
    bt5.place(x=100,y=250)
    bt6=Button(t,text='Navigate',command=showemployeenavigate)
    bt6.place(x=100,y=300)
    t.mainloop()
