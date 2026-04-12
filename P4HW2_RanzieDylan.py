# Dylan Ranzie
# 04/12/2026
# P4HW2
# This program calculates gross pay for multiple employees, including overtime.
# It also keeps track of total overtime pay, regular pay, gross pay,
# and number of employees entered using a sentinel-controlled loop.


"""
PSEUDOCODE (DETAILED ALGORITHM)

START

Set total_overtime_pay = 0
Set total_regular_pay = 0
Set total_gross_pay = 0
Set employee_count = 0

Prompt user for employee name or "Done"

WHILE employee name is not "Done"

    Ask for hours worked
    Ask for pay rate

    IF hours worked > 40
        overtime_hours = hours worked - 40
        regular_hours = 40
    ELSE
        overtime_hours = 0
        regular_hours = hours worked
    ENDIF

    overtime_pay = overtime_hours * pay rate * 1.5
    regular_pay = regular_hours * pay rate
    gross_pay = overtime_pay + regular_pay

    Add overtime_pay to total_overtime_pay
    Add regular_pay to total_regular_pay
    Add gross_pay to total_gross_pay

    Increase employee_count by 1

    Display employee results

    Ask for next employee name

END WHILE

Display:
    total number of employees
    total overtime pay
    total regular pay
    total gross pay

END
"""

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Start program
employee_name = input("Enter employee's name or \"Done\" to terminate: ")

while employee_name != "Done":

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Determine overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pay
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display employee info
    print("\nEmployee name:", employee_name)
    print()
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:.1f}           {pay_rate:.2f}       {overtime_hours:.1f}        "
          f"{overtime_pay:.2f}          ${regular_pay:.2f}        ${gross_pay:.2f}")
    print()

    # Next employee
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

# Final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")