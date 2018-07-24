# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:22:40 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:55:03 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-


from tkinter import *
import Employedb
    

def view_command():
    list1.delete(0,END)
    for row in Employedb.view():
        list1.insert(END,row)
def search_command():
    list1.Employedb(0,END)
    for row in data.search(firstname_text.get(),lastname_text.get(),mobile_text.get(),birth_text.get(),experience_text.get(),salary_text.get(),hire_text.get(),email_text.get(),address_text.get()):
        list1.insert(END,row)
def add_command():
    Employedb.insert(firstname_text.get(),lastname_text.get(),mobile_text.get(),birth_text.get(),experience_text.get(),salary_text.get(),hire_text.get(),email_text.get(),address_text.get())
    list1.delete(0,END)   
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[8])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[9])
def delete_command():
    EmployeDB.delete(selected_tuple[0])
def update_command():
    Employedb.update(selected_tuple[0],firstname_text.get(),lastname_text.get(),mobile_text.get(),birth_text.get(),experience_text.get(),salary_text.get(),hire_text.get(),email_text.get(),address_text.get())
 
window=Tk()
window.geometry("1000x500+0+0")
window.title("Employe Management System")
'''====================================FRAMES===================================================='''
frame1=Frame(window,height=200,width=500,bg="deep sky blue")
frame1.pack(side=TOP)

frame2=Frame(window,height=400,width=1000)
frame2.pack(side=TOP,padx=10,pady=10)

frame3=Frame(window,height=400,width=250,bg="deep sky blue")
frame3.pack(side=LEFT)

frame4=Frame(window,height=400,width=250,bg="deep sky blue")
frame4.pack(side=RIGHT)
'''====================================TITLE===================================================='''
title=Label(frame1,text="Employe Management System",font=("arial",50,"bold"),fg="red2",bd=12,anchor='w')
title.grid(row=0,column=0,padx=5,pady=5)
'''===================================Labels===================================================='''
l1=Label(frame2,text="First Name",anchor='w',bd=8,font=("arial",18,"bold"))
l1.grid(row=0,column=0)
    
l2=Label(frame2,text="Last Name",anchor='w',bd=8,font=("arial",18,"bold"))
l2.grid(row=0,column=2)
    
l3=Label(frame2,text="Mobile",anchor='w',bd=8,font=("arial",18,"bold"))
l3.grid(row=0,column=4)
    
l4=Label(frame2,text="Email",anchor='w',bd=8,font=("arial",18,"bold"))
l4.grid(row=2,column=2)
    
l5=Label(frame2,text="Experience",anchor='w',bd=8,font=("arial",18,"bold"))
l5.grid(row=1,column=2)
    
l6=Label(frame2,text="Salary",anchor='w',bd=8,font=("arial",18,"bold"))
l6.grid(row=1,column=4)
    
l7=Label(frame2,text="Address",anchor='w',bd=8,font=("arial",18,"bold"))
l7.grid(row=2,column=4)

l8=Label(frame2,text="Birth Date",anchor='w',bd=8,font=("arial",18,"bold"))
l8.grid(row=1,column=0)

l9=Label(frame2,text="Hire Date",anchor='w',bd=8,font=("arial",18,"bold"))
l9.grid(row=2,column=0)
'''====================================Entry============================================='''    
firstname_text=StringVar()
e1=Entry(frame2,textvariable=firstname_text,bd=5,bg="azure",font=('arial',13,'bold'))
e1.grid(row=0,column=1)
    
lastname_text=StringVar()
e2=Entry(frame2,textvariable=lastname_text,bd=5,bg="azure",font=('arial',13,'bold'))
e2.grid(row=0,column=3)
    
mobile_text=StringVar()
e3=Entry(frame2,textvariable=mobile_text,bd=5,bg="azure",font=('arial',13,'bold'))
e3.grid(row=0,column=5)
    
email_text=StringVar()
e4=Entry(frame2,textvariable=email_text,bd=5,bg="azure",font=('arial',13,'bold'))
e4.grid(row=2,column=3)
    
experience_text=StringVar()
e5=Entry(frame2,textvariable=experience_text,bd=5,bg="azure",font=('arial',13,'bold'))
e5.grid(row=1,column=3)
    
salary_text=StringVar()
e6=Entry(frame2,textvariable=salary_text,bd=5,bg="azure",font=('arial',13,'bold'))
e6.grid(row=1,column=5)
    
address_text=StringVar()
e7=Entry(frame2,textvariable=address_text,bd=5,bg="azure",font=('arial',13,'bold'))
e7.grid(row=2,column=5)

birth_text=StringVar()
e8=Entry(frame2,textvariable=birth_text,bd=5,bg="azure",font=('arial',13,'bold'))
e8.grid(row=1,column=1)

hire_text=StringVar()
e9=Entry(frame2,textvariable=hire_text,bd=5,bg="azure",font=('arial',13,'bold'))
e9.grid(row=2,column=1)
'''===========================================Button================================================='''    
b1=Button(frame3,text="View All",width=25,command=view_command,bd=7,bg="powder blue",font=('arial',10,'bold'))
b1.grid(row=3,column=0)
    
b2=Button(frame3,text="Search Entry",width=25,command=search_command,bd=7,bg="powder blue",font=('arial',10,'bold'))
b2.grid(row=4,column=0)
    
b3=Button(frame3,text="Add Entry",width=25,command=add_command,bd=7,bg="powder blue",font=('arial',10,'bold'))
b3.grid(row=5,column=0)
    
b4=Button(frame3,text="Update Selected",width=25,command=update_command,bd=7,bg="powder blue",font=('arial',10,'bold'))
b4.grid(row=6,column=0)
    
b5=Button(frame3,text="Delete Selected",width=25,command=delete_command,bd=7,bg="powder blue",font=('arial',10,'bold'))
b5.grid(row=7,column=0)
    
b6=Button(frame3,text="Close",width=25,command=window.destroy,bd=7,bg="powder blue",font=('arial',10,'bold'))
b6.grid(row=8,column=0)
    
list1=Listbox(frame4,heigh=80,width=200)
list1.grid(row=0,column=0,padx=2,pady=2)
    
list1.bind('<<ListboxSelect>>',get_selected_row)
    
sb1=Scrollbar(frame3,orient=VERTICAL,width=20)
sb1.grid(row=3,column=1,rowspan=35,ipady=85,padx=3)
    
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
window.mainloop()



