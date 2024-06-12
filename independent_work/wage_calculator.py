#Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
#The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.
def get_hours_worked_daily(): 
    hours_worked = 0
    while(True):
        try:
            hours_worked = float(input("Enter the number of hours worked daily: "))
            if hours_worked <= 0 or hours_worked >= 24:
                print("ERROR enter a number greater than 0 and less than 24")
                continue 
            else: 
                break
        except: 
            print("ERROR enter a number greater than 0 and less than 24")
    return hours_worked
hours_worked = get_hours_worked_daily()

def get_hourly_wage():
    hourly_wage = 0
    while(True):
        try: 
            hourly_wage = float(input("Enter the hourly wage: "))
            if hourly_wage <= 0:
                print("ERROR enter a number greater than 0")
                continue
            else: 
                break
        except: 
            print("ERROR enter a number greater than 0")
    return hourly_wage
hourly_wage = get_hourly_wage()

#Calculate the yearly wage given the two inputs
#Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
#It would help to first write down the mathematical formula needed to calculate the yearly wage
daily_wage = hours_worked * hourly_wage
days_worked = 350
yearly_wage = daily_wage * days_worked

#12% will be deducted from yearly earnings for taxes
tax_deducted = yearly_wage * 0.12
total_after_taxes = yearly_wage * 0.88

#Print the a Pay Advice containing: hours worked, hourly wage, wages before taxes, tax amount, annual wages after taxes
#money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places
print(f"Pay Advice:\n-----------\nHours Worked: {hours_worked:.2f}\nHourly Wage: ${hourly_wage:.2f}\nWages Before Taxes: ${yearly_wage:.2f}\nTax Amount: ${tax_deducted:.2f}\nAnnual Wage After Taxes: ${total_after_taxes:.2f}")
