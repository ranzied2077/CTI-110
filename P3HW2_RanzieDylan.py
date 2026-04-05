# Dylan Ranzie
# 03/15/26
# P3HW2
# This program calculates an employee's pay including overtime using IF/ELSE statements.

"""
PSEUDOCODE:

1. Ask user to enter employee name
2. Ask user to enter number of hours worked
3. Ask user to enter pay rate

4. IF hours worked > 40:
      overtime_hours = hours worked - 40
      regular_hours = 40
   ELSE:
      overtime_hours = 0
      regular_hours = hours worked

5. Calculate regular pay:
      regular_pay = regular_hours * pay rate

6. Calculate overtime pay:
      overtime_pay = overtime_hours * (pay rate * 1.5)

7. Calculate gross pay:
      gross_pay = regular_pay + overtime_pay

8. Display results neatly formatted:
      employee name
      pay rate
      hours worked
      overtime hours
      overtime pay
      regular pay
      gross pay
"""

# Input
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Overtime calculation
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Pay calculations
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

# Output
print("\n------------------------------------------")
print(f"Employee Name:   {employee_name}")
print("\nHours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")

# formatted output (based on your PDF)
print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}"
      f"{overtime_pay:<16.2f}{regular_pay:<15.2f}{gross_pay:<.2f}")