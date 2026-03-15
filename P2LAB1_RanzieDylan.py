# Dylan Ranzie
# 03/08/26
# P2LAB1
# The program will calculate the diameter, circumference, and area of a circle.

# import math module to use the constant, math.pi
import math

#get the radius from the user
radius = float(input("what is the radius of the circle"))
print()

#calculate diameter
diameter = 2 * radius

#Display diameter with 1 decimal point
print(f"the diameter of the circle is{diameter:.1f}")
# calculate circumference

circumference = 2 * math.pi * radius
#Display circumference with 2 decimal places
print(f"the circumference of the circle is{circumference:.2f}")

#Calculate the area
area = math.pi * radius**2

#Display area with 3 decial places
print(f"the area of the circle is{area:.3f}")