import pymysql


def get_details_from_name(name):
    
    conn = pymysql.connect(
        host='localhost', 
        user='root', 
        password='root', 
        db='hospital', 
        cursorclass=pymysql.cursors.DictCursor)
    
    query = '''
        SELECT p.ppsn, p.first_name, p.surname, d.name
        FROM patient_table AS p 
        INNER JOIN doctor_table AS d ON p.doctorID = d.doctorID
        WHERE p.surname LIKE %s
        '''

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, ("%"+name+"%"))
        return cursor.fetchall()
  
  
def main():
    sname = input("Enter full or partial surname: ")
    try:
        patients = get_details_from_name(sname)
        for i in patients:
            print(i)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()