# Addition
def add(x, y):
    return x + y

# Subtraction
def substract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

# Input values
def input_values():

    operation = input("""
Choose an operation from the list:

1. Add
2. Substract
3. Multiply
4. Divide
""")
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")

    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("You must enter a valid number! ")
        return input_values()

    return operation, number1, number2

# Calculation
def calculate():

    operation, number1, number2 = input_values()

    if operation == '1':
        print('{} + {} = '.format(number1, number2), round(add(number1, number2),3))

    elif operation == '2':
        print('{} - {} = '.format(number1, number2), round(substract(number1, number2),3))

    elif operation == '3':
        print('{} * {} = '.format(number1, number2), round(multiply(number1, number2),3))

    elif operation == '4':
        if number2 == 0:
            print("You cannot divide by 0! ")
            
        else:
            print('{} / {} = '.format(number1, number2), round(divide(number1, number2),3))

    else:
        print("Invalid choice, please try again. ")

    new()

# New calculation / calculation loop
def new():
    new_calc = input('Do you want another calculation? Y/N\n')

    if new_calc.upper() == 'Y':
        calculate()

    elif new_calc.upper() == 'N':
        print('Bye.')

    else:
        print("Invalid input!")
        new()

calculate()
