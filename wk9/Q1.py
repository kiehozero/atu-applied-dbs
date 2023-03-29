# following Gerard's demo

def main():
    nameStr = "Enter name: "
    ageStr = "Enter age: "
    while True:
        display_menu()
        choice = int(input("Choice:"))

        if choice == 1:
            name = get_name(nameStr)
            print(name.upper())

        elif choice == 2:
            age = get_age(ageStr)
            print(age + 1)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

def display_menu():
    print("MENU")
    print("====")
    print("1 - Get Name")
    print("2 - Get Age")
    print("3 - Exit")

def get_name(n):
    name = input(n)
    return name

def get_age(a):
    return input(a)

if __name__ == "__main__":
    main()