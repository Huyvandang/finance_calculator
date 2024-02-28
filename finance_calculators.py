"""
Create a program that allows the user to access two different financial calculators:
an investment and a home loan repayment calculator.
Top of the line should include 'import math'.
Write a code that shows the description of 'investment' and 'bond',
and then request use to select one of the option.
Case letters should not affect the users selection.

If the user selects 'investment',
    Ask the user to input:
         - The amount of money that they are depositing.
         - The interest rate (as a percentage). Do not include % symbol.
         - The number of years they are planning to invest.
         - Then ask the user if they want 'simple' or 'compound' interest.
    Print out the answer.

If the user selects 'bond',
    Ask the user to input:
        - The present value of the house.
        - The interest rate (as a percentage). Do not include % symbol.
        - The number of months they plan to repay the bond.S
    Calculate how much the user will have to repay each month and output the answer.
"""

import math

while True: # Loop if user enters anything apart from 'investment' or 'bond'
    # Show menu options
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")

    print()
    
    # Get user choice and convert it to lowercase
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    print(user_choice)

    # Check user's choice and get the investment detail from user
    if user_choice == "investment":
        deposit = float(input("Enter the amount of money you wish to deposit: "))
        interest_rate = float(input("Enter the interest rate (without %): ")) / 100
        years = int(input("Enter the number of years you are investing your money: "))

        while True: # Loop
            # Ask user which interest they would like to choose
            interest_type = input("Select 'simple' or 'compound' interest: ").lower()
            if interest_type == 'simple':
                total_amount = deposit * (1 + interest_rate * years)
                break
            elif interest_type == 'compound':
                total_amount = deposit * math.pow((1 + interest_rate), years)
                break
            else: 
                print("Invalid. Please enter 'simple' or 'compound'.")

        # Display total amount after interest         
        print(f"The total amount after {years} years at {interest_rate*100}% interest is: {total_amount:2f}")
        break
    
    # Get the bond investment detail from user
    elif user_choice == 'bond':
        house_value = float(input("Enter the present value of your house: "))
        interest_rate = float(input("Enter the interest rate (without %): ")) / 100
        months = int(input("Enter the number of months for repayments: "))

        # Calculate the monthly interest and bond repayment
        monthly_interest = interest_rate / 12
        repayment = (monthly_interest * house_value) / (1 - math.pow((1 + monthly_interest), -months))

        # Display monthly bond repayment
        print(f"The monthly bond repayment amount is: {repayment:.2f}")
        break
    
    # Print if invalid input from user
    else:
        print("Invalid option. Please enter 'investment' or 'bond': ")