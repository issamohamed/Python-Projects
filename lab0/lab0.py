# Name: Issa Mohamed
# Date: 9/21/21
# Class: CS 111

# Math Module Libary
import math
# Atom Weights (grams/mole)
hydrogen_weight = 1.0079 
carbon_weight = 12.011
oxygen_weight = 15.9994
# Atom Count
hydrogen_atom_count = 22.0
carbon_atom_count = 12.0
oxygen_atom_count = 11.0
# Conversion Equation
# Calculating Molecular Weight Of Atom
molecular_weight = (hydrogen_weight * hydrogen_atom_count) + (carbon_weight * carbon_atom_count) + (oxygen_weight * oxygen_atom_count)
# Rounding Function  
rounded_molecular_weight_result = round(molecular_weight, 3)
print("1. The molecular weight of an carbohydrate with 22 hydrogen atoms, 12 carbon atoms, and 11 oxygen atoms is",rounded_molecular_weight_result,"grams/moles") 
print("\n")

# Problem 2: Distance between 2 points 

# Points
x_1 = 10.0 
y_1 = 5.0
x_2 = 8.0
y_2 = 4.0

# Function
x_squared = (x_2 - x_1)**2
y_squared = (y_2 - y_1)**2
x_y_sum = (x_squared + y_squared)
distance = math.sqrt(x_y_sum)
print("2. The distance between the two 2D points (10, 5) and (8, 4) is", distance)
print("\n")
# Problem 3: Area of a triangle
#sides
side_a = 17.0
side_b = 15.0
side_c = 13.0

value_s = (side_a + side_b + side_c) / 2
# calculating the inside of the sqrt equation
inside_value = value_s * ( (value_s - side_a) *(value_s - side_b) * (value_s - side_c) )
# Squaring rooting the inside value
area = math.sqrt(inside_value)
print ("3. The area of the triangle with the sides 17, 15 and 13 is", area)
print("\n")
# Problem 4: Snow-Clearing Ladder
#variables
required_height = 8.5
required_degree = 75.0
#converting degrees to radians
required_angle = (math.pi / 180.0) * required_degree
length = (required_height/ (math.sin(required_angle)))
print("4. The length of the of the ladder when required to reach of 85 meters leaning at a 75 degree angle is", length, "meters")
print("\n")