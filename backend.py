import sqlite3

def connect():
    conn = sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS notemaking (id INTEGER PRIMARY KEY,notetitle text)") 
    conn.commit()
    conn.close()
    
def insert(notetitle):
    conn=sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("INSERT INTO notemaking VALUES (NULL,?)",(notetitle,))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("SELECT * FROM notemaking")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(notetitle):
    conn=sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("SELECT * FROM notemaking  WHERE notetitle =?",(notetitle,))
    rows=cur.fetchall() 
    conn.close()
    return  rows
    
def delete(id):
    conn=sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("DELETE FROM notemaking  WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,notetitle):
    conn=sqlite3.connect("notemaking.db")#making connection object
    cur=conn.cursor()#making cursor object
    cur.execute("UDATE notemaking SET notettitle=? WHERE id=?",(id,notetitle))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()

