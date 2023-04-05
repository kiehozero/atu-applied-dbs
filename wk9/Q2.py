
# Main function
def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			array = fill_array(array)
			display_menu()
		elif (choice == "2"):
			print(array)
			display_menu()
		elif (choice == "3"):
			find_gt_in_array(array)
			display_menu()
		elif (choice == "4"):
			break
		else:
			display_menu()
			

# choice 1		
def fill_array(array):
	# Write the necessary code to fill the array
	# -1 should not be part of the array
	array = []
	while True:
		digit = int(input("Enter a value to send to the array: "))
		if (digit == -1):
			break
		else:
			array.append(digit)
	return array


# choice 3
def find_gt_in_array(array):
	# Write the necessary code to get a number from the user
	# and print out all numbers in the array that are greater
	j = int(input("Enter a value to return the array values that are greater than it: "))
	greats = []
	for i in array:
		if (i > j):
			greats.append(i)
	print(greats)


# choice 3
def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")


if __name__ == "__main__":
	# execute only if run as a script 
	main()
