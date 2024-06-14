def main(): 
   
    while True:
        month_number = input("\nEnter month number 1-12: ")
        if month_number in ["12", "1", "2"]:
            print("\nThe season is winter")
        elif month_number in ["3", "4", "5"]:
            print("\nThe season is spring")
        elif month_number in ["6", "7", "8"]:
            print("\nThe season is summer")
        elif month_number in ["9", "10", "11"]:
            print("\nThe season is fall")
        else:
            print("ERROR enter a number between 1 and 12")
            continue
        break

main()