from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox
def showcompanydelete():
    
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="CompanyMaster",font=('arial',25))
    z.place(x=210,y=40) 
    
    def deletedata():
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from companymaster where compid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is deleted'%(xa))
        e1.delete(0,100)
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
    
    bt=Button(t,text='Delete',command=deletedata)
    bt.place(x=180,y=160)
    
    
    t.mainloop()
      
        
    