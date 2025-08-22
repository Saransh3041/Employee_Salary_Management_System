from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showcompanyfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="CompanyMaster",font=('arial',25))
    z.place(x=210,y=40)

    
   
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select compname,address,city,phone,email from companymaster where compid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        db.commit()
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        lt=[]
        sql="select compid from companymaster "
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt    
    
    
    
    a1=Label(t,text='Comp id')
    a1.place(x=50,y=120)
    e1=ttk.Combobox(t)
    filldata()
    e1.place(x=150,y=120)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=180,y=160)
    
    a2=Label(t,text='Comp Name')
    a2.place(x=50,y=200)
    e2=Entry(t,width=30)
    e2.place(x=150,y=200)
    
    a3=Label(t,text='Address')
    a3.place(x=50,y=240)
    e3=Entry(t,width=30)
    e3.place(x=150,y=240)
    
    a4=Label(t,text='City')
    a4.place(x=50,y=280)
    e4=Entry(t,width=30)
    e4.place(x=150,y=280)
    
    a5=Label(t,text='Phone')
    a5.place(x=50,y=320)
    e5=Entry(t,width=30)
    e5.place(x=150,y=320)
    
    a6=Label(t,text='Email')
    a6.place(x=50,y=360)
    e6=Entry(t,width=30)
    e6.place(x=150,y=360)
    
    t.mainloop()