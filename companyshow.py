from tkinter import ttk
import tkinter
import pymysql
from tkinter import*

from tkinter import messagebox
def showcompanyshow():
    t=tkinter.Tk()
    t.geometry('800x800')
    Ca1=Canvas(t,height=100,width=700,bg='Blue')
    Ca1.place(x=50,y=5)
    ca2=Canvas(t,height=600,width=700,bg='lightblue')
    ca2.place(x=50,y=105)
    z=Label(t,text="CompanyMaster",font=('arial',25))
    z.place(x=210,y=40)



    
    
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esmdb')
        cur=db.cursor()
        sql="select * from companymaster"
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
            msg=msg+"\n"
        db.close()
        w.insert(END,msg)
            
    
    w=Text(t,width=70,height=30)
    w.place(x=50,y=20)
    filldata()
    
    t.mainloop()