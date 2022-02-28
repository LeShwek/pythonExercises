def main():

    result = ""
    num = input("Please enter a 4 digit number: ")
    while num.isnumeric() == False or len(num) != 4:
        num = input("Please enter a 4 digit number: ")

    for dig in num:
        if dig == "9":
            result += "0"
        else:
            result += str(int(dig) + 1)

    print(result)
        

    
if __name__ == "__main__":
    main()
