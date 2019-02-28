# This program will get the larger area of the two rectangles or
# tell the user if both rectangles are equal. 
# 2-28-2019
# CTI-110 P3T1 - Areas of Rectangles
# Samantha Gibbons
#
# Declare the variables for the width and lenghth of the rectangle
# Ask the User to input the value
# Write the formula to determine the Areas of Rectangles
# Save, Run and Display the output
#
# Input the length and width of rectangle 1.
# Input the length and wideth of rectange 2.
# Calculate the area of rectangle 1.
# Calculate the area of rectangle 2.
# if area1 > area2
#           Display "Rectangle 1 has the greatest area."
# else if area2 > area1
#           Display "Rectangle 2 has the greatest area."
# else
#           Display "Both rectangles have the same area."
#
# Get the dimensions of Rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))
#
# Get the dimensions of Rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))
#
# Calculate the areas of the Rectangles.
area1 = length1 * width1
area2 = length2 * width2
#
# Determine which Rectangle has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area. ')
elif area2 > area1:
    print('Rectangle 2 has the greater area. ')
else:    
    print('Rectangle 1 and Rectangle 2 have equal areas. ')
    
    


