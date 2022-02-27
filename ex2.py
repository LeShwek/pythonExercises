def main():

    days = input("please enter a number of days: ")
    while days.isnumeric() == False:
        days = input("please enter a number of days: ")

    days = int(days)

    years = days // 365
    days = days % 365

    weeks = days // 7
    days = days % 7

    print("Years: " + str(years) + " Weeks: " + str(weeks) + " Days: " + str(days))

if __name__ == "__main__":
    main()
