# Ranzie Dylan
# 03/15/26
# P2HW2
# design a program that does the following: Asks the user to enter grades for following tests. Each grade is to be requested in a separate statement.

"""
PSEUDOCODE

1. Create an empty list to store module grades
2. Ask the user to enter grades for Module 1 through Module 6
3. Convert each input to float
4. Add each grade to the list
5. Calculate:
      lowest grade using min()
      highest grade using max()
      sum of grades using sum()
      average by dividing sum by number of grades
6. Display results formatted exactly like the example
7. Format average to two decimal places
"""

# Create list
module_grades = []

# Input grades
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Output
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest:.1f}")
print(f"Highest Grade:     {highest:.1f}")
print(f"Sum of Grades:     {total:.1f}")
print(f"Average:           {average:.2f}")
print("--------------------------------")