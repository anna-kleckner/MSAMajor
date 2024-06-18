def main():
    menu_prices ={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    #while loop, ask for item
    total_price = 0
    while True:
        try:
            user_order = input("\nItem: ")
            if user_order in menu_prices:
                total_price = total_price + (menu_prices[user_order])
                print(f"Total: ${total_price:.2f}")
                continue
            if user_order.lower() == "end":
                break
            else:
                continue
        except:
            continue


main()