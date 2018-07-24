# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:22:56 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:55:05 2018

@author: Deepak
"""

# -*- coding: utf-8 -*-


import sqlite3

def connect():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employe(id INTEGER PRIMARY KEY,firstname text,lastname text,mobile INTEGER,birth text,experience text,salary text,hire text,email text,address text)")
    conn.commit()
    conn.close()

def insert(firstname,lastname,mobile,birth,experience,salary,hire,email,address):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO employe VALUES(NULL,?,?,?,?,?,?,?,?,?)",(firstname,lastname,mobile,birth,experience,salary,hire,email,address))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employe")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(firstname="",lastname="",mobile="",birth="",experience="",salary="",hire="",email="",address=""):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employe WHERE firstname=? OR lastname=? OR mobile=? OR birth=? OR experience=? OR salary=? OR hire=? OR email=? OR address=?",(firstname,lastname,mobile,birth,experience,salary,hire,email,address))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE  FROM employe WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,firstname,lastname,mobile,birth,experience,salary,hire,email,address):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE employe SET firstname=?,lastname=?,mobile=?,birth=?,experience=?,salary=?,hire=?,email=?,address=? WHERE id=?",(firstname,lastname,mobile,birth,experience,salary,hire,email,address,id))
    conn.commit()
    conn.close()

