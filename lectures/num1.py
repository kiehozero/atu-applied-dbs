import num1DB

def get_number():
    return input("Enter Number: ")


def main():
    while True:
        try:
            number = int(get_number())
            # calls the other file we created in the same location, and the functions within it
            teachers = num1DB.get_experience(number)
            # probably a better way to deal with queries that return no matches
            if len(teachers) < 1:
                print("no entries")
            for i in teachers:
                print(i["Name"],", born ", i["dob"], ", has ",i["experience"]," years experience")
            # breaks here as query is returned
            break
        except Exception as e:
            print("invalid number")
            # no break so while loop continues as long as number is invalid

if __name__ == '__main__':
    main()