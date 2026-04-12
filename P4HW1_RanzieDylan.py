# Dylan Ranzie
# 04/12/2026
# P4HW1
# This program collects user scores, validates input, removes the lowest score,
# calculates the average, and assigns a letter grade.

# -------- PSEUDOCODE --------
# 1. Prompt user to enter the number of scores they want to input
# 2. Create an empty list to store scores
#
# 3. Loop from 1 to number of scores:
#     a. Ask user to enter a score
#     b. WHILE score is less than 0 OR greater than 100:
#         i. Display "INVALID Score entered!!!!"
#         ii. Display "Score should be between 0 and 100"
#         iii. Prompt user to re-enter the same score
#     c. Add valid score to the list
#
# 4. Find the lowest score in the list
# 5. Remove the lowest score from the list
#
# 6. Calculate the average of the remaining scores
#
# 7. Determine letter grade based on average:
#     a. If average >= 90 → grade = A
#     b. Else if average >= 80 → grade = B
#     c. Else if average >= 70 → grade = C
#     c. Else if average >= 60 → grade = D
#     d. Else → grade = F
#
# 8. Display results:
#     a. Lowest score
#     b. Modified list (without lowest score)
#     c. Average (formatted to 2 decimal places)
#     d. Letter grade
# --------------------------------

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

score_list = []

# Loop to collect scores
for i in range(num_scores):
    score = float(input(f"\nEnter score #{i+1}: "))
    
    # Validate score
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))
    
    score_list.append(score)

# Find and remove lowest score
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate average
average = sum(score_list) / len(score_list)

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")