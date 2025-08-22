# -*- coding: utf-8 -*-
"""
Created on Sat May 31 11:25:07 2025

@author: hp
"""
import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from Employeedashboard import *
from Companydashboard import *

from Departmentdashboard import *
from HODdashboard import *
from Holidaydashboard import *
from Salarydashboard import *
from Paymentdashboard import *


t=tkinter.Tk()
t.geometry("800x800")

Ca1=Canvas(t,height=100,width=1700,bg='Blue')
Ca1.place(x=0,y=5)
ca2=Canvas(t,height=600,width=1700,bg='lightblue')
ca2.place(x=0,y=105)

a=Label(t,text='ESM Dashboard',fg='red',font=('arial',50))
a.place(x=300,y=20)

a1=Button(t,text='Company Dashboard',font=('arial',20),fg='purple',bg='lightyellow',command=companydashboard)
a1.place(x=100,y=150)

a1=Button(t,text='Department Dashboard',font=('arial',20),fg='darkred',bg='lightyellow',command=departmentdashboard)
a1.place(x=600,y=150)

a1=Button(t,text='HODTable Dashboard',font=('arial',20),fg='Darkgreen',bg='lightyellow',command=HODdashboard)
a1.place(x=100,y=300)

a1=Button(t,text='Employee Dashboard',font=('arial',20),fg='Darkblue',bg='lightyellow',command=employeedashboard)
a1.place(x=600,y=300)

a1=Button(t,text='EmpSalary Dashboard',font=('arial',20),fg='darkorange',bg='lightyellow',command=salarydashboard)
a1.place(x=100,y=450)

a1=Button(t,text='Holidaymaster Dashboard',font=('arial',20),fg='Black',bg='lightyellow',command=holidaydashboard)
a1.place(x=600,y=450)

a1=Button(t,text='Payment Dashboard',font=('arial',20),fg='Green',bg='lightyellow',command=paymentdashboard)
a1.place(x=330,y=600)

t.mainloop()