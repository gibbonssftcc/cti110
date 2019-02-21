# Create a program that calculates the amount of tip for three different
# percentages based on the user entering the total cost of a meal.
# 2-20-2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Samantha Gibbons
#
# Determine what the variables are.
# Ask the user to enter the total cost of meal purchase to determine tip
# to be rendered.
# Write the input; the calculation for each amount of tip percentage.
# Save, Run and Display output.
#
# Assign variable total amount of meal
# Assign a value of 15% tip
# Assign a value of 18% tip
# Assign a value of 20% tip
#
#
# Give a variable for total cost of meal.  The total cost of the meal will
# be multiplied by the percentage in decial format. i.e. 25 * .15 will 
# equal the tip percentage for the total cost of meal.
#
# Get total amount of a meal purchased at a restaurant from user.
Total_cost = float(input('Enter the total cost of meal purchased: '))
#
# Assign value for a 15 percent tip
tip_fifteen = Total_cost * .15
#
# Assign value for a 18 percent tip
tip_eighteen = Total_cost * .18
#
# Assign value for a 20 percent tip
tip_twenty = Total_cost * .20
#
#
print('The 15% tip amount is $', format(tip_fifteen, ',.2f'),sep="")
print('The 18% tip amount is $', format(tip_eighteen, ',.2f'),sep="")
print('The 20% tip amount is $', format(tip_twenty, ',.2f'),sep="")

