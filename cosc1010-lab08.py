# Garrick McDonald
# UWYO COSC 1010
# November 2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: Logan Cabanaw


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def integ_or_float(num):
    list(num)
    dec_count = 0 
    symbol_count = 0
    index = 0
    outcome = []
    for i in num:
        if i.isdigit() and i != ".":
            outcome.append("1")
        elif i == ".":
            dec_count = +1
            if dec_count > 1:
                return(print("False"))
            outcome.append("2")
        elif i == "-" or i == "+":
            if index > 0:
                return(print("False"))
        elif i.isalpha():
            return(print("False"))
        else:
            return(print("False"))
        index += 1
    if "2" in outcome and "1" in outcome:
        return(print("Float"),float(num))
    elif "1" in outcome:
        return(print("Integer"),int(num))
    else:
        return(print("False"))

while True:
    num = input("Insert a number to see if it is an Integer or Float, type 'exit' to stop: ")
    if num.lower() == "exit":
        break
    integ_or_float(num)

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)):
        return False
    if x_lower > x_upper:
        return False
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)

    return y_values

while True:
    m_input = input("Enter the slope (m), or type 'exit' to quit: ")
    if m_input.lower() == 'exit':
        break
    b_input = input("Enter the y-intercept (b): ")
    x_lower_input = input("Enter the lower x bound: ")
    x_upper_input = input("Enter the upper x bound: ")
    try:
        m = float(m_input)
        b = float(b_input)
        x_lower = int(x_lower_input)
        x_upper = int(x_upper_input)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    result = slope_intercept(m, b, x_lower, x_upper)
    if result is False:
        print("Bounds must be integers, and the lower bound should be less than or equal to the upper bound.")
    else:
        print("The y-values for the given range are:", result)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def safe_sqrt(value):
    if value < 0:
        return None
    return value ** 0.5

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)
   
    if sqrt_discriminant is None:
        return None
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return root1, root2

while True:
    a_input = input("Enter the value of a (non-zero), or type 'exit' to quit: ")
    if a_input.lower() == 'exit':
        break
    b_input = input("Enter the value of b: ")
    c_input = input("Enter the value of c: ")

    try:
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
        if a == 0:
            print("The value of 'a' must be non-zero.")
            continue
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    result = quadratic_formula(a, b, c)
    if result is None:
        print("No real roots, as the discriminant is negative.")
    else:
        print("The roots are:", result)
