
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showemployeefind():
    t=tkinter.Tk()
    
    t.geometry('500x500')
    Ca1=Canvas(t,height=100,width=500,bg='Blue')
    Ca1.place(x=0,y=0)
    ca2=Canvas(t,height=400,width=500,bg='lightblue')
    ca2.place(x=0,y=100)
    z=Label(t,text="Employee",font=('arial',25))
    z.place(x=210,y=40)


    
    
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select name,city,address,email,phone,deptid from employee where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,str(data[5]))
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
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=180,y=140)
    
    a2=Label(t,text='Name')
    a2.place(x=50,y=180)
    e2=Entry(t,width=30)
    e2.place(x=150,y=180)
    
    a3=Label(t,text='City')
    a3.place(x=50,y=220)
    e3=Entry(t,width=30)
    e3.place(x=150,y=220)
    
    a4=Label(t,text='Address')
    a4.place(x=50,y=260)
    e4=Entry(t,width=30)
    e4.place(x=150,y=260)
    
    a5=Label(t,text='Email')
    a5.place(x=50,y=300)
    e5=Entry(t,width=30)
    e5.place(x=150,y=300)
    
    a6=Label(t,text='Phone')
    a6.place(x=50,y=340)
    e6=Entry(t,width=30)
    e6.place(x=150,y=340)
    
    a7=Label(t,text='Dept ID')
    a7.place(x=50,y=380)
    e7=Entry(t,width=30)
    e7.place(x=150,y=380)
    
    t.mainloop()