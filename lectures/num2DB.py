import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(
        host='localhost', 
        user='root', 
        password='root', 
        db='school', 
        cursorclass=pymysql.cursors.DictCursor)


def add_subject(n, t, lc):
    if (not conn):
        connect()
        
    sql = "INSERT INTO subject (Name, Teacher, OnLeavingCert) VALUES (%s, %s, %s)"
    
    with conn:
        cursor = conn.cursor()
        x = cursor.execute(sql, (n, t, lc))
        print(x)