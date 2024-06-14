#create a decision structure to determine the season based on the month 
# #winter: 12, 1, 2; spring: 3, 4, 5; summer: 6, 7, 8; fall: 9, 10, 11
#ask the user to enter the number of the month 
#output the season based on the month 

def get_user_month():
    user_month = 0
    while True:
        try:
            user_month = int(input("\nWhat is the month? Enter your answer as a number 1-12: "))
            if user_month < 1 or user_month > 12:
                print("ERROR enter a number between 1 and 12")
                continue
            else: 
                    break
        except:
            print("ERROR enter a number between 1 and 12")
    return user_month

#create a function to return the season based on the month (input: month number, output: season name)
def get_season(month_number):
    if month_number == 12 or month_number == 1 or month_number == 2:
        return "winter"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "spring"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "summer"
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return "fall"


def main():
    
    while True:
        user_month = get_user_month()
        season_name = get_season(user_month)
        print(f"\nThe season is {season_name}")

        #ask user if they want to continue
        run_again = input("Do you want to run the program again? Type yes or no: ")
        if run_again == "yes" or run_again == "Yes" or run_again == "y":
            continue
        else:
            print("Ending program...")
            break

main()