def main():

    num_list = []

    num1 = input("Please enter your first number: ")
    while num1.isnumeric() == False:
        num1 = input("Please enter your first number: ")

    num2 = input("Please enter your second number: ")
    while num2.isnumeric() == False:
        num2 = input("Please enter your second number: ")

    num3 = input("Please enter your third number: ")
    while num3.isnumeric() == False:
        num3 = input("Please enter your third number: ")

    num_list.extend([num1, num2, num3])
    num_list.sort()

    for item in num_list:
        print(item)


    
if __name__ == "__main__":
    main()
