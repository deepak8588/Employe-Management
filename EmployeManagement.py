# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 02:07:23 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 00:19:15 2018

@author: Deepak
"""

from tkinter import *
import work1
    

def view_command():
    list1.delete(0,END)
    for row in employe.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in employe.search(firstname_text.get(),lastname_text.get(),mobile_text.get(),email_text.get(),experience_text.get(),salary_text.get(),address_text.get()):
        list1.insert(END,row)
def add_command():
    employe.insert(firstname_text.get(),lastname_text.get(),mobile_text.get(),email_text.get(),experience_text.get(),salary_text.get(),address_text.get())
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
def delete_command():
    employe.delete(selected_tuple[0])
def update_command():
    employe.update(selected_tuple[0],firstname_text.get(),lastname_text.get(),mobile_text.get(),email_text.get(),experience_text.get(),salary_text.get(),address_text.get())
 
window=Tk()
l1=Label(window,text="First Name")
l1.grid(row=0,column=0)
    
l2=Label(window,text="Last Name")
l2.grid(row=0,column=2)
    
l3=Label(window,text="Mobile")
l3.grid(row=0,column=4)
    
l4=Label(window,text="Email")
l4.grid(row=1,column=0)
    
l5=Label(window,text="Experience")
l5.grid(row=1,column=2)
    
l6=Label(window,text="Salary")
l6.grid(row=1,column=4)
    
l7=Label(window,text="Address")
l7.grid(row=2,column=0)
    
firstname_text=StringVar()
e1=Entry(window,textvariable=firstname_text)
e1.grid(row=0,column=1)
    
lastname_text=StringVar()
e2=Entry(window,textvariable=lastname_text)
e2.grid(row=0,column=3)
    
mobile_text=StringVar()
e3=Entry(window,textvariable=mobile_text)
e3.grid(row=0,column=5)
    
email_text=StringVar()
e4=Entry(window,textvariable=email_text)
e4.grid(row=1,column=1)
    
experience_text=StringVar()
e5=Entry(window,textvariable=experience_text)
e5.grid(row=1,column=3)
    
salary_text=StringVar()
e6=Entry(window,textvariable=salary_text)
e6.grid(row=1,column=5)
    
address_text=StringVar()
e7=Entry(window,textvariable=address_text)
e7.grid(row=2,column=1)
    
b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=3,column=0)
    
b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=4,column=0)
    
b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=5,column=0)
    
b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=6,column=0)
    
b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=7,column=0)
    
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=0)
    
list1=Listbox(window,heigh=9,width=50)
list1.grid(row=3,column=2,rowspan=8,columnspan=3)
    
list1.bind('<<ListboxSelect>>',get_selected_row)
    
sb1=Scrollbar(window)
sb1.grid(row=3,column=1,rowspan=4)
    
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
window.mainloop()



