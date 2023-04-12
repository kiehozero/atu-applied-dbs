import pymysql.cursors

conn = pymysql.connect(host='localhost', user='root', password='root', database='school', cursorclass=pymysql.cursors.DictCursor)

# %s can be used to insert values

query = 'SELECT * FROM subject WHERE teacher LIKE %s'

ins = 'INSERT INTO subject(Name, Teacher, OnLeavingCert) VALUES (%s, %s, %s)'

with conn:
    cursor = conn.cursor()
    cursor.execute(query, ('Ms.%'))
    subjects = cursor.fetchall()
    for s in subjects:
        print(s['Name'])
