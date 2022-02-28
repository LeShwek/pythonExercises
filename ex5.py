def main():
    
    num = input("Please enter a number: ")
    while num.isnumeric() == False:
        num = input("Please enter a number: ")

    num = int(num)

    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

    
if __name__ == "__main__":
    main()
