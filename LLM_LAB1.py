# Dylan Ranzie
# 04/19/2026
# LLM_LAB1
# Number Guessing Game

"""
Pseudocode:
1. Import random module
2. Generate a random number between 1 and 100
3. Set attempt counter to 0
4. Ask user to guess the number
5. While guess is not correct:
    a. Increase attempt counter
    b. If guess is too high, tell user
    c. If guess is too low, tell user
    d. Ask for another guess
6. When correct, display number of attempts
"""

import random

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0
guess = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Game loop
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Correct! 🎉")
        print(f"You guessed the number in {attempts} attempts.")