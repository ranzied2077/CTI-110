# Ranzie Dylan
# 03/15/26
# P2HW2
# The program is going to work exactly as was requested for P1HW2, only the output will be nicely formatted. See image below.
print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining = budget - (gas + hotel + food)

print()
print("------------Travel Expenses------------")

print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")

print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accomodation:':<20}${hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")

print("---------------------------------------")

print(f"{'Remaining Balance:':<20}${remaining:.2f}")

