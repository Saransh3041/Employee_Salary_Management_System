
from tkinter import ttk
import tkinter
import pymysql
from tkinter import*
from tkinter import messagebox

def showemployeeshow():
    
    t=tkinter.Tk()
    t.geometry('500x500')
    Ca1=Canvas(t,height=100,width=500,bg='Blue')
    Ca1.place(x=0,y=0)
    ca2=Canvas(t,height=400,width=500,bg='lightblue')
    ca2.place(x=0,y=100)
    z=Label(t,text="Employee",font=('arial',25))
    z.place(x=210,y=40)



   
    
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select * from employee"
        cur.execute(sql)
        data=cur.fetchall()
        msg=''
        for res in data :
            msg=msg+str(res[0])+"\t"
            msg=msg+str(res[1])+"\t"
            msg=msg+str(res[2])+"\t"
            msg=msg+str(res[3])+"\t"
            msg=msg+str(res[4])+"\t"
            msg=msg+str(res[5])+"\t"
            msg=msg+str(res[6])+"\t"
            msg=msg+"\n"
        db.close()
        w.insert(END,msg)
    
    
   
    
    w=Text(t,width=70,height=30)
    w.place(x=50,y=120)
    
    filldata()
    
    t.mainloop()