def main():
    
    a = 5
    b = 7
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #print the appropriate letter greade based on the test score
    #A: 100-90, B: 89-80, C: 79-70, D: 69-60, F
    print("\nGrade Decision: 1")
    test_score = 79.3

    if test_score <= 100 and test_score >= 90:
        print(f"{test_score} --> A")
    elif test_score <= 90 and test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score <= 80 and test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score <= 70 and test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    #grade decision statement restructured 
    print("\nGrade Decision: 2")
    if test_score <= 100 and test_score >= 90:
        print(f"{test_score} --> A")
    elif test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    #create a decision structure to determine the season based on the month 
    #winter: 12, 1, 2; spring: 3, 4, 5; summer: 6, 7, 8; fall: 9, 10, 11
    #ask the user to enter the number of the month 
    #output the season based on the month 

    def get_user_month():
        user_month = 0
        while(True):
            try:
                user_month = int(input("\n\nWhat is the month? Enter your answer as a number 1-12: "))
                if user_month < 1 or user_month > 12:
                    print("ERROR enter a number between 1 and 12")
                    continue
                else: 
                    break
            except:
                print("ERROR enter a number between 1 and 12")
        return user_month

    user_month = get_user_month()

    if user_month == 12 or user_month == 1 or user_month == 2:
        print(f"\nThe season is winter")
    elif user_month == 3 or user_month == 4 or user_month == 5:
        print(f"\nThe season is spring")
    elif user_month == 6 or user_month == 7 or user_month == 8:
        print(f"\nThe season is summer")
    elif user_month == 9 or user_month == 10 or user_month == 11:
        print(f"\nThe season is fall")



main()