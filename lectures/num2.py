import num2DB

def main():
    subject = input("Enter subject name: ")
    teacher = input("Enter teacher name: ")
    leaving = input("On leaving cert? 1/0: ")
    
    try:
        num2DB.add_subject(subject, teacher, leaving)
    except pymysql.err.ProgrammingError as e:
        print("Programming Error: ", e)
    except pymysql.err.IntegrityError as e:
        print("Error,", subject, "already exists")
    except Exception as e:
        print("Error: ", e)
        
        
if __name__ == '__main__':
    main()