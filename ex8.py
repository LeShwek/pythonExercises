def main():
    
    path1 = input("Enter the first file's path: ")
    path2 = input("Enter the second file's path: ")

    try:
        file1 = open(path1, "a")
        file2 = open(path2, "r")
    except:
        print("file not found")

    file1.write("\n")
    for line in file2:
        file1.write(line)

    file1.close()
    file2.close()
    
if __name__ == "__main__":
    main()
