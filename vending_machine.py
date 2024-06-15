#prompt user to enter a coin
def get_get_coin_from_user():
    user_coin = 0
    while True: 
        try:
            user_coin = int(input("Insert Coin: "))
            if user_coin == 1 or user_coin == 5 or user_coin == 10 or user_coin == 25:
                break
            else:  
                continue
        except:
            continue
    return user_coin


def main():
    starting_amount = 50
    print(f"Vending Machine \n---------------- \nAmount Due: {starting_amount}")
    user_coin = get_get_coin_from_user()
    amount_due = starting_amount - user_coin
    
    print(f"\nAmount Due: {amount_due}")
    user_coin = get_get_coin_from_user()

main()
