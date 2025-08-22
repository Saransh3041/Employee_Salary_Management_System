# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:39:54 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from departmentsave import *
from departmentfind import *
from departmentdelete import *
from departmentupdate import *
from departmentshow import *
from departmentnavigate import *

def departmentdashboard():
    

    t=tkinter.Tk()
    t.geometry('500x500')
    
    a=Label(t,text='Department Dashboard',fg='red',font=('arial',30))
    a.place(x=300,y=20)
    bt1=Button(t,text='Save',command=showdepartmentsave)
    bt1.place(x=100,y=100)
    bt2=Button(t,text='Find',command=showdepartmentfind)
    bt2.place(x=100,y=140)
    bt3=Button(t,text='Deleted',command=showdepartmentdelete)
    bt3.place(x=100,y=180)
    bt4=Button(t,text='Update',command=showdepartmentupdate)
    bt4.place(x=100,y=220)
    bt5=Button(t,text='Show',command=showdepartmentshow)
    bt5.place(x=100,y=250)
    bt6=Button(t,text='Navigate',command=showdepartmentnavigate)
    bt6.place(x=100,y=300)
    t.mainloop()