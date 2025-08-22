
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showemployeedelete():
    t=tkinter.Tk()
    t.geometry('500x500')
    Ca1=Canvas(t,height=100,width=500,bg='Blue')
    Ca1.place(x=0,y=0)
    ca2=Canvas(t,height=400,width=500,bg='lightblue')
    ca2.place(x=0,y=100)
    z=Label(t,text="Employee",font=('arial',25))
    z.place(x=210,y=40)

   

   
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from employee where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is deleted'%(xa))
        e1.delete(0,100)
        db.close()
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select empid from employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.commit()
        db.commit()
        e1['values']=lt
            
    
   
    
    a1=Label(t,text='Emp ID')
    a1.place(x=50,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=150,y=100)
    
    bt=Button(t,text='Delete',command=deletedata)
    bt.place(x=180,y=150)
    
    t.mainloop()