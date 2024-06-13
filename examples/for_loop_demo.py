
def main():
    #print integers between 0 and 10
    for number in range(11):
        print(number)

    #print integers between 5 and 10 
    print("\n")
    for number in range(5, 11):
        print(number)

    #print even numbers between 0-10
    print("\n")
    for number in range(0, 11, 2):
        print(number)

    #print odd numbers 0-10
    print("\n")
    for number in range(1, 11, 2):
        print(number)

    #prompt the user for the start and stop values and print the numbers between start and stop 
    print("\n")
    start_value = int(input("Start value: "))
    stop_value = int(input("Stop value: "))
    for number in range(start_value, stop_value):
        print(number)


main()