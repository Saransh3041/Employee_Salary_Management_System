
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox

def showhodsave():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="HODtable",font=('arial',25))
    z.place(x=210,y=40)


   
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=int(e3.get())
        xd=e4.get()
        sql="insert into hodtable values(%d,'%s',%d,'%s')"%(xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is recorded'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        db.close()
    
    
    
    a1=Label(t,text='Hod id')
    a1.place(x=50,y=100)
    e1=Entry(t,width=30)
    e1.place(x=150,y=100)
    
    a2=Label(t,text='Hod Name')
    a2.place(x=50,y=140)
    e2=Entry(t,width=30)
    e2.place(x=150,y=140)
    
    a3=Label(t,text='Dept id')
    a3.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=150,y=180)
    
    a4=Label(t,text='Remarks')
    a4.place(x=50,y=220)
    e4=Entry(t,width=30)
    e4.place(x=150,y=220)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=160,y=270)
    
    
    t.mainloop()