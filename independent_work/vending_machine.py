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
    amount_due = 50
    print(f"Vending Machine \n---------------- \nAmount Due: {amount_due}")
    
    while True:
        user_coin = get_get_coin_from_user()
        amount_due = amount_due - user_coin

        if amount_due > 0:
            print(f"\nAmount Due: {amount_due}")
            continue
        elif amount_due == 0:
            print(f"\nAmount Due: 0")
            break
        else:
            change_returned = abs(amount_due)
            print(f"\nChange: {change_returned}")
            break

main()