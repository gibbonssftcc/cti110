# Write a program to convert pounds(lbs) to kilograms(kg).
# 2-19-2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Samantha Gibbons
#
# Declare the variables
# Ask the User for the value of pounds
# Write the formula to determine the calculations
# Save, Run and Display output
#
# By identifying the variables, the formula conversion is created. The number of pounds-per-kilogram
# is multiplied (2.2046) and lbs/kg. Kgs' will be divided by pounds-per-kilogram (2.2046).
# 2.206 X (1kg/2.2046) equals the conversion to kilograms.
#
# Pound = 2.2046 lbs is 1kg 
# kg = 2.2046 lbs
# kilogram = lbs * kg
#
#
kilograms = float(input("Enter value of pounds to be converted to kilograms: "))

# 2.2046 pounds is 1 kilogram
pounds = 2.2046

# 1 kg is 2.2046 lbs
kilograms = kilograms / 2.2046

# Convert pounds to kilograms
kg = pounds * kilograms

# Display lbs to kg
print('Pounds to Kilograms is ', format(kilograms, ',.2f'),sep="")

                                      







               
               




               

