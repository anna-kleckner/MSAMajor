def main(): 
    #create a while loop that prints integers between 0-10 
    output_value = 0
    stop_value = 10    
    #run the loop while the output value is less than or equal to the stop value
    while output_value <= stop_value:
        print(output_value)
        #increment the output value
        output_value += 1
        #output_value = output_value + 1


    print("\n")
    user_start = int(input("Start value: "))
    user_stop = int(input("Stop value: "))
    while user_start <= user_stop:
        print(user_start)
        user_start += 1



main()