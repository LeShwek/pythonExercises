def main():

    cel = input("Please enter degrees in Celsius: ")
    while cel.isnumeric() == False:
        cel = input("Please enter degrees in Celsius: ")
        
    cel = int(cel) * 9 / 5 + 32

    print("That equals to " + str(cel) + " degrees Fahrenheit")

    
if __name__ == "__main__":
    main()
