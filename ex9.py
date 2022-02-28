def main():
    
    path1 = input("Enter the first file's path: ")
    path2 = input("Enter the second file's path: ")
    path3 = input("Enter the third file's path: ")

    file1 = open(path1, "r")
    file2 = open(path2, "r")
    try:
        file3 = open(path3, "a")
    except:
        print("file not found")

    file3.write(file1.readline() + file2.readline())

    file1.close()
    file2.close()
    file3.close()
    
if __name__ == "__main__":
    main()
