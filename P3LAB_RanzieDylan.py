#Ranzie Dylan
# 03/22/26
#P3LAB
#This program allows the user to enter a money (float) value with two places after the decimal.

# Get user input
amount = float(input("Enter the amount of money: $"))

# Convert to cents
cents = int(round(amount * 100))

# Calculate dollars
dollars = cents // 100
cents -= dollars * 100

# Calculate quarters
quarters = cents // 25
cents -= quarters * 25

# Calculate dimes
dimes = cents // 10
cents -= dimes * 10

# Calculate nickels
nickels = cents // 5
cents -= nickels * 5

# Remaining cents are pennies
pennies = cents

# Display results
print("\nMoney breakdown:")

if dollars > 0:
    print(f"{dollars} Dollar" if dollars == 1 else f"{dollars} Dollars")

if quarters > 0:
    print(f"{quarters} Quarter" if quarters == 1 else f"{quarters} Quarters")

if dimes > 0:
    print(f"{dimes} Dime" if dimes == 1 else f"{dimes} Dimes")

if nickels > 0:
    print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")

if pennies > 0:
    print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")