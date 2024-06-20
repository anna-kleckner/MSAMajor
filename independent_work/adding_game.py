import random

#function to get level 
def get_user_level():
    #ask for a level 1-3 
    while True:
        try: 
            difficulty_level = int(input("\nEnter a difficulty level (1, 2, 3): "))
            if difficulty_level in [1, 2, 3]:
                break
            else: 
                print("ERROR: Enter a number between 1-3")
                continue
        except: 
            print("ERROR: Enter a number between 1-3")
            continue
    return difficulty_level

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
    questions_correct = 0

    #for loop with the number of questions
    for questions in range(number_of_questions): 

        if difficulty_level == 1:
            level_1_value_1 = random.randint(0, 9)
            level_1_value_2 = random.randint(0, 9)
            level_1_sum = level_1_value_1 + level_1_value_2  

            incorrect_tries = 0
            while True:
                try:
                    user_sum_1 = int(input(f"\n{level_1_value_1} + {level_1_value_2} = "))
                    if user_sum_1 == level_1_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum_1 != level_1_sum:
                        print("Incorrect")
                        incorrect_tries = incorrect_tries + 1
                        if incorrect_tries == 3:
                            print(f"Correct answer is: {level_1_sum}")
                            break
                    else:
                        break
                except:
                    print("Incorrect")
                    incorrect_tries = incorrect_tries + 1
                    if incorrect_tries == 3:
                        print(f"Correct answer is: {level_1_sum}")
                        break

        if difficulty_level == 2:
            level_2_value_1 = random.randint(10, 99)
            level_2_value_2 = random.randint(10, 99)
            level_2_sum = level_2_value_1 + level_2_value_2  

            incorrect_tries = 0
            while True:
                try:
                    user_sum_2 = int(input(f"\n{level_2_value_1} + {level_2_value_2} = "))
                    if user_sum_2 == level_2_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum_2 != level_2_sum:
                        print("Incorrect")
                        incorrect_tries = incorrect_tries + 1
                        if incorrect_tries == 3:
                            print(f"Correct answer is: {level_2_sum}")
                            break
                    else:
                        break
                except:
                    print("Incorrect")
                    incorrect_tries = incorrect_tries + 1
                    if incorrect_tries == 3:
                        print(f"Correct answer is: {level_2_sum}")
                        break

        if difficulty_level == 3:
            level_3_value_1 = random.randint(100, 999)
            level_3_value_2 = random.randint(100, 999)
            level_3_sum = level_3_value_1 + level_3_value_2  

            incorrect_tries = 0
            while True:
                try:
                    user_sum_3 = int(input(f"\n{level_3_value_1} + {level_3_value_2} = "))
                    if user_sum_3 == level_3_sum:
                        print("Correct!")
                        questions_correct = questions_correct + 1
                        break
                    if user_sum_3 != level_3_sum:
                        print("Incorrect")
                        incorrect_tries = incorrect_tries + 1
                        if incorrect_tries == 3:
                            print(f"Correct answer is: {level_3_sum}")
                            break
                    else:
                        break
                except:
                    print("Incorrect")
                    incorrect_tries = incorrect_tries + 1
                    if incorrect_tries == 3:
                        print(f"Correct answer is: {level_3_sum}")
                        break

    #tell user what percent of questions they got correct 
    percent_correct = questions_correct / number_of_questions * 100
    print(f"\nYou got {questions_correct} out of {number_of_questions} questions correct: {percent_correct:.2f}%")

main()