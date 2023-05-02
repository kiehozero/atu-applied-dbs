import pymysql

def add_patient(p, f, s, a, d):
    conn = pymysql.connect(
        host='localhost', 
        user='root', 
        password='root', 
        db='hospital', 
        cursorclass=pymysql.cursors.DictCursor)
        
    sql = "INSERT INTO patient_table (ppsn, first_name, surname, address, doctorID) VALUES (%s, %s, %s, %s, %s)"
    
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, (p, f, s, a, d))
        conn.commit()


       
def main():
    ppsn = input("Enter PPSN no.: ")
    fname = input("Enter first name: ")
    sname = input("Enter surname: ")
    add = input("Enter address: ")
    docid = input("Enter doctor ID: ")
    
    try:
        add_patient(ppsn, fname, sname, add, docid)
    except pymysql.err.IntegrityError as e:
        print("Error: Existing PPSN or non-existent Doctor ID entered", e)
    except pymysql.err.InternalError as e:
        print(e)
    except Exception as e:
        print("Error: ", e)
        
        
if __name__ == '__main__':
    main()