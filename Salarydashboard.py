# -*- coding: utf-8 -*-
"""
Created on Tue May 27 22:14:32 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from salarysave import *
from salaryfind import *
from salarydelete import *
from salaryupdate import *
from salaryshow import *
from salarynavigate import *

def salarydashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    a=Label(t,text='EmpSalary Dashboard',fg='red',font=('arial',30))
    a.place(x=300,y=20)
    bt1=Button(t,text='Save',command=showsalarysave)
    bt1.place(x=100,y=100)
    bt2=Button(t,text='Find',command=showsalaryfind)
    bt2.place(x=100,y=140)
    bt3=Button(t,text='Deleted',command=showsalarydelete)
    bt3.place(x=100,y=180)
    bt4=Button(t,text='Update',command=showsalaryupdate)
    bt4.place(x=100,y=220)
    bt5=Button(t,text='Show',command=showsalaryshow)
    bt5.place(x=100,y=250)
    bt6=Button(t,text='Navigate',command=showsalarynavigate)
    bt6.place(x=100,y=300)
    t.mainloop()