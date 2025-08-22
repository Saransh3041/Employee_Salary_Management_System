from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox



def showhodfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="HODtable",font=('arial',25))
    z.place(x=210,y=40)

   
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select hodname,deptid,remarks from hodtable where hodid =%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        db.close()
        
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select hodid from hodtable"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1['values']=lt
    
    
    
    a1=Label(t,text='Hod id')
    a1.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=150,y=100)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=160,y=140)
    
    a2=Label(t,text='Hod Name')
    a2.place(x=50,y=180)
    e2=Entry(t,width=30)
    e2.place(x=150,y=180)
    
    a3=Label(t,text='Dept id')
    a3.place(x=50,y=220)
    e3=Entry(t,width=30)
    e3.place(x=150,y=220)
    
    a4=Label(t,text='Remarks')
    a4.place(x=50,y=260)
    e4=Entry(t,width=30)
    e4.place(x=150,y=260)
    
    t.mainloop()