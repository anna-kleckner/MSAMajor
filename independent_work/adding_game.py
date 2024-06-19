import random

#function to get level 
def get_user_level():
    #ask for a level 1-3 
    while True:
        try: 
            difficulty_level = input("\nEnter a difficulty level (1, 2, 3): ")
            if difficulty_level in ["1", "2", "3"]:
                break
            else: 
                print("ERROR: Enter a number between 1-3")
                continue
        except: 
            print("ERROR: Enter a number between 1-3")
            continue
    return difficulty_level


#level 1: single digit (1-10)
#level 2: 2 digit (10-99)
#level 3: 3 digit (100-999)


#function to get the number of questions (1-10)
def get_number_of_questions():
    #ask for a number of questions (3-10)
    while True:
        try: 
            number_of_questions = int(input("\nEnter a number of questions (3-10): "))
            if number_of_questions >= 3 and number_of_questions <= 10:
                break
            else:
                print("ERROR: Enter a number between 3-10")
                continue
        except:
            print("ERROR: Enter a number between 3-10")
            continue
    return number_of_questions



def main():
    difficulty_level = get_user_level()
    number_of_questions = get_number_of_questions()

    #for loop wuth the difficulty 
    for difficulty_level == "1":
        #while loop that runs at most 3 times for each question

    #tell user what percent of questions they got correct 


main()