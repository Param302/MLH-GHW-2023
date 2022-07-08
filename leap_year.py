def is_leap(year:int) -> bool:

    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print("Python program to check an year is leap year or not.\n")
    year = int(input("Enter a year: "))

    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
