# Dylan Lewis
# 04/26/2026
# P5LAB
# This program simulates a self-checkout machine. It generates a random total owed,
# accepts user payment, calculates change, and displays the breakdown of coins and dollars.

import random

# Function to disperse change
def disperse_change(change):
    # Convert to cents to avoid float issues
    change = int(round(change * 100))

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    # Display results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")


# Main function
def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total_owed:.2f}")

    # Get user input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    if cash < total_owed:
        print("Not enough money provided.")
    else:
        change = round(cash - total_owed, 2)
        print(f"Change is: ${change:.2f}\n")

        # Call function
        disperse_change(change)


# Call main
main()