def main():
    
    num = input("Please enter a number: ")
    while num.isnumeric() == False:
        num = input("Please enter a number: ")

    print (num [::-1])





if __name__ == "__main__":
    main()
