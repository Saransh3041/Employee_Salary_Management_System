# -*- coding: utf-8 -*-
"""
Created on Sat May 31 09:56:32 2025

@author: hp
"""

import tkinter 
from tkinter import * 
import pymysql

from companysave import *
from companyfind import *
from companydelete import *
from companyupdate import *
from companyshow import *
from companynavigate import *

def companydashboard():
    

    
    t=tkinter.Tk()
    t.geometry('500x500')
    
    h1=Label(t,text='Company Dashboard',font=('arial',30))
    h1.place(x=70,y=20)
    
    bt1=Button(t,text='Save',command=showcompanysave)
    bt1.place(x=100,y=100)
    
    bt2=Button(t,text='Find',command=showcompanyfind)
    bt2.place(x=100,y=140)
    
    bt3=Button(t,text='Delete',command=showcompanydelete)
    bt3.place(x=100,y=180)
    
    bt4=Button(t,text='Update',command=showcompanyupdate)
    bt4.place(x=100,y=220)
    
    bt5=Button(t,text='Show',command=showcompanyshow)
    bt5.place(x=100,y=260)
    
    bt6=Button(t,text='Navigate',command=showcompanynavigate)
    bt6.place(x=100,y=300)
    
    t.mainloop()    