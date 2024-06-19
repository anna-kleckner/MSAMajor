def main():
    #get X, y, and Z by splitting and looking for a space .split(" ")
    while True: 
        try:
            user_expression = input("\nExpression: ")
            user_info = user_expression.split(" ")
            #expecting 3 items in the list (check the length)
            items_in_list = len(user_info)
            
            if user_expression.lower() == "end":
                break
            
            if items_in_list == 3:
            #determine what the y opperator is (if statement)
                float_1 = float(user_info[0])
                float_2 = float(user_info[2])
                operator = user_info[1]

                if operator not in ["+", "-", "*", "/"]:
                    print("Please use a vaild operator")
                    continue
                
                if operator == "+":
                    sum = float_1 + float_2
                    print(f"= {sum:.1f}")
                if operator == "-":
                    difference = float_1 - float_2
                    print(f"= {difference:.1f}")
                if operator == "*":
                    product = float_1 * float_2
                    print(f"= {product:.1f}")
                if operator == "/":
                    if float_2 == 0:
                        print("Divide by zero error")
                        continue
                    else:
                        quotient = float_1 / float_2
                        print(f"= {quotient:.1f}")
            else:
                print(f"Invalid input. Enter expression in X y Z format.")
                continue
        except:
            continue


main()