# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:52:50 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from holidaysave import *
from holidayfind import *
from holidaydelete import *
from holidayupdate import *
from holidayshow import *
from holidaynavigate import *

def holidaydashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    a=Label(t,text='Holiday Dashboard',fg='red',font=('arial',30))
    a.place(x=300,y=20)
    bt1=Button(t,text='Save',command=showholidaysave)
    bt1.place(x=100,y=100)
    bt2=Button(t,text='Find',command=showholidayfind)
    bt2.place(x=100,y=140)
    bt3=Button(t,text='Deleted',command=showholidaydelete)
    bt3.place(x=100,y=180)
    bt4=Button(t,text='Update',command=showholidayupdate)
    bt4.place(x=100,y=220)
    bt5=Button(t,text='Show',command=showholidayshow)
    bt5.place(x=100,y=250)
    bt6=Button(t,text='Navigate',command=showholidaynavigate)
    bt6.place(x=100,y=300)
    t.mainloop()