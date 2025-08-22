
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showcompanysave():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="Companymaster",font=('arial',25))
    z.place(x=210,y=40)


    
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        sql="insert into companymaster values(%d,'%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Your %s company is recorded.'%(xb))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        db.close()
    
    
    a1=Label(t,text='Comp id')
    a1.place(x=50,y=120)
    e1=Entry(t,width=30)
    e1.place(x=150,y=120)
    
    a2=Label(t,text='Comp Name')
    a2.place(x=50,y=160)
    e2=Entry(t,width=30)
    e2.place(x=150,y=160)
    
    a3=Label(t,text='Address')
    a3.place(x=50,y=200)
    e3=Entry(t,width=30)
    e3.place(x=150,y=200)
    
    a4=Label(t,text='City')
    a4.place(x=50,y=240)
    e4=Entry(t,width=30)
    e4.place(x=150,y=240)
    
    a5=Label(t,text='Phone')
    a5.place(x=50,y=280)
    e5=Entry(t,width=30)
    e5.place(x=150,y=280)
    
    a6=Label(t,text='Email')
    a6.place(x=50,y=320)
    e6=Entry(t,width=30)
    e6.place(x=150,y=320)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=180,y=360)
    
    t.mainloop()
    