# Basic Calculator Program

def basic_calculator():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask the user to input a mathematical operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation based on the user's input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /")
        return
    
    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator function
basic_calculator()