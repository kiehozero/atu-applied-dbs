import pymysql.cursors

conn = pymysql.connect(host='localhost', user='root', password='root', database='school', cursorclass=pymysql.cursors.DictCursor)

# READ

# %s can be used to insert values
query = 'SELECT * FROM subject WHERE teacher LIKE %s'

with conn:
    cursor = conn.cursor()
    cursor.execute(query, ('Ms.%'))
    subjects = cursor.fetchall()
    for s in subjects:
        print(s['Name'])

# INSERT

ins = 'INSERT INTO subject(Name, Teacher, OnLeavingCert) VALUES (%s, %s, %s)'

with conn:
    try:
        cursor = conn.cursor()
        cursor.execute(ins, ('Geography', 'Ms. Jones', 1))
        # commit adds to the database, can call rollback to undo this
        conn.commit()
        print('Insert successfull')
    # using except to handle various standard errors
    except pymysql.err.InternalError as e:
        print('Internal error', e)
    # name is a primary key in this table so attempting to add a duplicate will return an integrity errror
    except pymysql.err.IntegrityError:
        print('Subject already exists')
    except Exception as e:
        print('error', e)

# UPDATE

query = 'UPDATE subject SET teacher - %s WHERE name = %s'
subject = 'Maths'
newTeacher = 'Mr. Murphy'

with conn:
    try:
        cursor = conn.cursor()
        rowsAffected = cursor.execute(query, (newTeacher, subject))
        conn.commit()
        if (rowsAffected == 0):
            print(subject, 'not updated')
        else:
            print(subject, 'now taught by', newTeacher)
    except Exception as e:
        print('error', e)

# DELETE

query = 'DELETE FROM subject WHERE NAME = %s'
name = 'Maths'

with conn:
    try:
        cursor = conn.cursor()
        rowsAffected = cursor.execute(query, (name))
        conn.commit()
        if (rowsAffected == 0):
            print('nothing deleted - ', name, ' never existed')
        else:
            print(rowsAffected, 'row(s) deleted')
    except Exception as e:
        print('error', e)