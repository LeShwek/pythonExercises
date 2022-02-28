def main():
    
    str = input("Please enter a string: ")
    vowels = "aeiou"

    for letter in vowels:
        str = str.replace(letter, "")

    print(str)

    
if __name__ == "__main__":
    main()
