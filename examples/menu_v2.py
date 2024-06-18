#fuction to load menu items from the fileand create a dictionary
#input: none
#output: dictionary of menu items
def get_menu_prices():
    #create a file handle that gives us access to the file
    #"r" is for read and "w" is for write
    data_file = open("menu.txt", "r")

    #create an empty dictionary to store menu items
    menu_items = {}

    #loop through data in the file and read the file on line at a time
    for line_of_data in data_file:
        #split the line of data at the comma using .split()
        keys_and_values = line_of_data.split(",")
        #get item and price from the resulting list and store them in the dictionary
        item = keys_and_values[0]
        price = float(keys_and_values[1])
        menu_items[item] = price
    #close the file
    data_file.close()

    return menu_items


def main():
    #load the new menu items dictionary 
    menu_items = get_menu_prices()
    #while loop, ask for item
    total_price = 0
    while True:
        try:
            user_order = input("\nItem: ")
            if user_order in menu_items:
                total_price = total_price + (menu_items[user_order])
                print(f"Total: ${total_price:.2f}")
                continue
            if user_order.lower() == "end":
                break
            else:
                continue
        except:
            continue


main()