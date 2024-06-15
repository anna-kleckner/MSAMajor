#create a program that excepts a highway number and outputs the direction 
#user enters: 95, output: "Interstate 95 runs South to North"
#error check program so that it doesn't crash 

def get_hwy_number():
    hwy_number = 0
    while True:
        try:
            hwy_number = int(input("\nEnter the number of the highway: "))
            if hwy_number <= 0:
                print("ERROR enter a whole number greater than 0")
                continue
            else:
                break
        except:
            print("ERROR enter a whole number greater than 0")
    return hwy_number

def test_hwy_number(hwy_number):
    if hwy_number % 2 == 0:
        return "East to West"
    elif hwy_number % 2 >= 1:
        return "North to South"

def main():
    hwy_number = get_hwy_number()
    hwy_direction = test_hwy_number(hwy_number)
    print(f"Highway {hwy_number} runs from {hwy_direction}")


main()