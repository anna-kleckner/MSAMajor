def main():
    #capitalize a string
    my_name = "anna"
    print(my_name.capitalize())

    #make a string uppercase
    print(my_name.upper())

    #make a string lowercase
    last_name = "KLECKNER"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #determine if a string starts with a set of characters 
    print(my_name.capitalize().startswith("A"))

    if (not my_name.startswith("A") and not my_name.startswith("a")) :
        print(f"You spelled {my_name} wrong")
    else:
        print(f"You spelled {my_name} correctly")

    #determine if a string ends with a specified set of characters 
    print(my_name.endswith("na"))
    
    #find a set of characters in a string
    print(my_name.find("n", 2))

    #loop through a string
    print("\n")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of occurences of the word dog in sentence
    #expected output: 3
    #use a while loop to read the string 
    
    number_of_dogs = 0
    dog_index = 0
    while True:
        dog_index = sentence.find("dog", dog_index)
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            dog_index += 1
            continue
    print(f"Number of dogs: {number_of_dogs}")

    #how to use the split method 
    car_info = "Ferrari,f-50,2021,500000,4.8\n"
    car_data = car_info.split(",")
    print(car_data)


main()