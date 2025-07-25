#prompt the user
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

#the operator of choice
operation = input("Choose the operation (+, -, *, /):")

#operation in action

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _: 
        print("Invalid operation. Please choose from +, -, *, /.")