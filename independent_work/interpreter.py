def main():
    #get X, y, and Z by splitting and looking for a space .split(" ")
    while True: 
        try:
            user_expression = input("Expression: ")
            user_info = user_expression.split(" ")
            #expecting 3 items in the list (check the length)
            #determine what the y opperator is (if statement)
        except:
            continue


main()