# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:26:29 2025

@author: hp
"""

import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*

from paymentsave import *
from paymentfind import *
from paymentdelete import *
from paymentupdate import *
from paymentshow import *
from paymentnavigate import *

def paymentdashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    a=Label(t,text='Payment Dashboard',fg='red',font=('arial',30))
    a.place(x=300,y=20)
    bt1=Button(t,text='Save',command=showpaymentsave)
    bt1.place(x=100,y=100)
    bt2=Button(t,text='Find',command=showpaymentfind)
    bt2.place(x=100,y=140)
    bt3=Button(t,text='Deleted',command=showpaymentdelete)
    bt3.place(x=100,y=180)
    bt4=Button(t,text='Update',command=showpaymentupdate)
    bt4.place(x=100,y=220)
    bt5=Button(t,text='Show',command=showpaymentshow)
    bt5.place(x=100,y=250)
    bt6=Button(t,text='Navigate',command=showpaymentnavigate)
    bt6.place(x=100,y=300)
    t.mainloop()