# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 02:15:45 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:12:33 2018

@author: Deepak
"""

import sqlite3

def connect():
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employe(id INTEGER PRIMARY KEY,firstname text,lastname text,mobile INTEGER,email text,experience text,salary INTEGER,address text)")
    conn.commit()
    conn.close()

def insert(firstname,lastname,mobile,email,experience,salary,address):
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO employe VALUES(NULL,?,?,?,?,?,?,?)",(firstname,lastname,mobile,email,experience,salary,address))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employe")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(firstname="",lastname="",mobile="",email="",experience="",salary="",address=""):
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employe WHERE firstname=? OR lastname=? OR mobile=? OR email=? OR experience=? OR salary=? OR address=?",(firstname,lastname,mobile,email,experience,salary,address))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("DELETE  FROM employe WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,firstname,lastname,mobile,email,experience,salary,address):
    conn=sqlite3.connect("work.db")
    cur=conn.cursor()
    cur.execute("UPDATE employe SET firstname=?,lastname=?,mobile=?,email=?,experience=?,salary=?,address=? WHERE id=?",(firstname,lastname,mobile,email,experience,salary,address,id))
    conn.commit()
    conn.close()



