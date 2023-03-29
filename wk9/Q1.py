# Write a Python program that has 2 arrays in the main function:
#    One containing several elements which are numbers.
#    The other empty.
# Write another function which accepts a number as a parameter and returns the number doubled.
# The main function should call this function for each element of the 1st array and populate the 2nd array with the doubled values when the 2nd array is full it should be printed out

def main():
    oneArr = [1,2,15,7,3,6,23]
    twoArr = timesTwo(oneArr)
    print(oneArr)
    print(twoArr)


def timesTwo(firstArr):
    secondArr = []
    for i in firstArr:
        secondArr.append(i * 2)
    return secondArr

if __name__ == "__main__":
    main()